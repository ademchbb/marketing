# Principes : mesure, attribution et budget

> Tenu par `synthetiseur-connaissances`. Création : 2026-10-25 (grande synthèse, équipe S4 « publicité et mesure »).
> Périmètre : allocation du budget marketing, attribution, incrémentalité, tests de lift, ROI, rythme d'investissement.
> La lecture fine des métriques et le protocole de test sont dans `analyse-et-iteration.md` ; l'économie d'un client
> (CAC, LTV, marge, cash à 30 jours) dans `economie-unitaire.md` (autre équipe, renvois croisés) ; le système Meta dans
> `meta-ads.md` ; la création publicitaire dans `publicite.md`.
> Libellé « allocation budgétaire entre canaux » de la fiche Kotler (ligne « Hors liste ») : rangé ici d'après la table
> « Alias » d'`agents.md`.
>
> **Sources traitées (17 fiches, 15 experts distincts, plus la veille Meta)** :
> `binet-field-b2b-growth` (Binet & Field, IPA × LinkedIn B2B Institute, 2019) · `hopkins-scientific-advertising`
> (Hopkins, 1923) · `Br2KSsaTzUc` (Ogilvy) · `qBxEAqZbHVg` (Coudac, 03/2024) · `dAJyqo6wnq4` (Heath, 2026) ·
> `pILj7t-qQhs` (Wilcox × James, LinkedIn) · Hormozi (`6_CCutkM11g` *Money Models*, `k834E6OTGTM` *Leads*,
> `Jmkq5RLjm0U` : un expert) · `Ge8xTCIP0Zw` (Jay Abraham) · `sR-qL7QdVZQ` (Kotler) · `halbert-boron-letters` (Halbert) ·
> `OgRgbar2dOQ` (Kapferer) · `FN4eDk1pq6U` (Berger) · `lhlS-Wds02M` (Sutherland) · `yRgPbqywUJ8` (Denney) ·
> `J6Su5Vx3x5U` (Enns) · `veille/plateformes/meta-ads.md` §7 (attribution 2026).
>
> **Indépendance** : Ogilvy n'est pas indépendant de Hopkins (même école de réponse directe). Binet & Field et le
> LinkedIn Ads Show sont tous deux portés par LinkedIn. Les chiffres de Hormozi, Abraham et Coudac sont internes ou
> déclaratifs.
>
> **Chiffres porteurs non vérifiés** : les résultats de Binet & Field (ESOV, 46/54, effets « very large », 4 % des
> marketeurs qui mesurent au-delà de 6 mois) ne figurent ni au registre ni dans les passes 4a / 4b. Ils sont cités
> « selon Binet & Field (2019), non vérifié » (demande à `verificateur-faits` en fin de rapport).
>
> **Frameworks liés** : `cac-blended-et-mesure-du-mix.md` · `plan-d-atterrissage-et-timing.md` ·
> `plafond-de-conversion-et-cercles-du-marche.md` · `lecture-de-compte-hierarchie-gold-bronze.md` · `metriques-appariees.md` ·
> `money-model-sequence-d-offres.md` · `partenariats-aux-resultats.md` · `plan-offensif-en-recession.md` ·
> `regle-70-20-10.md` · `grille-source-deduction-praticiens.md`.
>
> **Labo** : `experiences/apprentissages.md` est **vide** au 2026-10-25. Aucun repère de budget n'est encore mesuré dans
> nos comptes ; les deux premières expériences Meta (rangs 1 et 3) servent précisément à l'étalonnage.

## Légende

- **Consensus** : experts distincts (Hormozi = 1 ; Hopkins et Ogilvy = 2, non indépendants).
- **Confiance** : **haute** = 3 experts ou plus convergents sans chiffre contredit, ou fait vérifié ✅ ; **moyenne** =
  2 experts ou chiffres 🟡 ; **faible** = un expert, ou chiffres ❓ / non vérifiés.
- Chiffres de créateurs et d'agences : « selon X, date », statut du registre.

## Résumé (11 principes)

