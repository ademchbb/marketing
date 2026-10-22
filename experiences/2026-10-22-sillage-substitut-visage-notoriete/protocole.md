# Sillage : substitut au visage humain dans une pub de notoriété contre aucune présence humaine

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-sillage-substitut-visage-notoriete` |
| Statut | en attente de marque |
| Priorité | 15 / 19 · score 3 × 3 × 3 = 27 |
| Marque | marque qui fait une campagne de notoriété ou de vue de vidéo avec des vidéos Sillage (sans visage) |
| Plateforme | Meta Ads (Reels, fil) ; YouTube in-stream si la marque y diffuse |
| Méthode | outil Creative testing de Meta (ou test A/B natif si l'objectif est la notoriété pure) |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
En notoriété, le playbook ABCD fait des humains le levier de connexion (« Make people core to your story »,
gros plan sur un visage) ; la présence humaine décroît le long de l'entonnoir et disparaît en action
[fiche:google-abcd-playbook-2022 p. 13, p. 24, enseignement 9]. Le playbook ne traite pas les pubs sans
visage ; la fiche propose un **substitut** (mains, geste d'usage, réaction d'un personnage animé), en
**déduction non testée** [fiche:google-abcd-playbook-2022 playbook étape 9]. Les vidéos Sillage sont sans
visage par construction.

## Hypothèse
Si une pub de notoriété Sillage montre un **substitut humain** (des mains réelles qui utilisent le produit,
ou un geste d'usage) plutôt que le produit et l'interface seuls, alors le temps de visionnage et la
mémorisation augmentent, parce que « we can't help but be drawn to other humans »
[fiche:google-abcd-playbook-2022 p. 13] et qu'un geste d'usage aide à se projeter.

## Variable testée (une seule)
La **présence d'un substitut humain** à l'image.

## Variantes
- **A (témoin)** : la vidéo Sillage habituelle (produit, interface, motion design), aucune présence
  humaine.
- **B** : même vidéo, mêmes durées de plans ; 2 plans remplacés par les **mêmes actions** montrées avec des
  mains réelles filmées (ou un personnage animé clairement graphique) en train d'utiliser le produit.

## Ce qui reste constant
Durée, ordre des plans, textes à l'écran, voix off, effets sonores, moment d'apparition de la marque,
ciblage, budget, période.

## Métriques
- **Principale** : temps de visionnage moyen (ou part de ThruPlay) rapporté à la durée.
- **Secondaires** : taux de bonne attribution de la marque (sondage, comme dans
  `2026-10-22-sillage-signature-sonore`), coût pour mille, interactions.
- **Garde-fou** : abandons dans les 2 premières secondes.

## Échantillon et durée
- 2 vidéos différentes testées chacune en A/B, 14 à 21 jours, budget égal par variante.
- Seuil : celui de l'outil de mémorisation si utilisé (à vérifier), sinon au moins 10 000 impressions par
  variante pour la métrique de visionnage (maison).

## Critère de décision (fixé avant)
- B devient une option recommandée pour les pubs de notoriété Sillage s'il augmente le temps de
  visionnage moyen d'au moins **10 %** sur les 2 vidéos, sans baisse de l'attribution de marque.
- Si B gagne sur une seule vidéo : non concluant, nouvelle paire.
- Si A gagne ou égale : on garde le motion pur, et la lacune L2 reçoit une donnée « le visage manque peu
  en notoriété pour ce type de marque ».

## Méthode et déroulé
1. `pont-motion-design` commande les deux versions au studio (tournage des mains ou animation du
   personnage) ; validation du rendu par l'utilisateur.
2. `predicteur-performance` consigne sa prédiction.
3. Validation de l'utilisateur ; `publicateur` lance le test.
4. `analyste-resultats` conclut.

## Garde-fous
- **Aucun humain photoréaliste généré par IA présenté comme réel** ; si une image de personne est générée,
  elle est signalée (libellé « AI info » de Meta) [veille:meta-ads règle 9] [veille:instagram règle 13].
  Par défaut : mains réelles filmées, avec l'accord de la personne.
- Aucun faux client, aucun faux témoignage.
- Jamais de musique ; effets sonores seulement.
- Aucune dépense sans validation de l'utilisateur.
