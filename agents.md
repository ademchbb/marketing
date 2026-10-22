# Carte des agents

**63 agents**, une micro-mission chacun. Définitions : `.claude/agents/<nom>.md`.
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
Niveau 2   AGENTS (63) : une micro-mission chacun, un seul dossier d'écriture
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

**Sous-délégation** (section identique dans les 63 définitions) :
> Tu ne lances aucun agent : seul l'orchestrateur le peut. Si une tâche déborde de ta micro-mission ou
> serait mieux faite par un autre agent (existant ou à créer), ne la fais pas toi-même. Termine ton
> rapport par une section « Demandes de délégation », une ligne par demande : agent visé (ou « à créer :
> <nom> — <mission> ») · entrée · sortie attendue · pourquoi. Rien à déléguer : « Demandes de délégation : aucune ».

**Pas de tiret long « — » (ni « -- ») dans les textes publiés ou envoyés au nom de la marque** : perçu
comme un marqueur de texte IA [fiche:HzoQgQS8czE]. Règle inscrite chez `redacteur-hooks`, `scenariste-reel`,
`redacteur-carrousel`, `redacteur-linkedin`, `redacteur-thread-x`, `redacteur-legende`,
`specialiste-seo-social`, `scenariste-youtube-long`, `titreur-miniatures`, `redacteur-newsletter`,
`adaptateur-multiplateforme`, `redacteur-ads`, `gestionnaire-communaute`, `prospecteur-collaborations`,
`pont-motion-design`, `redacteur-conditions-vente`, `controleur-qualite-marketing` (kit final, textes de pub, emails).
Le `correcteur` le vérifie.

**Offres et pitch** : la checklist de référence (prix barré, « valeur » affichée, urgence, garanties, prévente,
dénigrement, engagement acheté, closing) est dans `.claude/agents/garde-offres.md`, section « Checklist offres
et pitch » ; `strategiste-offre`, `redacteur-ads`, `redacteur-newsletter`, `gestionnaire-communaute`,
`redacteur-conditions-vente` et `controleur-qualite-marketing` (motif de veto) y renvoient. Renvois courts aux
identifiants du registre : `redacteur-legende`, `scenariste-reel`, `redacteur-carrousel` (OV06, OP10),
`redacteur-hooks`, `critique-hook` (OU01-OU03, OC04), `strategiste-contenu`, `ideateur` (OC01-OC03).