| # | Principe | Consensus | Confiance |
|---|---|---|---|
| B1 | Mesure la pub par les nouveaux clients et leur coût réel (CAC blended), pas par le ROAS déclaré | 6 | haute |
| B2 | Ne tranche jamais un canal sur l'attribution seule : teste l'incrémentalité et demande « où nous avez-vous connus ? » | 6 + Meta | haute |
| B3 | Fixe où tu veux atterrir (objectif, plancher de rentabilité), puis dépense le maximum au-dessus du plancher | 4 | moyenne |
| B4 | Finance la marque et l'activation ensemble, et vise large dans la catégorie plutôt que la seule fidélisation payante | 4 | moyenne |
| B5 | Pilote avec deux horloges : un indicateur rapide pour décider, un indicateur à plus de 6 mois pour la marque | 4 | moyenne |
| B6 | Teste petit, à perte plafonnée, puis augmente par paliers sur ce qui a prouvé | 7 + Meta | haute |
| B7 | Juge un coût à la qualité exploitable du résultat, jamais au prix unitaire (CPM, CPC, coût par lead) | 5 | haute |
| B8 | Calcule ce qu'un client rapporte, et quand, avant de fixer ce que tu acceptes de payer pour l'acquérir | 5 | moyenne |
| B9 | Investis au bon moment : fort quand le marché est chaud, avec un temps d'avance ; offensif en récession | 2 | faible |
| B10 | Prévois avec des repères prudents et datés, puis recale sur les données du compte dès les premiers jours | 1 + registre | moyenne |
| B11 | Fixe le budget de marque d'après un objectif de part de marché (part de voix), pas d'après un pourcentage du CA | 1 | faible |

---

## Principes partagés par 3 experts ou plus

### B1. Mesure la pub par les nouveaux clients et leur coût réel (CAC blended), pas par le ROAS déclaré
- **Pourquoi** : un CPA ou un ROAS peut être excellent alors que les achats viennent de clients existants ; exemple
  pédagogique de Coudac : même dépense, même CPA, valeur créée à un an presque du simple au double selon la part de
  nouveaux clients (calcul juste [verif:PG07 ✅]) [fiche:qBxEAqZbHVg 00:32-03:43]. Hopkins : « Your object in all
  advertising is to buy new customers at a price which pays a profit » [fiche:hopkins-scientific-advertising p. 82].
  Les plateformes revendiquent plus de ventes qu'il n'y en a (1 500 à 2 000 pour 1 000 selon Coudac [verif:PG05 🟡]).
- **Comment l'appliquer** :
  1. KPI de vérité : **nombre de nouveaux clients** et **CAC blended** = dépense marketing totale / nouveaux clients,
     suivis dans le temps et comparés entre mois aux mix différents (`cac-blended-et-mesure-du-mix.md`).
  2. Le ROAS de plateforme reste un indicateur de **pilotage quotidien**, jamais une preuve ; toujours en HT
     [verif:PG04].
  3. En B2B : rendez-vous qualifiés, pipeline et contrats signés, attribués aussi par le CRM ; LinkedIn propose un
     Revenue Attribution Report, à croiser avec un outil tiers pour ne pas surpondérer LinkedIn [fiche:pILj7t-qQhs 00:35].
- **Pour une marque d'entreprise / un studio B2B** : pour Sillage, la vérité est le coût par **nouveau client signé**,
  pas le coût par lead ni le ROAS affiché par Meta.
- **Sources** : [fiche:qBxEAqZbHVg enseignements 1, 2] · [fiche:hopkins-scientific-advertising enseignement 1] ·
  [fiche:Br2KSsaTzUc enseignement 1] · [fiche:sR-qL7QdVZQ enseignement 6] · [fiche:pILj7t-qQhs enseignement 10] ·
  [fiche:6_CCutkM11g enseignement 1 (bénéfice brut rapporté au CAC)].
- **Consensus** : 6 experts (Coudac, Hopkins, Ogilvy, Kotler, Wilcox, Hormozi).
- **Confiance** : **haute** sur le principe ; les ratios d'agence sont 🟡 ou ❓ (PG05, PG06).

