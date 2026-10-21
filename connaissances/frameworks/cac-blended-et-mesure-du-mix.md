# Mesurer le mix sans croire l'attribution : CAC blended, questionnaire post-achat, valeur à un an, outil tiers et effet de halo

> Famille : mesure / publicité payante · Niveau : pilotage business du mix marketing

## Origine
Deux sources disent la même chose sous deux formes : ne pas croire la plateforme sur parole, mesurer au niveau du business. Ce document les fusionne.
- **Coudac** (Paul, DG), *48 min pour enfin comprendre Meta Ads*, mars 2024 [fiche:qBxEAqZbHVg] :
  - la seule vraie mesure est le coût d'acquisition des nouveaux clients (enseignement 1 [00:32] [03:43] [39:56] [40:29]) ;
  - mesurer le mix sans faire confiance à l'attribution : CAC blended et questionnaire post-achat (framework H [23:40]-[30:45]) ;
  - valeur à un an par type de client (framework L [40:29]) ;
  - [FONDAMENTAL] selon la légende de datation de la fiche.
- **The LinkedIn Ads Show**, ép. 167 [fiche:pILj7t-qQhs] :
  - mesure « best-in-class » : outils de la plateforme **et** outil d'attribution tiers (framework K [00:35]-[00:38]) ;
  - analyse de l'effet de halo multicanal, cas Dreamdata (framework L [00:37]-[00:38]).
- Fiabilité : Coudac 3,5/5 (fondamentaux solides, **aucune donnée réelle**, exemples hypothétiques) ; LinkedIn 2,5/5 (chiffres « +20 à 30 % » promotionnels, sans méthode). « 1 500 à 2 000 ventes revendiquées pour 1 000 réelles » : **ordre de grandeur illustratif**. « Faire revenir un client coûte 7 fois moins cher » : statistique de seconde main, annoncée avec hésitation, **sans source primaire**.

## Problème résolu
Chaque régie revendique les mêmes ventes ; un modèle d'attribution suppose que chaque canal marche seul (« Facebook nourrit Google » le contredit) et pousse à couper le canal « moins rentable », ce qui casse la synergie. Un CPA ou un ROAS peut être excellent alors que les achats viennent de clients existants qu'un e-mail aurait suffi à faire revenir. Il faut des mesures qui disent la **vérité business** : combien de **nouveaux** clients, à quel coût, avec quelle valeur.

## Étapes

### 1. Séparer acquisition et réactivation
Meta (et la pub payante d'acquisition) pour les **nouveaux** clients ; e-mail, SMS et organique (canaux possédés) pour faire revenir les existants.
- Question : nos rapports séparent-ils nouveaux et existants ?

### 2. Calculer le CAC blended chaque mois
**CAC blended = dépense marketing totale / nouveaux clients** (non calculé par les plateformes).
| Scénario (exemple Coudac, 10 000 €/mois) | Meta | Google | Nouveaux clients | CAC blended |
|---|---|---|---|---|
| A | 5 000 € | 5 000 € | 400 | 25 € |
| B | 7 000 € | 3 000 € | 460 | ≈ 21,7 € |
Le mix B est meilleur quelles que soient les conversions revendiquées. « C'est votre CAC blended qui mesure la qualité de votre mix marketing. »
- Question : compare-t-on des mois comparables (saisonnalité, promos, événements) ? Sinon, annoter les biais (voir `lecture-de-compte-hierarchie-gold-bronze.md`).

### 3. Ajouter le questionnaire post-achat
« Où avez-vous entendu parler de nous ? », avec tous les canaux où la marque est présente. Comparer la **part de clients** venue de chaque canal à la **part de budget** investie.
- Biais à connaître (déduction de la fiche) : mémoire du client, ordre des réponses, Meta sous-déclaré quand l'acheteur répond « Instagram » ou « Google ».

### 4. Calculer la valeur à un an créée par la pub
1. Séparer les ventes d'une campagne en nouveaux et existants.
2. Valeur = (nouveaux × valeur à un an d'un nouveau) + (existants × valeur à un an d'un existant).
3. ROI à un an = valeur / dépense.
4. Comparer au **même CPA** : exemple Coudac (hypothétique), 10 000 € et 400 ventes dans les deux cas ; A (240 nouveaux) = 29 600 € (ROI ≈ 3) ; B (40 nouveaux) = 16 600 € (ROI ≈ 1,7).

### 5. Croiser outils de plateforme et outil tiers (B2B, LinkedIn)
1. Outils de la plateforme : Revenue Attribution Report (pipeline et revenu closed-won par campagne), Conversions API.
2. Outil d'attribution tiers (Dreamdata, Factors, HockeyStack…) pour ne pas surpondérer la plateforme.
3. Réinvestir sur ce qui marche **dans les deux lectures**.

### 6. Mesurer l'effet de halo
1. Après un lancement (TLA, campagne vidéo), surveiller la recherche de marque et les conversions Google.
2. Séparer les leads attribués à Google en « exposés avant à la campagne » / « non exposés ».
3. Comparer leurs taux de conversion dans l'entonnoir.
- Limite : les exposés sont peut-être déjà plus intéressés (biais de sélection). Un test d'incrémentalité est plus solide.

### 7. Arbitrer petit à petit
Ne jamais couper un canal parce qu'il paraît « moins rentable » dans un modèle d'attribution (surtout Meta lu dans un outil favorable au dernier clic). Déplacer le budget par petites touches et observer CAC blended + questionnaire.

## Exemple appliqué (illustratif : marque promue e-commerce, hypothétique)
- Mois 1 : 8 000 € (Meta 6 000, Google 2 000), 320 nouveaux clients → CAC blended 25 €. Questionnaire : 48 % « Instagram/Facebook », 30 % « Google », 22 % « bouche-à-oreille ».
- Mois 2 : on monte Meta à 7 000 €, Google à 1 000 € → 350 nouveaux clients → 22,9 €. On note qu'il n'y a pas eu de promo ni de passage TV ce mois-là.
- Le rapport (`rapporteur`) présente CAC blended et ROI à un an, et cite les ROAS de plateforme **comme des lectures internes**, pas comme la vérité.

## Erreurs fréquentes
- Additionner les conversions revendiquées par chaque plateforme.
- Piloter au ROAS de la plateforme comme s'il était absolu.
- Compter les clients existants comme de l'acquisition.
- Couper un canal sur la foi d'un modèle d'attribution.
- Comparer des mois aux contextes très différents sans annotation.
- Présenter « +20 à 30 % » (LinkedIn) ou « 7 fois moins cher » comme des faits.

## Limite à combler
Ni le CAC blended ni le questionnaire ne disent **quel** canal a créé la valeur. Les méthodes qui isolent l'effet causal (geo-holdout, conversion lift, MMM) ne sont dans aucune des deux sources : **lacune**.

## Agents qui doivent l'utiliser
`analyste-performance` (propriétaire), `strategiste-ads`, `rapporteur`, `analyste-resultats`, `predicteur-performance`, `strategiste-offre` (valeur à un an), `redacteur-newsletter` (réactivation par canaux possédés).

## Voir aussi
`lecture-de-compte-hierarchie-gold-bronze.md` · `plan-d-atterrissage-et-timing.md` · `metriques-appariees.md` · `sequence-tla-message-ad.md`
