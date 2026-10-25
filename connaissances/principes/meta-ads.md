# Principes : Meta Ads (Facebook + Instagram)

> Tenu par `synthetiseur-connaissances`. Création : 2026-10-25 (grande synthèse, équipe S4 « publicité et mesure »).
> Périmètre : le système publicitaire Meta (objectifs, Advantage+, Andromeda et la chaîne de diffusion, phase
> d'apprentissage, créatives, lecture du compte, règles propres à Meta). Les principes généraux de création
> publicitaire sont dans `publicite.md` ; attribution, incrémentalité et budget dans `mesure-budget.md` ; protocole de
> test dans `analyse-et-iteration.md` ; droit dans `conformite-juridique.md`. L'organique Instagram est dans
> `croissance-audience.md` et `formats-courts.md`.
>
> **Note de taxonomie** : aucune fiche ne porte encore le tag `meta-ads` (créé après leur consolidation). Les fiches
> `meta-andromeda`, `dAJyqo6wnq4` et `qBxEAqZbHVg` le signalent elles-mêmes (« pas de tag meta-ads » ; `instagram` et
> `publicite` portent l'essentiel). Leur contenu correspond mot pour mot à la définition du tag dans `agents.md`
> (« Facebook + Instagram : Advantage+, Andromeda, apprentissage ») : il est rangé ici.
>
> **Sources traitées (6 fiches, 4 experts + 1 éditeur) et la veille** :
> `meta-andromeda` (Engineering at Meta, 02/12/2024, **éditeur**) · `dAJyqo6wnq4` (Ben Heath, tutoriel 2026) ·
> `qBxEAqZbHVg` (Coudac, masterclass 03/2024, en partie **daté 2024**) · `yRgPbqywUJ8` (Dara Denney, 07/2026) ·
> Hormozi (`6_CCutkM11g`, `Jmkq5RLjm0U`, un expert) · `veille/plateformes/meta-ads.md` (2026-10-21, cité
> `[veille:meta-ads §x]`), qui fait foi pour l'état du système en 2026.
> Vérification : registre, lignes PA01 à PA25, PG01 à PG10, PC01 à PC11.
>
> **Indépendance** : Heath, Coudac et Denney vendent du conseil ou de la formation Meta ; Meta vend l'inventaire et
> promeut Advantage+. Aucun chiffre de performance de cette page n'est indépendant.
>
> **Frameworks liés** : `lancement-meta-structure-1-1-1.md` · `objectif-de-campagne-et-de-performance-meta.md` ·
> `filtre-humain-ia-et-enhancements-meta.md` · `lecture-de-compte-hierarchie-gold-bronze.md` · `matrice-depense-cpa.md` ·
> `plafond-de-conversion-et-cercles-du-marche.md` · `plan-d-atterrissage-et-timing.md` · `cac-blended-et-mesure-du-mix.md` ·
> `pub-reponse-directe-7-cases.md` · `audit-des-lacunes-du-compte-pub.md` · `grille-source-deduction-praticiens.md`.
> **Swipe-file** : `swipe-file/structures.md` P1 (pub Meta image) et P3 (plan de déclinaison créative).
>
> **Labo** : `experiences/apprentissages.md` est **vide** au 2026-10-25. Six expériences Meta attendent une marque
> (voir « Tests au labo ») ; la première à lancer est `2026-10-22-meta-regle-passage-tests-et-budget` (rang 1, 125/125).

## Légende

- **Consensus** : experts distincts (Hormozi = 1). Meta est compté à part, comme « éditeur ».
- **Confiance** (registre) : **haute** = règle officielle de Meta lue ou vérifiée ✅, ou 3 experts convergents sans
  chiffre contredit ; **moyenne** = 2 experts ou règle seulement relayée ; **faible** = un seul praticien ou chiffre ❓.
- **Niveaux de la veille** repris tels quels : [OFFICIEL], [OFFICIEL-relayé], [PRATICIEN], [DÉDUCTION].
- **Interface** : Meta ne publie aucun journal des libellés [verif:PA17 ❓] : toute procédure à l'écran se revérifie.
- **Chiffres de Meta** : affirmations d'éditeur, citées avec leur date, jamais comme promesse de résultat.

## Résumé (14 principes)

| # | Principe | Consensus | Confiance |
|---|---|---|---|
| MA1 | Optimise sur la vraie conversion la plus basse qui a assez de volume | 3 + Meta | haute |
| MA2 | Donne une direction au système, ne le contrains que pour une raison métier | 2 + Meta | haute |
| MA3 | Diversifie les concepts sur le fond : c'est la créative qui trouve l'audience | 3 + Meta | haute |
| MA4 | Pas de nombre magique : 3 à 5 concepts réellement distincts, un nouveau par semaine | 2 + Meta | moyenne |
| MA5 | Dimensionne le budget pour sortir d'apprentissage, puis ne touche à rien pendant l'apprentissage | 2 + Meta | moyenne |
| MA6 | Pose les fondations avant de lancer : compte, mesure, catégories, délais | 2 + Meta | haute |
| MA7 | Lis le compte de haut en bas, toujours par comparaison, en connaissant le réglage d'attribution | 1 + Meta | moyenne |
| MA8 | Coupe ou pousse une créative sur la matrice dépense × CPA, après le CPC ; lis les statuts | 1 + Meta | moyenne |
| MA9 | Reste le filtre humain de l'IA de Meta : chaque variante et chaque amélioration relues | 1 + Meta | haute |
| MA10 | Pour grandir, élargis la part chaude du marché au lieu d'empiler du budget sur la même cible | 1 | moyenne |
| MA11 | Livre des fichiers pub aux spécifications officielles, moment fort dans les 2 premières secondes | Meta | haute |
| MA12 | Teste une créative dans l'outil prévu pour, avec un critère fixé avant | 1 + Meta | moyenne |
| MA13 | Cite les chiffres de Meta comme des affirmations datées, jamais « Andromeda = +22 % » | 1 + registre | haute |
| MA14 | Aucune dépense ni mise en ligne sans validation explicite de l'utilisateur, via l'API officielle | règle du repo + Meta | haute |

---

## Principes partagés par 3 sources ou plus

### MA1. Optimise sur la vraie conversion la plus basse qui a assez de volume
- **Pourquoi** : « Meta's optimization system is very literal » ; c'est l'**objectif de performance**, pas l'objectif de
  campagne, qui décide de qui voit la pub. Demander des clics donne « des gens qui cliquent » [fiche:dAJyqo6wnq4
  00:09-00:25]. Coudac : seul compte le coût des **nouveaux clients** [fiche:qBxEAqZbHVg 00:32]. La sortie
  d'apprentissage demande environ 50 événements d'optimisation en 7 jours [verif:PA01 ✅, confiance moyenne, repère et
  non couperet].
- **Comment l'appliquer** :
  1. Leads ou Sales pour un compte qui débute ; Notoriété, Trafic et Interaction sont des pièges à petit budget
     (`objectif-de-campagne-et-de-performance-meta.md`).
  2. Événement d'optimisation = le plus bas du tunnel (Purchase, prise de rendez-vous) **si** son volume permet
     l'apprentissage, sinon l'étape juste au-dessus (MA5).
  3. Offres de valeurs différentes : maximiser la valeur, quitte à payer un coût par lead plus élevé.
  4. Juger un coût à la **qualité exploitable** du résultat : un lead moins cher qu'on ne peut pas servir ne vaut rien
     (« What's the point of having a lower cost per lead if you can't service those leads? ») [fiche:dAJyqo6wnq4 00:31].
- **Pour une marque d'entreprise / un studio B2B** : Sillage optimise sur la **prise de rendez-vous** (pixel + API
  Conversions sur la page de réservation), pas sur les vues de la vidéo.
- **Sources** : [fiche:dAJyqo6wnq4 enseignements 1, 2, 4, 10] · [fiche:qBxEAqZbHVg enseignement 1] ·
  [fiche:6_CCutkM11g (CAC récupéré, enseignement 10)] · [veille:meta-ads §6].
- **Consensus** : 3 experts (Heath, Coudac, Hormozi) + Meta (seuil d'apprentissage).
- **Confiance** : **haute**.

### MA2. Donne une direction au système, ne le contrains que pour une raison métier
- **Pourquoi** : depuis le 29/10/2025, les campagnes Sales, App et Leads ont l'automatisation Advantage+ activée dès le
  départ [veille:meta-ads §4, OFFICIEL] ; l'API ne permet plus de créer d'anciennes campagnes ASC ou AAC depuis le
  19/05/2026 [veille:meta-ads §4]. Heath : « Controls » pour les limites réelles (lieu, âge minimum, langue),
  « Suggestions » que Meta peut dépasser ; ciblage détaillé de 0 à 4 intérêts évidents, « not what we do anymore »
  [fiche:dAJyqo6wnq4 00:27-00:36]. Andromeda personnalise dès la présélection et réduit la logique à base de règles
  [fiche:meta-andromeda enseignements 3, 4] ; « moins on contraint, plus le modèle a de latitude » est une
  **déduction** de la fiche, pas une phrase de Meta.
- **Comment l'appliquer** :
  1. Advantage+ (audience, placements, budget) par défaut ; structure consolidée, jamais plusieurs ensembles sur des
     audiences et objectifs similaires [veille:meta-ads §10 règle 4].
  2. Contraintes seulement pour une raison écrite : zone réellement servie, âge légal, langue, exclusion des clients
     existants en acquisition (Customer Lifecycle Strategy, ouverte à tous le 06/10/2026 [veille:meta-ads §4]).
  3. « Advertise where your customers are » : ni élargir artificiellement (commerce local), ni restreindre
     artificiellement (marque nationale).
  4. Audience par créative (Marketing API, 19/10/2026) : seulement si une créative vise clairement une tranche d'âge ou
     un genre ; incompatible avec l'audience Advantage+ [veille:meta-ads §3.1, §10 règle 10].
- **Sources** : [fiche:dAJyqo6wnq4 enseignement 3] · [fiche:meta-andromeda enseignements 3, 4, playbook 4] ·
  [veille:meta-ads §4, §10 règles 4 et 10] · [fiche:yRgPbqywUJ8 (le persona porté par la créa)].
- **Consensus** : 2 experts (Heath, Denney) + Meta. Désaccord D1.
- **Confiance** : **haute** pour la règle officielle (Advantage+ par défaut) ; l'avantage de performance d'Advantage+
  sur le manuel reste **à tester** (`2026-10-22-meta-advantage-audience-vs-manuel`, rang 11).

### MA3. Diversifie les concepts sur le fond : c'est la créative qui trouve l'audience
- **Pourquoi** : « the focus has shifted from niche targeting to creative diversification as the best lever to find the
  most relevant audiences » (Meta, 22/04/2025) [verif:PA23 ✅] ; un porte-parole redit le 28/09/2026 « diversify your
  creative, test, and let the system optimize ». Meta confirme un **effet** : des créatives trop semblables peuvent être
  servies aux mêmes audiences et mener aux statuts « Creative limited » ou « Creative fatigue » ; il refuse de détailler
  le mécanisme [veille:meta-ads §2] [verif:PA24 ❓ pour toute « pénalité »]. Coudac : la créa est le levier n° 1 et une
  vidéo que les gens aiment regarder fait baisser le CPM (selon lui) [fiche:qBxEAqZbHVg 09:39-13:23]. Denney : personas ×
  angles × niveaux de conscience [fiche:yRgPbqywUJ8 13:41].
- **Comment l'appliquer** :
  1. Chaque concept diffère d'au moins un axe de fond : motivation ou frein d'achat, persona, situation d'usage
     (« Reimagine your products as different situations »), angle, format (9:16, 4:5, carrousel) [veille:meta-ads §3.1,
     §10 règle 1].
  2. Un brief créatif par semaine : ce qui marche, l'audience nouvelle visée, la direction (consigne Meta du
     19/11/2024) [veille:meta-ads §3.1].
  3. Ne pas multiplier des quasi-doublons en espérant plus de chances [fiche:meta-andromeda playbook 3].
  4. La note « Creative diversity » (High / Medium / Low, « in development ») est un indice, pas un verdict ; elle ne
     porte que sur le visuel [veille:meta-ads §3.1, §10 règle 3].
- **Pour une marque d'entreprise / un studio B2B** : pour Sillage, un concept = une situation client différente
  (lancement produit, levée de fonds, recrutement), pas la même animation avec un autre fond.
- **Sources** : [verif:PA23, PA24] · [fiche:meta-andromeda enseignements 2, 5, framework E] ·
  [fiche:qBxEAqZbHVg enseignement 7] · [fiche:yRgPbqywUJ8 enseignement 9] · [fiche:dAJyqo6wnq4 enseignement 8] ·
  [veille:meta-ads §2, §3]. Principe général : `publicite.md` P7.
- **Consensus** : 3 experts (Coudac, Denney, Heath) + Meta (officiel).
- **Confiance** : **haute** (consigne officielle vérifiée).

### MA6. Pose les fondations avant de lancer : compte, mesure, catégories, délais
- **Pourquoi** : fuseau horaire et devise sont « very difficult to change later on » ; les changer crée un nouveau compte
  selon des guides tiers [verif:PA09 🟡]. Les catégories spéciales non déclarées exposent au rejet, voire à la fermeture
  du compte [verif:PA07 ✅]. Coudac : tracking, RGPD et TTC/HT faussent le ROAS [fiche:qBxEAqZbHVg 30:49-33:58].
- **Comment l'appliquer** (checklist de `lancement-meta-structure-1-1-1.md`) :
  1. Compte d'une marque française en **EUR et Europe/Paris** dès la création [verif:PA09].
  2. Pixel + API Conversions + valeur ; vérifier l'ID du pixel ; **UTM systématiques** (règle de l'agence, écart
     assumé avec Heath : D5).
  3. Catégories spéciales (Financial Products and Services, Employment, Housing, Social Issues, Elections or Politics)
     déclarées ; **aucune pub sociale, électorale ou politique dans l'UE** depuis le 06/10/2025 [verif:PA07 ✅] (
     `conformite-juridique.md` J10).
  4. Valeurs de conversion en **HT** pour la France : ROAS HT = ROAS TTC / 1,2, soit 16,7 % de moins, pas 20 %
     [verif:PG04 ❌ de la fiche].
  5. Prévoir **jusqu'à 24 h** de vérification Meta avant la date de diffusion voulue, jamais 30 min [verif:PA08 🟡].
