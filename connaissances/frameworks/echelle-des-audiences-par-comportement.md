# Échelle des audiences par comportement d'achat : les 10 fichiers de Halbert et la récence-fréquence-montant

> Famille : ciblage / réponse directe · Niveau : choisir et hiérarchiser les audiences d'une campagne d'activation (pub de conversion, e-mail, retargeting)

## Origine
- **Gary Halbert**, *The Boron Letters* (1984) [fiche:halbert-boron-letters] :
  - l'échelle des 10 fichiers, de l'annuaire à sa propre liste de clients satisfaits (framework C [ch. 6]) ; fil rouge : réduire la « waste circulation », passer du fusil de chasse à la carabine ;
  - récence, fréquence, montant : « RECENCY is, by far, the most important of all » ; « Get 'em while they're hot! » (framework D [ch. 7]) ;
  - « THE BEST LIST OF ALL IS YOUR OWN CUSTOMER LIST! » à condition que « THEY MUST BE SATISFIED CUSTOMERS! » [ch. 6] ;
  - nuance de Halbert lui-même : la promotion des armoiries a très bien marché sur des noms tirés de l'annuaire ; le bon fichier dépend de l'**offre** (enseignement 3 [ch. 9]).
- Nom moderne : modèle **RFM** (déduction de la fiche). Les équivalents numériques (audiences personnalisées, fenêtres de récence, segments e-mail) sont des **déductions**, non testées dans la source.
- **Limite de périmètre** : cette échelle sert l'**activation** (convertir ceux qui achètent maintenant). Pour la **marque**, Binet & Field montrent que la portée large dans la catégorie bat la fidélisation ([fiche:binet-field-b2b-growth], fidélité 0,0 contre portée 1,6 effet « very large »). Ne pas concentrer tout le budget sur le haut de l'échelle.
- Fiabilité : 3,5/5 ; dispositif postal de 1984 (fichiers SRDS loués) ; aucun chiffre de test donné pour l'échelle.

## Problème résolu
On cible par démographie ou par revenu supposé, alors que le meilleur prédicteur d'un achat est un **achat passé** : dans le même canal, du même type de produit, récent, répété, cher. L'échelle classe les audiences de la moins à la plus probable et fait commencer les tests par le haut.

## L'échelle (exemple de Halbert : vendre un livre d'investissement par courrier) et ses transpositions
| Palier | Audience de Halbert | Transposition numérique (déduction) |
|---|---|---|
| 1 | Noms tirés de l'annuaire (« terrible idea ») | Audience large sans critère |
| 2 | Annuaire limité aux quartiers aisés | Ciblage géographique ou socio-démographique |
| 3 | Groupes à haut revenu présumé (médecins, avocats) | Ciblage par intitulé de poste ou centre d'intérêt |
| 4 | Gens aisés, **acheteurs prouvés par correspondance** de n'importe quoi | Personnes ayant déjà acheté en ligne dans le canal |
| 5 | … ayant acheté un produit **similaire** | Acheteurs de la catégorie (clients de concurrents identifiés par leur comportement, visiteurs de pages produit similaires) |
| 6 | … acheteurs **répétés** de ce type de produit | Acheteurs multiples de la catégorie |
| 7 | … ayant payé **cher** | Gros paniers |
| 8 | … ayant acheté **très récemment** | Fenêtre de récence courte (30 à 90 jours) |
| 9 | … signalés comme marchant « like crazy » pour des offres similaires | Audiences qui convertissent **en ce moment** dans vos propres tests |
| 10 | **Votre propre liste de clients, s'ils sont satisfaits** | Clients satisfaits (base CRM, abonnés acheteurs) |

## Étapes

### 1. Qualifier l'offre : universelle ou spécialisée ?
Une offre universelle (le nom de famille de chacun) peut vivre d'une audience faible ; une offre spécialisée exige le haut de l'échelle.
- Question : qui, dans la population, n'a **aucune** raison d'être intéressé ?

### 2. Placer chaque audience disponible sur l'échelle
Lister les audiences accessibles et leur palier. Le fil rouge : combien de personnes atteintes n'ont aucune chance d'acheter (gaspillage) ?

### 3. Scorer en récence, fréquence, montant
- **Récence** d'abord : plus l'achat similaire est récent, plus la réceptivité est forte.
- **Fréquence** : achats répétés = intérêt prouvé.
- **Montant** : celui qui a payé 100 $ est plus chaud que celui qui a payé 10 $.

### 4. Vérifier la satisfaction avant de solliciter ses clients
La liste de clients n'est la meilleure que si les clients sont **satisfaits** : relancer d'abord ceux qui ont eu un bon résultat ; traiter les mécontents à part (service, pas vente).

### 5. Tester du haut vers le bas
Commencer par les paliers 10, 9, 8, puis descendre tant que le coût par client reste rentable (`campagne-test-et-montee-en-charge.md`). « Many lists that should work don't… It really doesn't matter why » : les données tranchent, pas la théorie.

### 6. Séparer activation et marque
Le haut de l'échelle reçoit les messages d'activation (offre, preuve, prix). La pub de marque, elle, vise large dans la catégorie (`part-de-voix-et-equilibre-marque-activation.md`).

## Exemple appliqué (illustratif : Sillage, campagne d'activation pour l'offre « vidéo de lancement »)
- Palier 10 : clients satisfaits de 2025, invités à une offre « deuxième lancement » (relance e-mail, base légale vérifiée).
- Palier 8 : visiteurs de la page tarifs dans les 30 derniers jours (retargeting).
- Palier 5 : abonnés de la newsletter qui ont téléchargé la checklist de lancement.
- Palier 3 : fondateurs ciblés par intitulé de poste, réservés à la campagne de marque, pas à l'offre.
- Test : budget d'abord sur 10 et 8 ; descente vers 5 seulement si le coût par client reste sous le seuil fixé.

## Erreurs fréquentes
- Cibler par revenu supposé plutôt que par achat passé.
- Solliciter des clients mécontents avec une offre.
- Juger un palier par la théorie (« ça devrait marcher ») au lieu du test.
- Mettre tout le budget en haut de l'échelle et ne plus jamais toucher de nouveaux acheteurs.

## Garde-fous (honnêteté et conformité)
- **Fichiers et listes** : la location ou l'achat de fichiers et l'envoi de messages commerciaux suivent les règles de la CNIL (exception client, régime B2B, consentement en B2C) : `arbre-regime-message-electronique-cnil.md`.
- **Téléverser une liste de clients** sur une plateforme publicitaire (audiences personnalisées) est un traitement de données : base légale et information à vérifier par `garde-conformite`.
- **Données sensibles** (santé, situation financière, moments de vie) : pas de ciblage ni de message qui sous-entend la condition personnelle du destinataire (`objection-vers-angle.md`, étape 5).

## Agents qui doivent l'utiliser
`strategiste-ads` (propriétaire : audiences d'activation), `redacteur-newsletter` (segments e-mail RFM), `analyste-performance` (coût par client par palier), `concepteur-experiences` (ordre des tests), `architecte-persona`, `garde-conformite`.

## Voir aussi
`foule-affamee-le-marche-avant-le-produit.md` · `campagne-test-et-montee-en-charge.md` · `plafond-de-conversion-et-cercles-du-marche.md` · `arbre-regime-message-electronique-cnil.md` · `part-de-voix-et-equilibre-marque-activation.md`
