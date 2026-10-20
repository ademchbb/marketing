# Montage court « clarté + vitesse » (clip cutting, plan par phrase, sous-titres courts, zones d'interface)

> Famille : production · Niveau : montage d'une vidéo courte verticale

## Origine
- **Mino Lee** [fiche:AA1LoZwW_2Y 01:22-02:49] :
  - B2, dérushage ; B6, clip cutting à l'image près ; B3, sous-titres ; B4, B-roll ;
  - G, principes visuels « clarté + vitesse » ;
  - I, répertoire de B-roll.
- **Ava Yuergens** : monter sobrement, sous-titres présents mais légers ; illustrer chaque étape par des exemples réels et des enregistrements d'écran ; le montage arrive après hook, script et format [fiche:HzoQgQS8czE playbook 11, 00:20, 00:46].
- **Alex Hormozi** : visuels qui renforcent, visualisation de données [fiche:Jmkq5RLjm0U H.4].
- Fiabilité :
  - 3/5 ;
  - **réglages d'apps datés** (CapCut, InShot, polices, zones d'interface de 2024) : retenir les **principes**, pas les valeurs ;
  - à **exclure** : la musique de fond (droits, sécurité, règle Sillage), l'hyper-cut d'ouverture et le B-roll « aléatoire pour l'authenticité », contraires au style premium.

## Problème résolu
Une vidéo courte « lente » (blancs, plans statiques, sous-titres illisibles ou masqués par l'interface) perd le spectateur en quelques secondes. Ce framework garantit le **rythme perçu** et la **lisibilité** sans surcharge.

## Étapes
1. **Dérushage au mot près** : couper le blanc du début, chaque silence entre les phrases et la pause finale.
2. **Clip cutting à l'image près** : zoomer la timeline jusqu'aux images et supprimer chaque micro-silence (même 0,2 s). On ne gagne que 3 à 4 s, mais le rythme perçu change complètement. Selon Mino, c'est le plus gros levier, devant les effets.
3. **Quelque chose de nouveau à l'écran au moins toutes les 3 s**, et tout blanc de 0,5 s ou plus supprimé (règle empirique).
4. **Un plan par phrase ou demi-phrase**, qui **démarre sur l'action**, jamais sur un plan statique qui « ressemble à une photo ». Le plan **colle au propos** (chiffres → écran, client → client). Zoom lent possible.
5. **Illustrer par des exemples réels** : enregistrement d'écran, avant/après, résultat montré plutôt que dit.
6. **Sous-titres** : une ligne par bloc, environ 4 mots maximum, corrigés (fautes, noms propres), fort contraste, police lisible. **Jamais** dans les zones d'interface (bas, droite, haut) : vérifier les zones actuelles dans `veille/plateformes/`.
7. **Audio** : voix normalisée et parfaitement intelligible ; aucune piste ne déborde de la fin ; **effets sonores** synchronisés au mouvement ; **pas de musique** (Sillage).
8. **Export et publication** : depuis l'app native, au format recommandé par la plateforme (à revérifier).
9. **Boucle** : le dernier plan raccorde avec le premier si possible.

Questions de contrôle :
- Y a-t-il un moment où « rien ne se passe » pendant plus de 3 s ?
- Chaque plan sert-il le propos ?
- Un sous-titre est-il caché par l'interface ?
- La voix est-elle intelligible sans casque ?

## Adaptation Sillage (motion design)
- L'ouverture hyper-cut (plans de moins d'1 s, « stutter ») est **remplacée** par **un seul** effet d'accroche fort (transformation, révélation).
- Pas de B-roll aléatoire : chaque plan sert le message. Courbes easeOut et springs, aucun mouvement linéaire (voir le `CLAUDE.md` de motion-design).
- Texte à l'écran : 3-4 messages par vidéo, environ 5 mots chacun. Les sous-titres ne s'appliquent que s'il y a une voix off.

## Exemple appliqué (illustratif : reel Sillage avec voix off)
Voix off découpée au mot près. Un plan d'animation par phrase, démarré en mouvement. Sous-titres de 3-4 mots au centre-haut, hors des zones d'interface. Pop synchronisé à chaque apparition de texte, whoosh sur la transformation. Aucune musique. Le dernier plan revient au point lumineux du début (boucle).

## Erreurs fréquentes
- Laisser des respirations et des « euh ».
- Des plans statiques.
- Des sous-titres de 2 lignes ou sous les boutons.
- De la musique téléchargée (droits, sécurité, et interdite chez Sillage).
- Des effets partout au lieu d'un moment fort.

## Agents qui doivent l'utiliser
`directeur-creatif-visuel` (brief de montage), `pont-motion-design` (contraintes à transmettre au studio), `scenariste-reel` (un plan par phrase dans le script), `adaptateur-multiplateforme` (zones d'interface par plateforme), `controleur-qualite-marketing`, `veilleur-algorithmes` (mise à jour des zones d'interface et formats).

## Voir aussi
`pre-travail-et-priorites-de-production.md` · `script-educatif-court.md` · `hook-trois-canaux.md`