### B2. Ne tranche jamais un canal sur l'attribution seule : teste l'incrémentalité et demande « où nous avez-vous connus ? »
- **Pourquoi** : un modèle d'attribution suppose que chaque canal marche seul ; or « Facebook nourrit Google », et couper
  le canal « le moins rentable » peut casser la synergie [fiche:qBxEAqZbHVg 23:40-30:13]. GA4 utilise le modèle
  data-driven, qui ignore les impressions sans clic [verif:PA05 ✅, PA06 🟡]. Meta présente le Conversion Lift comme
  « the gold standard in measurement » et a déployé une attribution incrémentale [veille:meta-ads §7, OFFICIEL]. Hopkins
  comparait des **villes** sur les ventes totales quand la réponse n'était pas traçable
  [fiche:hopkins-scientific-advertising p. 8, p. 81]. Hormozi a coupé ses pubs deux semaines et vu les ventes continuer,
  ce qui l'a mené aux recommandations [fiche:k834E6OTGTM 00:54-00:57] ; il fait voter son public sur l'origine
  (« who here heard about this event from… ? ») [fiche:k834E6OTGTM 01:12]. Berger : on surestime ce qui laisse une trace
  (7 % du bouche-à-oreille en ligne, chiffre d'avant 2013, à ne jamais citer sans sa date) [fiche:FN4eDk1pq6U 00:05].
- **Comment l'appliquer** :
  1. UTM systématiques + pixel/API Conversions + CRM : la base sans laquelle rien ne se compare (`meta-ads.md` D5).
  2. **Questionnaire post-achat** ou à la prise de rendez-vous : « Où avez-vous entendu parler de nous ? » (réponse
     libre), suivi mois par mois.
  3. Avant toute décision de couper ou doubler un canal : test d'**incrémentalité** (Conversion Lift Meta, test
     géographique ou temporel avec zone témoin, pause contrôlée), protocole par `concepteur-experiences`.
  4. Effet de halo : suivre les recherches de marque et le trafic direct pendant une campagne
     [fiche:pILj7t-qQhs 00:37] (le chiffre Dreamdata est ❓ [verif:PB04], ne pas le citer).
  5. Données 2025 et 2026 non comparables telles quelles chez Meta (changement de la définition du clic en mars 2026)
     [verif:PA04].
- **Sources** : [fiche:qBxEAqZbHVg enseignements 2, 3] · [fiche:hopkins-scientific-advertising enseignement 2] ·
  [fiche:k834E6OTGTM enseignements 9, 10] · [fiche:pILj7t-qQhs enseignement 10] · [fiche:FN4eDk1pq6U enseignement 8] ·
  [fiche:binet-field-b2b-growth (effet de halo, enseignement 6)] · [verif:PA04, PA05, PA06] · [veille:meta-ads §7].
- **Consensus** : 6 experts (Coudac, Hopkins, Hormozi, Wilcox, Berger, Binet & Field) + Meta.
- **Confiance** : **haute**.

### B3. Fixe où tu veux atterrir (objectif, plancher de rentabilité), puis dépense le maximum au-dessus du plancher
- **Pourquoi** : « Je veux doubler mon budget » n'est pas un objectif ; un CPA cible n'a pas de sens sans objectif de CA
  ou de nouveaux clients ; le but est le volume maximal au-dessus d'un plancher de ROI [fiche:qBxEAqZbHVg 42:08-43:43].
  Hormozi fixe un plancher de trésorerie : bénéfice brut à 30 jours > 2 × (CAC + coût de service) [fiche:6_CCutkM11g
  00:09-00:30] (seuil d'auteur, 🟡). Abraham fixe le plafond d'acquisition à partir de la valeur d'une cohorte
  [fiche:Ge8xTCIP0Zw 00:08] ; Binet & Field à partir d'un objectif de part de marché (B11).
- **Comment l'appliquer** :
  1. Écrire l'objectif (nouveaux clients ou CA sur la période) et le **plancher** (rentabilité ou cash minimal) avant de
     fixer le budget (`plan-d-atterrissage-et-timing.md`).
  2. Réserver des enveloppes pour les saisons chaudes ; ne pas refuser une opportunité parce que « le ROI est déjà très
     bien » au-dessus du plancher.
  3. Le choix du plancher (cash à 30 jours ou LTV) est arbitré en D2.
- **Sources** : [fiche:qBxEAqZbHVg enseignement 9] · [fiche:6_CCutkM11g enseignement 1] · [fiche:Ge8xTCIP0Zw
  enseignement 3] · [fiche:binet-field-b2b-growth framework B].
- **Consensus** : 4 experts (Coudac, Hormozi, Abraham, Binet & Field).
- **Confiance** : **moyenne** (méthode partagée, seuils d'auteurs).

### B4. Finance la marque et l'activation ensemble, et vise large dans la catégorie plutôt que la seule fidélisation payante
- **Pourquoi** : selon Binet & Field (non vérifié), l'optimum tourne autour de la **moitié** du budget en marque en B2B
  (« 50/50 », « 46/54 », « 45/55 » selon les pages : ne jamais citer un chiffre au point près), environ 60/40 en B2C ;
  les campagnes de portée produisent le plus d'effets, celles de fidélisation presque aucun (0,0 sur la Fig. 7) ; la
  marque rend l'activation plus efficace (halo) [fiche:binet-field-b2b-growth p. 13-20, p. 27]. Coudac : Meta seul est
  « beaucoup beaucoup beaucoup moins efficace » que dans un mix, « une calèche à plusieurs chevaux »
  [fiche:qBxEAqZbHVg 04:15]. Hormozi : en ligne le CAC monte toujours ; on y répond par la **marque** (inbound, prix) et
  par la LTV [fiche:6_CCutkM11g 03:50].
- **Comment l'appliquer** :
  1. Dès qu'une marque a dépassé le test borné (`publicite.md` D4), réserver une part **marque** (récit, émotion,
     portée large dans la catégorie) à côté de l'**activation** (offre, réponse directe).
  2. « Large » se mesure **à l'intérieur de la catégorie** (tous les acheteurs potentiels, comité d'achat, futurs
     décideurs), pas sur la population générale [fiche:binet-field-b2b-growth enseignement 9].
  3. Ne jamais couper la marque pour « sauver » les leads sans test d'incrémentalité (B2).
  4. La fidélisation passe par les canaux possédés et l'expérience produit (D4), pas par des campagnes payantes
     dédiées.