- **Sources** : [fiche:dAJyqo6wnq4 enseignement 10] · [fiche:qBxEAqZbHVg enseignements 5, 6] · [verif:PA07, PA08, PA09,
  PG04] · [veille:meta-ads §7 bis, §10 règles 13 et 14].
- **Consensus** : 2 experts (Heath, Coudac) + Meta.
- **Confiance** : **haute** (règles vérifiées ; PA09 relayé seulement).

## Principes soutenus par 1 ou 2 experts (souvent appuyés par une règle officielle)

### MA4. Pas de nombre magique : 3 à 5 concepts réellement distincts, un nouveau par semaine
- **Pourquoi** : Meta ne donne **aucun nombre** lié à Andromeda [verif:PA25 🟡]. Seule consigne chiffrée officielle,
  pour Advantage+ shopping (19/11/2024) : « at least 20 diversified ads », de nouvelles pubs chaque semaine et « 20-30% of
  your overall ad budget towards testing new ads » [veille:meta-ads §3.1]. La règle « 6 pubs maximum par ensemble » a été
  retirée sans explication [verif:PA25].
- **Comment l'appliquer** (règle de travail de l'agence, déduction fondée sur l'officiel [veille:meta-ads §10 règle 2]) :
  1. Petit budget (Sillage, marque au lancement) : **3 à 5 concepts × 2 à 3 exécutions**, puis au moins **un nouveau
     concept par semaine**.
  2. Budget suffisant pour Advantage+ Sales : viser le repère officiel de 20 pubs diversifiées.
  3. 20 à 30 % du budget sur les nouvelles créatives.
  4. Au démarrage, Heath met une seule pub à 5 textes et 5 titres [fiche:dAJyqo6wnq4 00:55] : acceptable pour un test
     borné, à dépasser dès que les premiers résultats arrivent.
