#!/usr/bin/env python3
"""Télécharge l'audio d'épisodes choisis dans un flux RSS et le transcrit (faster-whisper, CPU).

Usage :
  python3 -I outils/podcast/transcrire.py <url-ou-fichier-rss> --motif REGEX [--exclure REGEX] --slug SLUG [options]
  python3 -I outils/podcast/transcrire.py <url-ou-fichier-rss> --guid GUID [--guid GUID ...] [--slug SLUG] [options]

Sélection (comme lister.py) :
  --motif REGEX       épisodes dont le titre correspond (sans casse) ; --exclure REGEX pour en retirer
  --guid GUID         épisode précis (répétable ; l'ordre des --guid est conservé)
  --ordre ORDRE       titre (tri naturel : Part 1, Part 2 … Part 11 ; défaut avec --motif) | date | flux
                      | arguments (ordre des --guid ; défaut avec --guid)
Les épisodes retenus forment UNE source, dans cet ordre, sur une horloge continue.

Options :
  --slug SLUG         nom du dossier de la source (obligatoire si plusieurs épisodes ;
                      sinon dérivé du titre de l'épisode)
  --titre TITRE       titre de la source (défaut : titre de l'épisode, ou « <podcast> : <slug> »)
  --sortie DOSSIER    dossier parent de la source (défaut : <repo>/sources/podcast) -> <DOSSIER>/<slug>/
  --travail DOSSIER   dossier de travail pour l'audio, HORS du repo (défaut : dossier temporaire
                      du système). Un sous-dossier neuf y est créé puis supprimé à la fin.
  --max-secondes N    ne transcrit que les N premières secondes de CHAQUE épisode (tests)
  --modele NOM        modèle faster-whisper (défaut : small.en ; voir README pour les vitesses)
  --langue CODE       langue forcée (défaut : en pour un modèle .en, sinon détection automatique)
  --threads N         fils de calcul CPU (défaut : tous les cœurs)
  --oui               ne demande pas confirmation pour une longue transcription (> 1 h d'audio)
  --simuler           affiche la sélection, l'ordre et le temps de calcul estimé, sans rien télécharger
  --sans-reprise      ignore les épisodes déjà transcrits lors d'un lancement interrompu (voir README)

Reprise : chaque épisode transcrit est mis de côté (texte seulement) dans
<travail ou dossier temporaire>/podcast-reprise-<slug>/ ; relancer la même commande après une coupure
reprend au premier épisode manquant. Ce dossier est supprimé une fois la source écrite.

Écrit dans <sortie>/<slug>/ (même format que outils/youtube/transcrire.py) :
  - metadata.json     podcast, flux, épisodes (titre, date, durée, guid, URL audio, début dans la source),
                      modèle, langue, vitesse mesurée
  - transcription.md  en-tête, « ## Épisodes », puis « ## Transcription » : blocs **[mm:ss]** texte d'environ
                      30 s séparés d'une ligne vide, un intertitre « ### Épisode i/N » à chaque épisode ;
                      « ## Chapitres » si les descriptions du flux donnent des horodatages « (12:34) - Titre »
Jamais d'audio dans la sortie : seuls le texte et les métadonnées sont écrits.
"""
import argparse, datetime, email.utils, hashlib, html, json, os, re, shutil, sys, tempfile, time, unicodedata
import urllib.error, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
SORTIE = RACINE / "sources" / "podcast"
ITUNES = "{http://www.itunes.com/dtds/podcast-1.0.dtd}"
AGENT = "Mozilla/5.0 (compatible; outils-podcast/1.0)"
TENTATIVES = 4
TAUX = 16000  # Hz, échantillonnage attendu par Whisper
OCTETS_PAR_S_MAX = 40000  # 320 kbit/s : majorant pour les téléchargements partiels (--max-secondes)


# ---------- flux RSS (copie autonome de lister.py : pas d'import entre scripts) ----------

def ouvrir(url, timeout=120):
    req = urllib.request.Request(url, headers={"User-Agent": AGENT})
    return urllib.request.urlopen(req, timeout=timeout)


def avec_tentatives(action, quoi):
    erreur = None
    for i in range(TENTATIVES):
        try:
            return action()
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            erreur = e
            if isinstance(e, urllib.error.HTTPError) and e.code in (401, 403, 404, 407, 410):
                break
            time.sleep(2 ** (i + 1))
    raise RuntimeError(f"{quoi} : {erreur}. Erreur TLS ou proxy : voir /root/.ccr/README.md")


