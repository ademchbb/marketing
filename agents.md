# Carte des agents

**60 agents**, une micro-mission chacun. Définitions : `.claude/agents/<nom>.md`.
Règle : un agent n'écrit **que** dans le dossier indiqué dans sa définition (section « Sortie »).

## Hiérarchie

```
Niveau 0   ORCHESTRATEUR (IA principale)
           décide · découpe en micro-missions · lance (en parallèle dès que c'est indépendant)
           · vérifie chaque livrable · renvoie au travail si le niveau n'est pas atteint
           Il ne produit rien lui-même.
   │
Niveau 1   PÔLES (regroupements de missions, pas des agents ; aucun « chef de pôle »)
           A Apprentissage · B Veille & concurrence · C Stratégie · D Création · E Qualité
           · F Labo d'expériences & performance · G Diffusion, communauté & croissance
           · H Publicité payante · I Méta
   │
Niveau 2   AGENTS (60) : une micro-mission chacun, un seul dossier d'écriture
```

**Contrainte technique** : un sous-agent n'a pas l'outil Agent et ne peut pas lancer un autre agent.
Toute délégation remonte donc au niveau 0. Aucun agent n'en appelle un autre directement.

### Boucle de sous-délégation (par les rapports)
1. Un agent qui rencontre une tâche hors de sa micro-mission ne la fait pas : il termine son rapport
   par une section « Demandes de délégation » (agent visé ou « à créer », entrée, sortie attendue, pourquoi).
2. L'orchestrateur lit chaque rapport, accepte, regroupe ou refuse chaque demande (en le notant dans
   `journal/etat.md`), puis lance les agents visés, en parallèle quand c'est indépendant.
3. Si le demandeur a besoin du résultat pour finir, l'orchestrateur le relance avec ce livrable en entrée.
4. Les recalés du contrôle qualité suivent la même boucle : `critique-hook` et
   `controleur-qualite-marketing` nomment les agents à relancer, l'orchestrateur les relance.

### Protocole de création d'un agent manquant
1. Déclencheur : une demande « à créer : <nom> — <mission> », une micro-mission sans agent, ou un agent
   recalé deux fois pour la même raison.
2. L'orchestrateur lance `architecte-agents` **sans demander l'accord de l'utilisateur** (autorisation
   permanente), avec la mission, l'entrée et la sortie attendues.
