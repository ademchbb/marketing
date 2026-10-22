# Plafond de la campagne de conversion et cercles du marché (froid, tiède, chaud)

> Famille : publicité payante / scaling · Niveau : comprendre pourquoi ajouter du budget ne suffit pas

## Origine
- **Coudac** (Paul), mars 2024 [fiche:qBxEAqZbHVg] :
  - plafond de la campagne de conversion (framework N [44:16]-[46:24]) — **[FONDAMENTAL] pour le mécanisme, [DATÉ 2024] pour la tactique** ;
  - cercles du marché (framework O [46:24]) [FONDAMENTAL].
- Éclairage complémentaire (à manier avec prudence) : Meta décrit son moteur de présélection comme conçu pour un **volume de créatives en forte hausse** et vise plus de **diversité** de candidates [fiche:meta-andromeda]. Le lien « créatives variées = nouvelles audiences » est une **interprétation de praticiens**, absente de cette source (voir `grille-source-deduction-praticiens.md`).
- Fiabilité : 3,5/5. L'exemple chiffré (hausse du CPM de 4 $ à 7 $) est une **hypothèse pédagogique**, pas une loi. Le schéma des cercles n'est connu que par le commentaire oral.

## Problème résolu
On augmente le budget d'une campagne de conversion qui marche, et le CPA se dégrade. Ce n'est pas forcément la créa : Meta ne juge acheteuse qu'**une partie** du marché, fixe à court terme. Plus de budget sur elle fait monter le CPM et la répétition, pas la portée. Pour scaler, il faut **agrandir la part chaude et tiède** du marché, ce qui prend du temps.

## Le mécanisme
1. Une campagne de conversion dit à Meta : « achète des impressions qui vont faire des ventes ».
2. Meta ne juge susceptible d'acheter qu'une partie de la cible.
3. Exemple (hypothétique) : 1 M de personnes ; 20 000 $ à 4 $ de CPM = 5 M d'impressions (répétition 5) ; 100 000 $ à 7 $ de CPM ≈ 14 M d'impressions (répétition ≈ 14) **sur le même million**.

## Les cercles du marché
- Un grand cercle (le marché cible) qui contient une part **tiède** et une part **chaude**.
- Le travail de la pub est d'**étendre ces cercles vers l'extérieur** d'année en année.
- L'année 2, il y a plus de gens chauds et tièdes, donc on peut investir plus **au même CPA**. « C'est parfaitement possible, mais ça prend du temps. »

## Étapes
1. **Surveiller le plafond** à chaque hausse de budget : suivre **répétition** et **CPM** en plus du CPA.
   - Question : la portée augmente-t-elle avec le budget, ou seulement la répétition ?
2. **Diagnostiquer** : CPM et répétition montent sans nouvelle portée → plafond probable (à distinguer d'une fatigue créative ou d'un biais, voir `lecture-de-compte-hierarchie-gold-bronze.md`).
3. **Élargir l'audience jugée acheteuse** :
   - tactique citée par Coudac [DATÉ 2024] : campagnes de **notoriété**, surtout de **vue de vidéo** (« on l'utilise énormément ») ;
   - à vérifier en 2026 (déduction de la fiche) : l'élargissement passe aussi par de **nouvelles créas réellement différentes**, Advantage+ ayant fait de la diversité des créas un levier majeur selon les praticiens.
4. **Mesurer sur des mois**, pas sur le ROAS tracké du mois : « s'émanciper des campagnes de conversion pures » ; suivre CAC blended et recherche de marque (voir `cac-blended-et-mesure-du-mix.md`).
5. **Planifier l'élargissement** dans le plan d'atterrissage (voir `plan-d-atterrissage-et-timing.md`) : une part du budget dédiée à faire grandir les cercles, jugée sur d'autres KPI que le CPA immédiat.

## Exemple appliqué (illustratif : marque promue, Sillage en production créa)
- Campagne de conversion à 300 €/jour : CPA 28 €. Passage à 600 €/jour : CPA 41 €, répétition hebdomadaire de 2,1 à 4,8, portée +12 % seulement → plafond probable.
- Action : 15 % du budget sur une campagne de vue de vidéo avec 3 vidéos Sillage **réellement différentes** (sans musique, effets sonores seulement), plus 2 nouvelles créas en conversion. Hypothèse consignée dans `experiences/predictions.md`, jugée sur 2 à 3 mois (recherche de marque, CAC blended), pas sur le CPA de la campagne vidéo.

## Erreurs fréquentes
- Attribuer toute hausse de CPA à la créa.
- Multiplier le budget sur la même cible en attendant que « l'algorithme trouve ».
- Juger une campagne d'élargissement sur son CPA immédiat.
- Présenter la hausse de CPM de l'exemple comme une loi.
- Croire que la vue de vidéo est le seul levier en 2026 (point daté).

## Agents qui doivent l'utiliser
`strategiste-ads` (propriétaire), `analyste-performance` (répétition, portée, CPM), `pont-motion-design` et `directeur-creatif-visuel` (vidéos d'élargissement), `veilleur-algorithmes` (revérifier la tactique datée), `predicteur-performance`.

## Voir aussi
`lecture-de-compte-hierarchie-gold-bronze.md` · `plan-d-atterrissage-et-timing.md` · `grille-source-deduction-praticiens.md` · `dimensionner-son-marche.md`
