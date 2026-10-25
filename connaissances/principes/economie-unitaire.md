# Principes : économie unitaire

> Tenu par `synthetiseur-connaissances`. Création : 2026-10-25 (grande synthèse, équipe S1 « offre et vente »).
> Tag `economie-unitaire` (économie d'un client : CAC, LTV, marge, délai de récupération, cash encaissé à 30 jours,
> acquisition financée par le client). Aucune fiche ne porte encore le tag lui-même (créé le 2026-10-22) : les
> passages sont rangés ici par la table des alias d'`agents.md` (« finance-tresorerie, CAC, LTV, marge »).
> L'allocation du budget entre canaux et l'attribution relèvent de `mesure-budget.md`.
> Sources traitées (13 fiches, 12 experts) :
> `6_CCutkM11g`, `JE2_7elAcxM`, `k834E6OTGTM` (Alex Hormozi, **un** expert) · `Ge8xTCIP0Zw` (Jay Abraham) ·
> `hopkins-scientific-advertising` (Claude Hopkins, 1923) · `halbert-boron-letters` (Gary Halbert, 1984) ·
> `qBxEAqZbHVg` (Coudac) · `yRgPbqywUJ8` (Dara Denney) · `xf0Mli0LVgI` (MrBeast) · `11rNI6BUey4` (Stan Leloup) ·
> `J6Su5Vx3x5U` (Blair Enns) · `oeG8NWrWV4Y` (Stanislas Niox-Chateau, Doctolib) · `SUzKZfyaAK8` (Dan Koe) ·
> `DJLtwT1Z0eo` (Justin Welsh).
> Frameworks liés : `frameworks/money-model-sequence-d-offres.md` (équation des 30 jours) ·
> `diagnostic-express-du-modele-economique.md` · `systeme-profit-fast-cash-et-prix.md` ·
> `cac-blended-et-mesure-du-mix.md` · `plan-d-atterrissage-et-timing.md` · `lancement-meta-structure-1-1-1.md`
> (étape 0, équation de croissance e-commerce) · `ancrage-sur-valeur-garantie.md`.
> Renvois : `monetisation-et-offre.md` (séquence d'offres, upsell, prix), `retention-client.md` (LTV par la
> fidélisation), `mesure-budget.md`, `publicite.md`, `meta-ads.md`, `lancement-produit.md`.
>
> **Labo** : `experiences/apprentissages.md` est vide au 2026-10-25. Aucune expérience en attente ne porte
> directement sur ce fichier ; `2026-10-22-meta-regle-passage-tests-et-budget` et
> `2026-10-22-meta-releve-cpm-premiers-comptes` fourniront les premiers coûts d'acquisition mesurés.

## Légende

