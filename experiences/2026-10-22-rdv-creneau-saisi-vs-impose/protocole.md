# Prise de rendez-vous : créneau choisi et saisi par la personne contre créneau proposé d'office

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-rdv-creneau-saisi-vs-impose` |
| Statut | en attente de marque |
| Priorité | 16 / 19 · score 3 × 4 × 2 = 24 |
| Marque | marque qui prend au moins 60 rendez-vous (appel découverte, démo, webinaire) en 2 mois |
| Plateforme | parcours de réservation de la marque (outil de prise de rendez-vous) + e-mail de confirmation |
| Méthode | alternance planifiée par semaine (semaines A et B tirées au sort) |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
Cialdini rapporte le projet NHS de Steve Martin : au lieu d'une carte de rendez-vous remplie par le
personnel, le patient écrit **lui-même** la date et l'heure ; résultat annoncé, −18 % d'absences
(« An active, public, voluntary commitment gave that promise legs ») [fiche:_hem3-8XbEI 00:59-01:00,
framework G]. La fiche juge ce levier mieux appuyé que le priming, mais la référence est citée de mémoire
et **à vérifier** ; le chiffre ne se cite pas. Version numérique proposée par la fiche : « Choisissez et
notez votre date » plutôt qu'un créneau imposé.

## Hypothèse
Si la personne **choisit son créneau et le recopie elle-même** (dans un champ de confirmation libre) au lieu
de recevoir un créneau proposé d'office qu'elle n'a qu'à accepter, alors le taux de présence au rendez-vous
augmente, parce qu'un engagement actif et volontaire tient mieux qu'un engagement passif
[fiche:_hem3-8XbEI enseignement 10].

## Variable testée (une seule)
Le **caractère actif de l'engagement** au moment de la réservation.

## Variantes
- **A (témoin) passif** : la marque propose un créneau (« Votre appel : mardi 14 h, cliquez pour
  confirmer ») ; un clic suffit.
- **B actif** : la personne choisit parmi les mêmes disponibilités, puis écrit elle-même le jour et l'heure
  dans un champ (« Notez ici votre créneau : … ») avant de valider.
Les mêmes créneaux sont disponibles dans les deux semaines.

## Ce qui reste constant
Offre du rendez-vous, page, durée, interlocuteur, rappels (même nombre, mêmes délais, même texte),
source du trafic, délai moyen entre réservation et rendez-vous (noté et comparé).

## Métriques
- **Principale** : taux de présence (rendez-vous honorés / rendez-vous réservés).
- **Secondaires** : taux de réservation (B ajoute une étape : il peut baisser), taux d'annulation
  anticipée, délai moyen avant le rendez-vous.
- **Garde-fou** : rendez-vous **honorés** par visiteur de la page (si B gagne en présence mais perd
  davantage en réservations, il perd au total).

## Échantillon et durée
- **Au moins 30 rendez-vous réservés par variante** (60 au total), sur 6 à 10 semaines, semaines A et B
  tirées au sort à l'avance.
- Exclure les semaines de vacances scolaires ou de fêtes, ou les répartir également.

## Critère de décision (fixé avant)
- B est adopté si son taux de présence dépasse celui de A d'au moins **10 points** **et** si le nombre de
  rendez-vous honorés par visiteur n'est pas inférieur.
- Si B gagne en présence mais perd en rendez-vous honorés par visiteur : rejet (la friction coûte plus
  qu'elle ne rapporte).
- Sinon : non concluant.

## Méthode et déroulé
1. La marque (ou `developpeur-outils` si l'outil le permet) configure les deux parcours ; aucune case
   pré-cochée.
2. Calendrier A/B tiré au sort et consigné ici avant le lancement ; `predicteur-performance` consigne sa
   prédiction.
3. Validation de l'utilisateur sur les deux parcours.
4. La marque relève présences et absences ; `analyste-resultats` conclut.

## Garde-fous
- Rien de pré-coché, consentement exprès pour tout envoi ultérieur [verif:JP07].
- Le champ libre ne sert qu'à l'engagement : aucune donnée personnelle supplémentaire collectée.
- Pas de fausse rareté des créneaux (« plus que 2 places ») si elle n'est pas réelle [verif:OU04].
- Ne pas citer le « −18 % » du NHS dans un contenu tant que `verificateur-faits` ne l'a pas confirmé.
