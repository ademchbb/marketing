# Équipe : organisation (un créateur par plateforme 85/15, chaîne d'assemblage, SOP) et internalisation (agence → interne)

> Famille : équipe · Niveau : structurer la production et décider interne / externe (fiche courte)

## Origine
Ralston, Hormozi et Yuergens décrivent chacun une partie de l'organisation d'une équipe contenu. Ce document fusionne leurs méthodes.
- **Caleb Ralston**, *Build* [fiche:Ch4Sl0POBhU] :
  - F21, allocation 85/15 (un créateur par plateforme) ;
  - F24, chaîne d'assemblage du contenu ;
  - F32, démarrer léger ;
  - F33, grille CDI ou freelance / agence (6 critères) ;
  - F34, recruter selon le stade ;
  - F38, remote ou présentiel (6 facteurs).
- **Caleb Ralston**, *START* : s'organiser avant d'avoir du contenu (arborescence, nommage, Kanban ouvert au talent) [fiche:uJ8Pg6t_iho framework 27].
- **Alex Hormozi**, O, playbook d'internalisation : agence basique → agence avancée avec **contrat d'apprentissage** et deadline → interne → conseil. Il décrit aussi le « cycle d'insanité des agences » [fiche:Jmkq5RLjm0U 01:25-01:33].
- **Ava Yuergens** [fiche:HzoQgQS8czE frameworks 26-28] :
  - process done-for-you ;
  - paliers de monteurs ;
  - SOP « à chaque clic », avec la question « qu'est-ce que je n'ai PAS besoin de faire ? ».
- Fiabilité : 4/5. Les prix d'agences et les résultats (x1,5 avec le modèle 85/15) sont déclaratifs.

## Problème résolu
- Le contenu « vanille » reposté partout par un généraliste.
- La dépendance coûteuse à une agence qui ne transmet rien.
- La production désorganisée, sans responsable par étape.

## Étapes

### 1. S'organiser dès le jour 1
- Arborescence identique par projet ou marque, convention de nommage.
- Tableau Kanban : rushes → à relire → approuvé → à sous-titrer et publier → publié, avec une vue calendrier.
- Le porte-parole ou le client a accès au tableau.

### 2. Chaîne d'assemblage avec un responsable par étape
Idéation → création → montage (optimisé par plateforme) → distribution et engagement → analyse. Le créateur répond lui-même aux commentaires, ou un compte « Team » transparent le fait. L'idéation est souvent le goulot (Ava).

### 3. Un créateur par plateforme (dès 3 monteurs ou plus)
- Classer les plateformes et les monteurs.
- Chacun passe 85 % de son temps en natif sur sa plateforme principale, 15 % en expérimentation sur une secondaire.
- Le même matériau brut sert à tous, avec un point d'entrée différent par plateforme.
- Chacun publie et suit sa plateforme : pas de social media manager généraliste.

### 4. Documenter
Des SOP écrites **et** vidéo, des paliers de difficulté (basique, intermédiaire, avancé) attribués selon le niveau, et la question permanente : « qu'est-ce que je n'ai pas besoin de faire ? ».

### 5. Interne ou externe : la grille des 6 critères
Budget · charge · expertise · vitesse · cohérence de marque (sujets interdits, phrases dangereuses hors contexte) · scalabilité. Le freelance sert à tester une hypothèse (par exemple une plateforme pendant 3-4 mois, avec un playbook en livrable).

### 6. Selon le stade
- Année 0-1 : surtout des freelances et des agences.
- Années 1-3 : on internalise les rôles critiques.
- Année 3 et plus : tout ce qui est critique et à fort volume est interne ; les agences restent pour l'ultra-spécialisé.

### 7. Playbook d'internalisation (Hormozi)
1. Agence basique pour imposer une cadence (3-6 mois).
2. Agence avancée avec un **contrat d'apprentissage de 6 mois** : on paie un supplément pour qu'elle explique le *pourquoi* de chaque décision.
3. Documenter en SOP et co-produire avec l'équipe.
4. Fixer une deadline connue de tous.
5. À parité, passer à un contrat de conseil.
6. Couper à l'amiable quand on n'apprend plus.

### 8. Remote ou présentiel
On classe les 6 facteurs (flexibilité, collaboration, productivité, coût, vivier, culture). Si le modèle est imposé, on emprunte les avantages du modèle opposé.

## Exemple appliqué (illustratif : l'agence d'agents et Sillage)
- La chaîne d'assemblage existe déjà : ce sont les pipelines d'`agents.md`, avec un agent responsable par étape et `adaptateur-multiplateforme` pour le natif par plateforme.
- Les SOP « à chaque clic » sont les définitions `.claude/agents/`.
- Si l'utilisateur engage une agence externe pour une plateforme, le script du contrat d'apprentissage d'Hormozi s'applique (texte complet dans `[fiche:Jmkq5RLjm0U]`, section Scripts).

## Erreurs fréquentes
- Un généraliste « bon partout », donc « nul partout ».
- Une agence sans transmission ni deadline.
- Sur-embaucher avant d'avoir prouvé le ROI.
- Pas de responsable unique par micro-tâche.

## Agents qui doivent l'utiliser
`architecte-agents` (structure de l'agence, un agent = une étape), `adaptateur-multiplateforme` (logique 85/15, natif par plateforme), `strategiste-contenu` (recommandation d'organisation pour une marque cliente), `pont-motion-design` (relation studio / agence), `rapporteur` (décisions interne / externe à soumettre à l'utilisateur).

## Voir aussi
`equipe-recrutement.md` · `equipe-onboarding-et-management.md` · `contenu-pilier-et-cascade.md`
