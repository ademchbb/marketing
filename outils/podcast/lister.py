#!/usr/bin/env python3
"""Liste les épisodes d'un flux RSS de podcast, filtrés par motif de titre.

Usage : python3 -I outils/podcast/lister.py <url-ou-fichier-rss> [options]

Options :
  --motif REGEX     garde les titres qui correspondent (expression régulière, sans casse)
  --exclure REGEX   retire les titres qui correspondent (sans casse)
  --ordre ORDRE     flux (défaut, ordre du flux) | date (plus ancien d'abord) | titre (tri naturel)
  --limite N        n'affiche que les N premiers résultats
  --format FORMAT   table (défaut, lisible) | tsv (une ligne par épisode, avec guid et URL audio) | json
  --urls            en format table, affiche aussi l'URL audio sous chaque épisode

N'écrit rien : affiche sur la sortie standard. Bibliothèque standard uniquement
(urllib + xml.etree). Code de sortie : 0 si au moins un épisode, 1 si aucun, 2 si erreur.
"""
import argparse, email.utils, html, json, re, sys, time, urllib.error, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ITUNES = "{http://www.itunes.com/dtds/podcast-1.0.dtd}"
AGENT = "Mozilla/5.0 (compatible; outils-podcast/1.0)"
TENTATIVES = 4


def telecharger_flux(source: str) -> bytes:
    """Contenu brut du flux : fichier local ou URL https (nouvelles tentatives espacées)."""
    if not re.match(r"https?://", source):
        return Path(source).read_bytes()
    erreur = None
    for i in range(TENTATIVES):
        try:
            req = urllib.request.Request(source, headers={"User-Agent": AGENT})
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            erreur = e
            if isinstance(e, urllib.error.HTTPError) and e.code in (401, 403, 404, 407, 410):
                break  # inutile d'insister (accès refusé, proxy ou introuvable)
            time.sleep(2 ** (i + 1))
    raise RuntimeError(f"flux injoignable ({source}) : {erreur}. Erreur TLS ou proxy : voir /root/.ccr/README.md")


def duree_s(texte):
    """itunes:duration -> secondes (accepte « 3261 », « 54:21 », « 1:02:03 »)."""
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
    """Codes HTML, balises et espaces insécables -> texte brut."""
    t = html.unescape(re.sub(r"<br\s*/?>|</p>", "\n", texte or "", flags=re.I))
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"[\u00a0\u2007\u202f\u200b\u2060]", " ", t)
    return "\n".join(re.sub(r"[ \t]+", " ", l).strip() for l in t.splitlines()).strip()


def episodes(contenu: bytes):
    """Flux RSS -> (infos du podcast, liste d'épisodes dans l'ordre du flux)."""
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
            "rang_flux": rang,
            "titre": propre(it.findtext("title")),
            "date": date_iso(it.findtext("pubDate")),
            "duree_s": duree_s(it.findtext(f"{ITUNES}duration")),
            "numero": it.findtext(f"{ITUNES}episode"),
            "saison": it.findtext(f"{ITUNES}season"),
            "guid": (it.findtext("guid") or "").strip(),
            "lien": it.findtext("link"),
            "audio_url": enc.get("url") if enc is not None else None,
            "audio_type": enc.get("type") if enc is not None else None,
            "description": propre(it.findtext("description") or it.findtext(f"{ITUNES}summary")),
        })
    return podcast, liste


def cle_naturelle(titre: str):
    return [int(x) if x.isdigit() else x.casefold() for x in re.split(r"(\d+)", titre)]


def filtrer(liste, motif=None, exclure=None, ordre="flux"):
    if motif:
        liste = [e for e in liste if re.search(motif, e["titre"], re.I)]
    if exclure:
        liste = [e for e in liste if not re.search(exclure, e["titre"], re.I)]
    if ordre == "date":
        liste = sorted(liste, key=lambda e: (e["date"] or "", -e["rang_flux"]))
    elif ordre == "titre":
        liste = sorted(liste, key=lambda e: cle_naturelle(e["titre"]))
    return liste


def hms(s):
    if s is None:
        return "?"
    s = int(s)
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    ap = argparse.ArgumentParser(description="Liste et filtre les épisodes d'un flux RSS de podcast.")
    ap.add_argument("flux")
    ap.add_argument("--motif")
    ap.add_argument("--exclure")
    ap.add_argument("--ordre", choices=["flux", "date", "titre"], default="flux")
    ap.add_argument("--limite", type=int)
    ap.add_argument("--format", choices=["table", "tsv", "json"], default="table")
    ap.add_argument("--urls", action="store_true")
    a = ap.parse_args()
    try:
        podcast, liste = episodes(telecharger_flux(a.flux))
        choix = filtrer(liste, a.motif, a.exclure, a.ordre)
    except (RuntimeError, OSError, ET.ParseError, re.error) as e:
        print(f"ERREUR : {e}", file=sys.stderr)
        sys.exit(2)
    if a.limite:
        choix = choix[: a.limite]
    if a.format == "json":
        print(json.dumps({"podcast": podcast, "nb_total": len(liste), "episodes": choix}, ensure_ascii=False, indent=2))
    elif a.format == "tsv":
        print("rang_flux\tdate\tduree_s\tnumero\tguid\ttitre\taudio_url")
        for e in choix:
            print("\t".join(str(e[k] or "") for k in ["rang_flux", "date", "duree_s", "numero", "guid", "titre", "audio_url"]))
    else:
        total = sum(e["duree_s"] or 0 for e in choix)
        print(f"{podcast['titre']} · {len(choix)}/{len(liste)} épisodes · durée cumulée {hms(total)}\n")
        for e in choix:
            print(f"{e['rang_flux']:>5}  {(e['date'] or '?')[:10]}  {hms(e['duree_s']):>8}  {e['numero'] or '-':>5}  {e['titre']}")
            if a.urls:
                print(f"{'':>7}{e['audio_url']}")
    sys.exit(0 if choix else 1)


if __name__ == "__main__":
    main()