- **Pour une marque d'entreprise / un studio B2B** : au lancement, Sillage n'a pas le budget d'une vraie part marque :
  la vidéo de marque (le portfolio animé, les décodages) joue ce rôle en organique ; la part payante reste un test
  d'activation tant que le cash ne permet pas plus (D1, D2).
- **Sources** : [fiche:binet-field-b2b-growth enseignements 2, 5, 6, 9] · [fiche:qBxEAqZbHVg enseignement 3] ·
  [fiche:6_CCutkM11g enseignement 6] · [fiche:OgRgbar2dOQ (levier marque hors pub)].
- **Consensus** : 4 experts (Binet & Field, Coudac, Hormozi, Kapferer sur la marque comme capital). Hopkins et Ogilvy
  contre (D1).
- **Confiance** : **moyenne** pour le principe, **faible** pour tout ratio (moins de 50 cas B2B, effets auto-évalués,
  non vérifié).

### B5. Pilote avec deux horloges : un indicateur rapide pour décider, un indicateur à plus de 6 mois pour la marque
- **Pourquoi** : Binet & Field placent à **six mois** le seuil où les effets de marque dominent ceux de l'activation, et
  jugent le ROMI utile comme mesure financière mais **dangereux comme KPI principal** parce qu'il favorise l'activation
  [fiche:binet-field-b2b-growth p. 37-38]. Hormozi cherche au contraire l'indicateur le plus **rapide** qui corrèle avec
  la qualité (le vrai résultat arrive avec 6 à 12 mois de latence, trop lent pour apprendre) [fiche:Jmkq5RLjm0U
  framework K]. Enns sépare indicateur avancé et retardé [fiche:J6Su5Vx3x5U framework H]. Coudac regarde la valeur d'un
  client à un an [fiche:qBxEAqZbHVg 03:43].
- **Comment l'appliquer** :
  1. Activation : indicateur rapide apparié quantité × qualité (coût par rendez-vous qualifié, taux d'opt-in, CAC à
     30 jours), revu chaque semaine (`metriques-appariees.md`).
  2. Marque : indicateurs à **6 mois et plus** : recherches de marque, trafic direct, réponses « je vous connaissais
     déjà » au questionnaire, part des demandes entrantes non sollicitées, sensibilité au prix (taux de remise
     accordé), étude de notoriété ou brand lift si le budget le permet.
  3. Le ROMI à court terme n'est jamais le seul critère d'arrêt d'une campagne de marque.
- **Sources** : [fiche:binet-field-b2b-growth enseignement 7] · [fiche:Jmkq5RLjm0U framework K] · [fiche:J6Su5Vx3x5U
  framework H] · [fiche:qBxEAqZbHVg enseignement 1] · framework `metriques-appariees.md`.
- **Consensus** : 4 experts (Binet & Field, Hormozi, Enns, Coudac), en désaccord sur le poids relatif (D1).
- **Confiance** : **moyenne** (« 4 % des marketeurs mesurent au-delà de 6 mois » : sondage LinkedIn sans méthode, ne
  pas citer).

