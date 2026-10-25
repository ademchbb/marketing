# Upsell, downsell et escalier de paiement (menu, ancre, rollover, step-downs)

> Famille : offre / monétisation · Niveau : ce qu'on propose juste après un oui, et juste après un non

## Origine
Deux sources d'Alex Hormozi décrivent les mêmes outils à des époques différentes. Une seule fiche, divergences explicitées.
- **Hormozi, *$100M Money Models*** [fiche:6_CCutkM11g] :
  - upsell : classic, menu, anchor, rollover (framework B2 [00:37]-[00:40]) et règles complémentaires de la Q&A [02:36] ;
  - downsell : payment plan, trial, feature (framework B3 [00:41]-[00:44]) ;
  - cas du tutorat (programme complet + financement + downsell à l'unité, framework C6 [06:31]-[06:33]).
- **Hormozi, *How to Sell Better than 99% Of People*** (compilation, segments 2019-2024 non datés) [fiche:JE2_7elAcxM] :
  - règle de la vente additionnelle ≈ 5× le ticket [03:25:51] ;
  - **sales step-downs** (« everyone buys something ») [03:34:07]-[03:36:50] ;
  - « customers are fractal » (le top 20 % a « 5× le pouvoir d'achat », heuristique) [03:26:24].
- **Doublon fusionné** : le *payment plan downsell* (Money Models) et les *sales step-downs* (vente) sont le même outil, l'un décrit en mécanisme, l'autre en escalier complet.
- Fiabilité : 3,5/5 pour les deux sources. Les chiffres de cas (Prestige Labs 270 k$ → 1,6 M$/mois, Equabody 7 000 $ contre 4 500 $, chaîne esthétique 200 → 800 $ par client) sont des **affirmations** ; **absents du registre** au 2026-10-22.

## Divergence à connaître : combien doit coûter l'upsell ?
| Source | Règle | Contexte |
|---|---|---|
| [fiche:6_CCutkM11g] [02:36] | ≈ **10× la base** (« if your base is $30 a month, your upsell might be like 300, not 97 ») | Abonnement grand public à petit prix (cours en ligne à 30 $/mois) |
| [fiche:JE2_7elAcxM] [03:25:51] | ≈ **5× le ticket actuel** (« if 20 % take it, the average basket doubles ») | Service en boutique à ticket moyen (médecine esthétique, ≈ 200 $) |

Lecture de l'agence (déduction) : ce sont deux **heuristiques dépendantes du contexte**, pas une contradiction. Point commun : une vente additionnelle à 10 % du ticket ne vaut pas la peine (« why bother »). Point de départ proposé : **5×** pour un ticket moyen ou un service, **10×** pour une base à petit prix ; à tester (consigner dans `experiences/predictions.md`). Calcul de contrôle donné par la source 6_CC : 20 % de prise à ~100 $ sur une base à 30 $ ajoute ~+67 % au panier ; 10-20 % de prise à 300 $ ajoutent +100 à +200 %.

## Étapes

### A. Concevoir l'upsell
1. **Partir de ce que le client espère, pas de ce qu'il attend.** « The core offer should be the thing that they expect to get. The upsell should be the thing they hope they get » : accès, formation, personnalisation.
2. **Résoudre un problème révélé par l'achat précédent** (« problem reveal ») ou augmenter la valeur. Voir aussi la pile par chaînage de Brunson dans `offre-quatre-composantes-brunson.md` : Brunson met ces problèmes chaînés **dans la même pile**, Hormozi les **étale dans le temps** en upsell.
3. **Servir d'abord à la main** quelques clients premium pour apprendre leurs vrais problèmes, puis **standardiser** la solution.
4. **Fixer le prix** (voir la divergence ci-dessus), puis calculer prise × prix.
- Questions :
  - Qu'est-ce que le client a découvert qu'il lui manquait **après** avoir acheté ?
  - L'upsell est-il ce qu'il « espère », ou une redite de ce qu'il a déjà ?

### B. Choisir le mécanisme d'upsell
| Mécanisme | Quand | Étapes |
|---|---|---|
| **Classic** | Juste après l'achat (page de confirmation, fin d'appel) | Présenter l'offre suivante au moment où le problème suivant apparaît. « They work without any real sales skills. You just present them. » |
| **Menu upsell** | Plusieurs options possibles, posture de conseil | 1) **désengager** ce dont il n'a pas besoin (« unsell ») ; 2) **prescrire** ce dont il a besoin ; 3) « préférez-vous **A ou B** ? » ; 4) **rendre le paiement facile**. « This thing slays. You have to use it ethically. » |
| **Anchor upsell** | Offre principale perçue comme chère | 1) présenter d'abord une option **très chère et réelle** ; 2) présenter l'offre principale, qui paraît raisonnable |
| **Rollover upsell** | Client en cours de palier | 1) afficher le palier suivant à son prix ; 2) **créditer** ce qui a déjà été payé ; 3) présenter le net ; 4) fixer le prix du palier pour rester rentable **après** crédit ; 5) le proposer **avant la fin** du palier en cours |

- Questions :
  - Dans le menu upsell, a-t-on vraiment retiré quelque chose dont il n'avait pas besoin ? (C'est ce qui crée la confiance.)
  - L'ancre est-elle une offre qu'on vend vraiment, à ce prix ?

### C. Installer un downsell à chaque « non »
Règle : « Anywhere someone can say no, you can and should install a downsell mechanism. » Le downsell change la **structure de paiement**, la **qualité ou la quantité**, ou les **conditions**. Il fait dire oui à **autre chose**, il ne force pas le oui à ce que le client ne veut pas.