- **Consensus** : nombre d'experts distincts (Hormozi = 1 pour ses trois vidéos).
- **Confiance** (d'après `verifications/registre.md`, `passe-4a-marque-pub.md`, `passe-4b-createurs-offres.md`) :
  - **haute** : au moins 3 experts convergents **et** aucun chiffre porteur contredit, ou appui sur un fait vérifié ;
  - **moyenne** : 2 experts ou plus, chiffres seulement plausibles ou absents ;
  - **faible** : un seul expert, ou principe adossé à des chiffres déclaratifs / invérifiables.
- **Chiffres porteurs non vérifiés** : le seuil « bénéfice brut à 30 jours > 2 × (CAC + COGS) » (heuristique
  d'Hormozi, parenthèse ambiguë à l'oral), la marge brute « ~80 % » (Leila Hormozi), la valeur « 10 fois le prix »
  (Doctolib), la grille abonnés → revenu de Koe. Le cas Icy Hot (80 % de rachat mensuel) est ❓ (V4B-JA05) et
  l'« 82 % des entreprises meurent du cash-flow » est ❓ (V4B-MM06) : **ni l'un ni l'autre n'est citable**. Le seul
  chiffre de contexte citable : selon l'enquête de la Fed publiée en 2024, 54 % des petites entreprises
  employeuses américaines n'étaient pas rentables fin 2023 (V4B-MM07 ✅), jamais « chaque année ».

## Résumé (10 principes)

| # | Principe | Consensus | Confiance |
|---|---|---|---|
| E1 | Calcule l'économie d'un client avant d'acheter du trafic | 7 | haute |
| E2 | Mesure le cash encaissé sur les 30 premiers jours face au coût d'acquérir et de servir | 4 | moyenne |
| E3 | Laisse la valeur vie payer un coût d'acquisition plus élevé, mais seulement sur une cohorte mesurée | 5 | moyenne |
| E4 | Juge l'acquisition au coût d'un nouveau client mesuré en global, pas au ROAS attribué | 2 | moyenne |
| E5 | Ne mets pas de pub payante sur un panier trop faible : bundle, séquence d'offres ou canal organique | 4 | moyenne |
| E6 | Teste petit, à risque plafonné, et monte par paliers en réinvestissant ce qui revient | 4 | moyenne |
| E7 | Calcule rémunérations et partages sur la marge brute, jamais sur le chiffre d'affaires | 3 | moyenne |
| E8 | Répare la rétention avant d'acheter plus de trafic | 3 | moyenne |
| E9 | Le temps de livraison plafonne le revenu : productise ce qui se répète | 3 | moyenne |
| E10 | Ne lance une marque propre que si le rachat répété, la marge et la croissance sont crédibles | 2 | moyenne |

---

## Principes partagés par 3 experts ou plus

### E1. Calcule l'économie d'un client avant d'acheter du trafic
- **Pourquoi** : « What cannot be done on a large scale profitably cannot be done on a small scale » (Hopkins).
  Une entreprise meurt d'abord de manquer de cash, parce qu'elle dépense plus pour acquérir et servir un client
  qu'il ne rapporte (Hormozi). La publicité est un levier qu'on ne tire qu'une fois (« fix the bucket »).
- **Comment l'appliquer** :
  1. Estimer, par offre : prix et marge brute, coût de livraison (COGS), coût d'acquisition prévu, revenu sur
     12 mois par client (rachat, cross-sell), part de l'audience concernée (Hopkins framework M).
  2. Mailing ou campagne : chiffrer « par mille » contacts (prix, coût par mille, taux de réponse supposé, profit
     par mille × milliers disponibles) avant de lancer (Halbert framework E).
  3. Vérifier la taille du marché accessible : CA visé ÷ prix = ventes nécessaires, rapportées à la population
     cible (Leloup : à 300 €, 333 ventes par an pour 100 000 €) ; test du « jeu qui ne vaut pas d'être joué »
     (Hormozi).
  4. Remplacer au plus vite chaque taux supposé par un taux mesuré (lien avec M4 de `monetisation-et-offre.md`).
- **Pour une marque d'entreprise / un studio B2B** : pour Sillage, un client vaut le premier projet plus les
  déclinaisons et le forfait éventuel ; le calcul se fait avant de payer de la pub LinkedIn ou Meta.
- **Sources** : [fiche:hopkins-scientific-advertising] enseignement 8, framework M ; [fiche:halbert-boron-letters]
  enseignement 4, framework E ; [fiche:6_CCutkM11g] enseignements 1, 6, framework F1 ; [fiche:11rNI6BUey4]
  framework F ; [fiche:Ge8xTCIP0Zw] enseignement 3 ; [fiche:qBxEAqZbHVg] framework A (CA = visiteurs × conversion
  × LTV) ; [fiche:xf0Mli0LVgI] framework F.
- **Consensus** : 7 experts (Hopkins, Halbert, Hormozi, Leloup, Abraham, Coudac, MrBeast).
- **Confiance** : haute pour le principe (convergence sur un siècle de sources). Les chiffres d'illustration ne
  sont pas des repères.

### E2. Mesure le cash encaissé sur les 30 premiers jours face au coût d'acquérir et de servir
- **Pourquoi** : si chaque client rembourse son acquisition très vite, on n'a besoin d'argent que pour le premier
  client, puis on réinvestit (« house money at the casino », Hormozi). Hopkins finançait l'extension « selon le
  délai de remboursement ».
- **Comment l'appliquer** :
  1. Pour chaque offre : bénéfice brut encaissé sur 30 jours rapporté à (CAC + COGS). Hormozi vise au moins 2× :
     **heuristique non vérifiée**, à traiter comme objectif de conception, pas comme seuil de décision.
  2. Noter le délai de récupération de la pub (payback).
  3. Leviers de cash immédiat sans changer le produit : attraction qui rapporte dès le premier jour, prépaiement
     avec remise, offre d'entrée courte payée d'avance (détails dans `monetisation-et-offre.md`, M14 et M23).
  4. Suivre le % de cash encaissé d'avance comme indicateur de conviction de l'acheteur (Hormozi).
- **Sources** : [fiche:6_CCutkM11g] enseignement 1, framework A ; [fiche:JE2_7elAcxM] framework I (cash
  d'avance) ; [fiche:hopkins-scientific-advertising] framework C ; [fiche:halbert-boron-letters] enseignement 4 (test
  financé à risque plafonné).
- **Consensus** : 4 experts (Hormozi, Hopkins, Halbert ; Abraham en contre-point, voir DE2).
- **Confiance** : moyenne.

### E3. Laisse la valeur vie payer un coût d'acquisition plus élevé, mais seulement sur une cohorte mesurée
- **Pourquoi** : « If leads cost too much, it's common that… you make too little » (Hormozi). Qui connaît la valeur
  vie peut surenchérir sur l'acquisition et payer un média plus que la première vente (Abraham). Le CAC en ligne
  monte à long terme : la LTV et la marque sont les deux réponses (Hormozi).
- **Comment l'appliquer** :
  1. Calculer la valeur d'une **cohorte réelle** (10 premiers acheteurs puis davantage) : rachat, autres produits,
     fréquence (Abraham framework D). Sans données de cohorte, ne pas payer au-delà de la marge de la première
     vente.
  2. Lire la valeur à un an plutôt qu'à la première commande (Coudac, `cac-blended-et-mesure-du-mix.md`).
  3. Chercher le « vrai business » en back-end (auto-école → location, Abraham) ; voir aussi R5 de
     `retention-client.md`.
  4. Comparer les segments par LTV:CAC × taille de marché et n'en garder qu'un en front-end (Hormozi).
- **Sources** : [fiche:6_CCutkM11g] enseignements 6, 9, frameworks F2, F10 ; [fiche:Ge8xTCIP0Zw] enseignements 3,
  4 ; [fiche:qBxEAqZbHVg] framework A ; [fiche:xf0Mli0LVgI] enseignement 7 (rachat répété) ;
  [fiche:hopkins-scientific-advertising] framework M (revenu annuel par client).
- **Consensus** : 5 experts (Hormozi, Abraham, Coudac, MrBeast, Hopkins).
- **Confiance** : moyenne. Le cas Icy Hot est une illustration invérifiable (V4B-JA04 🟡, JA05 ❓).

### E5. Ne mets pas de pub payante sur un panier trop faible : bundle, séquence d'offres ou canal organique
- **Pourquoi** : « You're not going to be able to sell a $20 product on Meta », les coûts d'acquisition sont trop
  élevés (Denney). Les petits prix sont les plus durs : ils demandent des millions de personnes touchées pour des
  marges « riquiqui » (Leloup). Un germicide qui dure des années ne rembourse pas son client (Hopkins).
- **Comment l'appliquer** :
  1. Pour un produit à petit prix : bundle orienté problème → solution, séquence d'offres après le premier achat,
     ou acquisition organique d'abord (Denney, Hormozi).
  2. Réserver les canaux possédés (e-mail, SMS, organique) aux clients existants ; ne pas y dépenser de la pub
     (Coudac).
  3. Vérifier que le prix plaît à une part suffisante du marché : un prix qui ne plaît qu'à 10 % du marché
     multiplie le coût de vente (Hopkins).
- **Sources** : [fiche:yRgPbqywUJ8] enseignement 3 ; [fiche:11rNI6BUey4] enseignement 4 ;
  [fiche:hopkins-scientific-advertising] enseignement 8, framework O ; [fiche:qBxEAqZbHVg] framework A ;
  [fiche:6_CCutkM11g] framework B.
- **Consensus** : 4 experts (Denney, Leloup, Hopkins, Hormozi). Coudac en désaccord partiel (DE1).
- **Confiance** : moyenne (le seuil de 20 $ est une opinion de praticienne).

### E6. Teste petit, à risque plafonné, et monte par paliers en réinvestissant ce qui revient
- **Pourquoi** : « Let the thousands decide for the millions » (Hopkins) ; un test de 1 000 à 5 000 plis avant
  tout déploiement (Halbert) ; une pub démarrée petit, suivie chaque jour, réinvestie (Hormozi, lancement
  autofinancé).
- **Comment l'appliquer** :
  1. Fixer la perte maximale acceptable du test et le critère de passage au palier suivant avant de dépenser.
  2. Ne jamais engager tout le budget le premier jour ; suivre chaque jour dépense et encaissement.
  3. Pour la pub Meta : règle de passage et paliers de budget de `2026-10-22-meta-regle-passage-tests-et-budget`
     (en attente) et `meta-ads.md`.
- **Sources** : [fiche:hopkins-scientific-advertising] enseignement 2, frameworks B, C ; [fiche:halbert-boron-letters]
  enseignement 4 ; [fiche:6_CCutkM11g] framework D ; [fiche:k834E6OTGTM] enseignement 7.
- **Consensus** : 4 experts (Hopkins, Halbert, Hormozi, Leloup avec la prévente à objectif chiffré).
- **Confiance** : moyenne. Les chiffres du lancement d'Hormozi (22 k$ → 34 k$ par jour) sont des affirmations.

### E7. Calcule rémunérations et partages sur la marge brute, jamais sur le chiffre d'affaires
- **Pourquoi** : « All your calculations in terms of compensation have to operate from gross profit » (Hormozi).
  Un partage de profit se fait après les coûts directs du partenaire (Abraham, 50/50). Les coûts du prestataire
  n'entrent pas dans le prix, mais la marge doit rester saine : 15 à 20 % avant impôt est un ordre de grandeur
  respectable pour une agence (Enns, GB06 🟡).
- **Comment l'appliquer** : toute commission (commerciaux, affiliés, apporteurs) et toute part variable se
  calcule sur la marge brute du contrat ; vérifier qu'un partage laisse la marge minimale fixée ; plan à deux
  variables au plus (Hormozi).
- **Sources** : [fiche:6_CCutkM11g] framework G ; [fiche:Ge8xTCIP0Zw] framework G ; [fiche:J6Su5Vx3x5U]
  enseignement 9 ; [fiche:JE2_7elAcxM] framework L (rémunération sous 10 % du CA quand les leads sont fournis).
- **Consensus** : 3 experts (Hormozi, Abraham, Enns).
- **Confiance** : moyenne.

### E8. Répare la rétention avant d'acheter plus de trafic
- **Pourquoi** : « I'd rather fix the bucket before we pour a bunch of water » (Hormozi). Le back-end, pas le
  front-end, fait la fortune (Abraham). Ce qui fait **gagner** un client puis le **garder** fait partie des questions
  de stratégie (Hopkins).
- **Comment l'appliquer** : mesurer le renouvellement par cohorte ; si la valeur vie est faible au regard du CAC,
  travailler l'onboarding, l'activation et les formats qui retiennent avant d'augmenter la pub (détail dans
  `retention-client.md`).
