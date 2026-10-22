# Audit des 4 lacunes d'un compte publicitaire (persona, conscience, diversité créative, planification)

> Famille : publicité payante / stratégie créative · Niveau : audit d'un compte actif (Meta surtout)

## Origine
- **Dara Denney** [fiche:yRgPbqywUJ8] :
  - les lacunes à auditer (framework G [13:09]-[15:55]) ;
  - persona gap (enseignement 5 [09:14] [13:09] [18:40]) ;
  - niveaux de conscience et diversité créative (enseignement 9 [13:41] [14:16]) ;
  - planification (framework H) ;
  - la grille d'audit est une **déduction** de la fiche.
- Les niveaux de conscience sont utilisés **sans être définis** (échelle classique de Schwartz supposée, non citée).
- Fiabilité : 3/5, observations d'audits **non chiffrées**, aucun résultat mesuré.

## Problème résolu
Un compte peut afficher de bons résultats tout en ignorant des personas entiers, en n'investissant que le bas de l'entonnoir et en répétant le même angle sous des formats différents. L'audit rend ces trous visibles et donne la liste de ce qu'il faut produire ensuite.

## Prérequis
- Accès en lecture au compte publicitaire (via l'utilisateur ou une API officielle ; jamais de connexion avec ses identifiants).
- Les personas issus de la recherche (voir `prompt-decouverte-personas.md`) avec leur **volume** et leur **intensité émotionnelle**.

## Étapes

### 1. Taguer chaque créa active
Par **persona**, **angle** et **niveau de conscience** (et, en option, créateur et format).
- Question : peut-on dire pour chaque pub à quel persona elle parle ? Si non, c'est déjà un signal.

### 2. Lacune 1 — Persona gap
Personas de la recherche contre personas réellement ciblés.
- Questions :
  - Des personas jamais ciblés ?
  - Des personas sur-représentés alors qu'une plus grosse opportunité (volume ou intensité) existe ?
  - Des clients « hors cible » satisfaits qui signalent un persona à ouvrir ?

### 3. Lacune 2 — Awareness gap
Répartition des créas par niveau de conscience.
- Observation de Denney : les meilleures pubs sont souvent très bas d'entonnoir et centrées sur l'offre. Remède proposé : produire plus de **haut d'entonnoir**.
- Question : quelle part de la dépense va aux prospects qui ne connaissent ni le problème ni la marque ?

### 4. Lacune 3 — Creative diversity gap
- Cible de couverture : plusieurs personas × **2 à 3 angles piliers** par persona (règle d'agence) × plusieurs niveaux de conscience. « That's not concepts. These are just big pillar ideas. »
- Programme créateurs diversifié : style de vie, genre, âge, métier, « vibe ».
- Formats à fort potentiel absents (exemple de Denney : aucune partnership ad chez Rhode au moment de l'analyse).
- Question : combien d'angles **réellement différents** tournent, une fois les variantes cosmétiques regroupées ?

### 5. Lacune 4 — Planning gap
Le compte est-il piloté au sprint hebdomadaire sans plan trimestriel ? Voir `sop-strategie-creative.md`, étape 6.

### 6. Remplir la grille et prioriser
| Persona (recherche) | Volume | Intensité émotionnelle | Créas actives | Angles couverts (cible 2-3) | Niveaux de conscience couverts | Créateurs |
|---|---|---|---|---|---|---|
| … | … | … | … | … | … | … |
- Prioriser : persona à forte opportunité et zéro créa > angle manquant sur un persona cœur > niveau de conscience manquant > format absent.
- Méthode associée : décliner la meilleure créa existante pour chaque persona cœur (voir `decliner-un-contenu-gagnant.md`, axe « par persona »).

## Exemple appliqué (illustratif, hypothétique)
| Persona | Volume | Intensité | Créas actives | Angles | Conscience | Créateurs |
|---|---|---|---|---|---|---|
| Actifs pressés le matin | 38 % | 2 | 14 | 1 (gain de temps) | produit, offre | 3 femmes 25-35 |
| Rassasiement jusqu'au déjeuner | 21 % | 4 | 0 | 0 | — | — |
| Parents qui préparent les petits-déjeuners | 12 % | 3 | 2 | 1 | offre | 1 |
Lacunes : persona « rassasiement » à ouvrir (3 angles) ; 0 créa en conscience « problème » ; créateurs peu diversifiés ; aucune partnership ad.

## Erreurs fréquentes
- Compter les variantes cosmétiques comme des angles différents.
- Auditer sans personas issus de la recherche (on compare le compte à lui-même).
- Conclure « il nous manque un format » sans lacune identifiée derrière.
- Basculer tout le budget vers le haut d'entonnoir sans mesure (la valeur du haut d'entonnoir reste à vérifier, voir Tension).

## Tension à connaître
Denney recommande plus de haut d'entonnoir en publicité ; Hormozi conteste que le contenu divertissant fasse basculer vers l'achat (en organique) [fiche:Jmkq5RLjm0U]. Terrains différents ; à trancher par test (`concepteur-experiences`).

## Agents qui doivent l'utiliser
`strategiste-ads` (propriétaire), `analyste-performance` (tags et répartition de la dépense), `architecte-persona`, `redacteur-ads` (angles manquants), `prospecteur-collaborations` (diversité des créateurs), `concepteur-experiences`, `planificateur-calendrier`.

## Voir aussi
`sop-strategie-creative.md` · `prompt-decouverte-personas.md` · `objection-vers-angle.md` · `matrice-depense-cpa.md` · `grille-source-deduction-praticiens.md`