**Taxonomie** : liste fermée des tags, fichiers de principes et alias : section « Taxonomie de référence » ci-dessous.

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
| `transcripteur-audio` | Transcrit l'audio d'une vidéo ou d'un podcast qui n'a pas de sous-titres (Whisper local) : en dernier recours après l'extracteur pour une vidéo, directement pour un épisode ou un livre audio publié par son auteur (flux RSS officiel). Utilise les scripts de `outils/podcast/` selon son `README.md` (`--simuler` d'abord, `--travail` dans le scratchpad, même commande relancée si coupée). Audio dans le scratchpad, supprimé après usage | `sources/youtube/<id>/` ou `sources/podcast/<slug>/` (+ ligne de `sources/index.md`) |
| `developpeur-outils` | Propriétaire des scripts de `outils/` : les écrit, corrige, teste sur un petit cas réel et documente (README, `requirements.txt` avec versions). Secrets en variables d'environnement, médias jamais dans le repo, tests écrits dans le scratchpad. Ne fait pas le travail de fond des autres agents | `outils/<domaine>/` |
| `analyste-transcription` | Lit UNE partie d'une transcription (vidéo, podcast, article long) et en extrait toutes les connaissances marketing actionnables dans des notes structurées | `connaissances/fiches/<id>/notes-partie-NN.md` |
| `consolidateur-fiche` | Fusionne les notes de toutes les parties d'une même source en UNE fiche de référence (thèse, frameworks, tactiques, niveau de fiabilité) | `connaissances/fiches/<id>/fiche.md` |
| `extracteur-hooks` | Extrait de toutes les fiches les hooks, accroches, structures de scripts et CTA réutilisables, et les classe en bibliothèque (swipe file) par type et par mécanisme psychologique. | `connaissances/swipe-file/` |
| `extracteur-frameworks` | Extrait chaque framework / méthode nommée des fiches et en fait une fiche-outil autonome, applicable pas à pas à n'importe quelle marque. | `connaissances/frameworks/` |
| `verificateur-faits` | Vérifie les affirmations chiffrées et les « règles » des experts (stats d'algorithme, durées idéales, taux d'engagement) avec des sources indépendantes, et attribue un niveau de confiance. | `connaissances/verifications/` |
| `synthetiseur-connaissances` | Fusionne toutes les fiches en principes thématiques (un fichier par thème), résout les contradictions entre experts et maintient l'index de la base de connaissances. | `connaissances/principes/` et `connaissances/index.md` |
| `cartographe-lacunes` | Compare la base de connaissances à un programme complet de marketing digital et liste ce qui manque, par priorité | `connaissances/lacunes.md` |
| `chercheur-sources` | Trouve les meilleures vidéos, articles, docs officielles et études pour combler les lacunes de la base de connaissances, et les met en file d'attente d'ingestion. | `sources/a-traiter.md` |
| `archiviste` | Tient les index à jour (sources, fiches, agents, marques), vérifie les liens entre fichiers et signale les doublons ou fichiers orphelins. **Propriétaire de `marques/_modele/`** (gabarit copié pour chaque nouvelle marque : un sous-dossier par dossier `marques/<slug>/…` de cette carte) | `sources/index.md`, `connaissances/index.md` (section « Carte des fichiers » seulement), `marques/index.md`, `marques/_modele/`, `journal/archives.md` |

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
| `redacteur-conditions-vente` | Rédige le projet de conditions de vente d'une offre payante (CGV ou conditions de l'offre, information précontractuelle, clause de prévente : date de livraison, acompte et non arrhes, fonctionnalité et information de rétractation, garanties) à partir du registre juridique et du dossier de la marque. Validation de l'utilisateur obligatoire, relecture par un juriste recommandée, jamais présenté comme un avis juridique | `marques/<slug>/conditions-vente.md` |
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
| `correcteur` | Relit tous les textes d'un post (écran, voix, légende, carrousel), d'une campagne de pub ou d'une séquence d'emails | un seul fichier selon le livrable : `marques/<slug>/05-posts/<post>/relecture.md`, `marques/<slug>/10-ads/relecture-<campagne>.md` ou `marques/<slug>/emails/<sequence>/relecture.md` |
| `garde-conformite` | Vérifie qu'un contenu (post, campagne de pub, séquence d'emails) respecte la loi et les règles des plateformes | un seul fichier selon le livrable : `marques/<slug>/05-posts/<post>/conformite.md`, `marques/<slug>/10-ads/conformite-<campagne>.md` ou `marques/<slug>/emails/<sequence>/conformite.md` |
| `simulateur-audience` | Joue le persona cible face à un post terminé | `marques/<slug>/05-posts/<post>/simulation.md` |
| `controleur-qualite-marketing` | Dernier contrôle avant validation utilisateur d'un post, d'une campagne de pub ou d'une séquence d'emails (grille /100, veto sous 85 ou sans feu vert conformité) | un seul fichier selon le livrable : `marques/<slug>/05-posts/<post>/qa.md` (+ `pret-a-publier.md`), `marques/<slug>/10-ads/qa-<campagne>.md` ou `marques/<slug>/emails/<sequence>/qa.md` |

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
Podcast ou livre audio officiel : `transcripteur-audio` remplace l'extracteur (même suite du pipeline).
Outillage, à la demande et avant l'étape qui en a besoin : `developpeur-outils` écrit ou corrige le script
(ex. `outils/podcast/` avant `transcripteur-audio`) ; l'orchestrateur reporte ensuite ses commandes dans
la section « Commandes » de `CLAUDE.md`.

### 2. Lancer une marque
```
analyste-marque → veilleur-concurrence → analyste-concurrent ×N ∥ ecouteur-audience ∥ chasseur-viraux → decodeur-viral ×N
  → architecte-persona → strategiste-positionnement → (architecte-personal-brand + banquier-histoires si personne)
  → strategiste-offre → redacteur-conditions-vente (si offre payante) → VALIDATION UTILISATEUR (conditions)
  → strategiste-contenu → concepteur-experiences → planificateur-calendrier
```
Avant la publication d'une offre : aucun post, pub, email ni page qui montre un prix, une garantie ou une prévente
ne part sans `marques/<slug>/conditions-vente.md` validé par l'utilisateur ; tout changement de prix, de garantie
ou de calendrier de livraison relance `redacteur-conditions-vente` puis `garde-conformite` sur les livrables touchés.

### 3. Fabriquer un post (une ligne du calendrier)
```
ideateur → redacteur-hooks → critique-hook
  → scenariste-reel | redacteur-carrousel | redacteur-linkedin | redacteur-thread-x | scenariste-youtube-long (+ titreur-miniatures)
  → redacteur-legende ∥ specialiste-seo-social ∥ directeur-creatif-visuel
  → correcteur ∥ garde-conformite ∥ simulateur-audience
  → controleur-qualite-marketing (veto, ≥ 85/100) → predicteur-performance
  → VALIDATION UTILISATEUR → pont-motion-design (si vidéo premium) → publicateur → adaptateur-multiplateforme
```