- **Sources** : [fiche:6_CCutkM11g] framework F4 ; [fiche:Ge8xTCIP0Zw] enseignements 4, 6 ;
  [fiche:hopkins-scientific-advertising] framework O.
- **Consensus** : 3 experts (Hormozi, Abraham, Hopkins). Tension avec la priorité à la portée de Binet & Field,
  traitée dans `retention-client.md` (DR1).
- **Confiance** : moyenne.

### E9. Le temps de livraison plafonne le revenu : productise ce qui se répète
- **Pourquoi** : « Your income, lifestyle and freedom are limited by the amount of time your products take to
  fulfill » (Koe). Facturer au temps revient à être « puni de devenir meilleur » (Enns). Ce qui a rapporté le plus
  (les cours) n'est pas forcément ce qui a le plus de valeur (Welsh).
- **Comment l'appliquer** : noter ce qui revient d'un client à l'autre, l'écrire en procédure, puis en faire un
  produit ou un forfait ; vendre des résultats (outcomes) plutôt que des heures ; séparer dans le reporting le
  revenu et la valeur relationnelle de chaque produit (Welsh).
- **Sources** : [fiche:SUzKZfyaAK8] enseignement 4, framework S ; [fiche:J6Su5Vx3x5U] enseignement 9 ;
  [fiche:DJLtwT1Z0eo] enseignement 6.
