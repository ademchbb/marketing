# Campagne test et montée en charge : économie unitaire, calcul par mille, test à risque plafonné, winning formula, paliers

> Famille : expérimentation / budget · Niveau : décider si une offre ou une campagne d'activation mérite d'être déployée, et à quel rythme

## Origine
- **Claude Hopkins** [fiche:hopkins-scientific-advertising] :
  - économie unitaire avant campagne : « What cannot be done on a large scale profitably cannot be done on a small scale » (framework M [p. 52, p. 57], enseignement 8) ;
  - campagne test sur 4 ou 5 villes, coût par client démarré, rachat, délai de remboursement, puis extension ; « Now we let the thousands decide what the millions will do » ; pari asymétrique « the safe side of a hundred to one shot » (framework C [p. 75-79], enseignement 2) ;
  - test continu sur une fraction du marché sans toucher au plan éprouvé [p. 78-79] ; test de décision produit par coupon et vote (framework D [p. 77-78]).
- **Gary Halbert** [fiche:halbert-boron-letters] :
  - calcul de rentabilité par mille lettres (framework E [ch. 8-9]) ;
  - les 7 étapes du succès en mailing et le **test financé à risque plafonné**, avec trois issues définies d'avance (framework T [ch. 22, 24]) ;
  - la **winning formula** par modules : tronc commun, dernier tiers propre au segment, première ligne qui nomme le segment (framework F [ch. 9]).
- **Philip Kotler** [fiche:sR-qL7QdVZQ] : basculer le budget vers un nouveau canal par paliers, environ 10 % puis +5 à 10 % sur l'usage prouvé, jamais 50 % d'un coup (framework K [00:51]-[00:53]).
- **Doublon fusionné** : le test de Hopkins (villes) et celui de Halbert (plis) ont la même logique : petit test chiffré, issues fixées d'avance, extension financée par le résultat. La winning formula de Halbert est la manière de **décliner** le gagnant ; les paliers de Kotler, la manière de **financer** la bascule.
- Fiabilité : méthode 3,5/5 ; chiffres de 1923 et de 1984 non transposables. Halbert fait des **erreurs de calcul** (9 920 $ au lieu de 7 920 $ ; 15 $ au lieu de 17,70 $ ; « 70 $ » pour ~66,67 $) : refaire chaque addition. « Those averages always hold » (Hopkins) : affirmation absolue non démontrée.

## Problème résolu
On déploie une campagne à pleine échelle sur la foi d'une intuition, ou on abandonne une idée gagnante après un test trop petit. La méthode chiffre l'économie avant de dépenser, plafonne la perte possible, fixe d'avance ce qui comptera comme succès, puis décline et étend ce qui gagne sans arrêter d'apprendre.

## Étapes

### 1. Vérifier l'économie unitaire avant tout test
1. Dépense annuelle d'un client (ou revenu sur la fenêtre de rachat connue).
2. Coût d'acquisition estimé.
3. Délai de remboursement acceptable.
4. Taille du marché accessible (pour ne pas surinvestir).
Si le revenu par client ne rembourse pas l'acquisition dans un délai acceptable : **ne pas lancer** (exemple de Hopkins : un germicide dont un flacon dure des années).

