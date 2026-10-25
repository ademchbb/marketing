# Architecture du choix : changer le contexte de décision plutôt que sermonner (nominatif, compétition visible, défaut, affichage côte à côte)

> Famille : comportement / offre · Niveau : faire adopter un comportement (achat d'une option, inscription, geste citoyen, bon usage) en modifiant la façon dont le choix se présente

## Origine
- **Dave Trott** [fiche:rl3SELihHqs] : architecture du choix et option par défaut (framework I [00:15] [00:40]-[00:44], enseignement 7) : « human understanding turned to business advantage » ; renoncer au sermon ; rendre **nominatif** (le prénom de chaque enfant sur l'emballage d'une confiserie du Kent) ; rendre la **compétition sociale visible** (le tableau des collèges d'un caviste d'Oxford) ; **inverser l'option par défaut** (don d'organes à Singapour : « We'll make that laziness work for us ») ; personnaliser la relation avec le décideur (Don Revie et l'arbitre).
- **Rory Sutherland** [fiche:lhlS-Wds02M] : l'affichage côte à côte et la valeur relative (framework H [00:15]-[00:16]) : ne pas forcer le choix de gamme avant d'avoir montré les prix ; un supplément paraît petit à côté d'un prix de base élevé (1 300 contre 1 500), grand à côté d'un prix bas (200 contre 500).
- **Robert Cialdini** [fiche:_hem3-8XbEI] : l'engagement actif, écrit par la personne (voir `demande-de-conseil-relation-et-engagement-actif.md`).
- **Doublon fusionné** : Trott et Sutherland parlent tous deux d'économie comportementale appliquée au contexte de décision ; Trott donne les leviers sociaux, Sutherland le levier d'affichage.
- **Correction indispensable** (`connaissances/verifications/registre.md`, passe 4) : Singapour présume bien le consentement depuis le *Human Organ Transplant Act* de 1987 ([verif:V4A-T06] ✅), mais **« they've got all the organs they need » est faux** : 7 à 9 donneurs décédés par million d'habitants et environ 9 ans d'attente pour un rein vers 2015 ([verif:V4A-T07] ❌). **Une option par défaut change un comportement déclaré ; elle ne garantit pas le résultat final.** Confiserie du Kent, caviste d'Oxford, Leeds United : anecdotes ❓ ([verif:V4A-T17]). Sutherland : « +10 M£ par an pour 25 000 £ d'UX », non sourcé.

## Problème résolu
Les panneaux, les reproches et les pubs incitatives changent peu les comportements. Observer la cause réelle (paresse, anonymat, esprit de compétition, comparaison) et modifier le contexte du choix coûte souvent moins cher et marche mieux. Mal utilisé, le même levier devient un piège (case pré-cochée, défaut payant) : la méthode inclut ses limites.

## Étapes

### 1. Renoncer au sermon
Lister les messages « faites ceci, ne faites pas cela » et suspendre leur production le temps de l'analyse.

### 2. Observer le comportement réel et sa cause
- Questions : que font les gens, concrètement, au moment du choix ? Pourquoi (paresse, anonymat, peur de se tromper, comparaison, envie de gagner) ? Que voient-ils à ce moment-là ?

### 3. Choisir le levier
| Levier | Quand | Procédure | Limite |
|---|---|---|---|
| **Rendre nominatif** | Le mauvais comportement profite de l'anonymat | Le nom ou l'identité de la personne sur l'objet ou l'action | Données personnelles : base légale, discrétion |
| **Compétition sociale visible** | La cible est compétitive, appartient à des groupes | Tableau, classement, compteur **réel** par groupe | Chiffres vrais, pas de classement truqué |
| **Inverser le défaut** | La paresse empêche un bon choix **pour la personne** | Le bon choix devient le défaut, **transparent et réversible en un geste** | Jamais pour un paiement, un consentement ou une option payante |
| **Affichage côte à côte** | On vend des gammes ou des options | Montrer toutes les options et leurs prix **ensemble**, avant de demander de choisir | Prix exacts, pas de fausse option « leurre » |
| **Personnaliser la relation avec le décideur** | Un tiers arbitre (acheteur, jury, partenaire) | Connaître la personne et la saluer par son nom, sincèrement | Jamais de pression ni d'avantage indu |

### 4. Écrire le défaut ou le contexte proposé, et son « envers »
Relire du point de vue de la personne : le choix reste-t-il libre, visible, réversible ? L'aide-t-il à faire ce qu'elle veut vraiment ? (Garde-fou de Cialdini, `controle-ethique-d-une-campagne.md`.)

### 5. Mesurer le résultat final, pas seulement le comportement déclaré
La leçon de Singapour : le taux d'inscription change, le résultat (organes disponibles) peut ne pas suivre. Mesurer ce qui compte vraiment (achats conservés, usages réels, satisfaction), pas seulement le taux d'acceptation.

## Exemple appliqué (illustratif : page de prix d'une marque promue)
- Comportement : 80 % choisissent l'offre de base sans voir les autres (choix forcé à l'étape 1 du parcours).
- Levier : affichage côte à côte des trois offres avec ce que chacune contient ; aucune n'est présélectionnée.
- Envers : rien de pré-coché, l'option « accompagnement » s'ajoute par un geste explicite.
- Mesure : part de l'offre intermédiaire **et** taux de remboursement à 30 jours (ne pas « gagner » par des achats regrettés).
- Communauté : un tableau mensuel réel « projets publiés par les membres, par ville », pour l'esprit de compétition, sans classement individuel.

## Erreurs fréquentes
- Citer Singapour comme preuve de l'efficacité totale d'un *nudge*.
- Mettre un paiement ou un consentement « par défaut ».
- Un classement ou un compteur inventé.
- Une option leurre au prix fictif pour pousser l'option chère.
- Mesurer l'acceptation sans mesurer le résultat.

## Garde-fous (honnêteté et conformité)
- **Paiement supplémentaire** : consentement exprès ; une option payante acceptée par défaut est remboursable ([verif:OU07]).
- **Consentement** (prospection, cookies) : jamais de case pré-cochée ([verif:JP07]).
- **Chiffres affichés** (classements, inscrits, places) : réels ([verif:OU03], [verif:OU06]).
- **Prix comparés** côte à côte : exacts et complets ; une réduction affichée suit la règle des 30 jours ([verif:OP01]).

## Agents qui doivent l'utiliser
`strategiste-offre` (pages de prix, options), `gestionnaire-communaute` (compétition visible), `strategiste-contenu` (campagnes de comportement, causes), `developpeur-outils` (parcours sans pré-cochage), `concepteur-experiences` (mesure du résultat final), `garde-conformite` puis `garde-offres`, `controleur-qualite-marketing`.

## Voir aussi
`demande-de-conseil-relation-et-engagement-actif.md` · `presenter-l-information-dans-l-unite-du-client.md` · `recadrer-le-probleme-en-amont.md` · `pre-suasion-le-moment-d-avant.md` · `upsell-downsell-et-escalier-de-paiement.md` (menu, ancre)
