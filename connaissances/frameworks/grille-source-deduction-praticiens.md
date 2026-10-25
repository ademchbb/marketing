# Grille « ce que dit la source / ce qu'on en déduit / ce que disent les praticiens » (exemple : Meta Andromeda)

> Famille : rigueur / lecture des sources · Niveau : avant de faire entrer une affirmation sur une plateforme dans `principes/` ou chez un client

## Origine
- **Engineering at Meta**, billet sur Andromeda (décembre 2024) [fiche:meta-andromeda], framework E. La fiche montre que des consignes très répandues chez les media buyers (« la créative est le nouveau ciblage », « il faut des dizaines de créatives », « les créatives semblables sont regroupées ou pénalisées ») **ne figurent pas** dans la source qu'on leur attribue.
- Généralisation de la grille à toute source de plateforme (Google ABCD, LinkedIn, etc.) : **déduction** de l'agence.
- Fiabilité de la source d'exemple : 3/5 (5/5 pour comprendre l'architecture ; 2/5 pour les chiffres de performance, affirmations d'éditeur ; 1/5 pour les consignes pratiques, absentes).

## Problème résolu
Une idée circule sur « l'algorithme », on la cite avec la source officielle en référence, et elle devient un principe de l'agence alors que la source ne la contient pas. La grille sépare trois statuts avant toute réutilisation, et oblige à dater et à attribuer chaque chiffre.

## Étapes

### 1. Lister les affirmations qu'on veut reprendre
Une ligne par affirmation, formulée telle qu'on voudrait l'écrire dans un principe ou un livrable client.

### 2. Attribuer un statut à chacune
| Statut | Définition | Règle d'usage |
|---|---|---|
| **Source** | Écrit dans la source, avec repère ([§ …], [hh:mm]) | Citable ; dater ; si c'est un chiffre de l'éditeur, écrire « affirmation de [éditeur] » |
| **Source, prospectif** | Écrit, mais comme une intention ou une projection | Citer comme une intention, jamais comme un résultat |
| **Déduction** | Notre lecture logique de la source | Marquer « (déduction) » ; à valider par un test ou une autre source |
| **Interprétation de praticiens** | Circule dans le métier, absente de la source | À sourcer séparément avant tout usage ; ne jamais l'attribuer à la source |

### 3. Pour chaque chiffre : qui, quand, comment
Éditeur ou tiers ? Date ? Méthode, échantillon, groupe de contrôle publiés ? Sinon : « affirmation d'éditeur, sans méthode publiée ».

### 4. Décider l'usage
- Source → principe possible (avec date).
- Déduction → hypothèse dans `experiences/predictions.md`.
- Interprétation de praticiens → demande à `chercheur-sources` / `verificateur-faits`.

### 5. Revérifier la date
Une source de plateforme vieillit vite (Andromeda : décembre 2024, passages prospectifs). Vérifier l'état actuel avant de bâtir une stratégie dessus (`veilleur-algorithmes`).

## Exemple de référence : Meta Andromeda
| Affirmation | Statut |
|---|---|
| Le système est conçu pour un volume de créatives en forte croissance | **Source** [§ Challenges] [§ Hierarchical indexing to support…] |
| La personnalisation se fait dès le retrieval (présélection) | **Source** [§ Meta's new paradigm] |
| La prochaine version vise plus de diversité de candidates | **Source, prospectif** [§ perspectives] |
| Moins de contraintes de ciblage laisse plus de latitude au modèle | **Déduction** [§ AI development efficiency] |
| Des créatives quasi identiques n'apportent pas de chances supplémentaires | **Déduction** [§ Hierarchical indexing for efficiency] |
| « La créative est le nouveau ciblage » / « créatives variées = nouveau ciblage » | **Interprétation de praticiens**, absente de la source |
| Il faut des dizaines de créatives différentes par campagne | **Interprétation de praticiens**, absente de la source |
| Les créatives trop semblables sont regroupées ou pénalisées | **Interprétation de praticiens**, absente de la source |
| +22 % de ROAS, +7 % de conversions estimées, +6 % de rappel, +8 % d'« ads quality » | **Source**, mais **affirmations d'éditeur** sans méthode ; le +22 % mêle créative et ciblage |

Formulation honnête pour un client (déduction de la fiche) : « Meta indique avoir conçu son moteur de présélection pour un volume de créatives en forte hausse, et vise plus de diversité dans les pubs proposées à chaque personne. Nous testons donc plusieurs créatives réellement différentes. »

## Erreurs fréquentes
- Citer une source primaire pour une idée qu'elle ne contient pas.
- Présenter un chiffre d'éditeur comme un résultat indépendant.
- Oublier la date d'une source de plateforme.
- Transformer une intention prospective en fait.
- Mélanger les statuts dans un même paragraphe sans marquage.

## Agents qui doivent l'utiliser
`verificateur-faits` (propriétaire), `synthetiseur-connaissances` (avant d'écrire un principe), `veilleur-algorithmes`, `strategiste-ads` (argumentaire client), `rapporteur`, `controleur-qualite-marketing`, `consolidateur-fiche` (marquage des statuts dans les fiches).

## Voir aussi
`plafond-de-conversion-et-cercles-du-marche.md` · `audit-des-lacunes-du-compte-pub.md` · `boucle-d-iteration.md`
