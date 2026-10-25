# Principes : analyse des données, tests et itération

> Tenu par `synthetiseur-connaissances`. Création : 2026-10-25 (grande synthèse, équipe S4 « publicité et mesure »).
> Périmètre : lecture des métriques (contenu, pub, tunnel de vente : taux par étape, conversion), tests A/B et itération,
> pour l'organique comme pour le payant. L'allocation du budget et l'attribution sont dans `mesure-budget.md` ; le
> système Meta dans `meta-ads.md`. Les principes de croissance organique déjà tirés des mêmes méthodes (accordéon,
> outliers, déclinaison des gagnants) sont dans `croissance-audience.md` (C5, C7, C8) : ce fichier en donne la mesure,
> sans les répéter. Numéros **A6** (accordéon) et **A10** (protocole de test des variantes) : déjà cités par
> `production-et-regularite.md` et `hooks-et-retention.md`, conservés.
> Libellé « méthode expérimentale, tests A/B et géographiques » (table « Alias » d'`agents.md`) : rangé ici.
>
> **Sources traitées (22 fiches, 18 experts distincts + 1 baromètre public)** :
> organique : `Jmkq5RLjm0U` (Hormozi ; avec `6_CCutkM11g` et `k834E6OTGTM`, un expert) · `Ch4Sl0POBhU` et
> `uJ8Pg6t_iho` (Ralston, un expert) · `HzoQgQS8czE` (Yuergens × Neel) · `AA1LoZwW_2Y` (Mino Lee) ·
> `Z2uoA3bhJT0` (Paddy Galloway) ·
> `xf0Mli0LVgI` (MrBeast) · `FN4eDk1pq6U` (Berger) · `lhlS-Wds02M` (Sutherland) ;
> pub et réponse directe : `hopkins-scientific-advertising` · `Br2KSsaTzUc` (Ogilvy) · `halbert-boron-letters` ·
> `sR-qL7QdVZQ` (Kotler) · `qBxEAqZbHVg` (Coudac) · `yRgPbqywUJ8` (Denney) · `binet-field-b2b-growth` ·
> `rl3SELihHqs` (Trott) · `OgRgbar2dOQ` (Kapferer) · `J6Su5Vx3x5U` (Enns) ;
> données publiques : `barometre-numerique-2026` (Crédoc, déclaratif).
> Veille : `veille/plateformes/instagram.md` (Trial Reels), `youtube.md` (Test & Compare), `meta-ads.md` (Creative testing).
>
> **Frameworks liés** : `metriques-appariees.md` · `multiplier-sheet.md` · `analyse-top-vs-bottom.md` ·
> `boucle-d-iteration.md` · `methode-accordeon.md` · `regle-70-20-10.md` · `recherche-d-outliers.md` ·
> `decliner-un-contenu-gagnant.md` · `lecture-de-compte-hierarchie-gold-bronze.md` · `matrice-depense-cpa.md` ·
> `tunnel-de-rendez-vous-presence-et-closing.md` · `grille-source-deduction-praticiens.md`.
>
> **Labo** : `experiences/apprentissages.md` est **vide** au 2026-10-25 : il n'existe encore aucune preuve maison.
> C'est le principe A11 lui-même : dès le premier résultat, il prime sur tout ce qui suit.

## Légende

- **Consensus** : experts distincts (Hormozi = 1 ; Ralston = 1 ; Yuergens et Neel = 1 épisode, comptés comme un).
- **Confiance** : **haute** = 3 experts ou plus, sans chiffre contredit, ou règle officielle ✅ ; **moyenne** = 2 ou
  plus avec chiffres 🟡 ou absents ; **faible** = un expert, ou chiffres ❓.
- Les ratios de méthode (70/20/10, 5×, 11 jours) sont des **heuristiques** [verif:G15 🟡, P09 🟡], pas des optimums.

## Résumé (14 principes)

| # | Principe | Consensus | Confiance |
|---|---|---|---|
| A1 | Suis 2 à 4 métriques qui changent une décision, appariées quantité × qualité, à faible latence | 5 | moyenne |
| A2 | Lis toujours en relatif : médiane du compte, attente prédite, période de référence | 4 | moyenne |
| A3 | Change une variable à la fois ; si c'est nettement sous l'attente, un seul changement radical | 5 | moyenne |
| A4 | Lis un tunnel comme une chaîne de transmission et répare d'abord le maillon le plus faible | 4 | moyenne |
| A5 | Raisonne en taux par contenu ou par exposition, pas en volume cumulé | 3 | moyenne |
| A6 | Ouvre l'accordéon pour apprendre, puis concentre l'effort sur ce qui marche | 5 | moyenne |
| A7 | Isole les ingrédients communs aux gagnants, et méfie-toi du biais du survivant | 5 | moyenne |
| A8 | Méfie-toi de ce qui est facile à mesurer : traces en ligne, clics, déclarations | 5 | moyenne |
| A9 | Attends le bon délai avant de juger, et juge une stratégie sur plusieurs cycles | 4 + registre | moyenne |
| A10 | Teste les variantes avec les outils natifs, critère et durée fixés avant, ta favorite en variante 1 | 4 + plateformes | haute |
| A11 | Enregistre chaque leçon et laisse nos propres tests trancher entre les experts | 4 | haute |
| A12 | Accepte un fort taux d'échec : finance le pari sûr et le joker | 4 | moyenne |
| A13 | Écris ta prédiction avant de publier ou de lancer | 1 + process maison | faible |
| A14 | Fais remonter les résultats mesurés jusqu'à ceux qui décident | 2 | faible |

---

## Principes partagés par 3 experts ou plus

### A1. Suis 2 à 4 métriques qui changent une décision, appariées quantité × qualité, à faible latence
- **Pourquoi** : les vues mesurent l'étendue de la pertinence, pas la valeur ; le vrai résultat arrive avec 6 à 12 mois
  de latence, trop lent pour apprendre [fiche:Jmkq5RLjm0U framework K]. « If it doesn't change your actions, don't track
  it » [fiche:Ch4Sl0POBhU F6, 03:07]. Enns distingue indicateur avancé et retardé [fiche:J6Su5Vx3x5U framework H]. Ava
  ne suivait pas les conversions de ses clics, et le regrette [fiche:HzoQgQS8czE]. Coudac place le CAC des nouveaux
  clients au-dessus de tout [fiche:qBxEAqZbHVg].
- **Comment l'appliquer** (`metriques-appariees.md`) :
  1. Écrire la conversion qui compte pour la marque, mesurée **en taux**.
  2. L'apparier à un indicateur rapide : vues × taux d'opt-in, DM qualifiés pour 1 000 vues, rendez-vous par post,
     coût par rendez-vous qualifié en pub.
  3. Vérifier rétrospectivement que l'indicateur rapide corrèle avec les ventes ; sinon, en changer.
  4. Tableau visible par tous les agents (`analyste-performance`, `rapporteur`).
- **Pour une marque d'entreprise / un studio B2B** : Sillage : demandes de devis qualifiées par 1 000 vues et taux de
  présence à l'appel, pas les vues seules.
- **Sources** : [fiche:Jmkq5RLjm0U frameworks K, Y] · [fiche:Ch4Sl0POBhU F6] · [fiche:J6Su5Vx3x5U framework H] ·
  [fiche:HzoQgQS8czE] · [fiche:qBxEAqZbHVg enseignement 1].
- **Consensus** : 5 experts. **Confiance** : **moyenne** (résultats chiffrés d'Hormozi internes, sans groupe témoin).

### A2. Lis toujours en relatif : médiane du compte, attente prédite, période de référence
- **Pourquoi** : 50 000 vues sont un échec pour un compte à 500 000 de médiane et un triomphe pour un compte à 10 000
  (`multiplier-sheet.md`, Ralston). Galloway juge une vidéo « par rapport à l'attente, pas au chiffre absolu » : 4 M de
  vues le premier jour peuvent être un échec [fiche:Z2uoA3bhJT0 01:21-01:27]. Coudac : trouver sa meilleure période
  passée et isoler la variable qui a changé [fiche:qBxEAqZbHVg 30:45-33:58]. Yuergens et Neel mesurent un outlier contre
  les abonnés **et** contre la moyenne du créateur [fiche:HzoQgQS8czE framework 1].
- **Comment l'appliquer** : multiplicateur = performance / médiane du format sur 75 à 90 jours ; comparer une campagne à
  une période de référence en notant les facteurs extérieurs (saison, conjoncture, panne de tracking) ; un contenu à
  3× ou plus se décline (`croissance-audience.md` C8).
- **Sources** : [fiche:Ch4Sl0POBhU F22] · [fiche:Z2uoA3bhJT0 enseignement 8] · [fiche:qBxEAqZbHVg enseignement 6] ·
  [fiche:HzoQgQS8czE framework 1].
- **Consensus** : 4 experts. **Confiance** : **moyenne** (« directionally correct, not scientifically accurate »).

### A3. Change une variable à la fois ; si c'est nettement sous l'attente, un seul changement radical
- **Pourquoi** : changer tout en même temps empêche de savoir ce qui a marché (`boucle-d-iteration.md`). Galloway : au
  dessus de l'attente, on ne touche à rien ; nettement en dessous, un changement radical (nouveau test A/B, puis
  nouveaux titres), « jamais dix changements par jour : on ne peut plus attribuer », « Good data > no data > bad data »
  [fiche:Z2uoA3bhJT0 01:38-01:43]. Hopkins testait les titres **à texte constant** [fiche:hopkins-scientific-advertising
  p. 28-29]. Ralston limite à 1 à 3 améliorations par tournage [fiche:uJ8Pg6t_iho framework 36]. Sur Meta, toute
  modification importante relance l'apprentissage [verif:PA02 ✅].
- **Comment l'appliquer** : chaque test écrit sa variable unique ; un contenu se teste sur l'accroche **ou** le format
  **ou** le CTA ; en pub, on regroupe les changements et on ne touche à rien pendant l'apprentissage (`meta-ads.md`
  MA6). Une refonte stratégique (Hormozi applique 6 changements d'un coup) n'est pas un test : elle se juge sur la
  tendance, pas sur une attribution fine (D4).
- **Sources** : [fiche:Z2uoA3bhJT0 enseignement 8] · [fiche:hopkins-scientific-advertising enseignement 4] ·
  [fiche:uJ8Pg6t_iho framework 36] · [fiche:Jmkq5RLjm0U framework U] · [verif:PA02].
- **Consensus** : 5 experts (Galloway, Hopkins, Ralston, Hormozi, Coudac). **Confiance** : **moyenne**.

### A4. Lis un tunnel comme une chaîne de transmission et répare d'abord le maillon le plus faible
- **Pourquoi** : argent → impressions → clics → ventes → CA ; un compte performant se distingue par la fluidité de
  chaque passage [fiche:qBxEAqZbHVg 10:44]. Hormozi : sous 70 % de présence aux rendez-vous, c'est un problème de
  processus ; passer de 40 % à 80 % de présence double le chiffre, doubler un closing de 35 % à 70 % est irréaliste
  (seuils d'auteur) [fiche:6_CCutkM11g 01:18, 03:13]. La courbe de rétention montre où l'on perd les gens
  [fiche:Z2uoA3bhJT0 01:38]. L'entonnoir « vues × % d'entrée × % d'achat × prix » ne vaut qu'avec des taux **mesurés**
  [verif:G10 ❓ pour les taux supposés de Mino Lee].
- **Comment l'appliquer** : une métrique par transition (CPM, CTR, CR, panier ; vues, opt-ins, appels, signatures) ;
  calculer le taux de chaque étape ; agir sur l'étape la plus faible avant d'acheter plus de trafic
  (`tunnel-de-rendez-vous-presence-et-closing.md`, `monetisation-et-offre.md` M4).
- **Sources** : [fiche:qBxEAqZbHVg enseignement 5] · [fiche:6_CCutkM11g enseignement 8] · [fiche:Z2uoA3bhJT0
  enseignement 8] · [fiche:HzoQgQS8czE frameworks 18-21].
- **Consensus** : 4 experts (Coudac, Hormozi, Galloway, Yuergens). **Confiance** : **moyenne**.

### A5. Raisonne en taux par contenu ou par exposition, pas en volume cumulé
- **Pourquoi** : « shared more in aggregate is different than likelihood of sharing » : s'il existe 1 000 contenus de
  chats pour 100 de chiens, les chats cumulent plus de partages même avec une probabilité plus faible
  [fiche:FN4eDk1pq6U 00:39]. Ralston mesure la conversion en taux [fiche:Ch4Sl0POBhU 01:21]. Coudac lit CTR, CR et CPA,
  des taux [fiche:qBxEAqZbHVg].
- **Comment l'appliquer** : comparer des formats ou des sujets au taux par contenu publié (vues médianes, opt-ins par
  1 000 vues), jamais au total d'une catégorie qui a été plus publiée ; pondérer les comparaisons de pubs par la
  dépense.
- **Sources** : [fiche:FN4eDk1pq6U enseignement 10] · [fiche:Ch4Sl0POBhU] · [fiche:qBxEAqZbHVg enseignement 5].
- **Consensus** : 3 experts. **Confiance** : **moyenne**.

### A6. Ouvre l'accordéon pour apprendre, puis concentre l'effort sur ce qui marche
- **Pourquoi** : on ne sait pas d'avance ce que l'audience appelle « qualité » ; « you're using quantity to inform what
  your audience says is quality » [fiche:uJ8Pg6t_iho 01:36] ; « Volume negates luck » [fiche:Jmkq5RLjm0U 02:35].
  Sutherland : explorer et exploiter sont « deux moitiés d'un même processus », une organisation qui n'explore plus
  finit par mourir de faim [fiche:lhlS-Wds02M enseignement 6]. Hopkins testait en continu sans interrompre le plan
  éprouvé [fiche:hopkins-scientific-advertising p. 78-79].
- **Comment l'appliquer** (`methode-accordeon.md`, `regle-70-20-10.md`) :
  1. Phase d'ouverture (compte neuf, 4 à 8 semaines) : volume tenable, formats et sujets variés.
  2. Classement au multiplicateur de la médiane (A2), puis fermeture : même effort total sur moins de pièces, plus
     travaillées.
  3. En régime : environ 70 % d'éprouvé, 20 % d'itération à une variable, 10 % de paris (heuristique [verif:G15 🟡]).
  4. Réouverture quand la réaction baisse. Le détail organique est dans `croissance-audience.md` C5 et
     `production-et-regularite.md`.
- **Pour une marque d'entreprise / un studio B2B** : chez Sillage, l'exploration porte sur les accroches et les angles
  (variantes en Trial Reels, concepts de pub), pas sur des dizaines d'animations complètes.
- **Sources** : [fiche:uJ8Pg6t_iho frameworks 16, 17] · [fiche:Ch4Sl0POBhU F11, F26] · [fiche:HzoQgQS8czE 00:41] ·
  [fiche:Jmkq5RLjm0U 02:35] · [fiche:lhlS-Wds02M enseignement 6] · [fiche:hopkins-scientific-advertising enseignement 2].
- **Consensus** : 5 experts (Ralston, Yuergens, Hormozi, Sutherland, Hopkins). **Confiance** : **moyenne** (seuils
  empiriques).

### A7. Isole les ingrédients communs aux gagnants, et méfie-toi du biais du survivant
- **Pourquoi** : comparer les meilleurs et les moins bons contenus fait apparaître l'ingrédient présent dans tous les
  gagnants (`analyse-top-vs-bottom.md`, Ralston et Hormozi). Galloway relève quatre marqueurs communs aux vidéos à
  10-100 M de vues [fiche:Z2uoA3bhJT0 enseignement 3]. Mais la « théorie des chats » confond corrélation et cause, comme
  appeler son enfant Bill parce que Bill Gates est célèbre [fiche:FN4eDk1pq6U 00:39] ; les « clés » de Kapferer
  viennent de quelques succès lus a posteriori, sans les échecs [fiche:OgRgbar2dOQ « Limites internes »].
- **Comment l'appliquer** : top 10 % contre bas 10 % sur la même période et le même format ; noter l'ingrédient
  candidat comme **hypothèse**, puis le tester (A3, A10) avant d'en faire une règle ; toujours chercher les contre-exemples
  (contenus qui avaient l'ingrédient et ont échoué).
- **Sources** : [fiche:Ch4Sl0POBhU] · [fiche:Jmkq5RLjm0U] · [fiche:Z2uoA3bhJT0 enseignement 3] ·
  [fiche:FN4eDk1pq6U enseignement 10] · [fiche:OgRgbar2dOQ].
- **Consensus** : 5 experts (Ralston, Hormozi, Galloway, Berger, Kapferer comme contre-exemple). **Confiance** : **moyenne**.

### A8. Méfie-toi de ce qui est facile à mesurer : traces en ligne, clics, déclarations
- **Pourquoi** : on surestime le bouche-à-oreille en ligne parce qu'il laisse une trace ; « just because we're measuring
  something, doesn't mean we're measuring the right thing » [fiche:FN4eDk1pq6U 00:05-00:06] (7 % en ligne : chiffre
  d'avant 2013, jamais sans sa date). Halbert se fie aux comportements d'achat, « jamais aux déclarations »
  [fiche:halbert-boron-letters]. Le baromètre du numérique est entièrement **déclaratif** (aucune mesure de
  comportement réel) [fiche:barometre-numerique-2026 « Pour qui »]. Bezos : « when the data and the anecdotes disagree,
  the anecdotes are usually right… it's usually that you're not measuring the right thing » [verif:V4B-MM14 ✅, CNBC
  2018]. GA4 ne voit pas les impressions sans clic [verif:PA06 🟡].
- **Comment l'appliquer** : pour chaque métrique, écrire ce qu'elle **ne voit pas** ; quand un retour client contredit
  un tableau de bord, réexaminer la mesure avant d'ignorer l'un ou l'autre ; préférer un comportement (achat, rendez-vous
  tenu) à une déclaration (« j'achèterais »).
- **Sources** : [fiche:FN4eDk1pq6U enseignement 8] · [fiche:halbert-boron-letters] · [fiche:barometre-numerique-2026] ·
  [verif:V4B-MM14] · [fiche:qBxEAqZbHVg enseignement 2] · [verif:PA06].
- **Consensus** : 5 experts (Berger, Halbert, Coudac, Kotler sur l'exposition théorique, Hormozi qui relaie Bezos).
  **Confiance** : **moyenne**.

### A9. Attends le bon délai avant de juger, et juge une stratégie sur plusieurs cycles
- **Pourquoi** : en organique, attendre environ 10-11 jours avant de mesurer un contenu (certains décollent vers le 7e
  jour) [verif:P09 🟡] ; en pub Meta, la fenêtre par défaut est 7 j clic + 1 j engage-through + 1 j vue
  [verif:PA04 ✅] : ce sont deux délais différents, à ne pas confondre (registre, « Doublons »). La marque se lit au-delà
  de six mois [fiche:binet-field-b2b-growth p. 38]. Denney : une stratégie ne se valide pas sur un test ou une poignée de
  tests [fiche:yRgPbqywUJ8 12:35]. Galloway prédit à 1 h, 1 jour, 1 semaine [fiche:Z2uoA3bhJT0 01:21].
- **Comment l'appliquer** : chaque test écrit sa date de lecture avant de commencer ; on ne coupe pas une créa Meta
  avant la fin de l'apprentissage, sauf dépense aberrante ; une stratégie se juge sur au moins deux à trois cycles
  mensuels.
- **Sources** : [verif:P09, PA04] · [fiche:binet-field-b2b-growth enseignement 7] · [fiche:yRgPbqywUJ8 enseignement 10] ·
  [fiche:Z2uoA3bhJT0 enseignement 8] · [fiche:Ch4Sl0POBhU F22].
- **Consensus** : 4 experts + registre. **Confiance** : **moyenne**.

### A10. Teste les variantes avec les outils natifs, critère et durée fixés avant, ta favorite en variante 1
- **Pourquoi** : les plateformes fournissent des tests propres : **Trial Reels** sur Instagram (non-abonnés seulement)
  [veille:instagram §4], **Test & Compare** sur YouTube pour titre et miniature, critère « temps de visionnage », 2 semaines
  [veille:youtube §2.1, §9.5], **Creative testing**
  sur Meta (jusqu'à 5 pubs, parts égales, sans recouvrement, 30 jours au plus) [verif:PA16 ✅]. Hopkins a testé près de
  2 000 titres sur un même produit à texte presque identique [fiche:hopkins-scientific-advertising p. 28-29]. Galloway
  enchaîne test A/B puis nouveaux titres [fiche:Z2uoA3bhJT0 01:38].
- **Comment l'appliquer** :
  1. Écrire avant le test : hypothèse, variable unique, critère de décision, durée, budget.
  2. Instagram : variantes en Trial Reels, puis mettre à niveau la gagnante. YouTube long : 3 paires titre + miniature
     dans Test & Compare, la **variante n° 1 est notre favorite** (elle reste si le test n'est pas concluant), rien
     modifié pendant le test (règle déjà retenue dans `hooks-et-retention.md`). Meta : Creative testing plutôt que des
     ensembles dupliqués (`meta-ads.md` MA12).
  3. Un seul test à la fois par ensemble de pubs, par compte organique et par liste de contacts (`experiences/index.md`).
  4. Protocole écrit par `concepteur-experiences`, prédiction par `predicteur-performance` (A13), verdict par
     `analyste-resultats`.
- **Sources** : [veille:instagram §4] · [veille:youtube §2.1, §9.5] · [verif:PA16] · [fiche:hopkins-scientific-advertising
  enseignement 4] · [fiche:Z2uoA3bhJT0 enseignement 8] · [fiche:uJ8Pg6t_iho 04:11] · [fiche:AA1LoZwW_2Y 02:07].
- **Consensus** : 4 experts (Hopkins, Galloway, Ralston, Mino Lee) + plateformes. **Confiance** : **haute** (outils
  officiels).

### A11. Enregistre chaque leçon et laisse nos propres tests trancher entre les experts
- **Pourquoi** : Hopkins décrit une agence qui code chaque annonce, compare, enregistre, et ne garde comme principe que
  ce qui gagne « invariablement » [fiche:hopkins-scientific-advertising p. 7-8]. Hormozi : « Don't get the same scar
  twice » [fiche:Jmkq5RLjm0U framework V.2]. Ralston : liste « brick by brick » et « à faire différemment » après chaque
  production [fiche:Ch4Sl0POBhU F23, F11.4]. Kotler : plusieurs messages, test, on garde le gagnant
  [fiche:sR-qL7QdVZQ framework L].
- **Comment l'appliquer** : tout résultat de test va dans `experiences/<id>/resultats.md`, puis, s'il est confirmé, dans
  `experiences/apprentissages.md`, qui **prime** sur les avis d'experts de toute la base (règle du synthétiseur) ; un
  apprentissage contraire à un principe le fait réviser ici, avec la mention « contredit par le labo ».
- **Sources** : [fiche:hopkins-scientific-advertising enseignements 1, 2] · [fiche:Jmkq5RLjm0U framework V] ·
  [fiche:Ch4Sl0POBhU F23] · [fiche:sR-qL7QdVZQ framework L] · `boucle-d-iteration.md`.
- **Consensus** : 4 experts. **Confiance** : **haute** (règle de méthode du repo).

### A12. Accepte un fort taux d'échec : finance le pari sûr et le joker
- **Pourquoi** : le business est du poker, 4 ou 5 mains décident du résultat, donc un fort taux d'échec des tests est
  sain ; quand on n'a droit qu'à une option on choisit toujours la sûre, il faut financer les deux
  [fiche:lhlS-Wds02M enseignements 7, 8]. Hormozi : « sur 6 stats, 4 sont mauvaises et 2 bonnes »
  [fiche:Jmkq5RLjm0U framework U]. Hopkins : « playing on the safe side of a hundred to one shot »
  [fiche:hopkins-scientific-advertising p. 77]. Bezos, cité par Hormozi : « 10 % chance of a 100 times payoff », les gros
  gagnants paient beaucoup d'expériences (lettre aux actionnaires de 2015) [verif:V4B-MM12 ✅].
- **Comment l'appliquer** : la part « paris » (10 % du 70/20/10, D3 de `mesure-budget.md`) n'est jamais supprimée pour
  « sécuriser » ; un test raté est documenté (A11), pas caché ; chaque pari a une perte plafonnée.
- **Sources** : [fiche:lhlS-Wds02M enseignements 6-8] · [fiche:Jmkq5RLjm0U framework U] ·
  [fiche:hopkins-scientific-advertising enseignement 2] · [verif:V4B-MM12] · [fiche:Ch4Sl0POBhU F26].
- **Consensus** : 4 experts (Sutherland, Hormozi, Hopkins, Ralston). **Confiance** : **moyenne**.

## Principes soutenus par 1 ou 2 experts

### A13. Écris ta prédiction avant de publier ou de lancer
- **Pourquoi** : chez Galloway, chaque membre de l'équipe prédit les vues à 1 h, 1 jour, 1 semaine et le rang attendu
  parmi les 10 dernières vidéos ; c'est l'écart à la prédiction qui déclenche l'action [fiche:Z2uoA3bhJT0 01:21-01:27].
  Le repo a institutionnalisé ce geste (`experiences/predictions.md`, agent `predicteur-performance`).
- **Comment l'appliquer** : prédiction chiffrée, datée et motivée avant chaque test et chaque campagne ; l'écart sert
  à calibrer nos repères (mesure-budget B10).
- **Sources** : [fiche:Z2uoA3bhJT0 enseignement 8] · `CLAUDE.md` (pipeline « Apprendre de ses résultats »).
- **Consensus** : 1 expert + process maison. **Confiance** : **faible** (aucune mesure de l'effet de la pratique).

### A14. Fais remonter les résultats mesurés jusqu'à ceux qui décident
- **Pourquoi** : Ogilvy demande pourquoi les experts de la réponse directe ne « sauvent » pas les généralistes de leurs
  folies : impressionnés par la taille des agences, ils ne les rencontrent jamais [fiche:Br2KSsaTzUc 00:01:42-00:02:17].
  Hormozi rend le tableau de bord visible en temps réel pour toute l'équipe [fiche:Jmkq5RLjm0U framework K].
- **Comment l'appliquer** : chaque rapport (`rapporteur`) remonte à l'orchestrateur et à l'utilisateur les résultats qui
  contredisent une hypothèse de marque ; un résultat mesuré n'est jamais écarté pour une question de prestige.
- **Sources** : [fiche:Br2KSsaTzUc enseignement 10] · [fiche:Jmkq5RLjm0U framework K].
- **Consensus** : 2 experts. **Confiance** : **faible**.

---

## Désaccords entre experts

### D1. Les données ou l'intuition ?
- **Positions** :
  - Hopkins, Ogilvy : seul ce qui est mesuré compte ; « on your side of the chasm I see knowledge and reality »
    [fiche:Br2KSsaTzUc 00:02:17]. Galloway : « Good data > no data > bad data », « I am a view maximizer »
    [fiche:Z2uoA3bhJT0].
  - Trott : le planning « has taken all the intuition out of it » ; l'émotion décide, la raison post-rationalise
    [fiche:rl3SELihHqs 00:48-00:51]. Sutherland : le cerveau ne remarque que l'écart à l'attendu, et les études ne
    demanderont jamais la surprise [fiche:lhlS-Wds02M enseignement 5]. MrBeast dit faire « less about retention data
    analytics » et plus d'émotion, tout en décrivant une intro pensée pour la rétention [fiche:xf0Mli0LVgI enseignement 4].
  - Bezos (relayé chez Hormozi) : quand données et anecdotes divergent, les anecdotes ont souvent raison, parce qu'on
    mesure la mauvaise chose [verif:V4B-MM14 ✅].
- **Recommandation de l'agence** : l'intuition **propose**, la mesure **tranche**. Une idée « contre les données »
  (surprise, émotion, rupture) entre dans les 10 % de paris (A12) avec un test borné ; un désaccord entre un retour
  client et un tableau de bord déclenche une vérification de la mesure (A8), pas un vote. La rétention est un socle,
  l'émotion une étape de maturité : ce n'est pas l'un ou l'autre (lecture de la fiche MrBeast).
- **Ce qui ferait changer** : une série de paris intuitifs qui battent systématiquement les choix « pilotés par les
  données » dans nos tests (ou l'inverse), enregistrée dans `apprentissages.md`.

### D2. Quelle est la métrique n° 1 : les vues, ou la valeur de l'audience ?
- **Positions** : Galloway : les vues sont la métrique « compréhensive » (clic, visionnage, satisfaction) ; CTR et
  durée moyenne affichés trompent (analogie du stand de limonade à Times Square) [fiche:Z2uoA3bhJT0 enseignement 8].
  Hormozi, Ralston : les vues mesurent l'étendue de la pertinence, pas la valeur ; on accepte de perdre des vues si la
  conversion monte [fiche:Jmkq5RLjm0U] [fiche:Ch4Sl0POBhU 01:23].
- **Recommandation de l'agence** : deux niveaux. Pour une décision de **diffusion** (packaging, accroche, format sur
  YouTube ou en Trial Reels), les vues rapportées à l'attente sont le bon juge. Pour une décision de **stratégie**
  (sujets, cible, offre), la métrique appariée de valeur (A1) l'emporte. Un sujet qui fait des vues sans demandes
  qualifiées sort du cœur éditorial.

### D3. Mesurer vite ou mesurer long ?
- **Positions** : Hormozi, bilan après 3 à 4 semaines et métrique la plus rapide possible [fiche:Jmkq5RLjm0U] ; Galloway,
  1 h / 1 jour / 1 semaine ; Binet & Field, effets de marque au-delà de six mois, les mesures courtes biaisent vers
  l'activation [fiche:binet-field-b2b-growth p. 38] ; Denney, plusieurs cycles.
- **Recommandation de l'agence** : les deux horloges de `mesure-budget.md` B5 et D1 : vite pour l'activation et le
  packaging, long pour la marque et la stratégie.

### D4. Combien de changements à la fois ?
- **Positions** : Hormozi applique 6 changements d'un coup à sa stratégie et en attend 2 bons sur 6
  [fiche:Jmkq5RLjm0U framework U] ; Ralston, 1 à 3 améliorations par tournage ; Galloway et Hopkins, une variable.
- **Recommandation de l'agence** : **une variable par test** (A3). Une refonte à plusieurs changements est permise
  quand un compte stagne depuis plus de 90 jours, mais elle est notée comme refonte, jugée sur la tendance et suivie de
  tests à une variable pour retrouver ce qui a porté.

---

## Tests au labo (`experiences/index.md`)
Tous les protocoles du backlog appliquent A3, A9, A10 et A13. Les plus liés à ce fichier :
- `2026-10-22-meta-regle-passage-tests-et-budget` (rang 1) : règle écrite de passage aux tests (A9, A10).
- `2026-10-22-intro-preuve-vs-promesse` (rang 2, Trial Reels) : test natif organique (A10).
- `2026-10-22-revue-in-situ-vs-ecran-montage` (rang 5) : une revue en contexte prédit-elle mieux la performance (A13) ?
- À créer : calibration des prédictions (`predictions.md`) après les dix premiers tests (A13).

## Journal
| Date | Modification |
|---|---|
| 2026-10-25 | Création (grande synthèse, équipe S4) : 14 principes (A6 et A10 aux numéros déjà cités ailleurs), 4 désaccords tranchés, 22 fiches + veille Instagram, YouTube, Meta + registre (P09, G10, G15, PA02, PA04, PA06, PA16) et passe 4b (V4B-MM12, MM14). |
