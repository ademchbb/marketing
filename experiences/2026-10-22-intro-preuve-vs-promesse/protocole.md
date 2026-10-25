# Ouverture « preuve d'abord » contre « promesse d'abord » dans un Reel

| Champ | Valeur |
|---|---|
| Identifiant | `2026-10-22-intro-preuve-vs-promesse` |
| Statut | en attente de marque |
| Priorité | 2 / 19 · score 4 × 4 × 5 = 80 |
| Marque | toute marque avec un résultat **réel et montrable** (produit, chiffre vérifié, démonstration) |
| Plateforme | Instagram Reels (transposable à TikTok et aux Shorts) |
| Méthode | Trial Reels (variantes montrées d'abord aux seuls non-abonnés), par paires |
| Conçu le | 2026-10-22 par `concepteur-experiences` |

## Le doute à lever
Les experts de la base s'accordent sur le but (confirmer vite au spectateur qu'il a bien choisi), pas sur
l'ordre des deux premiers temps :
- MrBeast : l'intro sert d'abord à **prouver que la promesse est réelle**, puis à lever l'objection
  suivante, et seulement ensuite on « ralentit » [fiche:xf0Mli0LVgI 01:04-01:07, framework A] ;
- Hormozi : Proof → Promise → Plan en éducatif [fiche:Jmkq5RLjm0U 00:54] (via
  `principes/hooks-et-retention.md` H3) ;
- Galloway : **tenir la promesse** du titre et de la miniature dans les 10 premières secondes, intrigue avec
  le minimum de contexte [fiche:Z2uoA3bhJT0 01:44-01:50, framework Q].
La fiche Galloway note la divergence sans la trancher (« Confrontation… Intro »). En format court, la
question devient : la première phrase ou la première image doit-elle être la **preuve** ou la **promesse** ?

## Hypothèse
Si le Reel s'ouvre sur la **preuve** (le résultat montré à l'image ou le chiffre réel, avant toute
annonce), alors la part des spectateurs qui dépassent 3 secondes et le temps de visionnage moyen
augmentent par rapport à une ouverture sur la **promesse**, parce que le doute (« est-ce vrai ? ») est
levé avant d'être formulé et que le premier plan est déjà le moment fort [fiche:xf0Mli0LVgI 01:06]
[principes:hooks-et-retention H1].

## Variable testée (une seule)
L'**ordre des deux premiers temps** de l'ouverture (0 à 5 s environ).

## Variantes
- **A (témoin) « promesse d'abord »** : temps 1 = la promesse en une phrase (voix off ou carton de
  ~5 mots) ; temps 2 = la preuve (résultat montré, chiffre réel).
- **B « preuve d'abord »** : temps 1 = la preuve (le résultat à l'image, le chiffre réel, la démonstration) ;
  temps 2 = la promesse.
Les deux variantes utilisent **les mêmes plans et les mêmes mots**, seul leur ordre change.

## Ce qui reste constant
Sujet, corps du Reel après l'ouverture, durée totale (à ±1 s), effets sonores, voix (s'il y en a une),
légende, couverture, heure et jour de publication (même créneau, à 24 h d'écart au plus entre les deux
Trial Reels d'une paire), hashtags (5 au plus [veille:instagram règle 10]).

## Métriques
- **Principale** : temps de visionnage moyen, rapporté à la durée du Reel (Instagram compare aux Reels de
  même durée [veille:instagram §2.1]).
- **Secondaires** : part des spectateurs au-delà de 3 s (si l'interface la donne), envois par portée,
  likes par portée [veille:instagram §2.1, règle 4].
- **Garde-fou** : taux de « Pas intéressé » ou de commentaires de doute (« faux », « montage ») : ne doit
  pas augmenter.

## Échantillon et durée
- **5 paires** (10 Trial Reels), 3 paires au minimum, sur des sujets différents de la même marque.
- Une paire est exclue si l'un des deux Trial Reels touche moins de 300 comptes (seuil maison, trop peu
  de signal).
- Lecture à **7 jours** après publication de chaque Trial Reel ; durée totale estimée : 3 à 5 semaines.

## Critère de décision (fixé avant)
- **B gagne** si B bat A sur la métrique principale dans au moins 4 paires sur 5 (ou 3 sur 3) **et** si
  le gain médian est d'au moins 10 %.
- **A gagne** dans le cas symétrique.
- Sinon : **non concluant**. On garde l'ordre au choix du scénariste, et on retente avec un autre type de
  preuve (chiffre contre démonstration).
- Le gagnant de chaque paire est mis à niveau (publié aux abonnés) ; le perdant ne l'est pas.

## Méthode et déroulé
1. `scenariste-reel` écrit l'ouverture en deux temps ; `pont-motion-design` produit les deux montages à
   partir des mêmes plans (seul l'ordre change).
2. `predicteur-performance` consigne sa prédiction (quelle variante gagne, de combien) dans
   `experiences/predictions.md`.
3. Validation de l'utilisateur sur les deux variantes avant toute publication.
4. `publicateur` publie les deux en Trial Reels par l'API (`trial_params.graduation_strategy = "MANUAL"`)
   [veille:instagram §4, règle 9].
5. À 7 jours, `analyste-performance` relève les métriques ; `analyste-resultats` conclut après la
   dernière paire.

## Garde-fous
- La preuve est **réelle et vérifiable** : produit réel, chiffre vérifié par `verificateur-faits` et daté,
  démonstration non truquée. Tout composite ou image générée qui pourrait passer pour une prise de vue
  réelle est signalé [fiche:xf0Mli0LVgI framework I] (`CLAUDE.md`, honnêteté).
- Jamais de Reel muet : effets sonores et/ou voix [verif:P02] [veille:instagram règle 6]. Pour Sillage,
  **jamais de musique**.
- Aucun chiffre d'expert repris comme fait (« selon X », ou pas du tout).

## Portée attendue de l'apprentissage
Règle d'ouverture par défaut pour `redacteur-hooks`, `scenariste-reel` et `pont-motion-design`. Si B gagne,
on pourra tester ensuite la même variable en YouTube long (intro de 45 s).
