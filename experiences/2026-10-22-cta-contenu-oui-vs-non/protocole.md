# Appel à l'action de fin de contenu : orienté « oui » contre orienté « non »

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-cta-contenu-oui-vs-non` |
| Statut | en attente de marque |
| Priorité | 13 / 19 · score 2 × 4 × 5 = 40 |
| Marque | marque qui propose une ressource gratuite réelle (guide, modèle, audit) obtenue par message privé |
| Plateforme | Instagram Reels |
| Méthode | Trial Reels par paires (variantes montrées aux seuls non-abonnés) |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
Même tension que `2026-10-22-relance-orientee-non-vs-oui`, dans l'autre contexte :
- Voss : question orientée vers le non, parce que le « oui » engage et fait peur [fiche:guZa7mQV1l0 00:05] ;
- Despas : micro-oui de validation pendant la présentation (« Est-ce que ce serait pertinent pour
  vous ? ») [fiche:nte_k2hPXR0 00:28] ; la fiche Voss propose de tester les deux « en rendez-vous comme en
  appel à l'action » [fiche:guZa7mQV1l0 « Confrontation »] ;
- conciliation non testée : micro-oui en présentation, « non » au blocage [fiche:aGI7puAXf6w].
Un contenu social est une **présentation** : la conciliation prédit que le CTA orienté oui gagne ici, alors
qu'elle prédit l'inverse pour la relance. Les deux tests ensemble mettent la conciliation à l'épreuve.

## Hypothèse
Si l'appel à l'action de fin d'un Reel est une question orientée vers le **oui** (« Ça vous serait utile ?
Écrivez GUIDE en message. ») plutôt que vers le **non** (« Seriez-vous contre l'idée de recevoir le guide ?
Écrivez GUIDE en message. »), alors plus de spectateurs envoient le mot-clé, parce qu'un spectateur qui vient
de suivre la démonstration est dans un état d'adhésion que la question de validation prolonge
[fiche:nte_k2hPXR0 framework H], et qu'il n'y a pas ici de résistance à désamorcer.

## Variable testée (une seule)
L'**orientation de la question** du CTA final (texte à l'écran et voix off, s'il y en a une).

## Variantes
- **A (témoin) orientée oui** : « Ça vous serait utile ? Écrivez [MOT] en message. »
- **B orientée non** : « Seriez-vous contre l'idée de recevoir [ressource] ? Écrivez [MOT] en message. »
Même mot-clé, même ressource, même durée du plan de fin.

## Ce qui reste constant
Tout le Reel sauf la question du CTA, la légende (qui ne répète pas la question), la couverture, le
créneau de publication, la ressource envoyée et le message automatique ou manuel de réponse.

## Métriques
- **Principale** : nombre de messages avec le mot-clé pour 1 000 comptes touchés.
- **Secondaires** : temps de visionnage moyen (contrôle : il doit être proche entre A et B), envois par
  portée, taux de téléchargement ou d'usage de la ressource.
- **Garde-fou** : messages qui trouvent la formulation étrange ou manipulatrice.

## Échantillon et durée
- **5 paires** de Trial Reels (3 au minimum), sujets différents.
- Minimum cumulé : **20 messages par variante** ; sinon on étend à 8 paires.
- Lecture à 7 jours par Reel ; durée 4 à 6 semaines.

## Critère de décision (fixé avant)
- Une variante gagne si elle a le meilleur ratio dans au moins 4 paires sur 5 et un ratio cumulé
  supérieur d'au moins 25 %, avec des temps de visionnage moyens à moins de 10 % l'un de l'autre (sinon,
  la différence vient du corps du Reel, pas du CTA).
- Sinon : non concluant.
- Lecture croisée par `analyste-resultats` avec le test de relance : conciliation **confirmée** si A gagne
  ici et B gagne dans la relance ; **infirmée** si la même orientation gagne les deux.

## Méthode et déroulé
1. `scenariste-reel` écrit le plan de fin en deux versions ; `pont-motion-design` produit les deux fins.
2. `predicteur-performance` consigne sa prédiction.
3. Validation de l'utilisateur ; `publicateur` publie en Trial Reels (`graduation_strategy = "MANUAL"`)
   [veille:instagram règle 9] ; la gagnante de chaque paire est mise à niveau.
4. `gestionnaire-communaute` envoie la ressource à chaque demande et compte les messages par variante.
5. `analyste-resultats` conclut.

## Garde-fous
- La ressource existe, est gratuite et livrée à chaque demande ; pas de fausse rareté (« plus que 10
  guides ») [verif:OU04].
- Le message de réponse respecte la prospection électronique : si la marque veut ensuite relancer par
  e-mail, recueillir la base légale prévue par l'arbre CNIL (`redacteur-newsletter`).
- Sur LinkedIn, ce format est **interdit** (« Commentez OUI » = appât à engagement pénalisé)
  [veille:linkedin §7 règle 2] : le test reste sur Instagram, en message privé et non en commentaire.
- Jamais de Reel muet ; pour Sillage, jamais de musique [verif:P02].
