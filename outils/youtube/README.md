# outils/youtube — transcription de vidéos YouTube et découpe des transcriptions

Scripts autonomes, lancés avec `python3 -I` depuis n'importe quel dossier. Dernier test : **2026-10-22**.

```bash
pip install -q -r outils/youtube/requirements.txt   # yt-dlp, youtube-transcript-api (versions fixées)
```

Aucune variable d'environnement ni clé API. Aucun média téléchargé : seuls les sous-titres (dossier temporaire
supprimé à la fin).

## `transcrire.py` — sous-titres + métadonnées d'une ou plusieurs vidéos

```bash
python3 -I outils/youtube/transcrire.py <url-ou-id> [<url-ou-id> …] [--sortie DOSSIER]
```

- Écrit `sources/youtube/<id>/` (ou `<DOSSIER>/<id>/` avec `--sortie`, pour tester hors du repo) :
  `metadata.json` (titre, chaîne, durée, date, vues, description, chapitres, tags, langue) et
  `transcription.md` (en-tête, `## Chapitres` si présents, `## Transcription` : blocs `**[mm:ss]** texte`
  d'environ 30 s séparés d'une ligne vide).
- Stratégie : yt-dlp (sous-titres manuels > automatiques « -orig » > automatiques), puis
  youtube-transcript-api en secours ; 5 tentatives espacées (YouTube renvoie parfois 429 depuis le cloud).
- Texte nettoyé : balises retirées, codes HTML décodés (`&gt;&gt;` → `>>` = changement de locuteur,
  `&amp;` → `&`, `&#39;` → `'`), espaces insécables remplacés (correctif du 2026-10-22 ; les transcriptions
  antérieures en contiennent encore, les régénérer si besoin).
- Code de sortie : 0 si toutes les vidéos ont une transcription, 1 sinon (message `ÉCHEC <id>`).

## `decouper.py` — découpe en parties d'environ N mots

```bash
python3 -I outils/youtube/decouper.py <id> [mots=12000]                    # sources/youtube/<id>/
python3 -I outils/youtube/decouper.py sources/podcast/<slug> [mots=12000]  # toute source au même format
```

- Écrit `<source>/parties/partie-NN.md` : en-tête de la source + `## Partie i/N (début → fin)` + blocs.
  Les anciens `partie-*.md` sont remplacés (aucun autre fichier du dossier n'est touché).
- Plage affichée : du début du premier bloc au **début de la partie suivante** (fin de la source pour la
  dernière). Avant le 2026-10-22, la fin affichée était le début du dernier bloc, ce qui faisait croire à un
  trou de ~30 s entre deux parties : il n'y en avait pas (contenu identique, vérifié bloc à bloc).
- Les intertitres `### …` (un par épisode dans les sources podcast) restent collés au bloc qui les suit.

## Limites connues

- Sous-titres automatiques : ponctuation pauvre, noms propres approximatifs.
- Pas de sous-titres du tout : passer par `transcripteur-audio` (Whisper local, voir `outils/podcast/`).