def telecharger_flux(source):
    if not re.match(r"https?://", source):
        return Path(source).read_bytes()

    def lire():
        with ouvrir(source) as r:
            return r.read()
    return avec_tentatives(lire, f"flux injoignable ({source})")


def duree_s(texte):
    if not texte:
        return None
    try:
        s = 0
        for p in texte.strip().split(":"):
            s = s * 60 + float(p)
        return int(s)
    except ValueError:
        return None


def date_iso(texte):
    try:
        return email.utils.parsedate_to_datetime(texte).isoformat()
    except (TypeError, ValueError):
        return None


def propre(texte):
    """Codes HTML (&amp;, &#39;…), balises et espaces insécables -> texte brut sur une ligne par paragraphe."""
    t = html.unescape(re.sub(r"<br\s*/?>|</p>", "\n", texte or "", flags=re.I))
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"[\u00a0\u2007\u202f\u200b\u2060]", " ", t)
    return "\n".join(re.sub(r"[ \t]+", " ", l).strip() for l in t.splitlines()).strip()


def chapitres(description):
    """« (0:00) - Titre » / « 12:34 Titre » dans la description -> [{"start_time": s, "title": t}]."""
    chap = []
    for l in description.splitlines():
        m = re.match(r"^\(?(\d{1,2}(?::\d{2}){1,2})\)?\s*[-–—:]?\s*(.+)$", l.strip())
        if m:
            chap.append({"start_time": duree_s(m.group(1)), "title": m.group(2).strip()})
    return chap if len(chap) >= 2 and chap[0]["start_time"] == 0 else []


def episodes(contenu):
    canal = ET.fromstring(contenu).find("channel")
    if canal is None:
        raise RuntimeError("pas de <channel> : ce n'est pas un flux RSS")
    podcast = {"titre": propre(canal.findtext("title")), "auteur": propre(canal.findtext(f"{ITUNES}author")),
               "lien": canal.findtext("link"), "langue": canal.findtext("language")}
    liste = []
    for rang, it in enumerate(canal.findall("item"), 1):
        enc = it.find("enclosure")
        liste.append({
            "rang_flux": rang, "titre": propre(it.findtext("title")),
            "date": date_iso(it.findtext("pubDate")), "duree_s": duree_s(it.findtext(f"{ITUNES}duration")),
            "numero": it.findtext(f"{ITUNES}episode"), "guid": (it.findtext("guid") or "").strip(),
            "lien": it.findtext("link"), "audio_url": enc.get("url") if enc is not None else None,
            "description": propre(it.findtext("description") or it.findtext(f"{ITUNES}summary")),
        })
    return podcast, liste


def cle_naturelle(titre):
    return [int(x) if x.isdigit() else x.casefold() for x in re.split(r"(\d+)", titre)]


def selectionner(liste, a):
    if a.guid:
        par_guid = {e["guid"]: e for e in liste}
        manquants = [g for g in a.guid if g not in par_guid]
        if manquants:
            raise RuntimeError(f"guid absent du flux : {', '.join(manquants)}")
        choix = [par_guid[g] for g in a.guid]
    else:
        choix = [e for e in liste if re.search(a.motif, e["titre"], re.I)]
    if a.exclure:
        choix = [e for e in choix if not re.search(a.exclure, e["titre"], re.I)]
    ordre = a.ordre or ("arguments" if a.guid else "titre")
    if ordre == "date":
        choix = sorted(choix, key=lambda e: (e["date"] or "", -e["rang_flux"]))
    elif ordre == "titre":
        choix = sorted(choix, key=lambda e: cle_naturelle(e["titre"]))
    elif ordre == "flux":
        choix = sorted(choix, key=lambda e: e["rang_flux"])
    return choix


# ---------- audio ----------

def dans_repo(p: Path) -> bool:
    p = p.resolve()
    return p == RACINE or RACINE in p.parents


