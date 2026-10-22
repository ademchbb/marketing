# Meta Ads : 3 concepts créatifs contre 6 concepts à budget égal

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-meta-volume-concepts-creatifs` |
| Statut | en attente de marque |
| Priorité | 9 / 19 · score 4 × 3 × 4 = 48 |
| Marque | marque dont une campagne Meta de conversion a passé l'étape 2 de la règle interne, et capable de produire 6 concepts distincts |
| Plateforme | Meta Ads |
| Méthode | test A/B natif de Meta au niveau campagne (deux cellules, audiences séparées, budget égal) |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
- Meta présente la diversification créative comme « the best lever to find the most relevant audiences »
  et recommande, pour Advantage+ Sales, « at least 20 diversified ads » et 20 à 30 % du budget en test
  (19/11/2024) ; Meta ne donne **aucun nombre lié à Andromeda** [verif:PA23] [veille:meta-ads §3.1].
- Praticiens : 15 à 20 pubs par ensemble, 8 à 12 concepts par campagne, ou 3 concepts réellement
  distincts si le budget est serré [veille:meta-ads §3.2] [verif:PA25].
- Notre règle de travail pour petit budget, **déduction non testée** : 3 à 5 concepts × 2 à 3 exécutions
  [veille:meta-ads règle 2].
- Ben Heath démarre avec une seule pub à plusieurs variantes [fiche:dAJyqo6wnq4 framework L].
À petit budget, plus de concepts peut diluer la dépense sous le seuil d'apprentissage ; moins de concepts
peut plafonner la portée.

## Hypothèse
Si l'on diffuse **6 concepts** distincts au lieu de 3, au même budget total, alors le coût par résultat
baisse, parce que des concepts différents sur le fond (motivation, frein, persona, situation d'usage)
touchent des sous-audiences différentes [verif:PA23] [veille:meta-ads règle 1].
Prédiction concurrente : à petit budget, 3 concepts gagnent, parce que chaque concept reçoit assez de
dépense pour que le système apprenne [verif:PA01].

## Variable testée (une seule)
Le **nombre de concepts créatifs** dans la campagne.

## Variantes
- **A (témoin)** : 3 concepts × 2 exécutions = 6 pubs.
- **B** : 6 concepts × 2 exécutions = 12 pubs. Les 3 concepts de A font partie des 6 de B (mêmes fichiers).
Un « concept » diffère des autres sur au moins un axe de fond (motivation ou frein d'achat, persona,
situation d'usage, angle) ; une couleur, un mot ou l'ordre des plans ne suffit pas [veille:meta-ads règle 1].

## Ce qui reste constant
Budget quotidien par cellule, objectif et événement d'optimisation, audience (Advantage+ dans les deux),
placements, page de destination, offre, période, réglage d'attribution, structure (1 campagne,
1 ensemble par cellule).

## Métriques
- **Principale** : coût par résultat de la cellule.
- **Secondaires** : nombre de résultats, CPM, portée, fréquence, part de la dépense captée par la meilleure
  pub (concentration), statut d'apprentissage de chaque cellule, note « Creative diversity » si affichée
  (indice seulement, « in development ») [veille:meta-ads §3.1].
- **Garde-fou** : qualité des résultats (leads qualifiés, panier moyen).

## Échantillon et durée
- **Au moins 50 résultats par cellule** (aligné sur [verif:PA01]) ; sinon le test est non concluant.
- Budget : chaque cellule doit pouvoir atteindre 50 résultats en 14 jours, soit environ
  (50 × CPA cible) / 14 par jour et par cellule (calcul à valider par l'utilisateur).
- Durée : 14 à 21 jours, sans modification pendant le test.
- Répéter sur **2 marques** avant d'en faire une règle générale.

## Critère de décision (fixé avant)
- Une cellule gagne si son coût par résultat est inférieur d'au moins **15 %**, avec au moins 50 résultats
  par cellule et, si l'outil A/B de Meta l'affiche, une confiance qu'il juge suffisante (libellé et
  seuil à vérifier à l'écran [verif:PA17]).
- Si B gagne sur 2 marques : la règle de travail passe de « 3 à 5 concepts » à « 6 concepts minimum ».
- Si A gagne : la règle « 3 à 5 concepts » est confirmée pour les petits budgets ; on testera 4 contre 8
  à budget plus élevé.
- Sinon : non concluant, règle actuelle conservée.

## Méthode et déroulé
1. `strategiste-ads` définit les 6 concepts (axes de fond écrits) ; `redacteur-ads`, `directeur-creatif-visuel`
   et `pont-motion-design` les produisent.
2. `garde-conformite` relit les 12 pubs.
3. `predicteur-performance` consigne sa prédiction.
4. Validation de l'utilisateur (créations, budget total des deux cellules, durée).
5. `publicateur` monte le test A/B natif ; lecture à la fin ; `analyste-resultats` conclut.

## Garde-fous
- Aucune dépense sans validation explicite de l'utilisateur.
- Chaque concept respecte l'honnêteté : preuves réelles, pas de faux témoignage, rareté réelle seulement.
- Musique IA et « add music » coupés ; variantes générées par Meta relues ou coupées pendant le test
  (sinon la variable n'est plus contrôlée) [veille:meta-ads règle 8].
- Jamais de musique sur les créations Sillage.