### B6. Teste petit, à perte plafonnée, puis augmente par paliers sur ce qui a prouvé
- **Pourquoi** : Hopkins : 4 ou 5 villes tests, puis on étend ; « playing on the safe side of a hundred to one shot »
  [fiche:hopkins-scientific-advertising p. 76-77]. Halbert : 1 000 à 5 000 plis de test, perte plafonnée, puis
  déploiement [fiche:halbert-boron-letters ch. 22, 24]. Kotler : environ 10 % du budget sur un nouveau canal, une preuve
  mesurée, puis +5 à 10 % sur l'usage précis qui a fait ses preuves ; jamais 50 % d'un coup [fiche:sR-qL7QdVZQ
  framework K]. Hormozi : quelques dollars par jour, sans plafond ensuite [fiche:k834E6OTGTM 00:17-00:23]. Heath : un
  budget qu'on peut perdre sans catastrophe [fiche:dAJyqo6wnq4 00:16]. Sutherland : le business est du poker, quelques
  coups font le résultat [fiche:lhlS-Wds02M enseignement 7]. Meta conseille 20 à 30 % du budget en test de nouvelles
  créatives [veille:meta-ads §3.1].
- **Comment l'appliquer** :
  1. Tout nouveau canal ou format : budget de test borné, critère de succès écrit, durée fixée, validation de
     l'utilisateur.
  2. Montée par paliers sur la variante gagnante seulement ; sur Meta, paliers calibrés par
     `2026-10-22-meta-regle-passage-tests-et-budget` (+20 % contre +50 %, rang 1) ; le « +20 % » courant ne vient que de
     praticiens [verif:PA02].
  3. Part permanente du budget réservée aux tests (D3).
  4. L'extrapolation linéaire « 1 000 clients → 1 million » est fragile : saturation et fatigue créative
     (`meta-ads.md` MA10).
- **Sources** : [fiche:hopkins-scientific-advertising enseignement 2] · [fiche:halbert-boron-letters enseignement 4] ·
  [fiche:sR-qL7QdVZQ enseignement 6] · [fiche:k834E6OTGTM enseignement 7] · [fiche:dAJyqo6wnq4 enseignement 6] ·
  [fiche:lhlS-Wds02M enseignements 7, 8] · [fiche:Ge8xTCIP0Zw (test avant mise à l'échelle des deals)] ·
  [veille:meta-ads §3.1].
- **Consensus** : 7 experts (Hopkins, Halbert, Kotler, Hormozi, Heath, Sutherland, Abraham) + Meta.
- **Confiance** : **haute** sur le principe ; les pourcentages sont des heuristiques (D3).

### B7. Juge un coût à la qualité exploitable du résultat, jamais au prix unitaire (CPM, CPC, coût par lead)
- **Pourquoi** : « ce qui est moins cher est souvent moins bon » : la réservation tient un CPM bas avec des impressions
  de moindre qualité (conclusion pratique juste, mécanisme ❓ [verif:PA15]), Audience Network est moins cher parce que
  peu demandé [verif:PA10 🟡] [fiche:dAJyqo6wnq4 00:08-00:37]. Hopkins : une annonce peut amener beaucoup de réponses
  sans valeur, d'où le coût **par client** [fiche:hopkins-scientific-advertising p. 8]. Ogilvy juge formats et horaires
  au coût par vente [fiche:Br2KSsaTzUc 00:01:42]. Kotler : la pub traditionnelle se jugeait au coût pour mille
  « théoriquement » exposés [fiche:sR-qL7QdVZQ 00:50]. Coudac classe CPM et CPC en indicateurs intermédiaires
  [fiche:qBxEAqZbHVg 16:40].
- **Comment l'appliquer** : chaque tableau de bord met le coût unitaire à côté d'un indicateur de qualité en aval
  (taux de présence au rendez-vous, taux de signature, panier, rachat) ; aucun arbitrage budgétaire sur le CPM seul.
- **Sources** : [fiche:dAJyqo6wnq4 enseignement 4] · [fiche:hopkins-scientific-advertising enseignement 1] ·
  [fiche:Br2KSsaTzUc enseignement 5] · [fiche:sR-qL7QdVZQ enseignement 6] · [fiche:qBxEAqZbHVg enseignement 5].
- **Consensus** : 5 experts (Heath, Hopkins, Ogilvy, Kotler, Coudac).
- **Confiance** : **haute**.

### B8. Calcule ce qu'un client rapporte, et quand, avant de fixer ce que tu acceptes de payer pour l'acquérir
- **Pourquoi** : « What cannot be done on a large scale profitably cannot be done on a small scale » ; un germicide dont
  un flacon dure des années ne rembourse pas son coût d'acquisition [fiche:hopkins-scientific-advertising p. 50-52].
  Abraham : qui connaît la valeur vie peut payer l'acquisition plus cher que ses concurrents [fiche:Ge8xTCIP0Zw 00:08].
  Hormozi : « If leads cost too much, it's common that they don't really cost too much, but that you make too little »
  [fiche:6_CCutkM11g 01:22]. Coudac compare la valeur à un an des nouveaux et des anciens clients [fiche:qBxEAqZbHVg].
  Denney : un panier trop faible peut rendre l'acquisition payante impossible (affirmation absolue sans données
  [verif:PG09 ❓]) [fiche:yRgPbqywUJ8 02:41].
- **Comment l'appliquer** :
  1. Avant toute campagne : marge par vente, rachat, panier, délai de récupération du CAC ; sans données, hypothèses
     écrites et marquées comme telles.
  2. LTV **mesurée sur une vraie cohorte** avant de payer l'acquisition au-delà de la première vente (D2).
  3. Si le calcul ne passe pas, travailler l'offre (bundle, séquence d'offres, continuité) avant d'augmenter la pub :
     « Fix the bucket before we pour a bunch of water » [fiche:6_CCutkM11g 03:19] (`monetisation-et-offre.md`,
     `economie-unitaire.md`).
