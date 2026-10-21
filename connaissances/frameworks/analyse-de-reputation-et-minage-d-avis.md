# Analyse de réputation (9 étapes), minage d'avis et grille de 5 questions pour l'IA

> Famille : recherche client · Niveau : livrables 1 à 3 de la SOP de stratégie créative · Vaut aussi pour l'organique

## Origine
- **Dara Denney** [fiche:yRgPbqywUJ8] :
  - analyse de réputation en 9 étapes (framework B [01:36]-[07:02]) et ses 4 familles d'objections [05:58] ;
  - minage d'avis (framework C [07:35]-[08:40]) ;
  - grille de 5 questions pour l'analyse IA des avis (framework D [08:40]-[09:14]) ;
  - « l'IA synthétise, l'humain choisit » (enseignement 8 [07:02] [08:40] [09:14]).
- Convergence : l'écoute de l'audience (Ralston, Hormozi, Mino Lee) dans `contenu-communautaire-et-ecoute.md`, qui travaille sur **sa propre** communauté ; ici on refait le **parcours de recherche d'un prospect** sur tout le web.
- Fiabilité : 3/5 (méthode cohérente et recoupant les bonnes pratiques de voix du client, sans résultat mesuré). Seuils (20 pubs, 12 mois) **arbitraires**. Outil « Runith » : nom incertain. IA d'Amazon : probablement Rufus (déduction).

## Problème résolu
Les angles publicitaires sont inventés en salle de réunion au lieu d'être tirés du **langage réel** des clients et prospects. L'analyse de réputation refait « the same research journey that a customer would » pour trouver les **objections**, le **grand point de friction** et les **déclencheurs d'achat**.

## Étapes

### A. Analyse de réputation (manuelle)
1. **La marque** : fondateurs, histoire de la fondation, « big why ».
2. **Les produits** : best-sellers, merchandising, offres poussées en paid social.
3. **Chaque best-seller** (en commençant par celui visé) : promesse initiale, transformation, preuves, caractéristiques, bénéfices, possibilités de **bundles**.
4. **Première page Google** : tout signal qui empêcherait d'acheter.
5. **Presse et actualité** : presse **gagnée** contre presse **achetée** (une série d'articles du même type est suspecte) ; actualité exploitable (IPO, entrée chez un distributeur, lancement) qui peut changer formats, offres, voire objectifs de campagne. La presse pèserait plus chez les publics âgés (opinion).
6. **Reddit** : critiques honnêtes et douleurs ; copier les **phrases exactes**.
7. **Amazon** (si présent) : best-seller Amazon contre DTC, produit le plus commenté et le mieux noté ; demander à l'IA d'Amazon « What type of people are buying this product? ».
8. **Réseaux de la marque** : contenus qui marchent, communauté, storytelling, EGC, coulisses, transparence, créateurs partenaires.
9. **YouTube** : vidéos d'avis (prudence : elles peuvent être payées) et surtout les **commentaires** (doutes, objections, FAQ). « La plateforme que les stratèges oublient. »

**Sortie** : liste des objections classées en 4 familles + le grand point de friction.
| Famille | Le prospect pense… |
|---|---|
| Efficacité | « Est-ce que ça marche vraiment ? » |
| Ça vaut le coup ? | « Est-ce que ça en vaut la peine ? » |
| Coût | « C'est trop cher. » |
| Valeur perçue | « Je ne vois pas pourquoi ça vaut ce prix. » |

Questions à chaque étape : qu'est-ce qu'un prospect qui compare les options verrait ici ? Quelle phrase exacte pourrait devenir un hook ? Quel signal ferait renoncer ?

### B. Minage d'avis
1. Copier le modèle de feuille.
2. **Exporter** tous les avis de la plateforme d'avis du client.
3. Ajouter **à la main** les phrases marquantes collectées en A (Reddit, Amazon…).
4. Miner les commentaires des **20 meilleures pubs des 12 derniers mois** (outil d'agrégation ou IA).
5. Classer les produits par **nombre d'avis** et par **note**.
6. Garder un tri **manuel** des avis à fort potentiel publicitaire.
- Question : chaque verbatim a-t-il sa source (URL, date, plateforme) ?

### C. Analyse IA des avis : la grille de 5 questions
Charger les avis (et l'analyse de réputation en contexte) dans un LLM et demander :
1. Quelles sont les forces et les faiblesses de la marque ?
2. Quelles sont les plaintes ou objections les plus fréquentes ?
3. Sont-elles semblables ou différentes de celles de l'analyse de réputation ?
4. Quelles phrases « golden nugget » et quelles tendances parmi les avis ?
5. Quels sont les déclencheurs d'achat (« trigger points that cause someone to buy ») ?
- Règle : la machine synthétise, **l'humain choisit** les verbatims (« they don't quite have the judgment of what could be a really impactful review that could lead to a top performing ad »).
- Contrôle : vérifier que chaque « golden nugget » retenu existe mot pour mot dans la source (pas de reformulation de l'IA présentée comme une citation).

## Exemple appliqué (illustratif : marque promue « studio de yoga en ligne », hypothétique)
- Google : un article « est-ce une arnaque ? » en 1re page → objection « efficacité/légitimité ».
- Reddit (verbatim à copier tel quel) : « j'ai résilié parce que les cours vont trop vite pour un débutant » → objection + persona « débutant complet ».
- YouTube (commentaires d'avis) : « est-ce que ça marche sans tapis ? » → FAQ à traiter.
- Grille IA, question 5 : déclencheur « mal de dos après le télétravail ».
- Sortie : grand point de friction = « pas pour les débutants ». Transmis à `objection-vers-angle.md`.

## Erreurs fréquentes
- S'arrêter aux avis du site de la marque.
- Prendre les vidéos d'avis YouTube pour neutres (elles peuvent être payées).
- Laisser l'IA choisir les verbatims, ou citer une reformulation comme un avis réel.
- Confondre presse achetée et presse gagnée.
- Réutiliser un avis en pub sans **accord** de son auteur (règle d'honnêteté du projet ; `garde-conformite`).

## Limites
- Suppose une marque avec des avis en volume, de la presse, voire Amazon. Pour une marque jeune : Reddit, commentaires des concurrents et `ecouteur-audience`.

## Agents qui doivent l'utiliser
`ecouteur-audience` (propriétaire des verbatims), `strategiste-ads`, `architecte-persona`, `analyste-marque` (étapes 1-3 et 8), `strategiste-positionnement` (objections → valeur différenciée), `redacteur-hooks` et `redacteur-ads` (phrases exactes), `strategiste-offre` (bundles), `garde-conformite` (accords avant réutilisation).

## Voir aussi
`sop-strategie-creative.md` · `prompt-decouverte-personas.md` · `objection-vers-angle.md` · `contenu-communautaire-et-ecoute.md`