3. `architecte-agents` vérifie cette carte (pas de chevauchement : sinon il ajuste l'agent existant),
   écrit `.claude/agents/<nom>.md` au format standard (règles communes ci-dessous incluses), met à jour
   le pôle, les pipelines, le dossier d'écriture et le journal de ce fichier.
4. L'orchestrateur lance le nouvel agent. Si la session ne le charge pas comme type : agent généraliste
   avec « Tu es l'agent `<nom>` : lis `.claude/agents/<nom>.md` et applique-le à la lettre pour : <mission> ».

## Règles communes à tous les agents

**Sous-délégation** (section identique dans les 60 définitions) :
> Tu ne lances aucun agent : seul l'orchestrateur le peut. Si une tâche déborde de ta micro-mission ou
> serait mieux faite par un autre agent (existant ou à créer), ne la fais pas toi-même. Termine ton
> rapport par une section « Demandes de délégation », une ligne par demande : agent visé (ou « à créer :
> <nom> — <mission> ») · entrée · sortie attendue · pourquoi. Rien à déléguer : « Demandes de délégation : aucune ».

**Pas de tiret long « — » (ni « -- ») dans les textes publiés ou envoyés au nom de la marque** : perçu
comme un marqueur de texte IA [fiche:HzoQgQS8czE]. Règle inscrite chez `redacteur-hooks`, `scenariste-reel`,
`redacteur-carrousel`, `redacteur-linkedin`, `redacteur-thread-x`, `redacteur-legende`,
`specialiste-seo-social`, `scenariste-youtube-long`, `titreur-miniatures`, `redacteur-newsletter`,
`adaptateur-multiplateforme`, `redacteur-ads`, `gestionnaire-communaute`, `prospecteur-collaborations`,
`pont-motion-design`, `controleur-qualite-marketing` (kit final). Le `correcteur` le vérifie.

**Base de connaissances** : les agents de stratégie (pôles C, H) et de création (pôle D, plus
`gestionnaire-communaute`, `prospecteur-collaborations`, `pont-motion-design`) listent dans leur section
« Entrée » les fiches de `connaissances/frameworks/` (voir son `index.md`) et de `connaissances/principes/`
qui les concernent. Seuls les fichiers existants y sont cités ; les principes prévus mais absents sont
marqués « à venir ».

## Pôle A — Apprentissage (ingestion & base de connaissances)

| agent | mission | écrit dans |
|---|---|---|
| `extracteur-youtube` | Récupère la transcription horodatée et les métadonnées (titre, chaîne, vues, chapitres, description) d'une ou plusieurs vidéos YouTube, et les découpe en parties analysables | `sources/youtube/<id>/` |
| `extracteur-web` | Récupère le texte propre d'un article, billet de blog, page de documentation, newsletter ou thread public, et le range comme source brute | `sources/web/<slug>/` |
| `extracteur-pdf` | Extrait le texte propre d'un PDF public (rapport, playbook, baromètre, livre du domaine public) avec repères `[p. N]`, et si possible le texte des planches en image ; vérifie les droits et refuse les livres sous droits mis en ligne sans autorisation. Le PDF reste dans le scratchpad, jamais dans le repo | `sources/pdf/<slug>/` |
| `extracteur-social` | Récupère ce qui est accessible publiquement d'un post Instagram, TikTok, X, LinkedIn ou d'un Short (légende, transcription si vidéo, métriques visibles, date) pour analyse | `sources/social/<plateforme>-<id>/` |
| `lecteur-images` | Décrit en texte les images d'une source web ou sociale déjà récupérée (planches, schémas, captures, graphiques, slides) : ce qu'elles montrent, texte lisible recopié tel quel, chiffres marqués « lu sur l'image, à vérifier ». Décrit sans commenter. Images téléchargées dans le scratchpad, jamais dans le repo. Les PDF restent à `extracteur-pdf` | `sources/<type>/<slug>/images.md` |
| `transcripteur-audio` | Transcrit l'audio d'une vidéo ou d'un podcast qui n'a pas de sous-titres (Whisper local), en dernier recours après l'extracteur | — |
| `analyste-transcription` | Lit UNE partie d'une transcription (vidéo, podcast, article long) et en extrait toutes les connaissances marketing actionnables dans des notes structurées | `connaissances/fiches/<id>/notes-partie-NN.md` |
| `consolidateur-fiche` | Fusionne les notes de toutes les parties d'une même source en UNE fiche de référence (thèse, frameworks, tactiques, niveau de fiabilité) | `connaissances/fiches/<id>/fiche.md` |
| `extracteur-hooks` | Extrait de toutes les fiches les hooks, accroches, structures de scripts et CTA réutilisables, et les classe en bibliothèque (swipe file) par type et par mécanisme psychologique. | `connaissances/swipe-file/` |
| `extracteur-frameworks` | Extrait chaque framework / méthode nommée des fiches et en fait une fiche-outil autonome, applicable pas à pas à n'importe quelle marque. | `connaissances/frameworks/` |
| `verificateur-faits` | Vérifie les affirmations chiffrées et les « règles » des experts (stats d'algorithme, durées idéales, taux d'engagement) avec des sources indépendantes, et attribue un niveau de confiance. | `connaissances/verifications/` |
| `synthetiseur-connaissances` | Fusionne toutes les fiches en principes thématiques (un fichier par thème), résout les contradictions entre experts et maintient l'index de la base de connaissances. | `connaissances/principes/` et `connaissances/index.md` |
| `cartographe-lacunes` | Compare la base de connaissances à un programme complet de marketing digital et liste ce qui manque, par priorité | `connaissances/lacunes.md` |
| `chercheur-sources` | Trouve les meilleures vidéos, articles, docs officielles et études pour combler les lacunes de la base de connaissances, et les met en file d'attente d'ingestion. | `sources/a-traiter.md` |
| `archiviste` | Tient les index à jour (sources, fiches, agents, marques), vérifie les liens entre fichiers et signale les doublons ou fichiers orphelins | `sources/index.md`, `connaissances/index.md` (section « Carte des fichiers » seulement), |

## Pôle B — Veille & concurrence

| agent | mission | écrit dans |
|---|---|---|
| `veilleur-concurrence` | Identifie les concurrents et comptes de référence d'une marque sur chaque plateforme (directs, indirects, créateurs de la même niche, comptes « aspirationnels ») et les classe par pertinence. | `marques/<slug>/veille/concurrents.md` |
| `analyste-concurrent` | Analyse en profondeur la stratégie de contenu d'UN concurrent ou compte de référence (formats, hooks, fréquence, piliers, posts qui sur-performent, offre, ton) et en tire ce qu'on peut copier et ce qu'on peut faire mieux. | `marques/<slug>/veille/concurrents/<nom>.md` |
| `veilleur-tendances` | Repère les tendances du moment par plateforme (formats, mèmes, sujets, styles de montage, sons) et évalue lesquelles conviennent à une marque | `veille/tendances/<AAAA-MM-JJ>.md` |
| `veilleur-algorithmes` | Suit les annonces officielles et les changements d'algorithme de chaque plateforme (signaux de classement, durées, formats favorisés, nouvelles fonctions) et tient une fiche à jour par plateforme. | `veille/plateformes/<plateforme>.md` |
| `chasseur-viraux` | Trouve dans une niche donnée les posts qui sur-performent massivement par rapport à la taille du compte (outliers), pour alimenter l'analyse de ce qui marche vraiment. | `veille/viraux/<niche>-<AAAA-MM-JJ>.md` |
| `decodeur-viral` | Décortique UN contenu viral seconde par seconde (hook visuel et verbal, rythme, rétention, structure, payoff, CTA, commentaires) pour en extraire un modèle reproductible. | `veille/viraux/decodages/<plateforme>-<id>.md` |
| `ecouteur-audience` | Écoute ce que la cible d'une marque dit réellement en ligne (Reddit, forums, commentaires YouTube/Instagram, avis, Quora) | `marques/<slug>/02-audience/verbatims.md` |

## Pôle C — Stratégie

| agent | mission | écrit dans |
|---|---|---|
| `analyste-marque` | Analyse le site, les réseaux et l'offre d'une marque (ou d'une personne pour un personal brand) et en tire le brief de référence | `marques/<slug>/01-brief/` |
| `architecte-persona` | Construit les personas / le client idéal (ICP) d'une marque à partir du brief et des verbatims réels | `marques/<slug>/02-audience/personas.md` |
| `strategiste-positionnement` | Définit le positionnement d'une marque | `marques/<slug>/03-strategie/positionnement.md` |
| `architecte-personal-brand` | Pour une marque personnelle (fondateur, créateur, expert) | `marques/<slug>/03-strategie/personal-brand.md` |
| `banquier-histoires` | Construit et enrichit la banque d'histoires d'une marque (anecdotes vécues, échecs, coulisses, moments clés, clients) en préparant des questions d'interview pour l'utilisateur puis en classant ses réponses. | `marques/<slug>/03-strategie/banque-histoires.md` |
| `strategiste-contenu` | Définit la stratégie de contenu d'une marque | `marques/<slug>/03-strategie/strategie-contenu.md` |
| `strategiste-offre` | Conçoit ou améliore l'offre, l'aimant à prospects (lead magnet) et les appels à l'action d'une marque pour que l'audience devienne des clients | `marques/<slug>/03-strategie/offre.md` |
| `planificateur-calendrier` | Transforme la stratégie de contenu en calendrier éditorial daté (2 à 4 semaines), une ligne par post, en équilibrant piliers, formats, plateformes et temps forts. | `marques/<slug>/04-calendrier/calendrier.md` |

## Pôle D — Création

| agent | mission | écrit dans |
|---|---|---|
| `ideateur` | Génère une grande quantité d'idées de contenus pour une marque et un pilier donnés, à partir des verbatims, de la banque d'histoires, des viraux de la niche et des formats qui marchent | `marques/<slug>/05-posts/idees.md` |
| `redacteur-hooks` | Écrit au moins 15 variantes d'accroche (texte écrit, première phrase parlée et premier visuel) pour UNE idée de post, en s'appuyant sur la bibliothèque de hooks. | `marques/<slug>/05-posts/<post>/hooks.md` |
| `scenariste-reel` | Écrit le script complet d'une vidéo courte verticale (Reel, TikTok, Short) à partir de l'idée et du hook gagnant | `marques/<slug>/05-posts/<post>/script-reel.md` |
| `redacteur-carrousel` | Écrit un carrousel (Instagram / LinkedIn) slide par slide | `marques/<slug>/05-posts/<post>/carrousel.md` |
| `redacteur-linkedin` | Écrit des posts texte LinkedIn (avec ou sans visuel) | `marques/<slug>/05-posts/<post>/linkedin.md` |
| `redacteur-thread-x` | Écrit des posts et threads pour X (Twitter) et Threads | `marques/<slug>/05-posts/<post>/x.md` |
| `redacteur-legende` | Écrit la légende (caption) d'un post Instagram / TikTok / YouTube Shorts | `marques/<slug>/05-posts/<post>/legende.md` |
| `specialiste-seo-social` | Optimise la découvrabilité d'un post | `marques/<slug>/05-posts/<post>/seo.md` |
| `scenariste-youtube-long` | Écrit le plan détaillé et le script d'une vidéo YouTube longue (8-30 min) | `marques/<slug>/05-posts/<post>/script-youtube.md` |
| `titreur-miniatures` | Propose et classe des titres et concepts de miniatures YouTube (et couvertures de Reels) | `marques/<slug>/05-posts/<post>/titres-miniatures.md` |
| `redacteur-newsletter` | Écrit les emails et newsletters d'une marque (bienvenue, hebdo, lancement, relance) | `marques/<slug>/05-posts/<post>/email.md` (ou `marques/<slug>/emails/<sequence>/` pour une séquence) |
| `directeur-creatif-visuel` | Rédige le brief visuel d'un post (cadrage, composition, couleurs, typographie, mouvement, effets sonores, références) prêt à être produit par le studio motion-design, Higgsfield ou un humain. | `marques/<slug>/05-posts/<post>/visuel.md` |
| `adaptateur-multiplateforme` | Décline un contenu validé pour d'autres plateformes (Reel → TikTok/Shorts/LinkedIn/X/Pinterest, vidéo longue → extraits) en adaptant format, durée, texte et CTA aux codes de chacune. | `marques/<slug>/05-posts/<post>/declinaisons.md` |

## Pôle E — Qualité (contrôles avant validation)

| agent | mission | écrit dans |
|---|---|---|
| `critique-hook` | Note et classe les variantes d'accroche d'un post comme le ferait un utilisateur pressé qui scrolle, selon une grille fixe, et désigne le gagnant (et la variante à tester contre lui). | `marques/<slug>/05-posts/<post>/critique-hooks.md` |
| `correcteur` | Relit tous les textes d'un post (écran, voix, légende, carrousel) | `marques/<slug>/05-posts/<post>/relecture.md` |
| `garde-conformite` | Vérifie qu'un contenu respecte la loi et les règles des plateformes | `marques/<slug>/05-posts/<post>/conformite.md` |
| `simulateur-audience` | Joue le persona cible face à un post terminé | `marques/<slug>/05-posts/<post>/simulation.md` |
| `controleur-qualite-marketing` | Dernier contrôle avant validation utilisateur | `marques/<slug>/05-posts/<post>/qa.md` |

## Pôle F — Labo d'expériences & performance

| agent | mission | écrit dans |
|---|---|---|
| `concepteur-experiences` | Conçoit des expériences marketing rigoureuses (A/B tests de hooks, formats, heures, durées, CTA, miniatures) avec hypothèse, variable unique, métrique, taille d'échantillon et critère de décision. | `experiences/<AAAA-MM-JJ>-<slug>/protocole.md` |
| `predicteur-performance` | Avant publication, prédit les performances d'un post (vues, rétention, partages) avec une justification ; après, compare à la réalité pour calibrer le jugement de l'agence. | `experiences/predictions.md` |
| `analyste-performance` | Analyse les statistiques réelles d'une marque (fournies par l'utilisateur ou via API officielle) | `marques/<slug>/06-performance/bilan-<AAAA-MM>.md` (ou `-S<semaine>`) |
| `analyste-resultats` | Conclut une expérience du labo (gagnant, significativité, limites) et met à jour le registre des apprentissages de l'agence, qui prime ensuite sur la théorie. | `experiences/<id>/resultats.md` et `experiences/apprentissages.md` |

## Pôle G — Diffusion, communauté & croissance

| agent | mission | écrit dans |
|---|---|---|
| `publicateur` | Publie ou programme UNIQUEMENT les posts explicitement validés par l'utilisateur, via les API officielles ou un outil de programmation, et tient le journal de publication | `marques/<slug>/07-diffusion/journal-publication.md` |
| `gestionnaire-communaute` | Prépare les réponses aux commentaires et messages privés, repère les questions récurrentes (futures idées de contenu) et les prospects chauds, dans le ton de la marque | `marques/<slug>/08-communaute/` |
| `prospecteur-collaborations` | Trouve des partenaires de croissance pour une marque | `marques/<slug>/09-croissance/collaborations.md` |

## Pôle H — Publicité payante

| agent | mission | écrit dans |
|---|---|---|
| `strategiste-ads` | Conçoit les campagnes publicitaires payantes d'une marque (Meta, TikTok, YouTube, LinkedIn) | `marques/<slug>/10-ads/plan-<campagne>.md` |
| `redacteur-ads` | Écrit les variantes de textes publicitaires (texte principal, titre, description, script de pub vidéo UGC) pour une campagne, par angle et par niveau de conscience. | `marques/<slug>/10-ads/textes-<campagne>.md` |

## Pôle I — Méta (l'agence qui s'améliore elle-même)

| agent | mission | écrit dans |
|---|---|---|
| `architecte-agents` | Crée de nouveaux agents ou améliore les existants quand une micro-mission n'a pas d'agent dédié, qu'un agent produit un niveau insuffisant, ou que la base de connaissances révèle une meilleure méthode | `.claude/agents/` et `agents.md`. |
| `pont-motion-design` | Transforme un post vidéo validé (script + brief visuel) en commande prête pour le studio motion-design (ademchbb/motion-design, Remotion + ElevenLabs), au format attendu par ses agents. | `livraisons/motion-design/<slug-marque>-<post>.md` |
| `rapporteur` | Rédige pour l'utilisateur un compte rendu court et clair de ce que l'agence a fait, appris et produit depuis le dernier rapport, avec les décisions qu'on attend de lui. | `journal/rapport-<AAAA-MM-JJ>.md` |

## Pipelines

### 1. Apprendre (vidéo, article, post envoyé par l'utilisateur)
```
extracteur-youtube | extracteur-web | extracteur-social | extracteur-pdf  (→ transcripteur-audio si pas de sous-titres)
  → lecteur-images (web ou social, si des images portent du contenu utile à l'analyse)
  → analyste-transcription ×N (une partie chacun, en parallèle)
  → consolidateur-fiche (une par source)
  → extracteur-hooks ∥ extracteur-frameworks ∥ verificateur-faits
  → synthetiseur-connaissances → cartographe-lacunes → chercheur-sources → (boucle)
  → archiviste, rapporteur
```

### 2. Lancer une marque
```
analyste-marque → veilleur-concurrence → analyste-concurrent ×N ∥ ecouteur-audience ∥ chasseur-viraux → decodeur-viral ×N
  → architecte-persona → strategiste-positionnement → (architecte-personal-brand + banquier-histoires si personne)
  → strategiste-offre → strategiste-contenu → concepteur-experiences → planificateur-calendrier
```

### 3. Fabriquer un post (une ligne du calendrier)
```
ideateur → redacteur-hooks → critique-hook
  → scenariste-reel | redacteur-carrousel | redacteur-linkedin | redacteur-thread-x | scenariste-youtube-long (+ titreur-miniatures)
  → redacteur-legende ∥ specialiste-seo-social ∥ directeur-creatif-visuel
  → correcteur ∥ garde-conformite ∥ simulateur-audience
  → controleur-qualite-marketing (veto, ≥ 85/100) → predicteur-performance
  → VALIDATION UTILISATEUR → pont-motion-design (si vidéo premium) → publicateur → adaptateur-multiplateforme
```

### 4. Apprendre de ses résultats
```
analyste-performance → predicteur-performance (calibration) → analyste-resultats → experiences/apprentissages.md
  → synthetiseur-connaissances (les résultats réels priment) → architecte-agents (améliorer les agents)
```

### Rituels hebdomadaires
- Lundi : veilleur-tendances, veilleur-algorithmes, chasseur-viraux (par niche active).
- Vendredi : analyste-performance, analyste-resultats, rapporteur.

## Journal des modifications
- 2026-10-20 : création des 58 agents initiaux (9 pôles).
- 2026-10-21 : pyramide explicite. Ajout des sections « Hiérarchie » et « Règles communes » ici.
  Les 58 définitions reçoivent la section « Sous-délégation » standard (un sous-agent ne peut pas lancer
  d'agent : toute délégation passe par les rapports et l'orchestrateur). Règle « pas de tiret long » pour
  les 16 agents qui produisent du texte publié, vérifiée par `correcteur` [fiche:HzoQgQS8czE]. Renvois aux
  frameworks et principes existants dans les entrées de 26 agents de stratégie et de création.
  `architecte-agents` : ces trois éléments entrent dans le format obligatoire d'un agent. Fond des missions inchangé.
- 2026-10-21 : création de `extracteur-pdf` (pôle A, 59 agents). Aucun extracteur ne couvrait les PDF (playbook ABCD
  2022, Binet & Field B2B, Baromètre du numérique, *Scientific Advertising*). Écrit dans `sources/pdf/<slug>/`
  (+ ligne de `sources/index.md`, comme les autres extracteurs). Contrôle des droits avant téléchargement, PDF
  gardé dans le scratchpad, `pdftotext -layout` (repli `pypdf`), pages image lues visuellement et marquées « à vérifier ».
