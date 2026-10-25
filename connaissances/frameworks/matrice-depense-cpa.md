# Matrice dépense × CPA (« Creative Data Center ») : couper, pousser, winner, erreur de media buying

> Famille : publicité payante / créa · Niveau : tri hebdomadaire des créas d'un compte

## Origine
- **Coudac** (Paul), mars 2024 [fiche:qBxEAqZbHVg] : framework J [35:03] [35:36] [36:39], enseignement 7 [09:39] [10:11] [13:23] [34:59] [35:03]. [FONDAMENTAL].
- « Creative Data Center » : outil **interne** de Coudac, nom exact non confirmé par la transcription. Le schéma n'a pas été transcrit : seuils et axes gradués **inconnus**, la matrice est reconstruite à partir du commentaire oral.
- Fiabilité : 3,5/5 ; aucune donnée publiée.

## Problème résolu
On coupe une créa trop tôt, ou on laisse tourner trop longtemps une créa qui coûte cher. La matrice croise **combien on a investi** sur la créa et **ce qu'elle a coûté par résultat**, pour décider vite et de façon cohérente.

## Prérequis
- La **mesure par créa** (nommage, UTM, rapports par pub).
- Des créas qui méritent l'interruption : Meta touche une audience **non intentionniste** ; sans contenu intéressant, « ils vont juste vous zapper en 2 secondes ».

## La matrice
| | CPA bon (bas) | CPA mauvais (élevé) |
|---|---|---|
| **Dépense forte** | **Winner** | **Erreur de media buying** : il fallait couper plus tôt |
| **Dépense faible** | **Pousser** : augmenter la dépense pour voir si le CPA tient à l'échelle | **Couper** : pas de potentiel |

## Étapes
1. **Fixer les seuils** avant de lire (la source ne les donne pas) : « CPA bon » par rapport au plancher du plan d'atterrissage (voir `plan-d-atterrissage-et-timing.md`) ; « dépense forte » par rapport au budget de la campagne.
   - Question : les seuils sont-ils écrits **avant** de regarder les résultats ?
2. **Placer chaque créa** de la période dans un quadrant.
3. **Garde-fou avant de couper** : l'attribution d'une vente à une créa est floue. Une créa peut avoir **un bon CPC mais un mauvais CPA** : vérifier le CPC avant de couper.
   - Question : le CPA est-il calculé sur assez de conversions pour être lu ? (Seuil non donné par la source : à fixer dans `experiences/`.)
4. **Agir** : couper tôt les peu diffusées à CPA élevé ; pousser les peu diffusées à bon CPA ; protéger les winners ; analyser chaque « erreur de media buying » pour couper plus tôt la prochaine fois.
5. **Renouveler** : les winners finissent par s'user ; les leçons du quadrant winner alimentent les nouvelles créas (voir `decliner-un-contenu-gagnant.md`).

## Exemple appliqué (illustratif, hypothétique)
Plancher : CPA ≤ 30 €. Dépense forte : > 15 % du budget de la campagne sur la semaine.
- Vidéo Sillage « point → fenêtre produit » : 22 % du budget, CPA 24 € → winner.
- Carrousel « 3 erreurs » : 4 %, CPA 19 € → pousser.
- Image « avant/après » : 3 %, CPA 55 €, mais CPC parmi les meilleurs → ne pas couper tout de suite, vérifier la landing.
- Vidéo « témoignage » : 20 %, CPA 48 € → erreur de media buying, couper et noter le seuil de coupure.

## Erreurs fréquentes
- Couper sur le seul CPA sans regarder le CPC.
- Fixer les seuils après coup.
- Laisser une créa chère consommer le budget « pour voir ».
- Juger des créas sur trop peu de conversions.
- Confondre « pas de diffusion » et « mauvaise créa » (Meta peut ne pas l'avoir montrée).

## Agents qui doivent l'utiliser
`analyste-performance` (propriétaire), `strategiste-ads`, `redacteur-ads` et `directeur-creatif-visuel` (leçons des winners), `concepteur-experiences` (seuils de lecture), `pont-motion-design` (nouvelles créas Sillage).

## Voir aussi
`lecture-de-compte-hierarchie-gold-bronze.md` · `audit-des-lacunes-du-compte-pub.md` · `multiplier-sheet.md` · `decliner-un-contenu-gagnant.md`