### 3 bis. Campagne payante et séquence d'emails
```
strategiste-ads → redacteur-ads → correcteur (10-ads/relecture-<campagne>.md)
  → garde-conformite (10-ads/conformite-<campagne>.md)
  → controleur-qualite-marketing (veto, ≥ 85/100 ; 10-ads/qa-<campagne>.md)
  → VALIDATION UTILISATEUR (campagne et budget) → publicateur (liste Advantage+ du plan, UTM) → analyste-performance
redacteur-newsletter (séquence) → correcteur (emails/<sequence>/relecture.md)
  → garde-conformite (emails/<sequence>/conformite.md)
  → controleur-qualite-marketing (veto, ≥ 85/100 ; emails/<sequence>/qa.md) → VALIDATION UTILISATEUR
```
Relecture ✏️ : l'orchestrateur fait appliquer les corrections par le rédacteur (`redacteur-ads` ou
`redacteur-newsletter`) avant `garde-conformite`. Recalé : l'orchestrateur relance les agents nommés dans le
fichier qa, puis `correcteur`, `garde-conformite` et le contrôle qualité à nouveau. `publicateur` ne met en ligne que la « Version validée » du fichier qa.

### Gabarit des marques
`marques/_modele/` appartient à `archiviste` : quand un agent reçoit un nouveau dossier `marques/<slug>/…`,
l'orchestrateur lance `archiviste` pour l'ajouter au gabarit (sous-dossier + `.gitkeep`).

### 4. Apprendre de ses résultats
```
analyste-performance → predicteur-performance (calibration) → analyste-resultats → experiences/apprentissages.md
  → synthetiseur-connaissances (les résultats réels priment) → architecte-agents (améliorer les agents)
```

### Rituels hebdomadaires
- Lundi : veilleur-tendances, veilleur-algorithmes, chasseur-viraux (par niche active).
- Vendredi : analyste-performance, analyste-resultats, rapporteur.

## Taxonomie de référence (tags des fiches → fichiers de principes)

