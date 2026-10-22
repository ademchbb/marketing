# LinkedIn Ads : Thought Leader Ads puis Message Ad, contre Message Ad seul (avec groupe témoin)

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-linkedin-tla-puis-message-ad` |
| Statut | en attente de marque · **prérequis bloquant à vérifier** (voir plus bas) |
| Priorité | 17 / 19 · score 4 × 2 × 2 = 16 |
| Marque | marque B2B avec un dirigeant qui publie (au moins 4 posts organiques utilisables), un budget LinkedIn Ads et un CRM |
| Plateforme | LinkedIn Ads (Thought Leader Ads, Sponsored Messaging) |
| Méthode | répartition aléatoire d'une liste de comptes ou de contacts en deux audiences téléversées (groupe traité / groupe témoin) |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
AJ Wilcox et Ruby James (LinkedIn) présentent la séquence « TLA en haut d'entonnoir, puis message privé au
nom du même dirigeant à ceux qui ont interagi » comme la séquence gagnante ; LinkedIn annoncerait une
conversion **×6** après un TLA [fiche:pILj7t-qQhs 00:30-00:32, framework I]. Ce ×6 est **invérifiable**
(oral seulement, aucune publication retrouvée) et porte un biais de sélection évident : ceux qui
interagissent avec un TLA sont déjà plus intéressés [verif:PB03]. La fiche demande de **mesurer soi-même
avec un groupe témoin** [fiche:pILj7t-qQhs playbook étape 11].

## Prérequis bloquant (à vérifier avant toute conception détaillée)
- **Disponibilité de Sponsored Messaging (Message Ads, Conversation Ads) pour des membres situés dans
  l'Union européenne.** Une restriction de diffusion dans l'UE est signalée de mémoire par le concepteur ;
  elle ne figure ni dans la base ni dans `veille/plateformes/linkedin.md`. **Non vérifié.** Si la
  restriction existe, ce test n'est possible que pour une cible hors UE, ou doit être reconçu avec un TLA
  « réservez un rendez-vous » à la place du message (séquence Fibbler [fiche:pILj7t-qQhs framework J]).
- Taille minimale d'audience téléversée exigée par LinkedIn (à vérifier dans Campaign Manager).

## Hypothèse
Si une audience de comptes cibles voit d'abord pendant 3 semaines des Thought Leader Ads du dirigeant, puis
reçoit une Message Ad signée par ce même dirigeant, alors son taux de rendez-vous est supérieur à celui
d'une audience équivalente qui reçoit la même Message Ad sans TLA, parce que le prospect reconnaît la
personne qui lui écrit (« such a strong cohesion ») [fiche:pILj7t-qQhs 00:31].

## Variable testée (une seule)
L'**exposition préalable aux TLA** du dirigeant.

## Variantes
- **A (témoin)** : Message Ad seule (même texte, même expéditeur, même offre).
- **B** : 3 semaines de TLA (3 à 4 posts réels du dirigeant), puis la même Message Ad.
**Point de méthode décisif** : la Message Ad est envoyée à **toute** l'audience B (et pas seulement à ceux
qui ont interagi avec les TLA) et à toute l'audience A. On compare des groupes tirés au sort, ce qui
supprime le biais de sélection du ×6. Une analyse secondaire compare, à l'intérieur de B, ceux qui ont
interagi et les autres (corrélation seulement).

## Ce qui reste constant
Liste source (mêmes critères ICP), tirage au sort des comptes ou contacts en deux moitiés, texte de la
Message Ad, expéditeur, offre (démo ou rendez-vous), date d'envoi du message, fréquence plafonnée par
LinkedIn, page ou formulaire de destination.

## Métriques
- **Principale** : rendez-vous ou démos obtenus pour 100 membres de l'audience (intention de traiter),
  attribués par le CRM sur 30 jours après le message.
- **Secondaires** : taux d'ouverture et de clic de la Message Ad, coût par rendez-vous (TLA compris pour
  B), opportunités ouvertes à 90 jours (Revenue Attribution Report si disponible [fiche:pILj7t-qQhs
  framework K]).
- **Garde-fou** : désabonnements ou plaintes sur la Message Ad.

## Échantillon et durée
- Au moins **2 × 300 comptes** (ou contacts) cibles ; en dessous, le nombre de rendez-vous attendu est
  trop faible pour conclure (seuil maison à revoir avec les premiers taux observés).
- Minimum décisionnel : **20 rendez-vous au total**.
- Durée : 3 semaines de TLA + 30 jours de suivi, soit environ 7 à 8 semaines.

## Critère de décision (fixé avant)
- B gagne si son taux de rendez-vous par 100 membres est au moins **1,5 fois** celui de A **et** si son coût
  par rendez-vous (TLA compris) n'est pas plus de 20 % supérieur.
- Si B gagne seulement en taux mais coûte nettement plus cher : la séquence est réservée aux comptes à
  forte valeur (ABM).
- Moins de 20 rendez-vous au total : non concluant, on prolonge ou on élargit la liste.
- Le ×6 annoncé par LinkedIn n'est **jamais** une référence de succès [verif:PB03].

## Méthode et déroulé
1. Vérifier le prérequis bloquant (`veilleur-algorithmes`, `verificateur-faits`).
2. `architecte-persona` et la marque construisent la liste ICP ; tirage au sort consigné ici.
3. `redacteur-linkedin` sélectionne les posts réels du dirigeant à sponsoriser et rédige la Message Ad
   (validée par le dirigeant) ; `garde-conformite` valide.
4. `predicteur-performance` consigne sa prédiction.
5. Validation de l'utilisateur (budget, audiences, textes) ; lancement par `publicateur` via l'API ou les
   outils officiels.
6. `analyste-resultats` conclut à J+30 et à J+90.

## Garde-fous
- Les TLA reprennent des **posts réels** du dirigeant, qui garde la dernière main ; jamais de post
  entièrement généré [fiche:pILj7t-qQhs framework F].
- Sponsoriser le post d'un client ou d'un créateur exige son accord explicite (hors périmètre de ce test)
  [fiche:pILj7t-qQhs playbook étape 17].
- Listes téléversées : base légale, information des personnes, minimisation ; pas de coordonnées obtenues
  par enrichissement non informé [verif:OD01-OD02] [verif:JP02].
- Aucun chiffre de l'épisode (+33 %, ×6, +24 %, +120 %, +20-30 %) présenté comme un fait
  [verif:PB01-PB04].
- Aucune dépense sans validation de l'utilisateur.