- **Consensus** : 3 experts (Koe, Enns, Welsh).
- **Confiance** : moyenne. Les revenus cités (Koe, Welsh) sont autodéclarés et incohérents : ne pas les citer.

## Principes soutenus par 1 ou 2 experts

### E4. Juge l'acquisition au coût d'un nouveau client mesuré en global, pas au ROAS attribué
- **Pourquoi** : « La seule vraie mesure est le coût d'acquisition des nouveaux clients » ; le ROAS n'a pas de
  valeur absolue et une grande part de l'effet de Meta n'est pas attribuée (Coudac). Le contenu améliore la
  conversion des autres canaux (effet de halo, Hormozi).
- **Comment l'appliquer** : CAC blended = dépense d'acquisition totale ÷ nouveaux clients sur la période ;
  questionnaire post-achat « où nous avez-vous connus ? » ; lecture à un an (`cac-blended-et-mesure-du-mix.md`).
  Le choix des modèles d'attribution et des tests d'incrémentalité relève de `mesure-budget.md`.
- **Sources** : [fiche:qBxEAqZbHVg] frameworks B, C ; [fiche:k834E6OTGTM] framework E ; registre PA04-PA06.
- **Consensus** : 2 experts (Coudac, Hormozi ; plus l'émission LinkedIn Ads dans le framework).
- **Confiance** : moyenne (les fenêtres d'attribution Meta sont vérifiées, PA04 ✅ ; le « −50 % de coût par lead »
  d'Hormozi ne l'est pas).

### E10. Ne lance une marque propre que si le rachat répété, la marge et la croissance sont crédibles
- **Pourquoi** : « A business is getting someone to buy that bottle of jelly every two months for the next 10
  years » : l'audience vend le premier achat, pas les suivants ; un acheteur ne paie un multiple que pour une
  croissance annuelle avec marge (MrBeast). Le continuum affiliation → sponsoring → equity → marque propre
  (Hormozi, M10) donne le cran à choisir.
- **Comment l'appliquer** : test de viabilité (meilleur que l'existant ? métier maîtrisé : rayon, prix,
  références, emballage, distribution ? rachat ? marge ?), puis comparaison chiffrée avec un partenariat récurrent
  (`partenariats.md`, P5). Prime n'est **plus** un exemple de marque de créateur durable : chiffre d'affaires
  britannique 2024 en recul de plus de 70 % (V4B-MB07 ✅).