- **Sources** : [veille:meta-ads §3, §10 règle 2] · [verif:PA23, PA25] · [fiche:dAJyqo6wnq4 enseignements 5, 8] ·
  [fiche:yRgPbqywUJ8 enseignement 9].
- **Consensus** : 2 experts (Heath, Denney) + Meta. Désaccord D2 (volume).
- **Confiance** : **moyenne** ; à tester : `2026-10-22-meta-volume-concepts-creatifs` (6 contre 3 concepts, rang 9).

### MA5. Dimensionne le budget pour sortir d'apprentissage, puis ne touche à rien pendant l'apprentissage
- **Pourquoi** : tout nouvel ensemble de pubs démarre en apprentissage ; ciblage, créative, événement, ajout d'une pub,
  pause de 7 jours ou plus, enchère et forte variation de budget le relancent [verif:PA02 ✅, relayé]. Le seuil de
  « +20 % de budget » ne vient que de praticiens [verif:PA02] [veille:meta-ads §6].
- **Comment l'appliquer** :
  1. Budget **quotidien**, au niveau campagne s'il y a plusieurs ensembles ; budget global déconseillé (dépense
     irrégulière [verif:PA03 🟡]) [fiche:dAJyqo6wnq4 00:14-00:17].
  2. Budget quotidien par ensemble ≥ (50 × CPA cible) / 7 [veille:meta-ads §10 règle 5, déduction] ; si c'est hors de
     portée, regrouper les ensembles ou optimiser un événement plus fréquent, **après accord de l'utilisateur**.
  3. Regrouper les modifications importantes ; prolonger une campagne qui marche au lieu de la recréer.
  4. Montant initial : assez pour tester plusieurs pubs, une somme qui « piquerait un peu » si elle était perdue,
     validée par l'utilisateur [fiche:dAJyqo6wnq4 00:16].
  5. Paliers de hausse : à calibrer sur nos comptes (`mesure-budget.md` B6).
