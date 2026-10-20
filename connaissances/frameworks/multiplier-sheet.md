# Multiplier sheet (mesure relative à la médiane) et définitions de l'outlier

> Famille : mesure · Niveau : tableau de bord de performance par plateforme et par format

## Origine
Les deux auteurs mesurent la performance de façon **relative**, l'un sur ses propres contenus, l'autre sur ceux des autres. Ce document fusionne leurs méthodes.
- **Caleb Ralston**, *Build* [fiche:Ch4Sl0POBhU] :
  - F22, multiplier sheet [02:59-03:05] : « directionally correct, not scientifically accurate » ;
  - F6 : « If it doesn't change your actions, don't track it » (2 à 4 métriques) [03:07].
- **Ava Yuergens et Jack Neel**, pour les contenus **des autres** [fiche:HzoQgQS8czE framework 1, 00:16] :
  - règle des 5x : vues ≥ 5 × abonnés (Ava) ;
  - ou vues comparées à la moyenne du créateur (Jack, logique ViewStats) ;
  - à mesurer des deux façons.
- **Alex Hormozi** : chez lui, environ 1 short sur 10 devient un outlier 2-3× [fiche:Jmkq5RLjm0U 01:53] (donnée interne).
- Fiabilité : 4/5 pour la méthode. Biais connu : la médiane est calculée sur des posts d'âges différents. Le délai de 11 jours repose sur l'observation que certains contenus décollent vers le 7e jour.

## Problème résolu
Les chiffres bruts ne veulent rien dire sans référence : 50 000 vues, c'est un échec pour un compte habitué à 500 000 et un triomphe pour un compte à 10 000 de médiane. Le multiplicateur rend les contenus **comparables** entre plateformes et dans le temps.

## Étapes

### 1. Extraire l'historique
Par plateforme : les 75 à 90 derniers jours (ou tout l'historique disponible). Données fournies par l'utilisateur ou via les API officielles.

### 2. Calculer la médiane, idéalement par format
Reels, carrousels, statiques, longs. Pourquoi la **médiane** et pas la moyenne : la moyenne est faussée par les gros succès isolés.

### 3. Fixer le benchmark
Cette médiane devient la référence.

### 4. Attendre 11 jours, puis calculer le multiplicateur
Multiplicateur = performance / médiane. Exemple : 150 000 / 100 000 = **1,5x**.

### 5. Choisir la métrique mesurée
Les vues, mais aussi (surtout pour une offre premium) les leads, les sauvegardes ou les partages, selon les 2 à 4 métriques retenues (voir `metriques-appariees.md`).

### 6. Exploiter
- Partager la feuille avec l'équipe ou les agents.
- Un contenu à **3x ou plus** se teste ailleurs (voir `decliner-un-contenu-gagnant.md`).
- Les contenus en dessous de 1x répétés signalent un format à sortir du 70 % (voir `regle-70-20-10.md`).

### 7. Recalculer chaque mois
La barre monte toute seule. Pour YouTube, des outils le calculent déjà (1of10, ViewStats).

### 8. Pour la veille (contenus des autres)
Noter pour chaque contenu repéré le ratio vues/abonnés (≥ 5x) **et** le ratio vues/moyenne du créateur.

Questions à chaque mise à jour :
- Le multiplicateur d'un contenu change-t-il une décision ? Si non, cette métrique ne sert à rien.
- Le gagnant l'est-il sur la métrique business ou seulement sur les vues ?

## Exemple appliqué (illustratif : Sillage)
| Plateforme / format | Médiane 90 j (vues) | Post | Vues à J+11 | Multiplicateur |
|---|---|---|---|---|
| LinkedIn / vidéo native | 2 000 | Avant/après client A | 7 000 | 3,5x → décliner sur Instagram |
| Instagram / reel | 1 200 | Décodage Linear | 1 000 | 0,8x |

Les chiffres sont fictifs, pour illustrer le calcul.

## Erreurs fréquentes
- Utiliser la moyenne.
- Juger à J+1.
- Mélanger les formats dans une même médiane.
- Suivre 15 métriques.
- Prendre le multiplicateur pour une vérité scientifique.
- Ne jamais recalculer la médiane.

## Agents qui doivent l'utiliser
`analyste-performance` (propriétaire de la feuille), `analyste-resultats`, `predicteur-performance` (prédire en multiplicateur), `chasseur-viraux` (ratios des autres), `concepteur-experiences`, `rapporteur`.

## Voir aussi
`analyse-top-vs-bottom.md` · `metriques-appariees.md` · `recherche-d-outliers.md`