- **Sources** : [fiche:xf0Mli0LVgI] enseignement 7, framework F ; [fiche:Jmkq5RLjm0U] framework X.
- **Consensus** : 2 experts (MrBeast, Hormozi).
- **Confiance** : moyenne.

---

## Désaccords entre experts

### DE1. Le panier moyen : levier ou impasse ?
- **Positions** : Coudac : « je n'ai jamais vu un problème de performance résolu par une hausse du panier moyen »,
  Meta agit surtout sur les visiteurs [fiche:qBxEAqZbHVg framework E]. Hormozi : la LTV est l'avantage durable ;
  un upsell bien placé double le panier [fiche:6_CCutkM11g enseignement 5]. Denney : bundle pour rendre un produit
  à petit prix vendable sur Meta [fiche:yRgPbqywUJ8 enseignement 3].
- **Recommandation de l'agence** : les deux parlent de deux horizons. Dans un compte publicitaire, à court terme,
  hausser le panier ne corrige pas une créa ou une audience qui ne convertit pas (Coudac a raison sur le
  diagnostic). Au niveau de l'entreprise, le panier et la LTV décident du CAC qu'on peut se permettre (Hormozi et
  Denney ont raison sur la conception). On diagnostique la pub sur ses métriques de diffusion et de conversion, et
  on conçoit l'offre pour que l'économie unitaire tienne avant de lancer.