- **Sources** : [fiche:dAJyqo6wnq4 enseignements 5, 6] · [verif:PA01, PA02, PA03] · [veille:meta-ads §6, §10 règle 5] ·
  [fiche:qBxEAqZbHVg enseignement 8 (variations d'investissement assumées)].
- **Consensus** : 2 experts (Heath, Coudac) + Meta.
- **Confiance** : **moyenne** (pages d'aide Meta lues seulement relayées) ; à tester :
  `2026-10-22-meta-regle-passage-tests-et-budget` (palier +50 % contre +20 %, rang 1).

### MA7. Lis le compte de haut en bas, toujours par comparaison, en connaissant le réglage d'attribution
- **Pourquoi** : un compte est une chaîne de transmission (argent → impressions → clics → ventes) ; on lit gold (CPA,
  ROAS) → intermédiaires (CPC, CPM) → bronze (CTR, CR, panier), et on ne descend que si le niveau supérieur va mal
  [fiche:qBxEAqZbHVg 10:44-22:36]. La performance bouge souvent sans vous (saison, conjoncture, tracking) : raisonner
  par comparaison avec une période de référence [fiche:qBxEAqZbHVg 30:45-33:58]. Les règles de mesure de Meta ont
  changé en 2026 : clic = **clic sur lien** depuis mars 2026, nouvelle catégorie « engage-through » 1 jour, fenêtres 7 j
  et 28 j après vue retirées de l'API le 12/01/2026 ; défaut : 7 j clic + 1 j engage-through + 1 j vue [verif:PA04 ✅].
- **Comment l'appliquer** :
  1. Commencer par les 20 % de campagnes qui font 80 % de la dépense ; CPA = panier moyen / ROAS.
  2. Chaque rapport indique le réglage d'attribution ; une baisse des conversions « clic » après mars 2026 est un
     **reclassement**, pas une baisse de performance [verif:PA04].
  3. Ne jamais trancher Meta contre GA4 sans test d'incrémentalité : GA4 (data-driven) ignore les impressions sans clic
     [verif:PA05 ✅, PA06 🟡] (`mesure-budget.md` B2).
  4. Le ROAS de plateforme est un indicateur de pilotage, pas la vérité business (`mesure-budget.md` B1).
- **Sources** : [fiche:qBxEAqZbHVg enseignements 5, 6] · [verif:PA04, PA05, PA06] · [veille:meta-ads §7].
  Framework `lecture-de-compte-hierarchie-gold-bronze.md`.
- **Consensus** : 1 expert (Coudac) + Meta (règles d'attribution).
- **Confiance** : **moyenne** (méthode d'une agence ; règles d'attribution vérifiées).

### MA8. Coupe ou pousse une créative sur la matrice dépense × CPA, après le CPC ; lis les statuts de diffusion
- **Pourquoi** : chaque créa se place selon sa dépense et son CPA (couper, pousser, winner, erreur de media buying) ;
  l'attribution par créa est floue, donc on vérifie le CPC avant de couper sur le seul CPA [fiche:qBxEAqZbHVg 35:03].
  Meta affiche « Creative limited », « Creative fatigue » et une note « Creative diversity » [veille:meta-ads §3].
- **Comment l'appliquer** : `matrice-depense-cpa.md` ; un statut « limited » ou « fatigue », ou une note Low, appelle
  un **nouveau concept**, pas une variante de plus [veille:meta-ads §10 règle 3]. Les définitions chiffrées de ces
  statuts circulent sans source Meta [veille:meta-ads §3.2, PRATICIEN] : ne pas les citer.
- **Sources** : [fiche:qBxEAqZbHVg enseignement 7] · [veille:meta-ads §3.1, §10 règle 3].
- **Consensus** : 1 expert (Coudac) + Meta.
- **Confiance** : **moyenne**.

### MA9. Reste le filtre humain de l'IA de Meta : chaque variante et chaque amélioration relues
- **Pourquoi** : « Absolutely use it, but you need to be the filter as the advertiser » ; Heath rejette un titre IA à la
  promesse fausse et les images où une personne générée le remplace [fiche:dAJyqo6wnq4 00:51-01:00]. Meta propose de la
  **musique générée par IA** (29/10/2025), de la vidéo à partir d'images statiques (pour tous depuis le 06/10/2026) et
  appose un libellé « AI info » ; un humain photoréaliste généré déclenche un libellé visible [veille:meta-ads §5].
- **Comment l'appliquer** (`filtre-humain-ia-et-enhancements-meta.md`) :
  1. Relire une à une les améliorations Advantage+ creative à chaque lancement (certaines seraient pré-cochées selon des
     praticiens, non vérifié [veille:meta-ads §5]).
  2. **Couper toute musique** (« add music », musique IA) : règle Sillage et grille de `garde-conformite`.
  3. Expansion d'image, arrière-plans générés, vidéo à partir d'images : seulement après validation explicite de
     l'utilisateur, en A/B contre l'original [veille:meta-ads §10 règle 8].
  4. Jamais d'humain IA comme faux client ou faux témoin, même étiqueté [veille:meta-ads §10 règle 9]
     (`conformite-juridique.md` J5).
- **Sources** : [fiche:dAJyqo6wnq4 enseignement 9] · [veille:meta-ads §5, §10 règles 8 et 9] ·
  [`.claude/agents/garde-conformite.md` grille « Plateforme »].
- **Consensus** : 1 expert (Heath) + Meta.
- **Confiance** : **haute** (règles du repo et faits officiels).

### MA10. Pour grandir, élargis la part chaude du marché au lieu d'empiler du budget sur la même cible
- **Pourquoi** : Meta ne juge acheteuse qu'une partie du marché ; plus de budget sur la même cible fait monter le CPM et
  la répétition, pas la portée (exemple pédagogique : répétition de 5 à environ 14 sur le même million, arithmétique
  juste [verif:PG07 ✅]) [fiche:qBxEAqZbHVg 44:16-46:24]. Le marché chaud et tiède s'élargit d'année en année :
  « C'est parfaitement possible, mais ça prend du temps. »
- **Comment l'appliquer** : surveiller CPM et répétition à chaque palier ; ouvrir de nouveaux personas et situations
  (MA3) avant d'ajouter du budget ; le moyen d'élargissement (campagnes de vue de vidéo ou diversité créative) est
  arbitré en D3. Framework `plafond-de-conversion-et-cercles-du-marche.md`.
- **Sources** : [fiche:qBxEAqZbHVg enseignement 10] · [verif:PG07].
- **Consensus** : 1 expert (Coudac) ; rejoint `mesure-budget.md` B4 (portée large selon Binet & Field).
- **Confiance** : **moyenne** (mécanisme cohérent ; tactique datée 2024).

### MA11. Livre des fichiers pub aux spécifications officielles, moment fort dans les 2 premières secondes
- **Pourquoi** : Ads Guide de Meta, consulté le 21/10/2026 : Reels et Stories 9:16 en **1440×2560**, zones de sécurité
  **14 % en haut, 35 % en bas, 6 % sur chaque côté** ; Facebook Feed **4:5 en 1440×1800** ; carrousel de 2 à 10 cartes,
  4:5 s'il n'y a que des images, 1:1 s'il contient des vidéos ; son et sous-titres « optional, but recommended »
  [veille:meta-ads §8]. « 46% of online purchase conversions with Reels now happen within the first 2 seconds of
  attention » (Meta, 03/03/2026, chiffre d'éditeur) [veille:meta-ads §3.2].
- **Comment l'appliquer** : exports pub de Sillage au-dessus du 1080 de l'organique (1440×2560 et 1440×1800), rien
  d'important dans les zones de sécurité, moment fort sous 2 s, voix et effets sonores, jamais de musique
  [veille:meta-ads §10 règle 7]. Ne pas concevoir pour le muet [verif:P02 ❌ de la croyance « 80-90 % sans le son »].
- **Écart à corriger** : `lancement-meta-structure-1-1-1.md` et la fiche Heath prévoient du **1:1** pour les fils ;
  l'Ads Guide recommande le **4:5** pour Facebook Feed (demande à `extracteur-frameworks`).
- **Sources** : [veille:meta-ads §8, §10 règle 7] · [fiche:dAJyqo6wnq4 enseignement 7] · [verif:P02].
- **Consensus** : règle officielle (Meta).
- **Confiance** : **haute**.

### MA12. Teste une créative dans l'outil prévu pour, avec un critère fixé avant
- **Pourquoi** : l'outil Creative testing compare jusqu'à 5 nouvelles pubs (10 sur certains comptes) dans un ensemble
  existant, dépense à parts égales, sans recouvrement d'audience, 30 jours au plus ; critère CPC, coût par résultat ou
  conversion [verif:PA16 ✅, confiance moyenne]. Des ensembles dupliqués se font concurrence sur les mêmes audiences
  (déduction de la veille [veille:meta-ads §10 règle 16]).
- **Comment l'appliquer** : critère, durée et budget écrits avant le test ; pas de test tant que la campagne n'a pas
  passé l'étape 2 de `2026-10-22-meta-regle-passage-tests-et-budget` (dépendance notée dans `experiences/index.md`) ;
  un seul test à la fois par ensemble de pubs. Protocole général : `analyse-et-iteration.md` A10.
- **Sources** : [verif:PA16] · [veille:meta-ads §3.1, §10 règle 16] · [fiche:dAJyqo6wnq4 enseignement 5 (à ignorer au
  tout début)].
- **Consensus** : 1 expert (Heath, pour le moment où l'on passe aux tests) + Meta.
- **Confiance** : **moyenne** (doc Meta lue seulement relayée).

### MA13. Cite les chiffres de Meta comme des affirmations datées, jamais « Andromeda = +22 % »
- **Pourquoi** : le +22 % de ROAS vise les annonceurs qui n'utilisaient pas Advantage+ creative et ont activé « its
  AI-driven targeting features », sans période, échantillon ni groupe témoin : ce n'est pas un résultat d'Andromeda
  [verif:PA18 ❓]. Le seul chiffre qu'Andromeda revendique pour lui-même est +8 % d'« ads quality » sur des segments
  sélectionnés [verif:PA20 🟡] ; le +7 % de conversions avec la génération d'images est une estimation [verif:PA19 ❓].
  Les chiffres ultérieurs (GEM +18,9 %, Generative Recommender +15,7 %) sont du même type [veille:meta-ads §1, §9].
- **Comment l'appliquer** : formulation honnête : « Meta présente la diversification créative comme “the best lever to
  find the most relevant audiences” (avril 2025) » ; « Entity ID », « seuil de similarité de 60 % », « 25 conversions
  suffisent » sont des hypothèses de praticiens [veille:meta-ads §3.2, §10 règle 12]. Grille
  `grille-source-deduction-praticiens.md`.
- **Sources** : [fiche:meta-andromeda enseignement 7, framework E] · [verif:PA18, PA19, PA20, PA25] · [veille:meta-ads §2].
- **Consensus** : 1 source (Meta, qui se cite) + registre.
- **Confiance** : **haute** (vérifié).

### MA14. Aucune dépense ni mise en ligne sans validation explicite de l'utilisateur, via l'API officielle
- **Pourquoi** : règle non négociable du repo (« Rien n'est publié sans validation explicite » ; « pas de robots avec
  mots de passe »). Cliquer « Publish » est une publication [fiche:dAJyqo6wnq4 « Pour Sillage »]. Le serveur MCP Meta Ads
  exige lui-même des permissions et une approbation explicite avant mise en ligne [veille:meta-ads §5, 06/10/2026].
- **Comment l'appliquer** : passage par `publicateur`, API Marketing ou serveur MCP officiel ; jamais d'automatisation
  par identifiants ; tout changement de budget au-delà du plan validé repasse par l'utilisateur.
- **Sources** : `CLAUDE.md` · [veille:meta-ads §10 règle 11].
- **Consensus** : règle du repo + Meta. **Confiance** : **haute**.

---

## Désaccords entre experts

### D1. Ciblage manuel ou Advantage+ : la créative est-elle devenue le ciblage ?
- **Positions** :
  - Meta : la diversification créative remplace le ciblage de niche comme « best lever » [verif:PA23 ✅] ;
    Advantage+ activé par défaut pour Sales, Leads et App depuis 2025 [veille:meta-ads §4]. Chiffres d'éditeur seulement
    (« +22 % » mal attribué [verif:PA18 ❓] ; −9 % de CPA annoncé le 22/04/2025).
  - Heath : direction plutôt que contraintes, 0 à 4 intérêts ; mais **décocher** « reach more people likely to
    respond » pour un commerce local, même si Meta promet un coût par résultat 6,7 % plus bas (estimation propre à son
    compte [verif:PC04 🟡]) [fiche:dAJyqo6wnq4 00:27-00:36].
  - Praticiens cités par la veille : « la diversification **remplace** le ciblage » (Jon Loomer, 20/10/2025) [PRATICIEN].
  - Nuance officielle récente : l'audience par créative (19/10/2026) réintroduit un ciblage âge-genre par pub, au prix de
    l'audience Advantage+ [veille:meta-ads §3.1].
  - Denney : on « cible » par le persona que porte la créa [fiche:yRgPbqywUJ8 enseignement 5].
- **Recommandation de l'agence** : audience **Advantage+ par défaut**, contraintes limitées aux raisons métier écrites
  (zone servie, âge légal, langue, exclusion des clients en acquisition). Le ciblage manuel n'est utilisé qu'avec une
  raison documentée (offre locale stricte, B2B de niche identifiable, réglementation). La formule « la créa est le
  ciblage » se dit avec la citation officielle de Meta, jamais avec un chiffre d'éditeur.
- **Test** : `2026-10-22-meta-advantage-audience-vs-manuel` (rang 11), A/B natif au coût par résultat **qualifié**.
- **Ce qui ferait changer** : un ciblage manuel nettement meilleur au coût par résultat qualifié sur au moins deux
  marques, ou une annonce officielle de Meta qui change le défaut.

### D2. Combien de créatives ?
- **Positions** :
  - Meta : aucun nombre lié à Andromeda [verif:PA25 🟡] ; repère Advantage+ shopping de 20 pubs diversifiées et
    nouvelles pubs chaque semaine (19/11/2024) ; cas client Dribbleup, de 3-4 à près de 50 nouvelles créatives par
    semaine [veille:meta-ads §3].
  - Hormozi (offre « Goated Ads » présentée au lancement de *Money Models*) : passer d'environ 5 à **600 pubs par mois**
    avec la structure hook – meat – CTA (affirmation de vente, non vérifiée) [fiche:6_CCutkM11g framework, ligne Leads].
  - Praticiens (veille) : 15 à 20 pubs par ensemble ; 8 à 12 concepts par campagne ; 3 concepts distincts renouvelés
    toutes les 2 semaines si le budget est serré ; Loomer : dépasser 2-3 pubs, mais 50 ne garantissent rien
    [veille:meta-ads §3.2, PRATICIEN].
  - Heath : au départ, une seule pub à 5 textes et 5 titres [fiche:dAJyqo6wnq4 00:55].
- **Recommandation de l'agence** : on compte en **concepts réellement distincts**, pas en fichiers. Petit budget :
  3 à 5 concepts × 2 à 3 exécutions, puis un nouveau concept par semaine et 20 à 30 % du budget en test ; gros budget
  Advantage+ Sales : le repère officiel de 20 pubs diversifiées. Le volume ne doit jamais faire baisser le niveau Sillage
  (« zéro défaut ») : mieux vaut 3 concepts justes que 30 variantes cosmétiques.
- **Test** : `2026-10-22-meta-volume-concepts-creatifs` (6 contre 3 concepts à budget égal, rang 9).
- **Ce qui ferait changer** : un gain net de 6 concepts sur 3 au coût par résultat, répété sur deux marques ; ou un
  nombre officiel publié par Meta.

### D3. Élargir l'audience : campagnes de vue de vidéo ou diversité créative ?
- **Positions** : Coudac (03/2024) : des campagnes de notoriété, en particulier de **vue de vidéo**, font entrer de
  nouvelles personnes dans l'audience jugée acheteuse (« on l'utilise énormément ») [fiche:qBxEAqZbHVg 45:21],
  **[DATÉ 2024]**. Meta (2025-2026) : la diversification créative est le levier pour trouver de nouvelles audiences
  [verif:PA23] ; Heath : notoriété = « an easy way to spend a bunch of money and not really see anything back » à petit
  budget [fiche:dAJyqo6wnq4 00:11].
- **Recommandation de l'agence** : la diversité créative est le moyen **par défaut** ; les campagnes de vue de vidéo
  restent une hypothèse à tester pour une marque qui plafonne déjà en conversion, pas un outil de démarrage. Pour
  Sillage, une campagne de marque vidéo se juge sur ses indicateurs de marque (`mesure-budget.md` B5), pas sur le coût
  par vue.
- **Ce qui ferait changer** : un test d'incrémentalité (Conversion Lift) montrant qu'une campagne de vue de vidéo baisse
  le CAC des campagnes de conversion sur la période suivante (expérience à créer).

### D4. Démarrer avec Meta (Heath) ou par l'organique (Coudac) ?
- Tranché dans `publicite.md` D4 : sans ventes constatées, un premier budget Meta est un **test borné**.

### D5. UTM : « overkill » pour un débutant (Heath) ou systématiques ?
- **Positions** : Heath les juge superflus au départ [fiche:dAJyqo6wnq4 « Limites »] ; l'agence en a besoin pour croiser
  Meta, l'analytics et le CRM (`lancement-meta-structure-1-1-1.md`).
- **Recommandation de l'agence** : **UTM systématiques**. Sans eux, ni `analyste-performance` ni `experiences/` ne
  peuvent comparer les canaux (`mesure-budget.md` B2).

### D6. Exclure des placements (Audience Network) ou laisser Advantage+ placements ?
- **Positions** : Heath exclut Audience Network en campagne Trafic et le dit moins bon (avis sans étude publique
  [verif:PA10 🟡]) ; il laisse tous les placements ouverts en conversion, mais « Meta ne place la pub que là où il prévoit
  le résultat » exagère [verif:PA11 🟡]. Meta a annoncé le 20/08/2026 à certains annonceurs le retrait de l'option
  d'exclusion, sans calendrier [verif:PA11].
- **Recommandation de l'agence** : Advantage+ placements par défaut, optimisation sur une conversion de qualité (MA1),
  ce qui limite d'elle-même la dépense sur les placements faibles selon les tests de Loomer [verif:PA10]. Aucune
  stratégie bâtie sur une exclusion ; exclusion seulement pour une raison de sécurité de marque documentée, tant que
  l'option existe [veille:meta-ads §10 règle 15].

---

## Tests au labo (`experiences/index.md`, tous « en attente de marque »)
- `2026-10-22-meta-regle-passage-tests-et-budget` (rang 1, 125/125) : MA5 et paliers de budget ; prérequis des quatre
  tests suivants.
- `2026-10-22-meta-releve-cpm-premiers-comptes` (rang 3) : étalonnage du CPM France (7-12 € attendus [verif:PG03]).
- `2026-10-22-pub-texte-long-vs-court` (rang 4) : `publicite.md` D3.
- `2026-10-22-meta-volume-concepts-creatifs` (rang 9) : D2.
- `2026-10-22-offre-nouvelle-opportunite-vs-amelioration` (rang 10) : angle d'offre.
- `2026-10-22-meta-advantage-audience-vs-manuel` (rang 11) : D1.
- `2026-10-22-slide-alignee-avant-cta` (rang 14) : carrousel.
- À créer : vue de vidéo contre diversité créative pour élargir l'audience (D3).

## Journal
| Date | Modification |
|---|---|
| 2026-10-25 | Création (grande synthèse, équipe S4) : 14 principes, 6 désaccords tranchés, 6 fiches + veille Meta du 2026-10-21 + registre (PA, PG, PC). |
