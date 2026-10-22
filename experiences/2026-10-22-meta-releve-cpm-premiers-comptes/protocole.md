# Relevé du CPM réel des premiers comptes Meta (étalonnage des prévisions)

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-meta-releve-cpm-premiers-comptes` |
| Statut | en attente de marque |
| Priorité | 3 / 19 · score 3 × 5 × 5 = 75 |
| Type | **relevé d'étalonnage**, pas un test A/B : aucune variable manipulée |
| Marque | toute marque française qui lance sa première campagne Meta |
| Plateforme | Meta Ads (Facebook + Instagram), France |
| Méthode | relevé standardisé sur les 14 premiers jours de chaque nouveau compte |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
Le chiffre d'agence « CPM de conversion à environ 5 € en France » (2024) est contredit : les relevés
2025-2026 donnent une médiane d'environ 8 à 10 $ en France, plus haut pour Instagram et pour les
campagnes de conversion ; la consigne est de prévoir **7 à 12 €** puis de recaler sur les données du
compte [verif:PG03] [fiche:qBxEAqZbHVg]. Sans relevé propre, `predicteur-performance` et les budgets
reposent sur une fourchette de tiers.

## Sources
- [verif:PG03] : 5 € contredit ; partir de 7 à 12 € et recaler dès les premiers jours.
- [fiche:qBxEAqZbHVg 13:23, 44:16-46:24] : le CPM dépend de la qualité de la créa ; il monte quand le
  budget augmente sur la même audience.
- [verif:PA04] [veille:meta-ads §7] : changement de définition du clic et de l'attribution en mars 2026 ;
  les données d'avant et d'après ne sont pas comparables telles quelles.
- [veille:meta-ads règle 6] : chaque rapport indique le réglage d'attribution utilisé.

## Hypothèse (prédiction à confirmer ou corriger)
Si l'on prévoit le CPM d'un premier compte français en objectif de conversion avec la fourchette 7 à 12 €,
alors le CPM médian observé sur les 14 premiers jours tombera dans cette fourchette pour au moins 2 comptes
sur 3, parce que les relevés de marché 2025-2026 placent la médiane France vers 8 à 10 $ [verif:PG03].

## Ce qui est mesuré (pas de variable testée)
Pour chaque compte, sur les jours 1 à 14 après la première diffusion :
- **Principale** : CPM médian journalier, toutes plateformes confondues.
- **Ventilation** : CPM par plateforme et placement (fil Facebook, fil Instagram, Reels, Stories), par
  objectif (Sales, Leads), et par semaine (semaine 1 contre semaine 2).
- **Contexte obligatoire** : secteur, objectif et événement d'optimisation, budget quotidien, zone et
  âge ciblés, format des créatives, réglage d'attribution, période (vacances, soldes, fêtes), statut
  d'apprentissage.
- **Secondaires** (pour la chaîne de transmission [fiche:qBxEAqZbHVg 16:40]) : CTR lien, CPC lien, taux de
  conversion de la page, coût par résultat, fréquence.

## Échantillon et durée
- 14 jours par compte ; **au moins 3 comptes** avant de modifier la fourchette de référence.
- Les comptes en catégorie spéciale (finance, emploi, logement) sont relevés à part [verif:PA07].

## Critère de décision (fixé avant)
- Si **au moins 2 comptes sur 3** ont un CPM médian hors de 7 à 12 €, `predicteur-performance` remplace la
  fourchette par celle observée (minimum et maximum des médianes, arrondis à l'euro), avec la mention
  « relevé interne, n = 3, <dates> ».
- Sinon, la fourchette 7 à 12 € est conservée et marquée « confirmée par n comptes ».
- La fourchette est revue tous les 3 nouveaux comptes ; une fourchette par secteur n'est créée qu'à partir
  de 3 comptes du même secteur.

## Méthode et déroulé
1. Avant lancement : `predicteur-performance` inscrit sa prévision de CPM (fourchette et confiance) dans
   `experiences/predictions.md`.
2. Jours 1 à 14 : `analyste-performance` exporte les données par jour et par placement (API officielle,
   lecture seule) et remplit le relevé dans ce dossier.
3. Jour 15 : comparaison prévision / réel ; après le 3e compte, `analyste-resultats` applique le critère.

## Garde-fous
- Les données d'un client ne sont **jamais publiées** ni citées nommément dans un contenu ; on ne publie
  qu'un agrégat anonymisé, et seulement avec l'accord des marques concernées.
- Ne jamais présenter ce relevé comme une norme du marché : c'est un **étalonnage interne** sur un petit
  nombre de comptes.
- Aucune dépense sans validation de l'utilisateur (le relevé se fait sur des campagnes déjà validées, il
  ne justifie aucune dépense en soi).
- Signaler dans le relevé toute donnée antérieure à mars 2026 (non comparable) [verif:PA04].