Seule copie de la liste fermée. Propriétaire : `architecte-agents` (ajouts sur demande dans un rapport, ou décision
de l'orchestrateur). Utilisée par `consolidateur-fiche` (ligne « Thèmes couverts ») et `synthetiseur-connaissances`
(un fichier de principes par tag ; il tient dans `connaissances/index.md` la liste des fichiers déjà créés). Un tag
n'est créé que s'il couvre au moins 2 sources ou une compétence que l'agence produira ; sinon, alias.

### Tags
| tag | fichier de `connaissances/principes/` | définition |
|---|---|---|
| `personal-branding` | `personal-branding.md` | marque personnelle d'un fondateur, créateur ou expert |
| `croissance-audience` | `croissance-audience.md` | abonnés, portée, diffusion des contenus |
| `instagram` · `tiktok` | `croissance-audience.md` | codes, formats et algorithme de la plateforme |
| `linkedin` | `linkedin.md` | codes, formats et algorithme de LinkedIn (organique) ; LinkedIn Ads = `publicite` |
| `x-twitter` | `x-twitter.md` | codes, formats et algorithme de X (ex-Twitter) : posts, threads ; veille `veille/plateformes/x.md` |
| `hooks` | `hooks-et-retention.md` | accroche (premières secondes, première ligne) et rétention |
| `storytelling` | `storytelling.md` | récit, structure narrative, histoires vécues |
| `formats-courts` | `formats-courts.md` | vidéos courtes verticales (Reels, TikTok, Shorts) |
| `youtube-long` | `youtube-long.md` | vidéos YouTube longues, séries |
| `monetisation` · `offre` | `monetisation-et-offre.md` | gagner de l'argent avec l'audience · offre (valeur, bonus, garanties, structure de prix) |
| `regularite` · `production` · `mindset` | `production-et-regularite.md` | rythme de publication · méthode de fabrication du contenu (écriture, prise de notes, outils, flux de travail) · état d'esprit du créateur |
| `recrutement-equipe` | `equipe-et-organisation.md` | embaucher et structurer l'équipe |
| `publicite` | `publicite.md` | pub payante en général ; système Meta = `meta-ads` |
| `communaute` | `communaute.md` | relation avec l'audience, modération courante |
| `positionnement` | `positionnement-et-niche.md` | positionnement, niche, différenciation |
| `analyse-donnees` | `analyse-et-iteration.md` | lecture des métriques (contenu, pub, tunnel de vente : taux par étape, conversion), tests A/B et itération ; allocation et attribution = `mesure-budget` |
| `meta-ads` | `meta-ads.md` | système publicitaire Meta (Facebook + Instagram : Advantage+, Andromeda, apprentissage) |
| `conformite-juridique` | `conformite-juridique.md` | droit, règles des plateformes, mentions obligatoires |
| `email` | `email.md` | newsletter, emailing, prospection électronique |
| `b2b` | `b2b.md` | vente et marketing vers des professionnels |
| `vente` | `vente.md` | conversation commerciale : rendez-vous, découverte, objections, prix présenté et défendu, négociation, pipeline, scripts |
| `generation-leads` | `generation-leads.md` | capter des contacts : lead magnets, scorecards et quiz, listes d'attente, qualification, prospection sortante |
| `copywriting` | `copywriting.md` | message de marque et rédaction persuasive (promesse, titres, pages, pubs) ; l'accroche seule = `hooks` |
| `site-web` | `site-web.md` | site et pages (accueil, page de vente, page de capture) : structure, parcours, conversion |
| `strategie-croissance` | `strategie-croissance.md` | croissance de l'entreprise : canaux d'acquisition, marque vs activation, go-to-market |
| `ethique` | `ethique.md` | ce qui est légal mais discutable en influence et en marketing (manipulation, exagération, produit nocif) |
| `mesure-budget` | `mesure-budget.md` | allocation du budget marketing, attribution, incrémentalité, tests de lift, ROI |
| `relations-presse` | `relations-presse.md` | médias et journalistes : angle, communiqué, pitch, dossier de presse, retombées |
| `identite-visuelle` | `identite-visuelle.md` | logo, couleurs, typographies, charte, actifs distinctifs (« marteau visuel ») |
| `psychologie-persuasion` | `psychologie-persuasion.md` | mécanismes psychologiques d'influence (Cialdini, biais, économie comportementale) et leur preuve |
| `lancement-produit` | `lancement-produit.md` | validation d'idée, étude de marché, prévente, lancement d'un produit ou d'une offre |
| `bouche-a-oreille` | `bouche-a-oreille.md` | recommandation, diffusion organique, mécanique de conversation, parrainage |
| `recherche-client` | `recherche-client.md` | immersion terrain, entretiens clients, test du discours, Jobs To Be Done (JTBD) |
| `culture-entreprise` | `culture-entreprise.md` | rituels centrés client, valeurs, onboarding des salariés ; embaucher et structurer l'équipe = `recrutement-equipe` |
| `packaging` | `packaging.md` | titres, miniatures, couvertures et couple titre + image avant le clic ; l'accroche une fois la vidéo lancée = `hooks`, titres de page ou de pub = `copywriting` |
| `ia-creation` | `ia-creation.md` | IA générative dans l'écriture et la production (génération, relecture, marqueurs de texte IA, images de synthèse, banalisation de l'information) |
| `retention-client` | `retention-client.md` | après l'achat : onboarding client, expérience et service client, fidélisation, réachat, abonnement et récurrent, churn ; offres de suite (upsell, continuité) = `offre` |
| `distribution` | `distribution.md` | accès au marché du produit : distributeurs, grande distribution, revendeurs, MDD, places de marché, disponibilité avant la pub ; diffusion des contenus = `croissance-audience` |
| `partenariats` | `partenariats.md` | alliances de croissance avec des tiers : joint ventures, recommended provider, **affiliation** (recruter, rémunérer, animer des affiliés), co-marketing, collaborations avec des créateurs ; parrainage client = `bouche-a-oreille`, sponsoring vu du créateur = `monetisation` |
| `brief-creatif` | `brief-creatif.md` | rédiger et challenger le brief : vrai problème à résoudre, cible, insight, message unique, contraintes, critère de réussite |
| `marketing-direct` | `marketing-direct.md` | réponse directe hors email : courrier, catalogues, fichiers et listes, mécanisme de réponse (coupon, code, enveloppe-réponse), mesure au retour ; la rédaction = `copywriting` |
| `economie-unitaire` | `economie-unitaire.md` | économie d'un client : CAC, LTV, marge, délai de récupération, cash encaissé à 30 jours, acquisition financée par le client ; allocation du budget = `mesure-budget` |
| `gestion-crise` | `gestion-crise.md` | réputation attaquée et communication de crise : bad buzz, polémique, mea culpa, parler tôt, preuve avant annonce (RSE), protocole ; modération courante = `communaute` |

