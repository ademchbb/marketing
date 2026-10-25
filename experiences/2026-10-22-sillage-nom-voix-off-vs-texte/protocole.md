# Sillage : nom de la marque dit en voix off contre nom écrit seulement

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-sillage-nom-voix-off-vs-texte` |
| Statut | en attente de marque |
| Priorité | 7 / 19 · score 3 × 4 × 5 = 60 |
| Marque | une marque produite par Sillage avec voix off (ElevenLabs ou voix réelle) |
| Plateforme | Meta Ads (Reels et fil) ; YouTube in-stream si la marque y diffuse |
| Méthode | outil Creative testing de Meta pour la diffusion + sondage de mémorisation |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
Le playbook ABCD remplace en action la marque affichée par un nom **chanté** (« FISH-OS ») et valorise la
voix humaine en notoriété [fiche:google-abcd-playbook-2022 p. 12, p. 22, p. 24]. Chez Sillage, le chant
est exclu ; la règle de la zone grise autorise un nom **dit**, même avec un rythme marqué
[fiche:google-abcd-playbook-2022 framework F]. Le style maison est « peu de texte », et le CTA peut être
doublé à l'audio [fiche:google-abcd-playbook-2022 p. 18]. On ne sait pas si dire le nom apporte quelque
chose quand il est déjà écrit.

## Hypothèse
Si le nom de la marque est **prononcé en voix off** au moment où il apparaît à l'écran, alors plus de
personnes exposées l'associent à la vidéo, parce que deux canaux (écrit et oral) portent la même
information [principes:hooks-et-retention H5] et que YouTube et les Reels se regardent majoritairement
avec le son [verif:PA28] [verif:P02].

## Variable testée (une seule)
La **présence du nom de marque dans la voix off**.

## Variantes
- **A (témoin)** : voix off identique, le nom n'est jamais prononcé ; il apparaît à l'écran (logo ou
  carton) aux mêmes moments que dans B.
- **B** : la voix off prononce le nom une fois en ouverture (dans les 5 premières secondes) et une fois à
  la fin, synchronisé avec son apparition à l'écran ; diction nette, rythme marqué autorisé, **jamais
  chanté**.

## Ce qui reste constant
Images, montage, effets sonores, textes à l'écran, durée (B rallonge de moins d'une seconde ; on ajuste
un silence de A pour égaliser), voix et ton, ciblage, budget, période.

## Métriques
- **Principale** : taux de bonne attribution de la marque dans un sondage après exposition (question
  ouverte), par variante.
- **Secondaires** : temps de visionnage moyen, part des vues au-delà de 3 s, coût par résultat si la pub
  vise une conversion.
- **Garde-fou** : abandons dans les 2 premières secondes (un nom trop tôt peut « faire pub » et faire
  partir).

## Échantillon et durée
- 2 vidéos différentes testées chacune en A/B (4 pubs), 14 à 21 jours.
- Taille : celle exigée par l'outil de mémorisation de Meta s'il est disponible (à vérifier), sinon un
  panel transparent d'au moins 30 répondants par variante.

## Critère de décision (fixé avant)
- B devient la règle pour les vidéos Sillage avec voix off si son taux d'attribution dépasse celui de A
  d'au moins **5 points** sur les 2 vidéos, sans hausse de plus de 10 % des abandons à 2 s.
- Si B gagne sur une vidéo seulement : non concluant, on relance sur 2 autres vidéos.
- Si B augmente les abandons de plus de 10 % : on teste ensuite le nom dit **à la fin seulement**.

## Méthode et déroulé
1. `scenariste-reel` adapte le texte de voix off ; `pont-motion-design` fait produire les deux versions
   (même rendu, seule la piste voix change).
2. `predicteur-performance` consigne sa prédiction.
3. Validation de l'utilisateur ; `publicateur` lance le Creative testing [verif:PA16].
4. Sondage en fin de diffusion ; `analyste-resultats` conclut.

## Garde-fous
- **Jamais de musique ni de nom chanté** ; effets sonores autorisés [fiche:google-abcd-playbook-2022
  framework F].
- Voix de synthèse : utiliser une voix autorisée par la licence de l'outil ; ne jamais imiter la voix
  d'une personne réelle sans son accord ; déclarer l'IA si la plateforme le demande
  [veille:meta-ads règle 9].
- Couper « add music » et toute musique générée par Meta [veille:meta-ads règle 8].
- Aucune dépense sans validation de l'utilisateur.

## Lien avec les autres tests
À lancer après ou en même temps que `2026-10-22-sillage-signature-sonore` mais **jamais sur les mêmes
vidéos** : deux variables audio sur un même contenu rendraient les résultats inattribuables.
