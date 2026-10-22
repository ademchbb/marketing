# Texte principal long contre texte court dans une publicité de réponse directe

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-pub-texte-long-vs-court` |
| Statut | en attente de marque |
| Priorité | 4 / 19 · score 4 × 4 × 4 = 64 |
| Marque | marque avec une offre de conversion traçable (achat, rendez-vous, devis) et une campagne Meta sortie de l'apprentissage |
| Plateforme | Meta Ads (fil Facebook et Instagram) |
| Méthode | outil Creative testing de Meta (pubs à parts égales, sans recouvrement d'audience) |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
- Hopkins : « The more you tell the more you sell », « Tell your full story »
  [fiche:hopkins-scientific-advertising p. 23, p. 41-44] ; Ogilvy : « long copy sells more », un texte
  court trahit le rédacteur qui n'a jamais fait de réponse directe [fiche:Br2KSsaTzUc 00:01:08, 00:04:34].
  Ces deux sources sont des **affirmations** (cas de 1923 non vérifiés, plaidoyer sans donnée) et ne sont
  pas indépendantes (Ogilvy recoupe Hopkins).
- Ben Heath, sur Meta en 2026 : texte principal en **2 phrases, 7 cases**, « We don't want to be writing
  essays » [fiche:dAJyqo6wnq4 00:50, framework I].
- La fiche Ogilvy propose déjà la synthèse « court pour attirer, long pour vendre, et tester »
  [fiche:Br2KSsaTzUc, « Transposition aux formats actuels »].

## Hypothèse
Si le texte principal d'une pub de conversion raconte l'offre en entier (problème, preuve, détails, offre,
garantie réelle, appel à l'action, environ 120 à 200 mots) au lieu de 2 phrases, alors le coût par résultat
baisse, parce que le lecteur qui déplie le texte se qualifie lui-même et arrive sur la page avec ses
objections levées [fiche:hopkins-scientific-advertising p. 23] [fiche:Br2KSsaTzUc 00:01:08].
Prédiction concurrente (Heath) : le texte court gagne, parce que le fil mobile ne laisse pas lire.

## Variable testée (une seule)
La **longueur du texte principal** (champ « primary text »).

## Variantes
- **A (témoin) court** : 2 phrases, les 7 cases de Heath (audience, problème, problème attisé,
  fonctionnalité, bénéfice, rareté réelle s'il y en a une, appel à l'action) [fiche:dAJyqo6wnq4 framework I].
- **B long** : 120 à 200 mots, mêmes idées développées : situation du client, preuve réelle (chiffre
  vérifié, cas client consenti), ce qu'on obtient exactement, appel à l'action. La première ligne (celle
  visible avant « voir plus ») est **identique** à la première phrase de A.

## Ce qui reste constant
Visuel, titre, description, bouton, page de destination, offre, ensemble de pubs (même audience, même
budget, même événement d'optimisation), période. Une seule langue.

## Métriques
- **Principale** : coût par résultat (événement d'optimisation de la campagne).
- **Secondaires** : CTR lien, CPC lien, taux de conversion de la page (UTM distincts par variante),
  qualité des résultats (pour des leads : part de rendez-vous honorés ou de leads qualifiés, relevée par
  la marque).
- **Garde-fou** : signalements et commentaires négatifs sur la pub.

## Échantillon et durée
- Outil Creative testing : les deux pubs reçoivent la même dépense, sans recouvrement d'audience, 30 jours
  au maximum [verif:PA16].
- Minimum : **30 résultats par variante** (maison), ou à défaut une dépense de 4 × CPA cible par variante.
- Durée : 14 à 30 jours. Répéter sur **3 offres ou marques** pour conclure sur la règle générale.

## Critère de décision (fixé avant)
- Une variante gagne un test si son coût par résultat est inférieur d'au moins 20 % **et** si chaque
  variante a atteint le minimum de résultats.
- **Règle générale adoptée** (pour `redacteur-ads`) si la même variante gagne au moins 2 tests sur 3 et
  n'en perd aucun.
- Si la qualité des leads de la variante gagnante est inférieure de plus de 25 % (part de rendez-vous
  honorés), le test est déclaré **non concluant** même si le coût par résultat est meilleur.
- Sinon : non concluant, longueur au choix du rédacteur selon le prix de l'offre (prédiction de travail :
  plus l'offre est chère, plus le long devrait gagner).

## Méthode et déroulé
1. Prérequis : la campagne satisfait l'étape 2 de `2026-10-22-meta-regle-passage-tests-et-budget`.
2. `redacteur-ads` écrit A et B ; `correcteur` et `garde-conformite` relisent les deux.
3. `predicteur-performance` consigne sa prédiction dans `experiences/predictions.md`.
4. Validation de l'utilisateur (textes et budget), puis lancement du Creative testing par `publicateur`.
5. Lecture à la fin du test ; `analyste-resultats` conclut.

## Garde-fous
- Le texte long ne crée **aucune** affirmation nouvelle non vérifiée : chaque chiffre est réel, sourcé et
  daté ; pas de faux témoignage ; rareté et urgence seulement si elles sont vraies [verif:OU04].
- Pas de « satisfait ou remboursé 14 jours » présenté comme un avantage pour une vente en ligne (c'est le
  droit légal) [verif:OG01].
- Relire les variantes générées par Meta (« text improvements ») ou les couper pendant le test, sinon la
  variable n'est plus contrôlée [fiche:dAJyqo6wnq4 framework J].
- Aucune musique ajoutée par Meta sur une pub Sillage [veille:meta-ads règle 8].
