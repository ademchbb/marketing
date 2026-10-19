#!/usr/bin/env python3
"""Découpe sources/youtube/<id>/transcription.md en parties d'environ N mots
(coupe sur un bloc horodaté) pour qu'un agent puisse analyser chaque partie à fond.

Usage : python3 outils/youtube/decouper.py <id> [mots_par_partie=12000]
Écrit sources/youtube/<id>/parties/partie-NN.md et affiche la plage horaire de chacune.
"""
import re, sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]


def main(vid, taille=12000):
    d = RACINE / "sources" / "youtube" / vid
    texte = (d / "transcription.md").read_text(encoding="utf-8")
    entete, _, corps = texte.partition("## Transcription")
    blocs = [b for b in corps.strip().split("\n\n") if b.strip()]
    parties, cur, n = [], [], 0
    for b in blocs:
        cur.append(b); n += len(b.split())
        if n >= taille:
            parties.append(cur); cur, n = [], 0
    if cur:
        parties.append(cur)
    (d / "parties").mkdir(exist_ok=True)
    for i, p in enumerate(parties, 1):
        debut = re.match(r"\*\*\[([\d:]+)\]", p[0]); fin = re.match(r"\*\*\[([\d:]+)\]", p[-1])
        plage = f"{debut.group(1) if debut else '?'} → {fin.group(1) if fin else '?'}"
        (d / "parties" / f"partie-{i:02d}.md").write_text(
            entete.strip() + f"\n\n## Partie {i}/{len(parties)} ({plage})\n\n" + "\n\n".join(p) + "\n", encoding="utf-8")
        print(f"partie-{i:02d}.md  {plage}  {sum(len(b.split()) for b in p)} mots")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 12000)