def telecharger_audio(ep, dossier: Path, max_s=None) -> Path:
    """Télécharge l'audio dans un dossier neuf. Avec max_s, s'arrête dès qu'il y a assez d'octets."""
    if not ep["audio_url"]:
        raise RuntimeError(f"pas d'URL audio pour « {ep['titre']} »")
    cible = dossier / "audio.bin"  # nom fixe : jamais le nom fourni par le serveur

    def recevoir():
        with ouvrir(ep["audio_url"], timeout=300) as r, open(cible, "wb") as f:
            total = int(r.headers.get("Content-Length") or 0)
            limite = None
            if max_s:
                debit = total / ep["duree_s"] if total and ep["duree_s"] else OCTETS_PAR_S_MAX
                limite = int(max_s * min(debit * 1.25, OCTETS_PAR_S_MAX)) + 256_000
            recu = 0
            while True:
                morceau = r.read(1 << 20)
                if not morceau:
                    break
                f.write(morceau)
                recu += len(morceau)
                if limite and recu >= limite:
                    break
            if not limite and total and recu < total:
                raise ConnectionError(f"téléchargement incomplet ({recu}/{total} octets)")
        return cible
    return avec_tentatives(recevoir, f"audio injoignable ({ep['audio_url']})")


def charger_audio(chemin: Path, max_s=None):
    from faster_whisper.audio import decode_audio  # décodage PyAV (pas de ffmpeg requis)
    audio = decode_audio(str(chemin), sampling_rate=TAUX)
    if max_s:
        audio = audio[: int(max_s * TAUX)]
    return audio


# ---------- sortie ----------

def ts(sec):
    sec = int(sec)
    return f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}" if sec >= 3600 else f"{sec // 60:02d}:{sec % 60:02d}"


def slugifier(texte):
    t = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:80] or "episode"


def blocs_30s(segs):
    """(début absolu, texte) -> lignes « **[mm:ss]** texte » d'environ 30 s."""
    lignes, bloc, debut = [], [], None
    for t, txt in segs:
        if debut is None:
            debut = t
        bloc.append(txt)
        if t - debut >= 30:
            lignes += [f"**[{ts(debut)}]** " + " ".join(bloc), ""]
            bloc, debut = [], None
    if bloc:
        lignes += [f"**[{ts(debut)}]** " + " ".join(bloc), ""]
    return lignes