### Alias : libellés « hors liste » → tag retenu
Le libellé n'est pas redemandé ; la fiche n'est pas modifiée, `synthetiseur-connaissances` range le passage sous le tag retenu.

| libellé | tag retenu |
|---|---|
| experience-client, service client, onboarding client, fidélisation, récurrent, back-end (offres vendues ensuite → `offre`) | `retention-client` |
| IA générative dans la création, banalisation de l'information | `ia-creation` |
| relation avec les revendeurs, accès au marché | `distribution` |
| joint venture, recommended provider, affiliation, affiliation-partenariats, collabs créateurs | `partenariats` |
| prospection-sortante (contact à froid multicanal : appels, DM, SMS, courrier ; le script de conversation → `vente`) | `generation-leads` |
| acquisitions (rachats, croissance externe ; récit après fusion → `storytelling`), franchise (vendue comme offre → `offre`) | `strategie-croissance` |
| marketing-cause, raison d'être (`ethique` si récupération d'une cause), communication-politique, marketing non marchand (pub politique → `conformite-juridique` ; l'agence n'en fait pas) | `positionnement` |
| reponse-directe (rédaction → `copywriting`) | `marketing-direct` |
| finance-tresorerie, CAC, LTV, marge | `economie-unitaire` |
| communication-crise, preuve avant annonce RSE | `gestion-crise` |
| formats-series-streaming : sortie hebdo ou en bloc, seuil d'épisodes (contrat de plateforme → `monetisation`) | `youtube-long` |
| écriture, prise de notes, second cerveau, autoformation (méthode de fabrication du contenu) | `production` |
| twitter, X, threads X | `x-twitter` |
| méthode expérimentale, tests A/B et géographiques | `analyse-donnees` |
| allocation budgétaire entre canaux | `mesure-budget` |
| tarification, prix, échantillonnage, essai gratuit | `offre` |
| psychologie de la persuasion, biais cognitifs, sciences comportementales | `psychologie-persuasion` |
| message de marque, BrandScript | `copywriting` |
| vente en rendez-vous, pitch commercial | `vente` |
| lead magnets, génération de leads | `generation-leads` |

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
- 2026-10-21 : création de `lecteur-images` (pôle A, 60 agents). Aucun agent ne décrivait les images des sources web
  et sociales (premier cas : les 6 planches et schémas de `sources/web/google-abcd-youtube-ads/source.md`). Écrit
  dans `sources/<type>/<slug>/images.md` (une section par image : URL, ce qu'elle montre, texte recopié tel quel,
  chiffres « lu sur l'image, à vérifier »). Images dans un dossier neuf du scratchpad, version pleine taille d'abord,
  GIF animés vue par vue. Pas de chevauchement : les pages image des PDF restent à `extracteur-pdf`. Placé dans le
  pipeline 1 entre l'extracteur et `analyste-transcription`, qui lit désormais `images.md` s'il existe ;
  `extracteur-web` et `extracteur-social` signalent dans leur rapport les images de contenu à faire lire.
- 2026-10-21 : création de `developpeur-outils` (pôle A, 61 agents). Les scripts de `outils/` (`youtube/transcrire.py`,
  `youtube/decouper.py`) n'avaient pas de propriétaire, et les livres audio officiels d'Alex Hormozi (*$100M Offers*,
  *$100M Leads*, *$100M Money Models* ; sources C1 et C5 de `sources/a-traiter.md`) ne sont accessibles que par le
  flux RSS de son podcast *The Game* (Spotify ne permet pas le téléchargement) : il faut un outil `outils/podcast/`.
  Écrit dans `outils/<domaine>/` uniquement (scripts autonomes lancés avec `python3 -I`, `README.md`,
  `requirements.txt` à versions fixées, option `--sortie` pour tester dans le scratchpad, test réel obligatoire
  avant de rendre). Pas de chevauchement : il écrit l'outil, `transcripteur-audio` et les extracteurs s'en servent.
  `transcripteur-audio` complété : entrée et sortie explicites (`sources/podcast/<slug>/`, un livre en plusieurs
  épisodes = une source, ligne de `sources/index.md`), audio d'origine officielle seulement, scripts de
  `outils/podcast/` d'abord puis méthode manuelle, audio dans le scratchpad au lieu de `/tmp`, bug ou outil
  manquant demandé à `developpeur-outils`. `extracteur-youtube` : erreur de script → `developpeur-outils`.
- 2026-10-21 : acquis du lot 2 intégrés (modifications ciblées, missions et dossiers d'écriture inchangés).
  `strategiste-ads` et `redacteur-ads` : entrées complétées par `veille/plateformes/meta-ads.md` (§10) et les fiches
  `dAJyqo6wnq4`, `qBxEAqZbHVg`, `meta-andromeda`, `google-abcd-youtube-ads`, `google-abcd-playbook-2022`,
  `pILj7t-qQhs`, `binet-field-b2b-growth` ; « 3-6 créas à tester » remplacé par la diversification (3 à 5 concepts
  réellement distincts × 2 à 3 exécutions, puis un nouveau concept par semaine) ; budget dimensionné pour la phase
  d'apprentissage (≥ 50 × CPA visé / 7 par jour et par ensemble) ; contrôle d'Advantage+ creative (musique IA
  coupée pour Sillage, aucune variante IA non relue, aucune personne générée) ; UTM toujours. `garde-conformite` :
  nouvelle section « Entrée » avec les checklists Bpifrance (influence) et CNIL B2B / B2C (la CNIL fait foi sur
  l'emailing), la liste « Hooks interdits ou bloqués » de `connaissances/swipe-file/hooks.md` et
  `journal/questions-utilisateur.md` ; grille complétée : pas de pub Meta sociale, électorale ou politique dans l'UE
  (TTPA, 06/10/2025), catégories spéciales (finance, emploi, logement), options automatiques Meta coupées (« add
  music », texte IA dans l'image, traduction), rareté et témoignages seulement si réels, aucune collaboration
  rémunérée avec un créateur tant que la question juridique 2 n'est pas tranchée. `consolidateur-fiche` et
  `synthetiseur-connaissances` : tags `meta-ads`, `conformite-juridique`, `email`, `b2b` ajoutés à la taxonomie
  (liste de référence commune, fichier de principes par tag). `veilleur-algorithmes` : `meta-ads` ajouté aux
  plateformes suivies (fiche `veille/plateformes/meta-ads.md`) avec ses sources officielles Meta.
- 2026-10-21 : passe ciblée après la mise à jour de `connaissances/frameworks/index.md` (76 fiches-outils, 15 sources)
  et la vérification `connaissances/verifications/passe-2-droit.md`. Aucun agent créé (61 agents).
  `garde-conformite` : sortie élargie (décision de l'orchestrateur) à `marques/<slug>/10-ads/conformite-<campagne>.md`
  et `marques/<slug>/emails/<sequence>/conformite.md` (un seul fichier par contrôle, selon le livrable) ; entrées
  `conformite-influence-commerciale.md`, `arbre-regime-message-electronique-cnil.md`,
  `filtre-humain-ia-et-enhancements-meta.md` et `passe-2-droit.md`, qui prime sur les grilles en cas d'écart ; grille
  corrigée : 6 catégories interdites (art. 4 I-VI, pas 7), CPF en trois régimes (promotion encadrée par le décret
  2026-233 ; contrepartie liée à l'inscription interdite ; démarchage individuel des titulaires interdit à tous),
  contrat écrit dès 1 000 € HT cumulés (annonceur, année, objectif), référentiel Arcom pour les jeux d'argent,
  crypto à revérifier après le 01/07/2026, créateur établi dans l'EEE (art. 5-1), « 3 ans sans contact » = repère CNIL
  non contraignant, enrichissement automatique des leads → base légale, information, minimisation (RGPD).
  `publicateur` : section « Pub Meta : contrôles avant toute mise en ligne » (feu vert conformité, liste Advantage+ du
  plan case par case, UTM vérifiés, 24 h de marge ; `meta-ads.md` §10). `strategiste-ads` (13 frameworks pub + SOP
  créative + crawl / walk / run) et `redacteur-ads` (frameworks de création publicitaire ; ceux de pilotage et de
  mesure restent au stratège) : entrées complétées. `strategiste-positionnement` et `strategiste-offre` : frameworks
  de positionnement (Dunford, Enns) et de prix (Enns). `architecte-persona` : `prompt-decouverte-personas.md`,
  `analyse-de-reputation-et-minage-d-avis.md`. `ecouteur-audience` : nouvelle section « Entrée » avec ces deux fiches,
  `contenu-communautaire-et-ecoute.md` et `principes/communaute.md`. Pipeline 3 bis (campagne payante, séquence
  d'emails) ajouté.
- 2026-10-22 : quatre décisions de l'orchestrateur appliquées. Aucun agent créé (61 agents).
  **Taxonomie** : 12 tags ajoutés à la liste fermée, avec une définition d'une ligne chacun, dans
  `consolidateur-fiche` et `synthetiseur-connaissances` : `vente`, `generation-leads`, `copywriting`, `site-web`,
  `strategie-croissance`, `ethique`, `mesure-budget`, `relations-presse`, `identite-visuelle`,
  `psychologie-persuasion`, `lancement-produit`, `bouche-a-oreille`. `synthetiseur-connaissances` reçoit le tableau
  complet tag → fichier de principes (fichier créé à la première fiche qui porte le tag, « à venir » sinon ; un tag
  hors tableau → demande à `architecte-agents`). **Droit** : la section « Conséquences pour les agents » de
  `connaissances/verifications/registre.md` (sections E-G, ex-`passe-2-droit.md`) est relayée, avec les numéros
  JI/JP/Q, dans `prospecteur-collaborations` (colonnes pays d'établissement et contrepartie ; EEE JI16, hors UE JI15,
  contrat 1 000 € HT cumulés JI11, contrepartie en attente tant que Q2 est ouverte), `redacteur-newsletter` (lettre
  informative = prospection JP03, freemium au cas par cas JP03/JP04, CNIL et non Bpifrance JI24, expéditeur et
  désinscription JP01/JP08, pas d'email CPF JI19 ; ligne « Régime d'envoi » par email d'une séquence),
  `scenariste-reel` et `pont-motion-design` (bandeau formation ≥ 135 px, ≥ 90 % de la durée, JI09-JI10 ; « Images
  virtuelles » / « Images retouchées » JI07) et `strategiste-contenu` (nouvelle section « Règles » : pas de cold
  email ni DM CPF JI19, tunnel newsletter JP03). **Contrôle qualité** : `controleur-qualite-marketing` couvre aussi
  les campagnes (`10-ads/qa-<campagne>.md`) et les séquences d'emails (`emails/<sequence>/qa.md`), une grille /100
  par type, veto sous 85 ou sans feu vert de `garde-conformite`, section « Version validée » au lieu d'un kit ;
  `publicateur` exige ce verdict avant toute pub Meta ; pipeline 3 bis mis à jour. **Gabarit** : `archiviste`
  devient propriétaire de `marques/_modele/` (un sous-dossier par dossier `marques/<slug>/…` de cette carte, ajout
  seulement) ; sa ligne du pôle A est complétée (dossiers d'écriture manquants) ; section « Gabarit des marques ».
- 2026-10-22 : taxonomie, 2 tags de plus demandés par la fiche Doctolib (décision de l'orchestrateur), dans
  `consolidateur-fiche` et `synthetiseur-connaissances` : `recherche-client` (immersion terrain, entretiens clients,
  test du discours, JTBD ; fichier `recherche-client.md`, à venir) et `culture-entreprise` (rituels centrés client,
  valeurs, onboarding ; fichier `culture-entreprise.md`, à venir). Frontière : embaucher et structurer l'équipe
  reste `recrutement-equipe`.
- 2026-10-22 : relecture et droit des offres (décisions de l'orchestrateur). Aucun agent créé (61 agents).
  `correcteur` : relit aussi les campagnes (`10-ads/textes-<campagne>.md` → `10-ads/relecture-<campagne>.md`) et
  les séquences d'emails (objet, préheader, corps, texte brut → `emails/<sequence>/relecture.md`), un seul fichier
  par relecture ; colonne « emplacement » (variante, email, champ) ; ne touche ni aux chiffres, ni aux allégations,
  ni aux liens et UTM. Pipeline 3 bis : `correcteur` avant `garde-conformite` ; relecture ✏️ → corrections par le
  rédacteur, puis conformité ; recalé → `correcteur` relancé aussi. `controleur-qualite-marketing` lit les deux
  nouveaux fichiers de relecture. `garde-conformite` : renvoi à `passe-2-droit.md` remplacé par
  `connaissances/verifications/registre.md` (sections E-G, version fusionnée ; sources JI / JP / Q) ; nouvelle
  entrée `passe-3-droit-offres.md` « quand il existe » (prix de référence, fausse urgence, prévente, publicité
  comparative, enrichissement de leads), qui prime sur la grille pour ces sujets ; sans elle, prix barré, compte à
  rebours, prévente ou comparaison nommée → ⚠️ et question. **Taxonomie** : tag `packaging` (titres, miniatures,
  couvertures, couple titre + image avant le clic ; frontières `hooks` et `copywriting`) dans `consolidateur-fiche`
  et `synthetiseur-connaissances` (fichier `packaging.md`, à venir), demandé par la fiche Paddy Galloway
  (Z2uoA3bhJT0), utile aussi pour Caleb Ralston ; `titreur-miniatures` cite `packaging.md` (à venir).
- 2026-10-22 : passe taxonomie (lot Kapferer, Abraham, Trott, Boron, Money Models, Séguéla, MrBeast) et outils.
  Aucun agent créé (61 agents). Règle : un tag n'est créé que s'il couvre au moins 2 sources ou une compétence
  que l'agence produira, sinon alias. **Créés** dans `consolidateur-fiche` et `synthetiseur-connaissances` (même
  liste, mêmes définitions, fichier de principes à venir) : `ia-creation`, `retention-client` (décisions de
  l'orchestrateur), `distribution`, `partenariats`, `brief-creatif`, `marketing-direct`, `economie-unitaire`
  (demandé sous le nom `finance-tresorerie`), `gestion-crise`. `analyse-donnees` élargi à toute lecture de
  métriques (contenu, pub, tunnel de vente) et passé dans le tableau. `culture-entreprise` : « onboarding des
  salariés » (l'onboarding client va à `retention-client`). **Rattachés** : experience-client → `retention-client`,
  acquisitions et franchise → `strategie-croissance`, marketing-cause et communication-politique → `positionnement`,
  communication-crise → `gestion-crise`, formats-series-streaming → `youtube-long`. `synthetiseur-connaissances`
  reçoit une table des alias (libellés « hors liste » des fiches existantes → tag retenu) pour reclasser sans
  toucher aux fiches ; `consolidateur-fiche` en a la version courte. `transcripteur-audio` et `extracteur-youtube`
  renvoient à `outils/podcast/README.md` et `outils/youtube/README.md` avec les règles qui évitent les erreurs
  (`--simuler`, `--vocabulaire` court, `--travail` dans le scratchpad, même commande relancée si coupée,
  `--max-secondes` et `--sortie` réservés aux essais, découpe par `decouper.py` à taille constante).
- 2026-10-22 : passe « garde-fous des offres » (`connaissances/verifications/passe-3-droit-offres.md`, OP / OU / OV /
  OC / OD / OG / OR / OQ, fusion en cours dans `registre.md` ; garde-fous de pitch des fiches `6_CCutkM11g`,
  `JE2_7elAcxM`, `rPZG5xfN7vI`, `buAY7UtjCb4`, `aGI7puAXf6w`, `SUzKZfyaAK8`, `k834E6OTGTM` ; question utilisateur
  n° 5). **Créé** `redacteur-conditions-vente` (pôle C, 62 agents) : aucune définition ne rédigeait CGV, information
  précontractuelle, clause de prévente (acompte et non arrhes, L. 214-1), rétractation et sa fonctionnalité en ligne
  (L. 221-21), garanties ; écrit dans `marques/<slug>/conditions-vente.md` ; statut « projet » jusqu'à la validation
  écrite de l'utilisateur, relecture juriste recommandée, jamais d'avis juridique ; placé dans le pipeline 2 après
  `strategiste-offre`, avec la règle « pas d'offre publiée sans conditions validées ». **`garde-conformite`** : section
  « Checklist offres et pitch » (15 règles, chacune avec son identifiant), dont prix de référence = plus bas sur
  30 jours sans exemption produit nouveau, pas de valeur fictive à côté du prix, fausse urgence interdite en B2B
  (L. 121-5), rétractation jamais vendue comme avantage, garantie = engagement, pas de dénigrement nominatif ni de
  fausse fermeture, pas d'engagement acheté, partenariat signalé, règle d'attente ≤ 30 % d'avance sur la prévente de
  formation (OQ1) ; grille générale resserrée ; la ligne « sans passe 3 → ⚠️ » supprimée (la passe existe).
  Renvois courts dans `strategiste-offre` (nouvelle section « Règles »), `redacteur-ads`, `redacteur-newsletter`,
  `gestionnaire-communaute` (réponses aux prospects) et `controleur-qualite-marketing` (motif de veto « offres et
  pitch », lecture de `conditions-vente.md`). **Taxonomie** : liste fermée, fichiers de principes et alias
  déplacés dans la section « Taxonomie de référence » de ce fichier (seule copie ; propriétaire `architecte-agents`,
  qui la tenait déjà de fait ; pas de fichier `connaissances/taxonomie.md` : il sortirait de mon périmètre et ferait
  un fichier de plus à indexer). `consolidateur-fiche` et `synthetiseur-connaissances` y renvoient (copies
  supprimées) ; `connaissances/index.md` ne liste plus que les fichiers de principes existants. Décisions de
  l'orchestrateur intégrées : tag `x-twitter` créé (fichier `x-twitter.md`, veille `veille/plateformes/x.md`) ; alias
  écriture / prise de notes / second cerveau / autoformation → `production`, affiliation-partenariats →
  `partenariats` (définition précisée), prospection-sortante → `generation-leads` (script → `vente`).
