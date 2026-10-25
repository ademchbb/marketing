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
  --vocabulaire TEXTE noms propres et termes à bien orthographier, séparés par des virgules
                      (défaut : auteur du podcast d'après le flux, ex. « Alex Hormozi » ; "" pour aucun)
  --beam N            largeur de faisceau (défaut 5 : qualité ; 1 : ~1,8 fois plus rapide, voir README)
  --seuil-fuite N     contrôle : un segment qui reprend N mots consécutifs ou plus du vocabulaire, à cheval
                      sur deux termes (« $100M Offers, Grand Slam Offer »), est une fuite du vocabulaire
                      (défaut 4 ; 0 : pas de détection)
  --trou-secondes S   contrôle : parole détectée (VAD) sans aucun texte pendant S s ou plus = passage sauté
                      (défaut 6 ; 0 : pas de détection). Fuites et trous sont retranscrits SANS vocabulaire,
                      consignés dans le journal, metadata.json et un commentaire <!-- contrôle … --> (voir README)
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
import argparse, datetime, email.utils, hashlib, html, json, os, re, shutil, signal, sys, tempfile, time, unicodedata
import urllib.error, urllib.request
from bisect import bisect_left
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
    try:
        racine = ET.fromstring(contenu)
    except ET.ParseError as e:
        debut = contenu[:80].decode("utf-8", "replace").strip() or "(vide)"
        raise RuntimeError(f"le contenu reçu n'est pas du XML ({e}) ; début : {debut!r}. URL du flux à vérifier") from e
    canal = racine.find("channel")
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


# ---------- contrôle : fuites du vocabulaire et passages sautés ----------
# faster-whisper place --vocabulaire (hotwords) dans le contexte « texte précédent » de CHAQUE fenêtre de 30 s.
# Il arrive que le modèle recopie ce contexte au lieu d'écouter, puis termine la fenêtre : le vocabulaire
# apparaît dans le texte et le reste de la fenêtre (jusqu'à 30 s de parole) disparaît. On repère donc
# (1) les segments qui recopient le vocabulaire, (2) la parole détectée sans texte, et on retranscrit ces
# passages sans vocabulaire.

MOT = re.compile(r"\w+(?:['’.,]\w+)*")


def suite_vocabulaire(vocabulaire):
    """Mots du vocabulaire mis bout à bout (deux tours : une répétition est aussi une fuite) + fins de terme."""
    termes = [[m.casefold() for m in MOT.findall(t)] for t in (vocabulaire or "").split(",")]
    termes = [t for t in termes if t]
    seq, fins = [], set()
    for _ in range(2):
        for t in termes:
            seq += t
            fins.add(len(seq) - 1)
    return seq, fins


def fuites(texte, seq, fins, n):
    """Passages de texte qui reprennent >= n mots consécutifs de la suite du vocabulaire en franchissant
    une limite entre deux termes -> [(début, fin) en caractères]. Un terme seul (« Grand Slam Offer ») passe."""
    if not seq or not n:
        return []
    toks = [(m.group().casefold(), m.start(), m.end()) for m in MOT.finditer(texte)]
    trouve, i = [], 0
    while i < len(toks):
        meilleur = 0
        for j, w in enumerate(seq):
            if w != toks[i][0]:
                continue
            k = 1
            while i + k < len(toks) and j + k < len(seq) and toks[i + k][0] == seq[j + k]:
                k += 1
            if k >= n and k > meilleur and any(j <= f < j + k - 1 for f in fins):
                meilleur = k
        if meilleur:
            trouve.append((toks[i][1], toks[i + meilleur - 1][2]))
            i += meilleur
        else:
            i += 1
    return trouve


def retirer(texte, passages):
    for d, f in reversed(passages):
        while f < len(texte) and texte[f] in ",.;:!?":
            f += 1
        texte = texte[:d] + texte[f:]
    return re.sub(r"\s+([,.;:!?])", r"\1", re.sub(r"\s{2,}", " ", texte)).strip()


def nb_mots(segs):
    return sum(len(s[-1].split()) for s in segs)


def parole_vad(audio):
    from faster_whisper.vad import VadOptions, get_speech_timestamps  # mêmes réglages que vad_filter=True
    return [(c["start"] / TAUX, c["end"] / TAUX) for c in get_speech_timestamps(audio, VadOptions())]


def trous(parole, segs, seuil):
    """Intervalles de parole (VAD) non couverts par un segment, d'au moins `seuil` secondes."""
    couvert, res = sorted((s, e) for s, e, _ in segs), []
    for p0, p1 in parole:
        t = p0
        for s, e in couvert:
            if e <= t or s >= p1:
                continue
            if s - t >= seuil:
                res.append((t, s))
            t = max(t, e)
        if p1 - t >= seuil:
            res.append((t, p1))
    return res


def controler(modele, audio, segs, options, vocabulaire, seuil_fuite, seuil_trou):
    """segs : [(début, fin, texte)] relatifs à l'épisode. Retranscrit sans vocabulaire chaque passage suspect
    (segment qui recopie le vocabulaire, ou parole sans texte) avec un segment de marge de chaque côté.
    -> (segments [(début, texte)] avec commentaires <!-- contrôle … -->, liste des contrôles pour metadata)."""
    duree = len(audio) / TAUX
    seq, fins = suite_vocabulaire(vocabulaire)
    starts = [s for s, _, _ in segs]
    zones = []  # [t0, t1, raisons]
    for k, (s, e, t) in enumerate(segs):
        f = fuites(t, seq, fins, seuil_fuite)
        if f:
            t0 = segs[k - 1][0] if k > 0 else 0.0
            t1 = segs[k + 1][1] if k + 1 < len(segs) else duree
            zones.append([t0, t1, ["fuite du vocabulaire : « " + " / ".join(t[d:g] for d, g in f) + " »"]])
    if seuil_trou:
        for u0, u1 in trous(parole_vad(audio), segs, seuil_trou):
            k = bisect_left(starts, u0) - 1  # dernier segment commencé avant le trou
            t0 = segs[k][0] if k >= 0 else max(0.0, u0 - 1)
            t1 = segs[k + 1][1] if k + 1 < len(segs) else min(duree, u1 + 1)
            zones.append([t0, max(t1, u1), [f"trou : {u1 - u0:.0f} s de parole sans texte à partir de {ts(u0)}"]])
    fusion = []
    for z in sorted(zones):
        if fusion and z[0] <= fusion[-1][1]:
            fusion[-1][1] = max(fusion[-1][1], z[1])
            fusion[-1][2] += z[2]
        else:
            fusion.append(z)
    sortie = [[s, e, t] for s, e, t in segs]
    controles, a_inserer = [], []
    for t0, t1, raisons in fusion:
        t0, t1 = max(0.0, t0 - 0.2), min(duree, t1 + 0.2)
        dedans = [x for x in sortie if t0 <= (x[0] + x[1]) / 2 <= t1]
        nettoye = [(s, e, retirer(t, fuites(t, seq, fins, seuil_fuite))) for s, e, t in dedans]
        morceau, _ = modele.transcribe(audio[int(t0 * TAUX):int(t1 * TAUX)], **options)
        neufs = [(round(t0 + s.start, 2), round(t0 + s.end, 2), propre(s.text)) for s in morceau if propre(s.text)]
        fuite = any("fuite" in r for r in raisons)
        if nb_mots(neufs) >= 0.8 * nb_mots(nettoye) and nb_mots(neufs) > (0 if fuite else nb_mots(nettoye)):
            action, garde = "retranscrit sans vocabulaire", neufs
        elif fuite:
            action, garde = "fuite retirée (la retranscription sans vocabulaire était moins complète)", nettoye
        else:
            action, garde = "inchangé : pas de parole supplémentaire reconnue (musique, silence ?)", None
        c = {"debut_s": round(t0, 1), "fin_s": round(t1, 1), "raisons": raisons, "action": action,
             "mots_avant": nb_mots(dedans), "mots_apres": nb_mots(garde if garde is not None else dedans)}
        controles.append(c)
        if garde is not None:
            ids = {id(x) for x in dedans}
            sortie = [x for x in sortie if id(x) not in ids]
            sortie += [[s, e, t] for s, e, t in garde if t]
            a_inserer.append((t0, f"<!-- contrôle {ts(t0)}–{ts(t1)} : {' ; '.join(raisons)} -> {action} "
                                  f"({c['mots_avant']} -> {c['mots_apres']} mots) -->"))
    sortie.sort(key=lambda x: x[0])
    res = [(round(s, 2), t) for s, _, t in sortie]
    for t, com in a_inserer:  # le commentaire précède le passage retranscrit
        res.insert(bisect_left([x[0] for x in res], t), (round(t, 2), com))
    return res, controles


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
              f"- Transcription : faster-whisper {meta['modele']} beam {meta.get('beam', 5)} (CPU, automatique, à relire), langue {meta['langue_transcription']}"]
    ctl = [c for e in eps for c in e.get("controles", [])]
    faits = [c for c in ctl if not c["action"].startswith("inchangé")]
    lignes.append(f"- Contrôle vocabulaire / passages sautés : {len(faits)} passage(s) corrigé(s), signalés par "
                  f"<!-- contrôle … --> ; {len(ctl) - len(faits)} trou(s) sans parole reconnue (metadata.json)"
                  if ctl else "- Contrôle vocabulaire / passages sautés : rien à corriger")
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
    ap.add_argument("--beam", type=int, default=5)
    ap.add_argument("--vocabulaire")
    ap.add_argument("--seuil-fuite", type=int, default=4)
    ap.add_argument("--trou-secondes", type=float, default=6.0)
    ap.add_argument("--oui", action="store_true")
    ap.add_argument("--simuler", action="store_true")
    ap.add_argument("--sans-reprise", action="store_true")
    return ap.parse_args()


