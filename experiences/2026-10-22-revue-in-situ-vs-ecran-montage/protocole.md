# Juger une vidéo dans un vrai fil (in situ) contre sur l'écran de montage

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-revue-in-situ-vs-ecran-montage` |
| Statut | en attente de marque |
| Priorité | 5 / 19 · score 3 × 4 × 5 = 60 |
| Type | expérience de **processus** : on teste la méthode de contrôle qualité, pas un contenu |
| Marque | toute marque qui publie au moins 8 vidéos courtes en 4 semaines (Sillage en priorité) |
| Plateforme | Instagram Reels (ou LinkedIn vidéo) |
| Méthode | double classement avant publication, puis comparaison au classement réel (alternance des conditions par lot) |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
Dave Trott : « The one place everybody judges ads is the one place they're never ever going to run, which
is on the boardroom table » ; « Everything only works in context ». Il recommande de maquetter la création
à son emplacement réel, entourée des autres messages [fiche:rl3SELihHqs 00:08, 00:48-00:51, framework K].
La fiche le transpose à Sillage : juger le rendu dans un vrai fil Instagram ou LinkedIn, pas en plein
écran sur un moniteur de montage. C'est une affirmation d'expert, sans donnée.
Aujourd'hui, notre contrôle qualité (`controleur-qualite-marketing`, `simulateur-audience`) juge les
vidéos hors contexte.

## Hypothèse
Si les relecteurs classent un lot de vidéos en les voyant **insérées dans un vrai fil sur téléphone**
(entre des contenus réels) plutôt qu'en plein écran sur l'écran de montage, alors leur classement prédit
mieux le classement réel des vidéos, parce que l'impact se joue face aux « 50 other identical things » du
fil et non dans l'attention payée d'une revue [fiche:rl3SELihHqs 00:50].

## Variable testée (une seule)
Les **conditions de visionnage** pendant la revue avant publication.

## Variantes
- **A (témoin) écran de montage** : chaque vidéo vue seule, en plein écran, avec le son, autant de fois
  que voulu.
- **B in situ** : chaque vidéo vue une seule fois, sur téléphone, insérée dans une maquette de fil
  (vidéo précédente et suivante = contenus réels et récents de la même plateforme, sans lien avec la
  marque), au rythme d'un défilement normal.

## Ce qui reste constant
Les mêmes vidéos, les mêmes relecteurs (au moins 3), la même consigne (« classez de la plus à la moins
performante »), la même grille (impact → compréhension → persuasion [fiche:rl3SELihHqs framework D]).
Chaque relecteur fait **les deux** conditions, dans un ordre tiré au sort, à au moins 48 h d'écart
(pour limiter la mémoire du premier passage).

## Métriques
- **Principale** : corrélation de rang (Spearman) entre le classement d'un relecteur et le classement réel
  du lot, calculé sur le temps de visionnage moyen rapporté à la durée.
- **Secondaires** : même corrélation sur les envois par portée ; réponse à « de quelle marque était-ce ? »
  posée juste après la condition B (taux de bonne attribution) [fiche:rl3SELihHqs playbook étape 10].

## Échantillon et durée
- **3 lots de 8 vidéos** (24 vidéos), au moins 3 relecteurs humains par lot.
- Classement réel lu à 7 jours après publication de chaque vidéo.
- Durée : 6 à 10 semaines selon le rythme de publication.

## Critère de décision (fixé avant)
- B est adopté dans le contrôle qualité si la corrélation moyenne de B dépasse celle de A d'au moins
  **0,2** sur au moins 2 lots sur 3.
- Si A et B sont proches (écart < 0,2) : non concluant ; on garde la revue actuelle et on ajoute seulement
  la question d'attribution de marque.
- Si aucune des deux conditions ne dépasse une corrélation de 0,3 : le jugement humain avant publication
  prédit mal, et l'agence doit s'appuyer davantage sur les tests (Trial Reels) que sur la revue.

## Méthode et déroulé
1. `controleur-qualite-marketing` prépare les lots et la maquette de fil (capture d'écran animée ou
   prototype local ; aucune publication réelle).
2. Les relecteurs classent ; `predicteur-performance` consigne aussi son propre classement dans
   `experiences/predictions.md` (point de comparaison).
3. Les vidéos sont publiées normalement, après validation de l'utilisateur, dans un ordre et à des
   créneaux comparables.
4. `analyste-performance` fournit le classement réel ; `analyste-resultats` calcule les corrélations et
   conclut.

## Garde-fous
- La maquette de fil n'utilise que des contenus publics vus en local, sans les republier ni les diffuser ;
  aucune connexion automatisée avec des identifiants (`CLAUDE.md`).
- Les relecteurs humains (l'utilisateur et toute personne qu'il désigne) donnent leur accord ; aucune
  donnée personnelle collectée hors du classement.
- Les vidéos restent soumises au contrôle qualité habituel : l'expérience ajoute une revue, elle ne retire
  aucun contrôle de conformité.
- Sillage : jamais de musique, y compris dans la maquette (les vidéos voisines sont vues sans le son si
  elles en contiennent, pour ne pas biaiser le jugement de l'audio).

## Limite connue
`simulateur-audience` ne peut pas « voir » une vidéo dans un fil : l'expérience porte sur des relecteurs
humains. Si B gagne, il faudra un agent ou un outil capable de produire la maquette de fil (voir rapport).
