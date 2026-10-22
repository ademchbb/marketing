#!/usr/bin/env python3
"""Découpe la transcription.md d'une source en parties d'environ N mots
(coupe sur un bloc horodaté) pour qu'un agent puisse analyser chaque partie à fond.

Usage : python3 -I outils/youtube/decouper.py <id-youtube | dossier-source> [mots_par_partie=12000]
  <id-youtube>      ex. dQw4w9WgXcQ            -> sources/youtube/<id>/
  <dossier-source>  ex. sources/podcast/<slug>  (chemin relatif au repo ou au dossier courant, ou absolu)
Écrit <source>/parties/partie-NN.md (anciennes parties supprimées) et affiche la plage horaire de chacune.
Les intertitres « ### … » (un par épisode dans les sources podcast) restent collés au bloc qui les suit.
"""
import re, sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
HORO = re.compile(r"\*\*\[([\d:]+)\]")


def dossier_source(arg: str) -> Path:
    if "/" not in arg and "\\" not in arg:  # un id YouTube ne contient jamais de « / »
        return RACINE / "sources" / "youtube" / arg
    p = Path(arg).expanduser()
    for cand in ([p] if p.is_absolute() else [Path.cwd() / p, RACINE / p]):
        if (cand / "transcription.md").is_file():
            return cand.resolve()
    sys.exit(f"ERREUR : pas de transcription.md dans {arg}")


def main(arg, taille=12000):
    d = dossier_source(arg)
    if not (d / "transcription.md").is_file():
        sys.exit(f"ERREUR : {d / 'transcription.md'} introuvable")
    texte = (d / "transcription.md").read_text(encoding="utf-8")
    entete, _, corps = texte.partition("## Transcription")
    blocs, titre = [], None
    for b in (b.strip() for b in corps.strip().split("\n\n")):
        if not b:
            continue
        if b.startswith("#"):  # intertitre : collé au bloc suivant
            titre = b if titre is None else titre + "\n\n" + b
            continue
        blocs.append(b if titre is None else titre + "\n\n" + b)
        titre = None
    if titre:
        blocs.append(titre)
    parties, cur, n = [], [], 0
    for b in blocs:
        cur.append(b); n += len(b.split())
        if n >= taille:
            parties.append(cur); cur, n = [], 0
    if cur:
        parties.append(cur)
    (d / "parties").mkdir(exist_ok=True)
    for ancien in (d / "parties").glob("partie-*.md"):
        ancien.unlink()
    for i, p in enumerate(parties, 1):
        debut = HORO.search(p[0]); fin = HORO.search(p[-1])
        plage = f"{debut.group(1) if debut else '?'} → {fin.group(1) if fin else '?'}"
        (d / "parties" / f"partie-{i:02d}.md").write_text(
            entete.strip() + f"\n\n## Partie {i}/{len(parties)} ({plage})\n\n" + "\n\n".join(p) + "\n", encoding="utf-8")
        print(f"partie-{i:02d}.md  {plage}  {sum(len(b.split()) for b in p)} mots")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 12000)