- **Ce qui ferait changer** : un test A/B d'offre (produit seul contre bundle, à créa identique) sur une marque
  e-commerce, mesuré au CAC et à la marge par commande (à proposer à `concepteur-experiences`).

### DE2. Se faire rembourser en 30 jours, ou payer plus que la première vente ?
- **Positions** : Hormozi : chaque client doit rapporter en 30 jours au moins deux fois son coût d'acquisition et
  de service [fiche:6_CCutkM11g enseignement 1]. Abraham : payer aux médias 115 % de la première vente, parce que
  le back-end rembourse sur l'année [fiche:Ge8xTCIP0Zw enseignement 3].
- **Recommandation de l'agence** : par défaut, la contrainte d'Hormozi (cash rapide), parce que nos marques n'ont
  ni données de cohorte ni trésorerie pour attendre. La logique d'Abraham n'est permise qu'avec une cohorte mesurée
  sur au moins un cycle de rachat et une trésorerie qui couvre le délai de récupération.
- **Ce qui ferait changer** : une cohorte réelle de plus de 6 mois sur une marque cliente, avec une LTV mesurée.

### DE3. Éduquer une catégorie : gaspillage ou croissance ?
- **Positions** : Hopkins : ne pas payer pour éduquer une catégorie dont les concurrents profiteront ; surfer la
  tendance [fiche:hopkins-scientific-advertising enseignement 8]. Binet & Field : la pub peut faire croître une
  catégorie et relever le plafond de croissance [fiche:binet-field-b2b-growth] (déduction de la fiche Hopkins).
- **Recommandation de l'agence** : pour une petite marque, Hopkins (capter la demande existante) ; l'arbitrage pour
  une marque déjà leader de sa niche est renvoyé à `strategie-croissance.md` et `mesure-budget.md`.

---

## Tests proposés au labo (`experiences/`)
1. Produit seul contre bundle, créa identique, mesuré au CAC et à la marge par commande (DE1).
2. Relevé systématique, sur chaque marque, du cash encaissé à 30 jours par client et du payback de la pub, pour
   remplacer l'heuristique « 2× en 30 jours » par nos propres valeurs (E2).

## Journal
| Date | Modification |
|---|---|
| 2026-10-25 | Création : 10 principes, 3 désaccords tranchés, à partir de 13 fiches (12 experts), du registre (passes 1 à 3) et des passes 4a et 4b (MM06, MM07, JA04, JA05, MB07). |
