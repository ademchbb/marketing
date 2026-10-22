# Sillage : signature d'effets sonores récurrente contre aucune signature

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-sillage-signature-sonore` |
| Statut | en attente de marque |
| Priorité | 6 / 19 · score 4 × 3 × 5 = 60 |
| Marque | une marque dont Sillage produit au moins 6 vidéos (pub ou organique) sur 6 semaines |
| Plateforme | Meta Ads (Reels et fil) pour la mesure ; organique en complément |
| Méthode | test A/B natif de Meta (audiences séparées) + mesure de mémorisation ; Trial Reels pour la rétention |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
Le playbook ABCD de Google fait de l'audio « your superpower » en notoriété, mais pousse la **musique**
(notes sur l'ouverture, nom chanté, jingle) à quatre endroits ; la règle Sillage l'interdit
[fiche:google-abcd-playbook-2022 p. 7, p. 12, p. 22, p. 24-25, enseignement 10]. Le substitut proposé,
**voix off + signature d'effets sonores non mélodique**, est une **déduction non testée** (lacune L2)
[fiche:google-abcd-playbook-2022 framework F]. Personne ne sait si une signature d'effets sonores aide à
reconnaître la marque.

## Hypothèse
Si chaque vidéo de la marque porte la même **signature d'effets sonores** (2 à 3 sons non mélodiques,
toujours les mêmes, calés sur l'apparition de la marque), alors la part des personnes exposées qui
attribuent correctement la vidéo à la marque augmente, parce que la répétition d'un indice sensoriel
distinctif crée un repère de marque (« frequency plus variety », p. 12) sans recourir à la musique.

## Variable testée (une seule)
La **présence d'une signature sonore récurrente** liée à la marque.

## Variantes
- **A (témoin)** : effets sonores synchronisés à l'image, choisis vidéo par vidéo (aucun son ne revient
  d'une vidéo à l'autre). La vidéo n'est **jamais muette** [verif:P02].
- **B** : mêmes vidéos, mêmes effets sonores, **plus** la signature : la même séquence de 2 à 3 effets non
  mélodiques (par exemple souffle, déclic, résonance courte) à chaque apparition du nom ou du logo, dans
  toutes les vidéos de la série.

## Ce qui reste constant
Images, montage, durée, voix off (présente ou absente dans les deux), textes à l'écran, moment
d'apparition de la marque, volume global, ciblage et budget de chaque cellule, période.

## Métriques
- **Principale** : taux de bonne attribution de la marque dans un sondage après exposition (« De quelle
  marque était la vidéo sur [sujet] ? », question ouverte), par cellule. Outil : l'étude de mémorisation
  intégrée de Meta si le compte y est éligible (seuils de budget et libellés **à vérifier**), sinon un
  panel recruté de façon transparente (au moins 30 personnes par variante) exposé dans les conditions
  du test in situ.
- **Secondaires** : temps de visionnage moyen, ThruPlay, coût par mille, recherches de la marque (si
  mesurables).
- **Garde-fou** : commentaires qui trouvent le son « agaçant » ; part d'abandons dans les 2 premières
  secondes.

## Échantillon et durée
- **Série de 3 vidéos minimum par cellule** (l'effet attendu est cumulatif) ; idéalement 6.
- Diffusion sur **3 à 4 semaines**, chaque personne devant voir au moins 2 vidéos de la série.
- Taille minimale : celle exigée par l'outil de mémorisation de Meta, ou 30 répondants par variante
  pour le panel.

## Critère de décision (fixé avant)
- B est adopté comme standard Sillage si le taux de bonne attribution de B dépasse celui de A d'au moins
  **5 points** (et que l'outil Meta, s'il est utilisé, conclut à un écart non nul) **sans** baisse de plus
  de 10 % du temps de visionnage moyen.
- Écart inférieur à 5 points : non concluant ; la signature reste optionnelle, au choix de la marque.
- Si B fait baisser le temps de visionnage de plus de 10 % : rejet, on revient à A.

## Méthode et déroulé
1. `pont-motion-design` commande au studio la signature (non mélodique) et les deux versions de chaque
   vidéo ; validation du caractère non musical par l'utilisateur avant production en série.
2. `strategiste-ads` monte un test A/B natif Meta à deux cellules (audiences séparées), campagne de
   notoriété ou de vue de vidéo ; validation de l'utilisateur sur budget et durée.
3. `predicteur-performance` consigne sa prédiction ; `publicateur` lance après validation.
4. Sondage en fin de diffusion ; `analyste-resultats` conclut.
5. En complément (non décisif) : 2 paires de Trial Reels organiques A/B pour vérifier que la signature ne
   nuit pas à la rétention [veille:instagram règle 9].

## Garde-fous
- **Jamais de musique** : pas de notes, pas de mélodie, pas de logo sonore de quelques notes, pas de
  nom chanté [fiche:google-abcd-playbook-2022 framework F, règles de la zone grise]. En cas de doute sur un
  son, l'utilisateur tranche avant production.
- Couper « add music » et toute musique générée par Meta sur les deux cellules
  [veille:meta-ads règle 8] [fiche:dAJyqo6wnq4 framework J].
- Panel : recrutement transparent, consentement, aucune donnée personnelle inutile ; aucun résultat
  présenté comme un fait général (n petit, une marque).
- Aucune dépense sans validation de l'utilisateur.

## Portée attendue
Si B gagne, la signature sonore devient un élément de la charte de chaque marque produite par Sillage,
et la lacune L2 reçoit une première donnée interne.
