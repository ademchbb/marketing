# Meta Ads : audience Advantage+ contre ciblage manuel

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-meta-advantage-audience-vs-manuel` |
| Statut | en attente de marque |
| Priorité | 11 / 19 · score 3 × 4 × 4 = 48 |
| Marque | marque avec un persona étroit et bien documenté (sinon le test n'a pas d'intérêt) et une campagne de conversion sortie de l'apprentissage |
| Plateforme | Meta Ads |
| Méthode | test A/B natif de Meta (deux ensembles de pubs, audiences séparées) |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
- Meta active l'automatisation de bout en bout par défaut pour Sales, Leads et App depuis fin 2025 ;
  sa consigne est de diversifier la créative plutôt que de cibler finement [veille:meta-ads §4, règle 4]
  [verif:PA23].
- Ben Heath : donner une **direction** (Controls pour les contraintes réelles, Suggestions pour 0 à
  4 intérêts évidents), plus de ciblage détaillé à l'ancienne [fiche:dAJyqo6wnq4 framework F].
- Le discours « laissez faire l'algorithme » est aussi celui de Meta, qui a intérêt à ce qu'on lâche le
  contrôle [fiche:dAJyqo6wnq4 « Biais structurel »].
Ce test vérifie sur nos propres comptes si le ciblage manuel garde un intérêt pour un persona étroit.

## Hypothèse
Si l'on laisse l'audience en **Advantage+** (suggestions seulement) plutôt que de la restreindre
manuellement au persona (âge, intérêts, comportements en limites strictes), alors le coût par résultat est
au moins aussi bon, parce que le système trouve des acheteurs hors des critères déclarés [veille:meta-ads
§2, règle 4]. Prédiction concurrente : pour un persona très étroit (B2B de niche), le ciblage manuel donne
des résultats de meilleure **qualité**.

## Variable testée (une seule)
Le **réglage d'audience** de l'ensemble de pubs.

## Variantes
- **A (témoin) Advantage+ audience** : Controls limités aux contraintes réelles (zone, âge légal, langue
  si nécessaire), suggestions de persona [fiche:dAJyqo6wnq4 framework F].
- **B manuel** : Advantage+ audience désactivé ; âge, genre (si la cible penche à 90 %) et 2 à 4 intérêts
  ou critères du persona appliqués comme **limites strictes**.

## Ce qui reste constant
Créatives (les mêmes pubs dans les deux ensembles), budget quotidien par ensemble, objectif et événement
d'optimisation, placements Advantage+, page, offre, période, attribution.

## Métriques
- **Principale** : coût par résultat.
- **Secondaires** : **qualité des résultats** (part de leads qualifiés ou de rendez-vous honorés, panier
  moyen), CPM, portée, fréquence, part de nouveaux clients (exclusion des clients existants via Customer
  Lifecycle Strategy si disponible [veille:meta-ads §4]).
- **Garde-fou** : part de résultats hors zone ou hors cible (leads inexploitables).

## Échantillon et durée
- **Au moins 50 résultats par ensemble** [verif:PA01] ; 14 à 21 jours, aucune modification.
- Répéter sur 2 marques avant d'en tirer une règle générale.

## Critère de décision (fixé avant)
- Le décideur est le **coût par résultat qualifié** (coût / résultats qualifiés), pas le coût par résultat
  brut, parce que c'est là que les deux prédictions divergent.
- B gagne si son coût par résultat qualifié est inférieur d'au moins **20 %** ; A gagne si l'écart est
  en sa faveur ou inférieur à 20 % (A est le réglage le plus simple et le défaut recommandé par Meta).
- Si B gagne : le ciblage manuel est autorisé pour les personas étroits de même type, et `strategiste-ads`
  le note comme exception documentée.

## Méthode et déroulé
1. `architecte-persona` fournit le persona et ses critères ; `strategiste-ads` traduit en réglages.
2. `predicteur-performance` consigne sa prédiction.
3. Validation de l'utilisateur ; `publicateur` monte le test A/B natif.
4. La marque relève la qualité des leads (CRM) ; `analyste-resultats` conclut.

## Garde-fous
- Aucune dépense sans validation de l'utilisateur.
- Pas de ciblage sur des attributs sensibles (santé, etc.) ni d'accroche qui les vise ; vérifier les
  catégories spéciales [verif:PA07].
- Ne pas présenter un résultat de ce test comme une vérité sur « l'algorithme » : il vaut pour un compte,
  une période, un persona.
- La fonction « audience par créative » (API, 19/10/2026) est hors du test : elle est incompatible avec
  Advantage+ audience et changerait deux choses à la fois [veille:meta-ads règle 10].
