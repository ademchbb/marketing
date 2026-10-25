# SOP de stratégie créative publicitaire : la couche avant le format, 5 livrables, plan trimestre → mois, question de contrôle

> Famille : publicité payante / stratégie créative · Niveau : onboarding d'une marque, avant toute production de pubs

## Origine
- **Dara Denney**, *How I Build an Elite Creative Strategy for a Brand in One Sitting* [fiche:yRgPbqywUJ8] :
  - « Real strategy lies in the layer before format selection » (enseignement 1 [00:00] [11:27] [12:01]) ;
  - la SOP de recherche et ses 5 livrables (framework A [00:31]-[01:04] [09:14]) ;
  - planification trimestrielle → mensuelle (framework H [15:21]-[16:27]) ;
  - la question de contrôle finale (framework J [20:52]-[21:57]).
- Horodatages au format [mm:ss].
- Fiabilité : **3/5**. Excellente valeur méthodologique, mais **aucun résultat mesuré** : les cas Grüns, Oats Overnight et Rhode sont des **propositions d'audit**, Grüns n'a jamais été cliente. Vidéo sponsorisée (Storyblocks). Le prompt persona, le PDF interne et le document concurrents ne sont pas transmis.
- Périmètre : marques produit **DTC sur Meta**, surtout problème → solution. Moins direct pour le B2B, les services, l'organique pur.

## Problème résolu
Sans recherche, le stratège retombe dans « What did our competitors do? They must know something that we don't », copie l'Ad Library ou décline un seul angle dans « a whole bunch of different formats » jusqu'à l'essoufflement. La SOP pose d'abord la **couche avant le format** : personas, piliers (angles), tendances de plateforme, et la relie à ce que l'entreprise veut accomplir ensuite.

## La couche avant le format (3 éléments)
1. **Personas** : cible-t-on les bonnes personnes ?
2. **Piliers ou angles** : les grandes douleurs qui déclenchent l'achat (« big pillar ideas », pas des concepts).
3. **Tendances de plateforme** : macro, pas des formats (EGC, coulisses, partnership ads).

## Étapes

### 1. Interdire le point de départ « concurrents »
L'Ad Library peut alimenter le document concurrents (livrable 4), jamais servir de base. Même filtrée par impressions.
- Question : notre première idée vient-elle d'une pub concurrente ? Si oui, revenir à la recherche.

### 2. Ouvrir la SOP de la marque (document vivant, 5 livrables)
| # | Livrable | Méthode | Statut de la source |
|---|---|---|---|
| 1 | Analyse de réputation | manuelle, la plus stratégique | détaillée (voir `analyse-de-reputation-et-minage-d-avis.md`) |
| 2 | Feuille de minage d'avis | export + verbatims manuels | détaillée (même fiche) |
| 3 | Analyse IA des avis | grille de 5 questions | détaillée (même fiche) |
| 4 | Document concurrents | — | **cité, jamais détaillé** |
| 5 | Deck personas | IA, revu en équipe | prompt non transmis (voir `prompt-decouverte-personas.md`, notre version) |

Chaque livrable devient un **document de contexte** chargé dans le LLM pour l'étape suivante.

### 3. Auditer l'offre avant la pub
Pour le produit prioritaire : promesse, transformation, preuves, caractéristiques, bénéfices, **possibilités de bundles**. Si le panier moyen est bas (≈ 20 $), proposer un bundle problème → solution **avant** d'investir.
- Règle « impossible de vendre un produit à 20 $ sur Meta » : **opinion absolue** de Denney ; dépend de la marge, du CPA, de la récurrence et de la LTV.

### 4. Auditer le compte (s'il existe)
Voir `audit-des-lacunes-du-compte-pub.md` (persona gap, awareness gap, creative diversity gap, planning gap).

### 5. Fixer la couche avant le format
- 2 à 3 angles piliers par persona prioritaire (règle d'agence), chacun décliné sur plusieurs niveaux de conscience, plus les tendances de plateforme à exploiter.
- Transformer les objections en angles (voir `objection-vers-angle.md`).

### 6. Planifier : trimestre → mois → semaine
1. **Trimestre** : lancements produits et périodes où attaquer chaque persona.
2. **Mois** : feuille de route stratégique (personas, angles, niveaux de conscience, créateurs, paris plus audacieux).
3. **Semaine** : la production découle du plan, au lieu de « churn and burn every single week ».
- Question : le plan laisse-t-il de la place à des « much bigger swings » (format, type de contenu, créateurs) ?

### 7. Contrôler chaque brief par écrit avant production
- Pourquoi cette créa ? Pourquoi ce persona ? Pourquoi cet angle ?
- Quelle lacune veut-on combler ?
- Quel nouveau persona veut-on cibler pour atteindre des audiences nouvelles ?
- Quel angle « big idea » sera plus rentable en paid social que sur une autre plateforme ?
- Nuance : parfois la lacune **est** un format (Rhode n'avait aucune partnership ad). C'est légitime quand le format comble une lacune identifiée.

### 8. Juger sur plusieurs cycles
« A single creative test or even a handful of tests is not going to be able to tell you hey do we have the right strategy or not. » Le critère de Denney (« la stratégie se reflète dans l'organique ») est **vague** : pour l'agence, consigner les prédictions dans `experiences/predictions.md` et suivre le pipeline « Apprendre de ses résultats ».

### 9. Conformité des angles sensibles
Santé, « arnaque », exclusion, attributs personnels : `garde-conformite` avant production.

## Exemple appliqué (illustratif : marque promue DTC fictive « thé fonctionnel »)
- Livrables 1-3 : objections dominantes = « est-ce que ça marche vraiment ? » et « trop cher pour du thé ». Déclencheur d'achat récurrent : « je ne voulais plus de café l'après-midi ».
- Offre : panier moyen 18 € → proposer un coffret « 30 jours sans café l'après-midi » (bundle problème → solution), décision de la marque.
- Couche avant le format : persona « sevrage café » (3 angles : énergie stable, sommeil, rituel) ; persona « cadeau » (2 angles).
- Plan : trimestre = lancement du coffret en janvier (résolutions) ; mois = 60 % persona sevrage, tests partnership ads avec 2 créateurs.
- Contrôle d'un brief : « Pourquoi ? Persona sevrage sous-représenté (0 créa active), angle sommeil jamais testé, niveau de conscience "problème". »

## Erreurs fréquentes
- Copier l'Ad Library, même « intelligemment ».
- Changer de format chaque semaine en croyant changer de stratégie.
- Produire avant d'avoir audité l'offre (panier trop bas).
- Sauter la revue humaine des sorties IA.
- Juger la stratégie sur un seul test.
- Citer les cas Grüns / Oats / Rhode comme des pubs gagnantes (ce sont des propositions).

## Agents qui doivent l'utiliser
`strategiste-ads` (propriétaire), `redacteur-ads` (angles par persona et niveau de conscience), `architecte-persona`, `strategiste-positionnement`, `strategiste-offre` (bundle), `ecouteur-audience` (livrables 1 à 3), `analyste-concurrent` (livrable 4, en entrée secondaire), `planificateur-calendrier` (plan trimestre → mois), `controleur-qualite-marketing` (question de contrôle), `garde-conformite`, `predicteur-performance`.

## Voir aussi
`analyse-de-reputation-et-minage-d-avis.md` · `prompt-decouverte-personas.md` · `audit-des-lacunes-du-compte-pub.md` · `objection-vers-angle.md` · `decliner-un-contenu-gagnant.md`
