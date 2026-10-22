# outils/podcast — flux RSS et transcription d'épisodes (faster-whisper, CPU)

Pour `transcripteur-audio` : lister les épisodes d'un podcast (flux RSS officiel), puis transcrire ceux qu'on
choisit dans **une seule source** `sources/podcast/<slug>/`, au format de `outils/youtube/transcrire.py`.
Scripts autonomes (aucun import entre eux), lancés avec `python3 -I` depuis n'importe quel dossier.

Dernier test : **2026-10-22** (flux *The Game with Alex Hormozi*, 60 s d'un épisode, 2 épisodes × 20 s regroupés).

## Installation (une fois par conteneur)

```bash
pip install -q -r outils/podcast/requirements.txt
```

`lister.py` n'a besoin que de la bibliothèque standard. `transcrire.py` a besoin de faster-whisper (le
décodage audio passe par PyAV, fourni avec : **pas de ffmpeg requis**). Le modèle Whisper (~480 Mo pour
`small.en`) est téléchargé depuis Hugging Face au premier usage, dans `~/.cache/huggingface/` (hors repo),
puis réutilisé sans appel réseau.

Variables d'environnement : aucune obligatoire (pas de clé API). Facultatif : `HF_HOME` pour déplacer le
cache des modèles, `TMPDIR` pour le dossier temporaire par défaut (doit rester hors du repo).

## 1. `lister.py` — lister / filtrer les épisodes d'un flux

```bash
python3 -I outils/podcast/lister.py <url-ou-fichier-rss> [--motif REGEX] [--exclure REGEX]
        [--ordre flux|date|titre] [--limite N] [--format table|tsv|json] [--urls]
```

- `--motif` / `--exclure` : expressions régulières sur le titre, sans casse. Mettre le motif entre
  **apostrophes** et échapper le dollar : `'\$100M'`.
- `--ordre titre` : tri naturel (Part 1, Part 2 … Part 10, Part 11). `date` : plus ancien d'abord.
- `--format tsv` : `rang_flux, date, duree_s, numero, guid, titre, audio_url` (une ligne par épisode).
  `json` : infos du podcast + épisodes complets (avec description).
- N'écrit rien. Code de sortie : 0 si au moins un épisode, 1 si aucun, 2 si erreur (réseau, XML, regex).

## 2. `transcrire.py` — télécharger et transcrire des épisodes choisis

```bash
python3 -I outils/podcast/transcrire.py <url-ou-fichier-rss> --motif REGEX --slug SLUG \
        [--exclure REGEX] [--ordre titre|date|flux] [--titre TITRE] \
        [--sortie DOSSIER] [--travail DOSSIER] [--max-secondes N] \
        [--modele small.en] [--beam 5] [--langue en] [--threads N] [--oui] [--simuler] [--sans-reprise]
# ou par épisodes précis, dans l'ordre donné :
python3 -I outils/podcast/transcrire.py <flux> --guid GUID1 --guid GUID2 --slug SLUG
```

- **Sélection** : `--motif` (ordre par défaut : `titre`, tri naturel) ou `--guid` répétable (ordre des
  arguments). Toujours vérifier d'abord avec `lister.py` ou `--simuler` (affiche la sélection numérotée,
  l'ordre, la durée et le temps de calcul estimé, sans rien télécharger).
- **Plusieurs épisodes = une seule source**, dans l'ordre, sur une horloge continue ; `--slug` obligatoire.
- `--sortie DOSSIER` : dossier parent (défaut `<repo>/sources/podcast`) → écrit `<DOSSIER>/<slug>/`.
- `--travail DOSSIER` : où l'audio est téléchargé (défaut : dossier temporaire du système). **Refusé s'il est
  dans le repo.** Chaque épisode est téléchargé dans un sous-dossier neuf (`podcast-XXXX/audio.bin`, nom fixe),
  décodé en mémoire, puis le sous-dossier est supprimé **avant** la transcription. L'audio n'est jamais exécuté
  ni écrit dans la sortie.
- `--max-secondes N` : ne télécharge (partiellement) et ne transcrit que les N premières secondes de
  chaque épisode — pour les tests.