# x temps réel, beam 5, int8, 4 cœurs (mesures du README, 2026-10-22) ; beam 1 : environ x1,8
VITESSE = {"small.en": 2.34, "distil-small.en": 4.59, "base.en": 5.06}


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
    return hashlib.sha1(json.dumps([e["guid"], e["audio_url"], a.modele, a.langue, a.max_secondes, a.beam, a.vocabulaire,
                                  a.seuil_fuite, a.trou_secondes, "controle-v1"]).encode()).hexdigest()[:16]


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
    vocabulaire = podcast["auteur"] if a.vocabulaire is None else a.vocabulaire.strip()
    if a.modele.endswith(".en") and langue != "en":
        sys.exit(f"ERREUR : le modèle {a.modele} ne transcrit que l'anglais ; prendre un modèle multilingue (ex. small)")

    total = sum(min(e["duree_s"] or 0, a.max_secondes or 1e12) for e in choix)
    if a.modele in VITESSE:
        x = VITESSE[a.modele] * (1.8 if a.beam == 1 else 1)
        estime = f"~{ts(total / x)} de calcul estimé sur 4 cœurs (x{x:.1f} temps réel)"
    else:
        estime = "durée de calcul non mesurée pour ce modèle"
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
    signal.signal(signal.SIGTERM, lambda *_: sys.exit("ARRÊT (SIGTERM) : relancer la même commande pour reprendre"))
    if a.travail:  # restes d'un lancement tué brutalement (SIGKILL, coupure) : audio abandonné depuis 10 min
        for vieux in a.travail.glob("podcast-*"):
            if vieux.is_dir() and not vieux.name.startswith("podcast-reprise-") and \
                    all(time.time() - f.stat().st_mtime > 600 for f in [vieux, *vieux.iterdir()]):
                shutil.rmtree(vieux, ignore_errors=True)
                print(f"nettoyé : {vieux} (reste d'un lancement interrompu)")
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
            sys.exit(f"ÉCHEC épisode {i} « {e['titre']} » : {err}")
        finally:  # aussi sur SIGTERM / Ctrl-C : l'audio ne survit jamais à l'étape de décodage
            shutil.rmtree(tmp, ignore_errors=True)
        secondes = len(audio) / TAUX
        t2 = time.time()
        options = dict(language=langue, beam_size=a.beam, vad_filter=True, condition_on_previous_text=False)
        segments, info = modele.transcribe(audio, hotwords=vocabulaire or None, **options)
        bruts = [(round(s.start, 2), round(s.end, 2), propre(s.text)) for s in segments if propre(s.text)]
        relatifs, controles = controler(modele, audio, bruts, options, vocabulaire, a.seuil_fuite, a.trou_secondes)
        for c in controles:
            print(f"  contrôle [{ts(decalage + c['debut_s'])}–{ts(decalage + c['fin_s'])}] {' ; '.join(c['raisons'])}"
                  f" -> {c['action']} ({c['mots_avant']} -> {c['mots_apres']} mots)", flush=True)
        segs = [(decalage + t, txt) for t, txt in relatifs]
        t_calc = time.time() - t2
        calcul += t_calc
        langue_vue = langue_vue or info.language
        m_ep = ({k: e[k] for k in ["titre", "date", "duree_s", "numero", "guid", "lien", "audio_url", "description"]}
                | {"chapitres": chapitres(e["description"]), "secondes_transcrites": round(secondes, 1),
                   "langue_detectee": info.language, "nb_segments": sum(not t.startswith("<!--") for _, t in segs),
                   "controles": controles})
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
            "modele": a.modele, "beam": a.beam, "vocabulaire": vocabulaire, "langue_transcription": langue or langue_vue,
            "nb_segments": sum(e["nb_segments"] for e in meta_eps),
            "seuil_fuite": a.seuil_fuite, "trou_secondes": a.trou_secondes,
            "date_transcription": datetime.date.today().isoformat(),
            "vitesse_temps_reel": round(decalage / max(calcul, 0.01), 2)}
    d = a.sortie / slug
    ecrire(d, meta, par_episode)
    shutil.rmtree(reprise, ignore_errors=True)
    print(f"OK {slug} -> {d} ({meta['nb_segments']} segments, {ts(decalage)} d'audio en {ts(calcul)} de calcul, "
          f"x{meta['vitesse_temps_reel']} temps réel)")


if __name__ == "__main__":
    main()