### 2. Faire le calcul par mille contacts
Transposition (déduction) : mille e-mails, mille visiteurs, mille impressions.
| Ligne | Calcul |
|---|---|
| Prix encaissé | prix + frais facturés |
| Coût d'exécution par commande | production, livraison, commissions |
| Taux de conversion supposé | hypothèse écrite, prudente |
| Commandes pour 1 000 | taux × 1 000 |
| Marge brute pour 1 000 | commandes × (prix − coût d'exécution) |
| Coût des 1 000 contacts | média, location, production amortie |
| **Profit par mille** | marge brute − coût des contacts |
| Potentiel | profit par mille × milliers disponibles (et par mois si le vivier se renouvelle) |
Faire refaire l'addition par un second agent.

### 3. Fixer d'avance les trois issues
| Issue | Seuil (écrit avant le test) | Suite |
|---|---|---|
| Perdant | coût par client > seuil haut | perte absorbée, projet suivant |
| Marginal | entre les deux seuils | nouvelle décision de test (une variable) |
| Gagnant | coût par client < seuil bas | étape suivante, taille fixée d'avance |
La prédiction est écrite dans `experiences/predictions.md` avant le lancement (`predicteur-performance`).

### 4. Lancer un petit test, à risque plafonné
- Petite taille : quelques zones, un petit budget, quelques milliers de contacts (Halbert : 1 000 à 5 000 plis ; Hopkins : 4 ou 5 villes moyennes).
- Une offre qui démarre vite (échantillon, essai, première commande facile : `offre-d-essai-echantillon-et-mode-de-reponse.md`).
- Budget maximal de perte écrit.

### 5. Mesurer le coût par client démarré, puis le rachat
Attendre et observer : achètent-ils, **rachètent**-ils, combien, à quel rythme ? En combien de temps le profit rembourse-t-il le coût de vente ? (Hopkins : parfois avant l'échéance des factures, « situation idéale ».)

### 6. Étendre par paliers
- Logique Halbert : 1 000-5 000 → 20 000-100 000 → déploiement.
- Logique Kotler (nouveau canal) : environ 10 % du budget, puis +5 à 10 % **uniquement sur l'usage précis** qui a fait ses preuves.
- Surveiller l'usure : l'extrapolation « mille clients → un million » est fragile (fatigue créative, saturation, coûts croissants : `plafond-de-conversion-et-cercles-du-marche.md`).

### 7. Décliner le gagnant en winning formula
1. Séparer le **tronc commun** (environ deux tiers du produit ou du message) de la **couche propre au segment** (le dernier tiers).
2. Réécrire seulement la couche et la **première ligne** pour chaque segment (« a great new way for doctors of chiropractic to make… »).
3. Tester segment par segment.

### 8. Garder une fraction permanente pour tester
Tester de nouveaux plans sur une part du marché sans interrompre le plan éprouvé (Hopkins : plus de 50 plans en cinq ans). Ne pas changer un gagnant par goût.

### 9. Trancher les décisions produit par le même moyen
Faire essayer la nouvelle version à un échantillon (coupon, accès), recueillir l'avis écrit, décider sur le **pourcentage d'approbation**.

## Exemple appliqué (illustratif : offre « audit vidéo express » de Sillage)
- Économie : prix 490 € HT, coût d'exécution 150 €, objectif de 20 % des audits convertis en vidéo premium à 9 500 € (hypothèse).
- Calcul par mille visiteurs de la page : 1,5 % de conversion supposée → 15 audits → marge 5 100 € − 1 200 € de pub = 3 900 € (à recalculer par `analyste-performance`).
- Issues : perdant si coût par audit > 200 € ; gagnant si < 80 €.
- Test : 1 200 € sur deux audiences, quatre semaines.
- Gagnant → winning formula : tronc commun (méthode d'audit) + couche par segment (SaaS B2B, apps grand public), première ligne réécrite.
- Bascule : 10 % du budget pub mensuel, puis +5 % par mois tant que le coût par audit tient.

## Erreurs fréquentes
- Tester sans seuils fixés d'avance (on rationalise ensuite).
- Juger au coût par lead sans attendre le rachat ou la conversion finale.
- Extrapoler linéairement un petit test.
- Changer plusieurs variables en déclinant le gagnant.
- Recopier les additions de Halbert sans les refaire.

## Garde-fous (honnêteté et conformité)
- **Test financé par un partenaire** (modèle de Halbert, partage 50/50) : contrat écrit, issues et partage définis avant le test (`partenariats-aux-resultats.md`, `negociation-echange-a-haute-valeur-et-reputation.md`).
- **Offres testées** : chaque version proposée au public est une offre réelle, honorée. Tester des prix différents : si le prix est **personnalisé** par une décision automatisée, l'information est obligatoire ([verif:OD05]).
- Fausse urgence pour « accélérer » un test : interdite ([verif:OU01]).

## Agents qui doivent l'utiliser
`concepteur-experiences` (propriétaire du protocole), `analyste-performance` (calcul par mille, coût par client, rachat), `predicteur-performance` (prédiction écrite avant), `strategiste-ads` et `strategiste-offre` (paliers, winning formula), `analyste-resultats` (apprentissages), `rapporteur`, `garde-offres`.

## Voir aussi
`publicite-codee-et-cout-par-client.md` · `boucle-d-iteration.md` · `regle-70-20-10.md` · `decliner-un-contenu-gagnant.md` · `lancement-meta-structure-1-1-1.md` (budget « qui pique ») · `lancement-inverse-et-prevente-honnete.md`
