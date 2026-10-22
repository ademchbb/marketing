# Le filtre humain sur l'IA de Meta : 4 motifs de rejet et le tableau des 10 « enhancements » (adapté aux règles de l'agence)

> Famille : publicité payante / Meta · Niveau : relecture des variantes IA avant publication
> **Interface et liste d'enhancements datées fin 2025 / début 2026 : revérifier avant usage.**

## Origine
- **Ben Heath** [fiche:dAJyqo6wnq4] : framework J [00:51]-[01:01] [01:02] [01:03] ; enseignement 9 (« Absolutely use it, but you need to be the filter as the advertiser »).
- **Adaptations de l'agence** (signalées dans la fiche, « Conflits avec les règles du projet ») : **couper « add music »** (règle Sillage « jamais de musique ») ; relecture obligatoire de toutes les variantes par `garde-conformite` ; aucune personne réelle de la marque remplacée ou simulée ; rareté et preuves seulement si réelles et documentées.
- Fiabilité : 4/5 pour la démonstration. Ses jugements sur l'effet des enhancements (« ad overlays can often improve performance », « typically don't make a huge amount of difference ») sont des **opinions** sans données. « Une variante absurde ne fait pas réagir, Meta l'apprend et arrête » : **mécanisme supposé**.

## Problème résolu
L'IA de Meta génère des textes, des images et des transformations (texte dans l'image, musique, animation, déplacement de textes). Certaines améliorent la diffusion, d'autres **inventent une personne**, **inventent une promesse**, ou brouillent le message. Une impression trompeuse ou hors charte est déjà un coût, même si Meta finit par l'écarter. Il faut un filtre humain systématique.

## Étapes

### 1. Pour chaque sortie IA : garder, retoucher ou rejeter
Rejeter ce qui :
- **(a)** fait une **promesse que l'offre ne tient pas** (contre-exemple réel : « Unlock ad mastery in five minutes daily ») ;
- **(b)** **remplace ou invente une personne** alors que l'offre repose sur une personne réelle (« It has to actually be me in there ») ;
- **(c)** **brouille le message** ou le rend incohérent ;
- **(d)** promet une **langue ou un service** qu'on ne peut pas livrer.
Ajouts de l'agence : rejeter toute rareté, urgence, preuve ou chiffre **non réels et documentés** ; toute musique.
- Questions :
  - Cette variante dit-elle quelque chose de faux, même légèrement ?
  - Un produit (décor varié : souvent acceptable) ou une personne (risqué) ?

### 2. Régler les enhancements un par un
| Enhancement | Défaut Meta | Choix de Heath | **Réglage agence** (déduction de la fiche) |
|---|---|---|---|
| Enhanced media text (texte IA dans l'image) | off | off | **off** (message clair et constant ; texte non relu) |
| Translate text | off | off | **off** sauf service réellement livrable dans la langue |
| Enhanced CTA | off | off | **off** |
| Ad overlays | on | off (visuel déjà chargé) | **off** par défaut ; à tester sur un visuel léger |
| Visual touch-ups (recadrage, extension) | on | on | on, **vérifier l'aperçu** (personne réelle non altérée) |
| Add music (image → vidéo avec jingle) | on | on | **OFF obligatoire** (règle Sillage) ; vérifier qu'aucune variante n'en ajoute |
| Text improvements (Meta déplace les textes) | on | on | à couper si l'ensemble devient incohérent ; sinon on avec relecture |
| Multi-image format | on | on | on si carrousel ou plusieurs images, aperçu vérifié |
| Animation | on | on | on si l'aperçu reste conforme à la charte |
| Flex media (carré ↔ vertical) | on | on | on, mais préférer des visuels 1:1 et 9:16 dédiés |
« Optimize text per person » : Heath le laisse activé ; pour l'agence, seulement si chaque texte de base a été relu, car les variantes ne seront pas toutes vues avant diffusion.

### 3. Contrôler l'aperçu sur chaque placement
Faire défiler fil Facebook, fil Instagram, Stories, Reels… ; contrôler une à une les variantes d'image générées.

### 4. Faire valider par `garde-conformite`, puis par l'utilisateur
Aucune pub ne part sans ces deux validations ; publication via `publicateur`.

## Exemple appliqué (illustratif : pub Sillage)
- Variantes de titre proposées par Meta : « Une vidéo de lancement en 24 h » → **rejet (a)** (délai non tenu) ; « Votre lancement en un seul moment » → garder.
- Variante d'image où Meta remplace le fondateur par un visage généré → **rejet (b)**.
- Add music : coupé ; vérification dans l'aperçu Reels qu'aucun jingle n'apparaît.
- Ad overlays : off (visuel avec une phrase déjà à l'écran).

## Erreurs fréquentes
- Accepter tous les enhancements par défaut.
- Croire que « le marché corrigera » une variante trompeuse.
- Laisser « add music » activé sur une pub Sillage.
- Ne pas regarder l'aperçu de chaque placement.
- Laisser l'IA inventer une rareté (« places limitées ») qui n'existe pas.

## Agents qui doivent l'utiliser
`garde-conformite` (propriétaire de la relecture), `strategiste-ads`, `redacteur-ads`, `directeur-creatif-visuel`, `pont-motion-design` (aucune musique), `controleur-qualite-marketing`, `publicateur`.

## Voir aussi
`lancement-meta-structure-1-1-1.md` · `pub-reponse-directe-7-cases.md` · `conformite-influence-commerciale.md` (mention « Images virtuelles » pour un visage IA dans un contenu d'influence)