- `--oui` : pas de question de confirmation au-delà d'une heure d'audio (la question n'est posée que si le
  terminal est interactif ; un agent n'est donc pas bloqué).
- **Reprise après coupure** : chaque épisode terminé est mis de côté (texte seulement) dans
  `<travail ou /tmp>/podcast-reprise-<slug>/`. Relancer **la même commande** (même `--travail`) reprend au
  premier épisode manquant. Le dossier est supprimé quand la source est écrite. `--sans-reprise` repart de zéro.
  Indispensable pour un livre entier : une commande en arrière-plan est coupée au bout de 2 h.

### Fichiers produits (`<sortie>/<slug>/`)

- `transcription.md` : `# titre`, lignes d'en-tête (podcast, durée, flux, modèle), `## Épisodes` (début de
  chaque épisode dans la source), `## Chapitres` si les descriptions du flux donnent des horodatages
  `(12:34) - Titre`, puis `## Transcription` : blocs `**[mm:ss]** texte` (ou `**[hh:mm:ss]**`) d'environ 30 s
  séparés d'une ligne vide, un intertitre `### Épisode i/N · <titre> (début hh:mm:ss)` avant chaque épisode
  quand il y en a plusieurs.
- `metadata.json` : `type`, `slug`, `titre`, `podcast` (titre, auteur, lien, langue), `flux`, `episodes[]`
  (titre, date, duree_s, numero, guid, lien, audio_url, description, chapitres, secondes_transcrites,
  langue_detectee, nb_segments, debut_dans_source_s), `duree_transcrite_s`, `max_secondes`, `modele`, `beam`,
  `langue_transcription`, `nb_segments`, `date_transcription`, `vitesse_temps_reel`.

### Découpe (plus de 15 000 mots)

```bash
python3 -I outils/youtube/decouper.py sources/podcast/<slug> 15000   # -> sources/podcast/<slug>/parties/
```

Les intertitres d'épisode restent collés au bloc qui les suit ; la plage affichée va du premier bloc de la
partie au début de la partie suivante.

## Modèle et vitesse mesurée (CPU 4 cœurs, int8, 2026-10-22)

VITESSE_A_REMPLIR

Défaut : **`small.en`, beam 5** — meilleur compromis qualité/vitesse pour de l'anglais parlé clairement
(livre audio lu par l'auteur). Contenu non anglais : `--modele small` (multilingue, détection automatique ou
`--langue fr`). Accent marqué ou audio de mauvaise qualité : `--modele medium` (≈ 3 fois plus lent).

## Exemple réel : livres audio d'Alex Hormozi (flux officiel *The Game*)

Flux : `https://rss2.flightcast.com/zz5nwp81tktx53wb8fw6qq7j.xml` (1 158 épisodes au 2026-10-22).
Le flux contient des **doublons** (rediffusions 2026 « $100M Offers Audiobook Part N », « … Part 3 | Ep 581 ») :
les motifs ci-dessous ne retiennent que la série complète d'origine.

| Livre | Motif | Épisodes | Audio |
|---|---|---|---|
| $100M Offers | `'^Part \d+: \$100M Offers Book$'` | 7 | 4:05:01 |
| $100M Leads | `'\| \$100M Leads Book$'` | 11 | 6:26:05 |
| $100M Money Models | `'^Part \d+: .*\$100M Money Models'` | 9 | 3:46:35 |

```bash
F=https://rss2.flightcast.com/zz5nwp81tktx53wb8fw6qq7j.xml
python3 -I outils/podcast/transcrire.py $F --motif '^Part \d+: \$100M Offers Book$' \
  --slug hormozi-100m-offers --titre '$100M Offers (Alex Hormozi, livre audio)' \
  --travail <scratchpad>/travail-podcast --oui
```

## Limites connues

- Transcription automatique : noms propres, chiffres (« 100 million dollar » pour *$100M*) et termes
  techniques à relire ; pas de séparation des locuteurs.
- `--max-secondes` télécharge un début de fichier estimé d'après la taille annoncée ; un MP3 à débit
  variable peut donner un peu moins que N secondes.
- L'audio décodé d'un épisode est gardé en mémoire (~230 Mo par heure d'audio).
- Seuls les flux RSS publics (champ `<enclosure>`) sont gérés ; pas de flux privé à identifiant, pas de
  Spotify/Apple (pas de téléchargement autorisé).
- La reprise se fait par épisode : un épisode interrompu en cours de route est retranscrit en entier.
