# Lire un compte publicitaire : chaîne de transmission, hiérarchie gold / intermédiaire / bronze, règle 20/80, biais et comparaison

> Famille : mesure / publicité payante · Niveau : lecture hebdomadaire d'un compte Meta (transposable aux autres régies)

## Origine
- **Coudac** (Paul), mars 2024 [fiche:qBxEAqZbHVg] :
  - chaîne de transmission et boucle secondaire (framework C [10:44] [16:40] [18:17] [19:53]) ;
  - métriques de diffusion contre métriques de conversion (framework D [13:23] [15:00]) ;
  - hiérarchie des métriques en 3 niveaux (framework E [21:29]-[23:08]) ;
  - règle du 20/80 (framework F [12:19]) ;
  - raisonner par comparaison (framework G [23:08]) ;
  - typologie des biais (framework I [30:45]-[34:31]).
- Horodatages [mm:ss]. Légende : **[FONDAMENTAL]** principe durable, **[DATÉ 2024]** à revérifier.
- Fiabilité : 3,5/5. **Erreur de calcul de la source corrigée ici** : passer le ROAS de TTC à HT (TVA 20 %) le fait baisser de **16,7 %**, pas de 20 % (c'est le ROAS TTC qui est 20 % plus haut). Repère « CPM ≈ 5 € en France sur une campagne de conversion, 10 € = alerte » : **[DATÉ 2024]**, expérience d'agence.
- Contradiction interne signalée par la fiche : le CR est « souvent la métrique la plus importante » [15:00] puis rangé en bronze [22:36]. Lecture probable : il compte pour la performance, mais le media buyer a peu de prise dessus.

## Problème résolu
Les annonceurs ont une masse de données « phénoménale » non hiérarchisée et analysent campagne par campagne. Ils réagissent à une baisse sans savoir si elle vient d'eux, du marché ou du tracking. Cette lecture dit **dans quel ordre** regarder, **quand s'arrêter** et **comment expliquer** une variation avant d'agir.

## La chaîne (une métrique par transition) [FONDAMENTAL]
| Transition | Métrique | Formule |
|---|---|---|
| Argent → impressions | CPM | dépense / impressions × 1 000 |
| Impressions → clics | CTR | clics / impressions |
| Clics → ventes | CR | ventes / clics sortants |
| Ventes → CA | AOV (panier moyen) | CA / nombre de ventes |
Composites : CPC (argent → clics), CPA (argent → ventes, connu seulement a posteriori), ROAS (CA attribué / dépense). **CPA = AOV / ROAS.**
- **Diffusion** (expérience dans la plateforme) : CPM, CTR, CPC. **Conversion** (site et offre) : CR, CPA, AOV, ROAS.
- **Boucle secondaire** : beaucoup de ventes arrivent des jours après une vue, par d'autres canaux ; une grande part de l'impact n'est pas mesurable avec précision. Le ROAS dépend de la fenêtre (7 j clic / 1 j vue par défaut, [DATÉ 2024]), du tracking et du TTC/HT : il **n'a pas de valeur absolue**.

## Étapes (lecture hebdomadaire)

### 0. Avant de lire : la mesure est-elle saine ?
- Fenêtre d'attribution notée et **constante** ; ne jamais comparer des ROAS calculés sur des fenêtres différentes.
- Valeur de conversion en **TTC ou HT** notée dans tout rapport.
- Alerte de panne de tracking (zéro conversion sur 24 h alors que la boutique vend) (déduction).
- Dates de toute intervention sur le tracking ou de mise en conformité RGPD annotées.

### 1. Commencer par les 20 % de campagnes qui font 80 % de la dépense
- Question : quelles campagnes portent la dépense de la période ?

### 2. Niveau gold : CPA et ROAS
Santé du compte en un coup d'œil. S'ils vont bien, **on s'arrête là**.

### 3. Niveau intermédiaire : CPC et CPM (seulement si le gold se dégrade)
On paie les clics ou les impressions plus cher → problème de créa ou de saisonnalité. Le CPM monte quand l'expérience proposée est moins intéressante (facteur n°1 selon l'auteur).

### 4. Niveau bronze (rarement)
- CTR : seulement si le CPC est mauvais **et** le CPM bon.
- CR : varie surtout avec la saisonnalité selon l'auteur (position **contestée** par les praticiens du CRO).
- Panier moyen : « je n'ai jamais vu un problème de performance résolu par une hausse du panier moyen » (opinion).

### 5. Expliquer la variation avant d'agir : les biais
Un biais fait bouger la performance **indépendamment de vos actions** :
- **Externes** [FONDAMENTAL] : saisonnalité ; conjoncture (exemple 2022 : guerre en Ukraine) ; événements propres (passage TV, bad buzz).
- **Tracking** : panne ; conversions invisibles pour la plateforme (« 30 % », illustratif) ; mise en conformité RGPD ; TTC/HT.
- **Attribution** : dernier clic favorable à Google Ads ; guerre des régies.
Tenir un **journal des biais** daté (déduction de la fiche).

### 6. Raisonner par comparaison
1. Trouver la meilleure période passée.
2. Comparer ce qu'on faisait alors à aujourd'hui.
3. Isoler la variable qui a changé.
4. Classer la cause : extérieure (biais) ou intérieure (ce qu'on a fait dans le compte).

### 7. Décider
Agir sur la cause intérieure identifiée ; pour les créas, utiliser `matrice-depense-cpa.md` ; pour le budget, `plan-d-atterrissage-et-timing.md`. Remonter au CAC blended pour la vérité business (`cac-blended-et-mesure-du-mix.md`).

## Exemple appliqué (illustratif, hypothétique)
- Semaine 14 : CPA +35 %. Les 2 campagnes qui font 82 % de la dépense sont en cause.
- Intermédiaire : CPM stable, CPC +30 % → le CTR a chuté (bronze consulté parce que CPC mauvais et CPM bon).
- Biais : aucune panne, pas de promo, pas d'actualité ; la meilleure période (semaine 9) tournait sur 6 créas, aujourd'hui 2 (fatigue probable). Cause intérieure → nouvelles créas.
- Journal des biais : « S14 : RAS externe ; tracking OK ; HT ».

## Erreurs fréquentes
- Lire toutes les campagnes au même niveau, sans pondérer par la dépense.
- Descendre au CTR alors que le CPA va bien.
- Comparer des ROAS sur des fenêtres ou des bases (TTC/HT) différentes.
- Couper ou relancer après une baisse sans avoir écarté biais et tracking.
- Reprendre l'erreur « −20 % » du passage TTC → HT.

## Agents qui doivent l'utiliser
`analyste-performance` (propriétaire), `strategiste-ads`, `rapporteur` (rapports en paliers gold/bronze), `analyste-resultats`, `veilleur-algorithmes` (revérifier fenêtres d'attribution et repères datés), `predicteur-performance`.

## Voir aussi
`cac-blended-et-mesure-du-mix.md` · `matrice-depense-cpa.md` · `plafond-de-conversion-et-cercles-du-marche.md` · `boucle-d-iteration.md` · `analyse-top-vs-bottom.md`
