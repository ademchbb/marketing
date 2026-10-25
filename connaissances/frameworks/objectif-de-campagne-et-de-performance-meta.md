# Arbre de décision de l'objectif de campagne et réglage de l'objectif de performance (Meta)

> Famille : publicité payante / Meta · Niveau : niveaux campagne et ad set
> **Interface datée fin 2025 / début 2026 : revérifier les libellés.**

## Origine
- **Ben Heath** [fiche:dAJyqo6wnq4] :
  - « Meta optimise au sens littéral » (enseignement 1 [00:09] [00:10] [00:22] [00:25]) ;
  - Leads ou Sales pour plus de 90 % des débutants (enseignement 2, **opinion**) ;
  - arbre de décision de l'objectif de campagne (framework C [00:09]-[00:13]) ;
  - réglage de l'optimisation au niveau ad set (framework D [00:19]-[00:27]).
- Convergence : Coudac, « la seule vraie mesure est le coût d'acquisition des nouveaux clients » [fiche:qBxEAqZbHVg] (voir `cac-blended-et-mesure-du-mix.md`).
- Fiabilité : 4/5. Sales n'est **pas montré** dans la démo (« very much applies to sales », libellés différents).

## Problème résolu
« Meta's optimization system is very literal. » Si on demande des clics, Meta trouve des gens qui cliquent, pas des gens qui achètent. Et « you can still mess up a good campaign objective selection with a bad performance goal » : c'est l'**objectif de performance**, pas l'objectif de campagne, qui décide de qui voit la pub.

## Étapes

### 1. Partir de la conversion réelle
Quelle est la conversion réelle de l'offre (achat, rendez-vous, devis, appel) ? Est-elle **traçable** sur notre site ?

### 2. Choisir l'objectif de campagne
1. Une app → **App promotion**.
2. Conversion traçable : achat direct en ligne → **Sales** ; rendez-vous, devis, appel avant l'achat → **Leads**.
3. Conversion non traçable (site tiers) → **Traffic**, en dernier recours, **sans Audience Network**.
4. **Awareness** → gros budgets, ou stratégie « omniprésente » pour un service haut de gamme ou d'expertise (seulement mentionnée par Heath, non détaillée).
5. **Engagement** → pas pour un débutant.
- Question : pourquoi pas Leads ou Sales ? (Il faut une raison écrite pour choisir autre chose.)

### 3. Choisir le lieu de conversion (ad set)
- Par défaut « website and instant forms » ; **Website** quand une landing page existe déjà ; **Instant forms** seul sans site ; Messenger, WhatsApp, appels là où ces canaux dominent.

### 4. Choisir l'objectif de performance
- Une offre, prospects de valeur égale → **maximize number of conversions**.
- Offres de valeurs différentes (prospect à 200 $ contre 5 000 $) ou e-commerce → **maximize value of conversions** (ROAS), prérequis : pixel, valeur de chaque conversion remontée, idéalement API Conversions.
- **Jamais** : link clicks, landing page views, daily unique reach, impressions.

### 5. Choisir l'événement de conversion
Vérifier que le pixel est relié au data set ; prendre l'événement **le plus bas du tunnel** (Purchase, Schedule, Lead) **si son volume suffit** pour que Meta apprenne, sinon remonter d'une étape (Add to cart). (Seuil de volume non donné par Heath.)

### 6. Stratégie d'enchère et calendrier
**Highest volume** (défaut) ; pas de cost per result goal ni de bid cap au début. Date de fin facultative (utile pour ne pas oublier une campagne).

### 7. Juger le coût à la qualité exploitable
« Ce qui est moins cher est souvent moins bon » (réservation contre enchère, Audience Network, expansion géographique). Juger un coût par résultat à la **qualité exploitable** du résultat, pas au prix unitaire.

## Exemple appliqué (illustratif)
- Sillage (rendez-vous découverte sur sa page) → **Leads**, lieu **Website**, **maximize number of conversions**, événement **Schedule** si le volume suffit, sinon **Lead** (formulaire de contact).
- Marque promue e-commerce à paniers variés → **Sales**, **maximize value**, événement **Purchase**.
- Marque dont la vente se fait sur une marketplace tierce non traçable → **Traffic** sans Audience Network, en le signalant comme un pis-aller dans le plan (`strategiste-ads`).

## Erreurs fréquentes
- Choisir Trafic « pour avoir du monde sur le site ».
- Un bon objectif de campagne gâché par un objectif de performance « clics » ou « portée ».
- Optimiser sur Purchase avec trop peu d'achats pour que Meta apprenne.
- Maximize value sans valeur remontée.
- Se réjouir d'un coût par lead bas sur des prospects qu'on ne peut pas servir.

## Agents qui doivent l'utiliser
`strategiste-ads` (propriétaire), `analyste-performance` (événements, valeur), `strategiste-offre` (définir la conversion réelle), `veilleur-algorithmes` (libellés).

## Voir aussi
`lancement-meta-structure-1-1-1.md` · `cac-blended-et-mesure-du-mix.md` · `lecture-de-compte-hierarchie-gold-bronze.md`
