# Règle interne Meta Ads : quand passer de la structure 1/1/1 aux tests, puis comment monter le budget

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-meta-regle-passage-tests-et-budget` |
| Statut | en attente de marque |
| Priorité | 1 / 19 · score impact × facilité × fréquence = 5 × 5 × 5 = 125 |
| Type | règle de décision permanente + expérience de calibration intégrée (taille du palier de budget) |
| Marque | toute marque qui lance sa première campagne Meta (Sales ou Leads) |
| Plateforme | Meta Ads (Facebook + Instagram) |
| Méthode | règle appliquée à chaque compte ; calibration par alternance planifiée tirée au sort |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
Ben Heath fait démarrer en 1 campagne → 1 ensemble → 1 pub à plusieurs variantes, puis renvoie les tests
et la mise à l'échelle à « later down the line », **sans aucun seuil** de budget, de conversions, de durée
ni de résultat [fiche:dAJyqo6wnq4 01:03, 01:06 ; section « Lacunes de la source »]. Sans règle écrite à
l'avance, l'agence déciderait au ressenti, ce que Hopkins et Ogilvy condamnent
[fiche:hopkins-scientific-advertising p. 20] [fiche:Br2KSsaTzUc 00:01:42].

## Sources
- [fiche:dAJyqo6wnq4] : structure 1/1/1, budget quotidien « qui piquerait un peu », Creative testing
  ignoré au début, aucun critère de passage (lacune explicite, étape 14 du playbook).
- [verif:PA01] : environ 50 événements d'optimisation en 7 jours pour sortir de l'apprentissage
  (confirmé, confiance moyenne ; « more of a guide than a hard and fast rule »).
- [verif:PA02] : toute modification importante (créative, ciblage, ajout de pub, forte variation de
  budget, pause de 7 jours ou plus) relance l'apprentissage ; le seuil « budget ±20 % » ne vient que de
  praticiens.
- [verif:PA16] : outil Creative testing, jusqu'à 5 pubs à parts égales, 30 jours au maximum.
- [veille:meta-ads §10, règles 2 à 6 et 16] : 3 à 5 concepts × 2 à 3 exécutions ; nouveau concept si
  « Creative limited » ou « Creative fatigue » ; budget ≥ (50 × CPA cible) / 7 ; incrémentalité avant
  une montée en budget ; critère fixé avant tout test.
- [fiche:qBxEAqZbHVg] : piloter au coût d'acquisition des nouveaux clients, vérifier le CPC avant de couper
  une créa, une campagne de conversion plafonne quand le budget monte sur la même audience (CPM et
  répétition montent).

## Partie 1 : la règle (seuils fixés avant, tous à calibrer)
Les valeurs chiffrées marquées « maison » sont des **choix de conception**, pas des faits sourcés. Elles
seront revues après les 3 premiers comptes (partie 3).

**Étape 0 : avant toute dépense**
1. Pixel + API Conversions + valeur des conversions vérifiés, bon identifiant de pixel ; UTM sur chaque
   pub [fiche:dAJyqo6wnq4 playbook étapes 4 et 11].
2. CPA cible écrit, dérivé d'un objectif de nouveaux clients ou de CA et d'un plancher de rentabilité
   [fiche:qBxEAqZbHVg 42:08-43:43].
3. Budget quotidien de l'ensemble ≥ (50 × CPA cible) / 7 [veille:meta-ads règle 5]. Si c'est hors de
   portée : optimiser sur un événement plus haut dans le tunnel, **après accord de l'utilisateur**.
4. Validation explicite de l'utilisateur sur le budget et la durée.

**Étape 1 : phase 1/1/1**
- 1 campagne, 1 ensemble, 1 pub avec 3 à 5 textes principaux, 3 à 5 titres, 2 à 3 visuels, issus de
  **concepts réellement distincts** [fiche:dAJyqo6wnq4] [veille:meta-ads règle 2].
- **Aucune modification importante pendant 7 jours pleins** [verif:PA02].

**Étape 2 : condition de passage aux tests (toutes requises)**
- (a) l'ensemble est sorti de l'apprentissage, **ou** 14 jours se sont écoulés (maison) ;
- (b) au moins 50 résultats cumulés sur l'ensemble (aligné sur [verif:PA01]) ;
- (c) coût par résultat de la semaine 2 à ±25 % de celui de la semaine 1 (maison : stabilité) ;
- (d) suivi validé : les résultats Meta et l'analytics du site (UTM) divergent de moins de 30 % (maison).
- Si (b) n'est pas atteint au bout de 21 jours : ne pas tester, diagnostiquer d'abord (offre, page,
  événement d'optimisation, budget) et le signaler à l'utilisateur.

**Étape 3 : tester**
- Outil : **Creative testing** dans l'ensemble existant (pas d'ensemble dupliqué) [verif:PA16]
  [veille:meta-ads règle 16].
- Au plus 5 nouvelles pubs, chacune d'un concept différent de la pub en place.
- Critère fixé avant : coût par résultat. Jugement seulement quand chaque pub testée a **au moins
  20 résultats ou une dépense de 3 × CPA cible** (maison).
- Gagnante : coût par résultat ≤ 0,8 × celui de la pub en place. Sinon : non concluant, on garde la pub
  en place.

**Étape 4 : couper une pub**
- Dépense ≥ 2 × CPA cible sans aucun résultat, ou coût par résultat > 1,5 × CPA cible après au moins
  10 résultats (maison).
- Avant de couper, vérifier le CPC et le CTR lien : un CPC normal avec un CPA mauvais pointe vers la page
  ou l'offre, pas la créa [fiche:qBxEAqZbHVg 35:03].
- Statut « Creative limited », « Creative fatigue » ou note « Creative diversity » basse → produire un
  **nouveau concept**, pas une variante [veille:meta-ads règle 3].

**Étape 5 : monter le budget**
- Conditions : coût par résultat ≤ CPA cible sur 7 jours glissants, ensemble hors apprentissage, au moins
  7 jours depuis la dernière modification de budget (maison, aligné sur la fenêtre de [verif:PA01]).
- Palier : voir partie 2 (petit palier par défaut tant que la calibration n'a pas tranché).
- Retour arrière : si le coût par résultat dépasse 1,3 × CPA cible sur les 7 jours qui suivent un
  palier, revenir au budget précédent (maison).
- Au-delà de 2 × le budget initial : demander une mesure d'incrémentalité (attribution incrémentale,
  Conversion Lift ou comparaison du CAC blended) avant le palier suivant [veille:meta-ads règle 6]
  [fiche:qBxEAqZbHVg 26:56-30:13].
- Chaque palier est validé par l'utilisateur avant d'être appliqué.

## Partie 2 : expérience de calibration intégrée (une seule variable)

**Hypothèse** : si l'on monte le budget par paliers de +50 % au lieu de +20 %, alors le coût par résultat
des 7 jours suivants ne se dégrade pas davantage, parce que la règle « ±20 % » ne vient que de praticiens
[verif:PA02] et qu'un budget quotidien piloté au niveau de la campagne absorbe les variations.

- **Variable testée** : la taille du palier de montée de budget.
- **A (témoin)** : +20 % du budget quotidien.
- **B** : +50 % du budget quotidien.
- **Constant** : ensemble, créatives, ciblage, événement d'optimisation, réglage d'attribution
  (noté dans chaque relevé, [verif:PA04]), aucune autre modification dans les 7 jours avant et après.
- **Attribution du palier** : à chaque montée autorisée par l'étape 5, tirage au sort A ou B (alternance
  planifiée aléatoire, consignée avant d'appliquer le changement).
- **Métrique principale** : ratio coût par résultat (7 jours après) / coût par résultat (7 jours avant).
- **Secondaires** : retour ou non en apprentissage, CPM, fréquence, nombre de résultats par jour.
- **Échantillon** : au moins 5 paliers par variante (10 au total), sur au moins 2 comptes. Durée
  estimée : 2 à 4 mois selon le rythme des comptes.
- **Critère de décision (fixé avant)** : B est adopté comme palier par défaut si, sur au moins
  5 paliers B, le ratio médian est ≤ 1,15 **et** au plus 1 palier B déclenche le retour arrière de
  l'étape 5. Sinon, on garde A. Si moins de 5 paliers par variante après 4 mois : non concluant.
- **Biais connus** : saisonnalité et promotions (noter tout événement externe dans le relevé et exclure
  le palier s'il coïncide avec une promotion ou un pic saisonnier), petit nombre de comptes.

## Partie 3 : revue de la règle
Après 3 comptes ou 6 mois, `analyste-resultats` compare chaque seuil maison à ce qui s'est passé (combien
de décisions ont été prises trop tôt ou trop tard) et propose des seuils corrigés. Les seuils officiels
de Meta, s'ils changent (seuil d'apprentissage, outil Creative testing), priment sur ce protocole
[veille:meta-ads §6, §11].

## Garde-fous
- **Aucune dépense, aucun changement de budget, aucune mise en ligne sans validation explicite de
  l'utilisateur**, publication via `publicateur` et API officielle (`CLAUDE.md`).
- Musique IA et « add music » coupés sur toute pub ; variantes générées par Meta relues par
  `garde-conformite` [veille:meta-ads règle 8] [fiche:dAJyqo6wnq4 framework J].
- Rareté, urgence, témoignages chiffrés seulement s'ils sont réels et documentés [verif:OU04].
- Aucune pub sur un sujet social, électoral ou politique dans l'UE ; catégories spéciales déclarées
  [verif:PA07].
- Prévoir jusqu'à 24 h de vérification Meta [verif:PA08].

## Après chaque compte
- Prédiction du coût par résultat de la semaine 1 consignée avant lancement dans
  `experiences/predictions.md` (`predicteur-performance`).
- Relevé des décisions (passage aux tests, coupures, paliers) et résultats dans ce dossier
  (`analyste-performance`, puis `analyste-resultats`).