- **Sources** : [fiche:hopkins-scientific-advertising enseignement 8] · [fiche:Ge8xTCIP0Zw enseignements 3, 4] ·
  [fiche:6_CCutkM11g enseignements 1, 6] · [fiche:qBxEAqZbHVg enseignement 1] · [fiche:yRgPbqywUJ8 enseignement 3].
- **Consensus** : 5 experts (Hopkins, Abraham, Hormozi, Coudac, Denney).
- **Confiance** : **moyenne** (principe solide ; chiffres d'illustration ❓, dont Icy Hot [verif:V4B-JA05]).

## Principes soutenus par 1 ou 2 experts

### B9. Investis au bon moment : fort quand le marché est chaud, avec un temps d'avance ; offensif en récession
- **Pourquoi** : le bon media buyer investit fort dès le début d'une promo puis module avec un peu d'avance sur la
  demande (profil de l'année précédente) ; le mauvais est toujours à contretemps [fiche:qBxEAqZbHVg 36:39-38:50].
  Abraham : en marché baissier, les médias aux enchères baissent, les médias à tarif fixe deviennent négociables et les
  concurrents se retirent, « as long as they manage their cash flow » [fiche:Ge8xTCIP0Zw 00:04-00:13].
- **Comment l'appliquer** : calendrier d'investissement annuel calé sur la saisonnalité réelle de la marque
  (`planificateur-calendrier`) ; en période de repli des concurrents, tester l'achat d'espace à prix réduit (B6).
- **Sources** : [fiche:qBxEAqZbHVg enseignement 8] · [fiche:Ge8xTCIP0Zw enseignements 7, 8] ·
  `plan-offensif-en-recession.md`.
- **Consensus** : 2 experts (Coudac, Abraham). **Confiance** : **faible** (récits d'agence, timeshare « 40 à 130-140 M$ »
  non vérifié).

### B10. Prévois avec des repères prudents et datés, puis recale sur les données du compte dès les premiers jours
- **Pourquoi** : le « CPM de 5 € normal en France » de Coudac (2024) n'est plus une norme ; les relevés 2025-2026
  donnent une médiane d'environ 8 à 10 $ [verif:PG03 ❌ comme norme 2026]. Les seuils d'apprentissage varient selon les
  comptes [verif:PA01].
- **Comment l'appliquer** : prévision de départ à **7-12 € de CPM** en France, puis remplacement par les valeurs
  mesurées ; chaque repère porte sa source et sa date (`predicteur-performance`).
- **Sources** : [verif:PG03, PA01] · [fiche:qBxEAqZbHVg] · expérience `2026-10-22-meta-releve-cpm-premiers-comptes`
  (rang 3).
- **Consensus** : 1 expert (Coudac, corrigé) + registre. **Confiance** : **moyenne**.

### B11. Fixe le budget de marque d'après un objectif de part de marché (part de voix), pas d'après un pourcentage du CA
- **Pourquoi** : selon Binet & Field (non vérifié), une part de voix supérieure à la part de marché fait croître la
  part de marché, environ +0,7 point par an pour +10 points d'excès de part de voix en B2B ; c'est le seul résultat
  qu'ils déclarent statistiquement significatif [fiche:binet-field-b2b-growth p. 10-12].
- **Comment l'appliquer** : pour une marque qui connaît sa part de marché et celle de voix de ses concurrents, partir
  d'un objectif de croissance de part ; pour une petite marque sans ces données (cas courant), ce principe reste un
  cadre de discussion, pas un calcul.
- **Sources** : [fiche:binet-field-b2b-growth enseignement 1, framework B].
- **Consensus** : 1 source. **Confiance** : **faible** (non vérifié ; données jusqu'en 2018, surtout britanniques).

---

## Désaccords entre experts

### D1. Vente immédiate et mesure « au dollar » (Hopkins, Ogilvy) contre construction de marque à long terme, ROMI dangereux comme KPI (Binet & Field)
- **Positions** :
  - Hopkins : la pub n'a qu'un but, des ventes mesurables ; il refuse de payer pour « garder le nom présent dans les
    esprits » ; tout ce qui n'est pas tracé est suspect [fiche:hopkins-scientific-advertising p. 12, p. 44, p. 94-96].
    Ogilvy : seuls ceux qui mesurent « to a dollar » savent [fiche:Br2KSsaTzUc 00:00:35]. Kotler : le marketing direct
    est le modèle de redevabilité [fiche:sR-qL7QdVZQ 00:53]. Hormozi : l'indicateur le plus rapide possible.
  - Binet & Field : au-delà de six mois les effets de marque dominent ; la fame et l'émotion produisent le plus
    d'effets ; le ROMI est un bon instrument financier mais un mauvais KPI principal [fiche:binet-field-b2b-growth p. 30,
    p. 37-38]. Le « culte du coupon » est exactement le biais qu'ils dénoncent [fiche:hopkins-scientific-advertising
    « Confrontation avec Binet & Field »].
  - Points de contact : Hopkins pratiquait lui-même de la marque sans la mesurer (voix constante, « by making a man
    famous we make his product famous ») ; ses **tests par villes sur les ventes totales** mesurent une partie des
    effets de marque, mieux que le coupon. Binet & Field gardent l'activation, environ la moitié du budget.
  - Niveau de preuve : Hopkins s'appuie sur des cas anonymes de 1923 ; Binet & Field sur moins de 50 cas B2B primés,
    auto-évalués, en corrélation, financés par LinkedIn. Aucun des deux n'est vérifié par notre registre.
- **Recommandation de l'agence** :
  1. **Deux budgets, deux juges.** L'activation est jugée à la manière de Hopkins (coût par nouveau client, tests
     codés, B1, B7). La marque est jugée à la manière de Binet & Field (indicateurs à 6 mois et plus, B5), jamais au
     ROMI de court terme seul.
  2. **Le pont, c'est l'incrémentalité** (B2) : tests géographiques ou temporels sur les ventes totales, qui voient
     les deux effets.
  3. **La séquence dépend du cash** : une marque qui démarre (cas de Sillage) commence par l'activation mesurée et la
     marque en organique ; la part payante de marque grandit quand le plancher de cash (B3, D2) est tenu.