def ecrire(d: Path, meta, par_episode):
    d.mkdir(parents=True, exist_ok=True)
    (d / "metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    eps = meta["episodes"]
    dates = sorted({(e["date"] or "?")[:10] for e in eps})
    lignes = [f"# {meta['titre']}", "",
              f"- Podcast : {meta['podcast']['titre']} · Auteur : {meta['podcast']['auteur']} · "
              f"Durée transcrite : {ts(meta['duree_transcrite_s'])} · Épisodes : {len(eps)} · Publié : {', '.join(dates)}",
              f"- Flux RSS : {meta['flux']}",
              f"- Transcription : faster-whisper {meta['modele']} (CPU, automatique, à relire), langue {meta['langue_transcription']}"]
    if meta.get("max_secondes"):
        lignes.append(f"- TEST : limité aux {meta['max_secondes']} premières secondes de chaque épisode")
    lignes += ["", "## Épisodes", ""]
    lignes += [f"- [{ts(e['debut_dans_source_s'])}] {e['titre']} ({ts(e['duree_s'] or 0)}, {(e['date'] or '?')[:10]})" for e in eps]
    chap = [(e["debut_dans_source_s"] + c["start_time"], c["title"]) for e in eps for c in e["chapitres"]
            if c["start_time"] < e["secondes_transcrites"]]
    if chap:
        lignes += ["", "## Chapitres", "", "(d'après les descriptions du flux, horloge de la source)", ""]
        lignes += [f"- [{ts(t)}] {titre}" for t, titre in chap]
    lignes += ["", "## Transcription", ""]
    for i, (e, segs) in enumerate(zip(eps, par_episode), 1):
        if len(eps) > 1:
            lignes += [f"### Épisode {i}/{len(eps)} · {e['titre']} (début {ts(e['debut_dans_source_s'])})", ""]
        lignes += blocs_30s(segs)
    (d / "transcription.md").write_text("\n".join(lignes).rstrip() + "\n", encoding="utf-8")


# ---------- programme ----------

def arguments():
    ap = argparse.ArgumentParser(description="Transcrit des épisodes de podcast (flux RSS) avec faster-whisper.")
    ap.add_argument("flux")
    sel = ap.add_mutually_exclusive_group(required=True)
    sel.add_argument("--motif")
    sel.add_argument("--guid", action="append")
    ap.add_argument("--exclure")
    ap.add_argument("--ordre", choices=["titre", "date", "flux", "arguments"])
    ap.add_argument("--slug")
    ap.add_argument("--titre")
    ap.add_argument("--sortie", type=Path, default=SORTIE)
    ap.add_argument("--travail", type=Path)
    ap.add_argument("--max-secondes", type=float)
    ap.add_argument("--modele", default="small.en")
    ap.add_argument("--langue")
    ap.add_argument("--threads", type=int, default=os.cpu_count() or 4)
    ap.add_argument("--oui", action="store_true")
    ap.add_argument("--simuler", action="store_true")
    ap.add_argument("--sans-reprise", action="store_true")
    return ap.parse_args()


VITESSE = {"tiny.en": 7.0, "base.en": 4.5, "distil-small.en": 3.5, "small.en": 2.4, "small": 2.2,
           "medium.en": 0.8, "medium": 0.8}  # x temps réel mesurés sur 4 cœurs (README) ; indicatif


def charger_modele(nom, threads):
    """Modèle en cache d'abord (évite l'appel réseau au Hub), téléchargement sinon."""
    from faster_whisper import WhisperModel
    try:
        return WhisperModel(nom, device="cpu", compute_type="int8", cpu_threads=threads, local_files_only=True)
    except Exception:  # noqa: BLE001  pas encore en cache
        for i in range(TENTATIVES):
            try:
                return WhisperModel(nom, device="cpu", compute_type="int8", cpu_threads=threads)
            except Exception as e:  # noqa: BLE001
                if i == TENTATIVES - 1 or isinstance(e, ValueError):
                    raise RuntimeError(f"modèle {nom} introuvable ou non téléchargeable : {e}. "
                                       "Erreur TLS ou proxy : voir /root/.ccr/README.md") from e
                time.sleep(2 ** (i + 1))


def cle_reprise(e, a):
    return hashlib.sha1(json.dumps([e["guid"], e["audio_url"], a.modele, a.langue, a.max_secondes]).encode()).hexdigest()[:16]


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    a = arguments()
    if a.travail and dans_repo(a.travail):
        sys.exit(f"ERREUR : --travail {a.travail} est dans le repo ; l'audio doit rester hors du repo (scratchpad).")
    try:
        podcast, liste = episodes(telecharger_flux(a.flux))
        choix = selectionner(liste, a)
    except (RuntimeError, OSError, ET.ParseError, re.error) as e:
        sys.exit(f"ERREUR : {e}")
    if not choix:
        sys.exit("ERREUR : aucun épisode ne correspond (vérifier avec lister.py)")
    if len(choix) > 1 and not a.slug:
        sys.exit(f"ERREUR : {len(choix)} épisodes retenus : --slug est obligatoire pour les regrouper en une source")
    slug = a.slug or slugifier(choix[0]["titre"])
    if slug != slugifier(slug):
        sys.exit(f"ERREUR : slug invalide « {slug} » (minuscules, chiffres, tirets : {slugifier(slug)})")
    langue = a.langue or ("en" if a.modele.endswith(".en") else None)
    if a.modele.endswith(".en") and langue != "en":
        sys.exit(f"ERREUR : le modèle {a.modele} ne transcrit que l'anglais ; prendre un modèle multilingue (ex. small)")

    total = sum(min(e["duree_s"] or 0, a.max_secondes or 1e12) for e in choix)
    estime = f"~{ts(total / VITESSE[a.modele])} de calcul estimé sur 4 cœurs" if a.modele in VITESSE else "durée de calcul inconnue"
    print(f"{len(choix)} épisode(s), {ts(total)} d'audio à transcrire, modèle {a.modele} ({estime}) -> {a.sortie / slug}")
    for i, e in enumerate(choix, 1):
        print(f"  {i:>3}. {(e['date'] or '?')[:10]}  {ts(e['duree_s'] or 0):>8}  {e['titre']}")
    sys.stdout.flush()
    if a.simuler:
        return
    if total > 3600 and not a.oui and sys.stdin.isatty():
        if input("Continuer ? [o/N] ").strip().lower() not in ("o", "oui", "y", "yes"):
            sys.exit(1)

    try:
        import faster_whisper  # noqa: F401
    except ImportError:
        sys.exit("ERREUR : faster-whisper manquant : pip install -q -r outils/podcast/requirements.txt")
    t0 = time.time()
    try:
        modele = charger_modele(a.modele, a.threads)
    except RuntimeError as e:
        sys.exit(f"ERREUR : {e}")
    print(f"modèle chargé en {time.time() - t0:.0f} s", flush=True)

    if a.travail:
        a.travail.mkdir(parents=True, exist_ok=True)
    reprise = Path(a.travail or tempfile.gettempdir()) / f"podcast-reprise-{slug}"
    if dans_repo(reprise):
        sys.exit(f"ERREUR : dossier de reprise {reprise} dans le repo ; passer --travail <scratchpad>")
    if a.sans_reprise:
        shutil.rmtree(reprise, ignore_errors=True)
    reprise.mkdir(parents=True, exist_ok=True)
    meta_eps, par_episode, decalage, calcul, langue_vue = [], [], 0.0, 0.0, None
    for i, e in enumerate(choix, 1):
        fichier_reprise = reprise / f"{cle_reprise(e, a)}.json"
        if fichier_reprise.exists():
            try:
                deja = json.loads(fichier_reprise.read_text(encoding="utf-8"))
                segs = [(decalage + t, txt) for t, txt in deja["segments"]]
                meta_eps.append(deja["meta"] | {"debut_dans_source_s": round(decalage, 1)})
                par_episode.append(segs)
                calcul += deja["calcul_s"]
                langue_vue = langue_vue or deja["meta"]["langue_detectee"]
                decalage += deja["meta"]["secondes_transcrites"]
                print(f"[{i}/{len(choix)}] {e['titre']} : déjà transcrit (reprise)", flush=True)
                continue
            except (ValueError, KeyError):
                fichier_reprise.unlink()
        tmp = Path(tempfile.mkdtemp(prefix="podcast-", dir=a.travail))  # dossier neuf par épisode
        if dans_repo(tmp):  # TMPDIR pointé dans le repo
            shutil.rmtree(tmp, ignore_errors=True)
            sys.exit(f"ERREUR : dossier de travail {tmp} dans le repo ; passer --travail <scratchpad>")
        try:
            t1 = time.time()
            audio = charger_audio(telecharger_audio(e, tmp, a.max_secondes), a.max_secondes)
            t_dl = time.time() - t1
        except Exception as err:  # noqa: BLE001
            shutil.rmtree(tmp, ignore_errors=True)
            sys.exit(f"ÉCHEC épisode {i} « {e['titre']} » : {err}")
        shutil.rmtree(tmp, ignore_errors=True)  # l'audio décodé reste en mémoire seulement
        secondes = len(audio) / TAUX
        t2 = time.time()
        segments, info = modele.transcribe(audio, language=langue, beam_size=5, vad_filter=True,
                                           condition_on_previous_text=False)
        relatifs = [(round(s.start, 2), propre(s.text)) for s in segments if propre(s.text)]
        segs = [(decalage + t, txt) for t, txt in relatifs]
        t_calc = time.time() - t2
        calcul += t_calc
        langue_vue = langue_vue or info.language
        m_ep = ({k: e[k] for k in ["titre", "date", "duree_s", "numero", "guid", "lien", "audio_url", "description"]}
                | {"chapitres": chapitres(e["description"]), "secondes_transcrites": round(secondes, 1),
                   "langue_detectee": info.language, "nb_segments": len(segs)})
        fichier_reprise.write_text(json.dumps({"meta": m_ep, "segments": relatifs, "calcul_s": round(t_calc, 1)},
                                              ensure_ascii=False), encoding="utf-8")
        meta_eps.append(m_ep | {"debut_dans_source_s": round(decalage, 1)})
        par_episode.append(segs)
        print(f"[{i}/{len(choix)}] {e['titre']} : {secondes:.0f} s d'audio, téléchargé+décodé en {t_dl:.0f} s, "
              f"transcrit en {t_calc:.0f} s (x{secondes / max(t_calc, 0.01):.1f} temps réel), {len(segs)} segments",
              flush=True)
        decalage += secondes

    meta = {"type": "podcast", "slug": slug,
            "titre": a.titre or (choix[0]["titre"] if len(choix) == 1 else f"{podcast['titre']} : {slug}"),
            "podcast": podcast, "flux": a.flux, "episodes": meta_eps,
            "duree_transcrite_s": round(decalage, 1), "max_secondes": a.max_secondes,
            "modele": a.modele, "langue_transcription": langue or langue_vue,
            "nb_segments": sum(len(s) for s in par_episode),
            "date_transcription": datetime.date.today().isoformat(),
            "vitesse_temps_reel": round(decalage / max(calcul, 0.01), 2)}
    d = a.sortie / slug
    ecrire(d, meta, par_episode)
    shutil.rmtree(reprise, ignore_errors=True)
    print(f"OK {slug} -> {d} ({meta['nb_segments']} segments, {ts(decalage)} d'audio en {ts(calcul)} de calcul, "
          f"x{meta['vitesse_temps_reel']} temps réel)")


if __name__ == "__main__":
    main()