| Mécanisme | Principe | Étapes données |
|---|---|---|
| **Payment plan** (« cash flow algorithm ») | « Je ne peux pas payer » → échelonner **sans baisser le prix** | 1) proposer un échelonnement (« what if we did 250 a month for 24 months? ») ; 2) découper le montant (payment chunking) ; 3) « seesaw » : grosse économie au comptant maintenant, ou petites mensualités ; 4) prévoir **comment s'assurer d'être payé** |
| **Trial** | Essai « with a catch » qui écarte les curieux : le client utilise, constate, puis paie | Étapes non données (« awesome for beginners ») |
| **Feature** (« lock and key ») | Retirer ou changer qualités, quantités ou options pour coller au budget ; le rapport prix/valeur n'est pas de 1 pour 1 | Étapes non données |

### D. L'escalier complet des step-downs (« everyone buys something »)
Dans l'ordre, en ne descendant d'une marche qu'après un vrai « non » :
1. **Prépaiement** (avec la remise de prépaiement, voir `presenter-le-prix-en-rendez-vous.md`).
2. **Financement par un tiers** ou par carte.
3. **Paiement partiel**, avec une remise plus faible.
4. **Plan de paiement** calé sur le rythme de livraison (passage possible au récurrent : `continuite-et-revenu-recurrent.md`).
5. **En dernier recours, réserver la prochaine séance** (devenu automatique pour tous dans le cas de la chaîne esthétique).
- Variante 6_CC (tutorat vendu à l'heure) : mesurer le nombre d'unités au-delà duquel les clients obtiennent le résultat (statistique **maison**, collectée sur ses propres clients) ; en faire l'offre principale (pack complet) ; ajouter un partenaire de financement ; garder l'unité en downsell de dernier recours. L'exemple « 89 % se sentent prêts à 50 h » est **inventé** par l'auteur pour l'illustration.
- Questions :
  - Chaque marche est-elle une offre qu'on est content de livrer ?
  - A-t-on une règle écrite pour être payé (acompte, prélèvement, partenaire) ?

## Exemple appliqué (illustratif : Sillage, prix hypothétiques)
- Offre cœur : vidéo de lancement premium.
- **Rollover** : l'audit vidéo express (attraction) est crédité sur la vidéo premium si elle est commandée sous 30 jours. Le prix de la vidéo est fixé pour rester rentable après crédit.
- **Menu upsell** en fin d'appel : « Vous n'avez pas besoin des 6 déclinaisons, votre lancement se joue sur LinkedIn. Je vous recommande la vidéo + 2 formats LinkedIn. Préférez-vous la livraison en 3 semaines ou en 10 jours ? »
- **Downsell** après « trop cher » : la même vidéo payée en trois fois au même prix ; sinon une version plus courte (feature downsell) clairement décrite comme telle.
- Upsell après livraison (ce que le client « espère ») : l'accompagnement le jour J du lancement, à ≈ 5× le prix d'une déclinaison (point de départ à tester).

## Erreurs fréquentes
- Un upsell à 10 % du ticket.
- Un upsell qui vend ce que le client attendait déjà (il se sent « pris pour un pigeon »).
- Baisser le prix au premier « non » au lieu de changer la structure de paiement.
- Descendre l'escalier trop vite, ou le présenter d'un bloc.
- Un downsell sans règle de recouvrement (impayés, marchandage).
- Une ancre fictive.

## Garde-fous (honnêteté et conformité)
- **Ancre et rollover** : le prix affiché du palier doit être un **prix réellement pratiqué et disponible** ; « 10 000 $ − 3 000 $ crédités = 7 000 $ » présenté comme une baisse est une annonce avantageuse de prix, soumise aux règles du prix de référence ([verif:OP01], [verif:OP06] dans `passe-3-droit-offres.md`).
- **Financement par un tiers, crédit, carte** : crédit à la consommation encadré ; ne jamais pousser à s'endetter, ni aider à ouvrir une carte de crédit (proscrit dans [fiche:JE2_7elAcxM] « Limites »). Validation `garde-conformite` obligatoire. Formation vendue à un particulier : le paiement intégral d'avance peut être interdit ([verif:OV07], question ouverte [verif:OQ1]).
- **Option ajoutée** : tout paiement supplémentaire exige un consentement exprès, jamais une case pré-cochée ([verif:OU07]).
- **Trial** : un essai « gratuit » ne doit cacher aucun coût autre que l'inévitable ([verif:OP10]) ; la contrepartie (« catch ») est annoncée.
- **Menu upsell « éthique »** : on ne retire que ce dont le client n'a vraiment pas besoin, et on ne prescrit que ce qu'on recommanderait sans commission.

## Agents qui doivent l'utiliser
`strategiste-offre` (propriétaire), `redacteur-newsletter` (séquences post-achat), `redacteur-ads` (pages de confirmation, offres de suivi), `analyste-performance` (taux de prise, panier moyen), `garde-conformite` puis `garde-offres` (ancre, financement, consentement), `redacteur-conditions-vente` (échelonnements, essai), `concepteur-experiences` (test 5× contre 10×).

## Voir aussi
`money-model-sequence-d-offres.md` · `continuite-et-revenu-recurrent.md` · `presenter-le-prix-en-rendez-vous.md` · `offre-quatre-composantes-brunson.md` · `trois-regles-de-prix.md` · `offer-stack.md`
