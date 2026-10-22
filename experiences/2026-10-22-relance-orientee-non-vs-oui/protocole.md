# Relance d'un prospect silencieux : question orientée vers le « non » contre question orientée vers le « oui »

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-relance-orientee-non-vs-oui` |
| Statut | en attente de marque |
| Priorité | 8 / 19 · score 3 × 5 × 4 = 60 |
| Marque | marque B2B (ou agence) avec au moins 60 prospects ou contacts entrants restés sans réponse |
| Plateforme | e-mail professionnel ou message LinkedIn (un seul canal par test) |
| Méthode | répartition aléatoire de la liste en deux moitiés (alternance planifiée) |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
- Voss : le « oui » engage et fait peur, le « non » protège ; on pose des **questions orientées vers le
  non** (« Is now a bad time to talk? ») [fiche:guZa7mQV1l0 00:03, 00:05, framework B].
- Despas (vente) : accumuler des **micro-oui** par des questions de validation (« Est-ce que ce serait
  pertinent pour vous ? ») [fiche:nte_k2hPXR0 00:28, framework H].
- Despas (négociation) : au blocage, « est-ce que ça veut dire que c'est impossible de faire affaire
  ensemble ? », qui est orientée vers le non [fiche:aGI7puAXf6w 00:10, 00:18].
- Conciliation proposée par les deux fiches, **non testée** : le micro-oui sert pendant la présentation,
  la question orientée vers le non sert **au moment du blocage** [fiche:aGI7puAXf6w « Confrontations »]
  [fiche:guZa7mQV1l0 « Confrontation avec nte_k2hPXR0 »].
Ce test porte sur le moment du **blocage** (un prospect qui ne répond plus). Le test frère
`2026-10-22-cta-contenu-oui-vs-non` porte sur le moment de la **présentation**. La conciliation prédit des
gagnants opposés dans les deux tests.

## Hypothèse
Si la relance d'un prospect silencieux pose une question orientée vers le non (« Avez-vous mis ce projet
de côté ? ») plutôt qu'une question orientée vers le oui (« Avez-vous 15 minutes cette semaine pour en
parler ? »), alors le taux de réponse augmente, parce que répondre « non » ne l'engage à rien et lui
redonne le contrôle [fiche:guZa7mQV1l0 framework A].

## Variable testée (une seule)
L'**orientation de la question finale** du message de relance.

## Variantes (gabarits, à adapter à la marque)
- **A (témoin) orientée oui** : « […] Avez-vous 15 minutes cette semaine pour qu'on en parle ? »
- **B orientée non** : « […] Est-ce que ce projet est passé au second plan pour vous ? »
Le reste du message est **mot pour mot identique** (rappel du contexte réel du premier échange, une
phrase de valeur, signature).

## Ce qui reste constant
Expéditeur, objet de l'e-mail (ou première ligne du message), longueur, jour et heure d'envoi (envois
alternés A, B, A, B dans le même créneau), délai depuis le dernier échange, canal.

## Métriques
- **Principale** : taux de réponse à 7 jours (toute réponse humaine, hors réponse automatique).
- **Secondaires** : taux de réponses « utiles » (qui donnent une information sur le projet, y compris un
  « non, c'est abandonné »), taux de rendez-vous obtenus à 14 jours.
- **Garde-fou** : taux de désinscription ou de demande d'arrêt des contacts.

## Échantillon et durée
- **Au moins 30 prospects par variante** (60 au total), tirés au sort dans la même liste (même source,
  même ancienneté). Idéalement 50 par variante.
- Durée : envoi sur 1 semaine, lecture à 14 jours.
- Si la liste est plus petite : cumuler 2 vagues (même protocole) avant de conclure.

## Critère de décision (fixé avant)
- B gagne si son taux de réponse dépasse celui de A d'au moins **8 points** **et** si son taux de
  rendez-vous n'est pas inférieur à celui de A.
- A gagne dans le cas symétrique.
- Sinon : non concluant ; on garde la formulation au choix du rédacteur.
- Avec moins de 30 prospects par variante, aucune conclusion n'est tirée (seulement une tendance
  notée).

## Méthode et déroulé
1. `redacteur-newsletter` (ou le rédacteur de prospection désigné) rédige les deux versions ;
   `garde-conformite` valide.
2. Tirage au sort de la liste en deux moitiés (consigné dans ce dossier avant l'envoi).
3. `predicteur-performance` consigne sa prédiction.
4. Envoi par la marque ou par un outil d'envoi officiel, après validation de l'utilisateur ; aucun robot
   qui se connecte avec des identifiants (`CLAUDE.md`).
5. Relevé à 7 et 14 jours ; `analyste-resultats` conclut et croise avec le test frère.

## Garde-fous
- **Prospection électronique** : en B2B, pas de consentement systématique exigé par la CNIL mais un
  message en rapport avec la fonction de la personne, une information claire et un moyen simple de
  s'opposer dans chaque message [verif:JP02] ; liste d'opposition respectée.
- Pas de démarchage individuel de titulaires de CPF (interdit à tous) [verif:JI19].
- Le contexte rappelé doit être **réel** (vrai premier échange) ; pas de faux « suite à notre échange ».
- Pas de fausse urgence ni de fausse rareté, y compris en B2B [verif:OU04].
- Pas de manipulation : la question orientée vers le non doit pouvoir recevoir une réponse « non »
  sans pression ensuite (Voss lui-même : partenariat, pas de mensonge [fiche:guZa7mQV1l0 enseignement 10]).
