# outils/podcast — flux RSS et transcription d'épisodes (faster-whisper, CPU)

Pour `transcripteur-audio` : lister les épisodes d'un podcast (flux RSS officiel), puis transcrire ceux qu'on
choisit dans **une seule source** `sources/podcast/<slug>/`, au format de `outils/youtube/transcrire.py`.
Scripts autonomes (aucun import entre eux), lancés avec `python3 -I` depuis n'importe quel dossier.

Dernier test : **2026-10-25** (contrôle du vocabulaire : 150 s des parties 3 et 4 de *$100M Offers*, 3 passages
réparés ; reprise après SIGTERM sans vocabulaire, 2 épisodes × 45 s). Test précédent 2026-10-22 : 60 s d'un épisode ;
3 épisodes × 20 s regroupés, coupés par SIGTERM puis repris ; découpe de la source obtenue.

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
        [--modele small.en] [--beam 5] [--langue en] [--vocabulaire 'Nom, Terme'] [--seuil-fuite 4] [--trou-secondes 6] \
        [--threads N] [--oui] [--simuler] [--sans-reprise]
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
- `--vocabulaire 'Alex Hormozi, Leila Hormozi, $100M Offers'` : noms propres et termes à bien orthographier
  (`hotwords` de faster-whisper, appliqué à chaque fenêtre). Défaut : l'auteur du podcast lu dans le flux ;
  `--vocabulaire ''` pour aucun. Test : sans vocabulaire « Alex Hermosi », « 100 million dollar money models » ;
  avec, « Alex Hormozi », « $100M Money Models », « $250,000 ». Effet de bord observé : « by a mile » est devenu
  « Buy a Mile » : garder la liste courte (noms propres, titres). Effet de bord grave, désormais corrigé
  automatiquement : voir « Contrôle du vocabulaire » ci-dessous.
- `--seuil-fuite N` (défaut 4, `0` : désactivé) et `--trou-secondes S` (défaut 6, `0` : désactivé) : réglages du
  contrôle ci-dessous. Les valeurs par défaut conviennent ; ne les changer que pour un diagnostic.
- `--oui` : pas de question de confirmation au-delà d'une heure d'audio (la question n'est posée que si le
  terminal est interactif ; un agent n'est donc pas bloqué).
- **Reprise après coupure** : chaque épisode terminé est mis de côté (texte seulement) dans
  `<travail ou /tmp>/podcast-reprise-<slug>/`. Relancer **la même commande** (même `--travail`) reprend au
  premier épisode manquant. Le dossier est supprimé quand la source est écrite. `--sans-reprise` repart de zéro.
  Indispensable pour un livre entier : une commande en arrière-plan est coupée au bout de 2 h.

### Contrôle du vocabulaire et des passages sautés (depuis le 2026-10-25)

**Le problème.** faster-whisper n'a pas de vrai « biais de vocabulaire » : `hotwords` place la liste dans le
contexte « texte précédent » de **chaque** fenêtre de 30 s (même mécanisme qu'`initial_prompt`, répété ; et
`condition_on_previous_text=False` n'y change rien). Il arrive que le modèle **recopie ce contexte** au lieu
d'écouter, puis clôt la fenêtre : la liste apparaît dans le texte (« … problem solving $100M Offers, Grand Slam
Offer Per 100 Calls … ») **et le reste de la fenêtre, jusqu'à 30 s de parole, disparaît**. Constaté dans
`sources/podcast/hormozi-100m-offers` (transcrit le 2026-10-22). Reproduit sur 2 × 150 s : 2 trous de 30 s avec
`hotwords` (en liste comme en phrase), 0 sans. Sans vocabulaire, l'orthographe se dégrade (« $100 million offers »,
« grand slam offer ») mais rien ne se perd.

**Ce que fait le script** (toujours actif, avec ou sans vocabulaire), après la transcription de chaque épisode :
1. **Fuite** : un segment qui enchaîne au moins **deux termes complets** du vocabulaire (dans n'importe quel ordre,
   avec éventuellement un bout de terme avant ou après) et totalise au moins `--seuil-fuite` mots (défaut 4).
   Un terme isolé (« a Grand Slam Offer ») n'est jamais une fuite.
2. **Trou** : de la parole détectée par le VAD (mêmes réglages que `vad_filter`) qui n'est couverte par aucun
   segment pendant au moins `--trou-secondes` secondes (défaut 6 ; les pauses naturelles font moins de 3 s).
3. Chaque passage suspect, élargi d'un segment de chaque côté, est **retranscrit sans vocabulaire** et remplace
   l'original s'il donne au moins 80 % des mots (et, pour un trou, davantage de mots). Sinon : pour une fuite, le
   texte parasite est seulement retiré ; pour un trou, rien ne change (musique, silence).
4. Tout est consigné : une ligne `contrôle […] …` dans le journal ; `episodes[].controles` dans `metadata.json`
   (`debut_episode_s`, `fin_episode_s` — **relatifs à l'épisode** —, `raisons`, `action`, `mots_avant`,
   `mots_apres`) ; un commentaire `<!-- contrôle, passage de N s : … -> … (avant -> après mots) -->` dans
   `transcription.md` juste avant le passage remplacé ; une ligne de bilan dans l'en-tête.