- **Ce qui ferait changer** : sur nos marques, un test d'incrémentalité à 6 mois où la part marque n'apporte rien de
  mesurable (on réduirait la part marque), ou l'inverse (on l'augmenterait). Expérience à créer par
  `concepteur-experiences` (aucune n'est encore au backlog).

### D2. Payer plus de 100 % de la première vente (Abraham) contre rentabilité à 30 jours (Hormozi, *Money Models*)
- **Positions** :
  - Abraham : Icy Hot offrait aux médias **115 % de la première vente** sur leur espace invendu, sans fixe, parce que
    le back-end (rachats, autres produits) rendait l'opération rentable ; « ils auraient pu reverser 49 $ sur 50 $ » de
    la première année [fiche:Ge8xTCIP0Zw 00:08-00:10]. Récit constant de l'auteur sans source indépendante
    [verif:V4B-JA04 🟡] ; le calcul de LTV est une illustration [verif:V4B-JA05 ❓].
  - Hormozi : un bon money model rapporte en **30 jours** au moins deux fois ce que le client coûte à acquérir et à
    servir ; chaque client finance les deux suivants ; « the channel doesn't matter as long as it pays back in 30
    days » [fiche:6_CCutkM11g enseignements 1, 10] (seuils d'auteur, chiffres du lancement déclaratifs).
  - Point commun : les deux partent de la valeur réelle du client. La vraie différence est le **risque de trésorerie** :
    Abraham ne paie qu'**au résultat** (le média porte le risque du fixe) et s'appuie sur un back-end **déjà observé** ;
    Hormozi raisonne pour une entreprise qui paie sa pub d'avance et peut mourir de manquer de cash.
- **Recommandation de l'agence** :
  1. **Règle par défaut : récupérer le CAC sur la première vente ou dans les 30 jours** (version prudente d'Hormozi),
     surtout pour une marque sans historique de rachat, et toujours pour Sillage au lancement.
  2. **Dépasser la première vente** seulement si les quatre conditions sont réunies : (a) LTV mesurée sur une vraie
     cohorte (au moins 6 à 12 mois de données), (b) trésorerie qui couvre le délai de récupération, (c) structure au
     résultat ou risque plafonné (B6), (d) validation écrite de l'utilisateur.
  3. Calculs détaillés : `economie-unitaire.md`.
- **Ce qui ferait changer** : des données de cohorte d'une marque cliente montrant un rachat stable ; un échec de
  trésorerie causé par la règle des 30 jours (opportunités rentables refusées).

### D3. Quelle part du budget pour tester ?
- **Positions** : Kotler, 10 % sur un nouveau canal puis +5 à 10 % [fiche:sR-qL7QdVZQ framework K] ; Meta, 20 à 30 % du
  budget sur les nouvelles créatives [veille:meta-ads §3.1] ; Ralston, 70/20/10 entre éprouvé, itération et paris
  (heuristique [verif:G15 🟡]) ; Hopkins, test permanent sans interrompre le plan éprouvé
  [fiche:hopkins-scientific-advertising p. 78-79].
- **Recommandation de l'agence** : ce ne sont pas les mêmes tests. **Nouveau canal** : environ 10 % (Kotler).
  **Nouvelles créatives dans un canal qui marche** : 20 à 30 % (Meta). **Contenu organique** : 70/20/10
  (`analyse-et-iteration.md` A6). À recaler sur nos résultats.

### D4. Faut-il payer pour fidéliser ? (Binet & Field contre Coudac, Hormozi, Abraham)
- **Positions** : Binet & Field, les campagnes de fidélisation ont « a zero success rate » (Fig. 7) et la fidélité ne
  monte qu'avec la pénétration [fiche:binet-field-b2b-growth p. 16-20]. Coudac : faire revenir un client coûte bien moins
  cher (5 à 25 fois selon le secteur d'après HBR 2014 [verif:PG01 🟡], pas « 7 fois ») ; Abraham : c'est le back-end qui
  fait la fortune ; Hormozi : la LTV est l'avantage durable.
- **Recommandation de l'agence** : pas de contradiction réelle. Le **budget payant** sert l'acquisition et la portée ;
  la **fidélité** se travaille par l'expérience produit, l'offre suivante et les canaux possédés (email, SMS,
  organique), qui ne coûtent pas d'enchère (`retention-client.md`). On n'achète pas de campagne payante de fidélisation
  sans test d'incrémentalité.

---

## Tests au labo (`experiences/index.md`)
- `2026-10-22-meta-regle-passage-tests-et-budget` (rang 1) : B6 (paliers +20 % contre +50 %).
- `2026-10-22-meta-releve-cpm-premiers-comptes` (rang 3) : B10.
- À créer : test d'incrémentalité marque contre activation à 6 mois (D1) ; questionnaire « où nous avez-vous
  connus ? » comparé à l'attribution Meta et GA4 sur une même période (B2).

## Journal
| Date | Modification |
|---|---|
| 2026-10-25 | Création (grande synthèse, équipe S4) : 11 principes, 4 désaccords tranchés, 17 fiches + veille Meta §7 + registre (PA, PG, PB, G15) et passe 4b (V4B-JA). |
