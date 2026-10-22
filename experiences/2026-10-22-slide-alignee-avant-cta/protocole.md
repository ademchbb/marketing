# Carrousel : slide « alignée » avant le CTA contre slide neutre (pré-suasion)

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-slide-alignee-avant-cta` |
| Statut | en attente de marque |
| Priorité | 14 / 19 · score 2 × 4 × 4 = 32 |
| Marque | marque avec une offre dont le concept central est clair (sécurité, compétence, appartenance…) et une campagne Meta de conversion |
| Plateforme | Meta Ads, format carrousel (fil Instagram et Facebook) |
| Méthode | outil Creative testing de Meta (deux carrousels à parts égales) |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
Cialdini : ce qui se passe **juste avant** une demande en change la réception ; l'indice préalable doit
évoquer **le même concept** que la demande (« Romance is associated with flowers, not frosted donuts »)
[fiche:_hem3-8XbEI 00:12-00:14, frameworks A et B]. Son playbook propose de travailler « la slide qui
précède la slide CTA » et de comparer à une version neutre [fiche:_hem3-8XbEI playbook étapes 3 et 12].
**Avertissement** : presque toutes les études citées relèvent du priming comportemental, très touché par la
crise de réplication ; plusieurs viennent probablement de l'équipe Guéguen [fiche:_hem3-8XbEI
« Avertissement scientifique »]. C'est l'hypothèse la plus fragile du backlog : d'où sa priorité basse, et un
test bon marché plutôt qu'une règle.

## Hypothèse
Si l'avant-dernière carte d'un carrousel publicitaire évoque **le concept dont dépend l'offre** (par
exemple, pour une garantie : une image de sécurité réelle et liée au produit) plutôt qu'une image neutre
du produit, alors le coût par résultat baisse, parce que l'indice préalable rend ce concept saillant au
moment de la demande [fiche:_hem3-8XbEI enseignement 2].

## Variable testée (une seule)
Le **contenu de l'avant-dernière carte** du carrousel.

## Variantes
- **A (témoin) neutre** : avant-dernière carte = plan produit neutre, sans message nouveau.
- **B alignée** : avant-dernière carte = image ou phrase qui évoque le concept central de l'offre, choisie
  par le test d'alignement (« évoque-t-elle le même concept que la demande ? ») [fiche:_hem3-8XbEI
  framework B].
Même nombre de cartes, même dernière carte (CTA), même ordre ailleurs.

## Ce qui reste constant
Toutes les autres cartes, texte principal, titre, bouton, page, offre, ensemble de pubs, période.

## Métriques
- **Principale** : coût par résultat.
- **Secondaires** : CTR lien de la dernière carte (si l'interface le ventile par carte), taux de conversion
  de la page.
- **Garde-fou** : qualité des résultats.

## Échantillon et durée
- Au moins **30 résultats par variante** ; 14 à 30 jours [verif:PA16].
- **3 tests** sur 3 offres ou concepts différents avant de conclure (l'effet de priming, s'il existe, est
  petit et instable).

## Critère de décision (fixé avant)
- B est retenu comme pratique de `redacteur-carrousel` seulement s'il gagne **3 tests sur 3** avec un coût
  par résultat inférieur d'au moins 15 % à chaque fois.
- Tout autre résultat : non concluant ou infirmé, et l'hypothèse est classée « non reproduite chez nous »
  dans `apprentissages.md` (c'est aussi un apprentissage utile).

## Méthode et déroulé
1. `strategiste-offre` écrit l'élément central de la demande (« la demande est X ; elle dépend du concept
   Y ») ; `redacteur-carrousel` et `directeur-creatif-visuel` produisent les deux versions.
2. `garde-conformite` applique la règle éthique de Cialdini (voir ci-dessous).
3. `predicteur-performance` consigne sa prédiction.
4. Validation de l'utilisateur ; `publicateur` lance le Creative testing.
5. `analyste-resultats` conclut.

## Garde-fous
- **Règle éthique de Cialdini, non négociable** : l'indice placé en tête est la caractéristique **la plus
  vraie et la plus représentative** de l'offre, celle qui mène à un **choix sage** ; jamais un indice qui
  détourne l'attention du prix, des conditions ou des enjeux [fiche:_hem3-8XbEI encadré, framework E].
- Aucun visage de banque d'images présenté comme un client ; preuve sociale = clients réels avec accord.
- Pas de logos de cartes bancaires ou d'indices conçus pour faire dépenser plus [fiche:_hem3-8XbEI
  framework C].
- Pour Sillage : aucune musique ; la carte alignée peut être une animation sobre.