Coût : un passage du VAD par épisode et la retranscription des passages suspects (≈ 30 à 70 s d'audio chacun).
Test 2026-10-25 (150 s des parties 3 et 4, vocabulaire `Alex Hormozi, $100M Offers, Grand Slam Offer`) :
3 contrôles, 77 → 362 mots sur les passages réparés ; texte identique à une transcription sans vocabulaire sur ces
passages, orthographe du vocabulaire conservée ailleurs. Mesure du surcoût sur un livre entier : à faire.

Lecture d'une transcription : un commentaire `<!-- contrôle … -->` n'est pas du contenu ; les passages qu'il
précède ont l'orthographe « sans vocabulaire » (ex. « $100 million offers » pour *$100M Offers*).

### Fichiers produits (`<sortie>/<slug>/`)

- `transcription.md` : `# titre`, lignes d'en-tête (podcast, durée, flux, modèle), `## Épisodes` (début de
  chaque épisode dans la source), `## Chapitres` si les descriptions du flux donnent des horodatages
  `(12:34) - Titre`, puis `## Transcription` : blocs `**[mm:ss]** texte` (ou `**[hh:mm:ss]**`) d'environ 30 s
  séparés d'une ligne vide, un intertitre `### Épisode i/N · <titre> (début hh:mm:ss)` avant chaque épisode
  quand il y en a plusieurs.
- `metadata.json` : `type`, `slug`, `titre`, `podcast` (titre, auteur, lien, langue), `flux`, `episodes[]`
  (titre, date, duree_s, numero, guid, lien, audio_url, description, chapitres, secondes_transcrites,
  langue_detectee, nb_segments, debut_dans_source_s), `duree_transcrite_s`, `max_secondes`, `modele`, `beam`,
  `langue_transcription`, `nb_segments`, `date_transcription`, `vitesse_temps_reel`, `vocabulaire`, `seuil_fuite`,
  `trou_secondes` ; par épisode, `controles` (voir ci-dessus).

### Découpe (plus de 15 000 mots)

```bash
python3 -I outils/youtube/decouper.py sources/podcast/<slug> 15000   # -> sources/podcast/<slug>/parties/
```

Les intertitres d'épisode restent collés au bloc qui les suit ; la plage affichée va du premier bloc de la
partie au début de la partie suivante.

## Modèle et vitesse mesurée (CPU 4 cœurs, int8, 2026-10-22)

Mesure : 300 s du début de *$100M Leads* partie 1 (voix lue, anglais), `vad_filter`, `--threads 4`.
« x2,34 » = 1 h d'audio transcrite en 1 h / 2,34 ≈ 26 min.

| Modèle | Beam | Calcul pour 300 s | Vitesse | Mots | Remarque |
|---|---|---|---|---|---|
| `small.en` | 5 | 128 s | **x2,34** | 1 055 | défaut : la meilleure qualité des modèles testés |
| `small.en` | 1 | 70 s | x4,26 | 1 060 | `--beam 1` : presque deux fois plus rapide ; écart de qualité non mesuré en détail |
| `distil-small.en` | 5 | 65 s | x4,59 | 997 | perd des mots (−5 %) : déconseillé pour une source de connaissances |
| `base.en` | 5 | 59 s | x5,06 | 1 057 | plus d'erreurs sur les noms et chiffres ; brouillon rapide seulement |

À ajouter : chargement du modèle (quelques secondes en cache, ~45 s s'il faut le télécharger) et
téléchargement de l'audio (~3 s pour un épisode de 30 min). Test de bout en bout (60 s) : x2,4.
Pour 1 h d'audio en `small.en` beam 5 : ≈ 26 min de calcul.

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
  --vocabulaire 'Alex Hormozi, Leila Hormozi, Acquisition.com, $100M Offers, Grand Slam Offer' \
  --travail <scratchpad>/travail-podcast --oui
# Leads : --motif '\| \$100M Leads Book$' --slug hormozi-100m-leads (vocabulaire : …, $100M Leads, Core Four)
# Money Models : --motif '^Part \d+: .*\$100M Money Models' --slug hormozi-100m-money-models
```

Durée de calcul estimée (`small.en`, beam 5, 4 cœurs, x2,34) : Offers ≈ 1 h 45, Leads ≈ 2 h 45, Money Models
≈ 1 h 37, soit ≈ 6 h 10 pour les trois. Une commande en arrière-plan étant coupée au bout de 2 h, lancer un
livre par commande et **relancer la même commande** si elle est coupée (reprise automatique par épisode).


## Limites connues

- Transcription automatique : noms propres, chiffres (« 100 million dollar » pour *$100M*) et termes
  techniques à relire ; pas de séparation des locuteurs.
- `--max-secondes` télécharge un début de fichier estimé d'après la taille annoncée ; un MP3 à débit
  variable peut donner un peu moins que N secondes.
- L'audio décodé d'un épisode est gardé en mémoire (~230 Mo par heure d'audio).
- Seuls les flux RSS publics (champ `<enclosure>`) sont gérés ; pas de flux privé à identifiant, pas de
  Spotify/Apple (pas de téléchargement autorisé).
- La reprise se fait par épisode : un épisode interrompu en cours de route est retranscrit en entier. Les fichiers
  de reprise d'une version antérieure au 2026-10-25 ne sont pas réutilisés (clé différente) : l'épisode est refait.
- Contrôle du vocabulaire : une fuite qui ne contient qu'**un seul** terme (« Grand Slam Offer » collé à la fin
  d'une phrase) n'est pas repérée dans le texte ; seul le trou qu'elle provoque l'est (s'il dure ≥ 6 s). Une fuite
  à cheval sur deux segments n'est pas repérée non plus. Aux bords d'un passage retranscrit, un mot peut être
  doublé ou perdu. Les passages réparés ne sont pas recontrôlés.
- Avec `--max-secondes`, la fin coupée de l'audio peut produire une fuite ou un trou artificiel (réparé comme les
  autres).
