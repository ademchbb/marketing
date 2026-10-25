# Principes : hooks et rétention

> Tenu par `synthetiseur-connaissances`. **Dernière mise à jour : 2026-10-25** (grande synthèse, équipe S5a).
> Sources traitées : 26 fiches (20 experts ou sources), les frameworks liés, `swipe-file/hooks.md` et `structures.md`,
> le registre de vérification (fusion des passes 1 à 4 du 2026-10-25) et les fiches `veille/plateformes/` (YouTube
> revalidée le 2026-10-22, § 9).
> Lecteurs : `redacteur-hooks`, `critique-hook`, `scenariste-reel`, `scenariste-youtube-long`, `titreur-miniatures`,
> `redacteur-carrousel`, `redacteur-linkedin`, `directeur-creatif-visuel`, `simulateur-audience`, `pont-motion-design`.
> Titres et miniatures (avant le clic) : `packaging.md`. Récit et enjeux : `storytelling.md`. Vidéo longue :
> `youtube-long.md`.

## Comment lire ce fichier

- **Experts du lot 1** : Caleb Ralston (`Ch4Sl0POBhU` + `uJ8Pg6t_iho`, compté **une seule fois**), Alex Hormozi
  (`Jmkq5RLjm0U`, puis `k834E6OTGTM` : même expert), Ava Yuergens et Jack Neel (`HzoQgQS8czE`, comptés comme un),
  Mino Lee (`AA1LoZwW_2Y`).
- **Experts ajoutés le 2026-10-25** : MrBeast (`xf0Mli0LVgI`, fin 2024, **[DATÉ]** sur l'algorithme), Paddy Galloway
  (`Z2uoA3bhJT0`, 09/2026), Gary Vaynerchuk (`IWuVEcQexWo`), Dan Koe (`SUzKZfyaAK8`), Google ABCD
  (`google-abcd-youtube-ads` + `google-abcd-playbook-2022`, une source), Dave Trott (`rl3SELihHqs`), Stanislas Leloup
  sur Joseph Sugarman (`1N2XALudegQ`), Donald Miller (`S8lH_TdQZgs`), Gary Halbert (`halbert-boron-letters`), Claude
  Hopkins (`hopkins-scientific-advertising`), Quentin Despas (`aGI7puAXf6w` + `nte_k2hPXR0`, un), Justin Welsh
  (`DJLtwT1Z0eo`), Jonah Berger (`FN4eDk1pq6U`), Andy Raskin (`U1b1o-m5bpI`), playbook LinkedIn × Scale VP
  (`scalevp-founder-led-growth-2025`), Robert Cialdini (`_hem3-8XbEI`, marginal).
- **Consensus** : depuis le 2026-10-25, il se compte en **nombre d'experts distincts** qui soutiennent le principe
  (les anciennes mentions « x/4 » portaient sur les 4 experts du lot 1). Galloway n'a encore **aucune ligne au
  registre** : ses chiffres sont des affirmations non vérifiées ; seuls ses points revalidés par la veille sont cités
  comme règles.
- **Veille** : `[veille:<plateforme> §x]` renvoie aux fiches `veille/plateformes/`. Une règle officielle d'une plateforme
  pèse plus qu'un avis d'expert, et la veille 2026 prime sur une fiche datée.
- **Confiance** : **haute** = confirmée par le registre ou par une source officielle de plateforme ; **moyenne** = experts
  convergents, chiffres seulement plausibles ; **faible** = un seul expert, ou chiffres invérifiables.
- **Labo** : `experiences/apprentissages.md` est **toujours vide au 2026-10-25**. Aucun principe n'est encore confirmé ou
  contredit par nos propres tests. Dès qu'un apprentissage y entre, il **prime** sur ce fichier. Expériences en attente
  qui touchent ce fichier (`experiences/index.md`) : `2026-10-22-intro-preuve-vs-promesse` (D6),
  `2026-10-22-revue-in-situ-vs-ecran-montage` (H19), `2026-10-22-sillage-signature-sonore` et
  `2026-10-22-sillage-nom-voix-off-vs-texte` (D7), `2026-10-22-cta-contenu-oui-vs-non` (H15).
- **Honnêteté** : tout chiffre d'expert est une *affirmation* (« selon X »). On n'en cite aucun comme un fait.
  **Statistiques « zombies »** (registre, leçon de la passe 4) : une statistique d'accroche sans étude nommée, datée et
  lue est refusée, même si « tout le monde la cite » (« 89 % de la pub n'est pas remarquée », V4A-T01 ; « 65 % des
  métiers de demain », V4B-DK01 ; « 80 à 90 % sans le son », P02).

## Résumé (21 principes, du plus partagé au plus isolé)

Les numéros H1 à H15 sont conservés (d'autres fichiers et des protocoles du labo les citent) ; H16 à H21 sont
ajoutés le 2026-10-25. Le classement ci-dessous suit le nombre d'experts.

| # | Principe | Consensus | Confiance |
|---|---|---|---|
| H1 | Arrête le scroll en moins de 2 s : le premier plan est déjà le moment fort | 11 + officiel | haute |
| H2 | Sois clair avant d'être original | 9 | moyenne |
| H7 | Tiens exactement la promesse de l'emballage : jamais d'appât à clic | 7 + officiel | haute |
| H9 | Préfère l'affirmation à contre-courant et le résultat chiffré réel, sans perdre la nuance | 7 | faible à moyenne |
| H20 | Relance l'attention par des boucles ouvertes, et récompense ceux qui restent | 7 | moyenne |
| H3 | Livre la valeur dans la phrase qui suit l'accroche, au bon moment | 6 | moyenne |
| H8 | Emprunte la structure des accroches qui ont marché, jamais la valeur | 6 | moyenne |
| H18 | Romps la convention du support : différent bat meilleur | 6 | moyenne |
| H4 | Parle à un inconnu à chaque contenu | 5 + officiel | moyenne |
| H14 | Produis plusieurs accroches pour le même contenu et laisse l'audience trancher | 5 + officiel | haute |
| H15 | Ferme la boucle : la fin renvoie à l'accroche ou au contenu suivant | 5 + officiel | haute |
| H10 | Retiens par l'apprentissage et la structure, pas par les effets | 5 | moyenne |
| H11 | Annonce le plan comme une boucle ouverte et traite l'objection avant qu'il parte | 5 | faible à moyenne |
| H17 | Donne un enjeu à chaque contenu, vrai et conforme à son contrat | 5 | moyenne |
| H21 | En organique, ne ressemble pas à une pub dans la première seconde, mais rends la marque indispensable au moment fort | 5 | moyenne |
| H16 | Confirme le choix dans les 10 premières secondes : promesse et preuve visibles, intro sans sommaire | 4 + officiel | moyenne |
| H5 | Aligne les trois canaux sur une seule promesse, en commençant par le visuel | 4 | moyenne |
| H13 | Supprime chaque temps mort, et fais démarrer chaque plan sur l'action | 4 | moyenne |
| H19 | Juge l'accroche à son vrai emplacement, dans le fil, jamais sur l'écran de montage | 3 | moyenne |
| H6 | Ne publie jamais une vidéo muette ; lecture possible sans le son | 1 + officiel | haute |
| H12 | Choisis une durée que le spectateur va finir | 1 + officiel | moyenne |

---

## Principes (du plus partagé au plus isolé)

### H1. Arrête le scroll en moins de 2 secondes : le premier plan est déjà le moment fort
- **Pourquoi** : le spectateur décide en quelques secondes. Instagram prédit l'abandon « en moins de 3 s » à partir des
  abandons **en moins de 2 s** ; TikTok pondère le visionnage complet comme un signal fort ; YouTube lit la performance
  en vues **engagées** (le spectateur reste au-delà des premières secondes).
- **Comment** :
  - aucun logo, carton d'intro, « Salut, je m'appelle » ou « Hey guys » en ouverture ;
  - ouvrir sur le résultat, la transformation, le geste ou la phrase la plus forte (on la cherche aussi **au montage** :
    couper l'intro pour ouvrir sur la meilleure phrase) ;
  - format court : accroche de 2 à 3 s maximum ; format long : la promesse est visible dès la première image.
- **Pour une marque sans visage (Sillage)** : le hook est une **transformation visuelle** (point → fenêtre produit,
  avant/après, révélation par masque), soulignée par un effet sonore (pop, whoosh). C'est la règle studio « accroche
  < 2 s » : elle est confirmée par la plateforme, pas seulement par le goût maison.
- **Ajouts du 2026-10-25** :
  - Google : « Start big! » : au milieu de l'action, gros plan, audio, couleur et contraste, image audacieuse dès
    l'ouverture [fiche:google-abcd-youtube-ads § A] ;
  - Trott : le vrai problème n'est pas d'être détesté mais d'être **invisible** ; l'impact passe avant la
    compréhension et la persuasion (« People must notice this advertising »). Son chiffre « 89 % de pub ni remarquée
    ni mémorisée » n'a **aucune source primaire** (registre V4A-T01) : on garde l'idée, jamais le chiffre
    [fiche:rl3SELihHqs 00:07-00:20] ;
  - Halbert : « You either hook a reader or lose him when he very first looks at your ad » [fiche:halbert-boron-letters
    ch. 19] ; le playbook Scale VP : « If it doesn't make someone pause, the rest doesn't matter »
    [fiche:scalevp-founder-led-growth-2025 p. 13] ; Vaynerchuk place les 3 premières secondes en deuxième levier de
    diagnostic, juste après la miniature [fiche:IWuVEcQexWo 00:48] ;
  - MrBeast et Galloway : voir H16 pour l'intro des vidéos longues.
- **Sources** : [fiche:HzoQgQS8czE 00:17] [fiche:Ch4Sl0POBhU 02:09] [fiche:AA1LoZwW_2Y 00:33] [fiche:uJ8Pg6t_iho 03:09]
  [fiche:google-abcd-youtube-ads § A] [fiche:rl3SELihHqs 00:07-00:20] [fiche:halbert-boron-letters ch. 19]
  [fiche:scalevp-founder-led-growth-2025 p. 13] [fiche:IWuVEcQexWo 00:48] [fiche:xf0Mli0LVgI 01:04-01:07]
  [fiche:Z2uoA3bhJT0 01:44-01:47] [veille:instagram §2.1, §8 règle 1] [veille:tiktok §0, §1] [veille:youtube §6 règle 1].
- **Consensus** : 11 experts (Yuergens, Ralston, Mino, Hormozi, Google, MrBeast, Galloway, Vaynerchuk, Trott, Halbert,
  playbook Scale VP) + règles officielles.
- **Confiance** : **haute** (registre P10 confirmé, source Meta Reels Chaining du 11/11/2025).

### H2. Sois clair avant d'être original : un inconnu comprend en une seconde ce qu'il y gagne
- **Pourquoi** : le premier défaut d'un hook n'est pas le manque d'originalité, c'est le flou. Une seule idée, des mots
  simples : le spectateur ne fait aucun effort pour comprendre.
- **Comment** :
  - écrire la promesse en une phrase avant de chercher la forme ;
  - **une seule idée** par contenu ;
  - passer le texte dans un outil de lisibilité (Hemingway ou équivalent) et couper tout mot inutile ;
  - **test de l'inconnu impitoyable** : un inconnu qui scrolle depuis une heure répondrait-il « personne n'a demandé » ?
    Si oui, réécrire (voir `frameworks/echelle-de-specificite.md`).
- **Ajouts du 2026-10-25** : test du coup d'œil et logline d'une ligne (« if it doesn't fit a logline, it's just a
  random thought ») [fiche:Z2uoA3bhJT0 00:33-00:36] ; « Don't be vague, don't be elusive, don't be cute, don't be
  clever, be clear » et la question « What did you mean by that? », dont la réponse est la phrase à garder
  [fiche:S8lH_TdQZgs 00:17-00:22] ; qualité du brief inversement proportionnelle à la longueur des mots, test de
  l'enfant de 11 ans [fiche:rl3SELihHqs 00:11, 00:46] ; clarté avant style (« the very best writing goes unnoticed »)
  [fiche:halbert-boron-letters ch. 17] ; le titre mystérieux attire du monde, pas les acheteurs
  [fiche:hopkins-scientific-advertising p. 26-27].
- **Sources** : [fiche:AA1LoZwW_2Y 00:33, 02:11] [fiche:HzoQgQS8czE 01:33-01:37] [fiche:Jmkq5RLjm0U 00:49-00:51]
  [fiche:uJ8Pg6t_iho 02:16] [fiche:Z2uoA3bhJT0 00:33-00:36] [fiche:S8lH_TdQZgs 00:17-00:22] [fiche:rl3SELihHqs 00:11,
  00:46] [fiche:halbert-boron-letters ch. 17] [fiche:hopkins-scientific-advertising p. 26-27].
- **Consensus** : 9 experts (Mino, Yuergens, Hormozi, Ralston, Galloway, Miller, Trott, Halbert, Hopkins).
- **Confiance** : **moyenne** pour le principe (très convergent). L'argument d'Ava « la plupart des Américains lisent sous
  le niveau CM2 » est **contredit** (registre G04) : ne pas le citer, garder seulement « mots simples ».

### H3. Livre la valeur dans la phrase qui suit l'accroche
- **Pourquoi** : « bury the value » est mort, c'est la patience qui baisse. Le spectateur qui part tôt doit repartir avec
  quelque chose, sinon il ne revient pas.
- **Comment** :
  - court : hook → solution immédiate en une phrase, sans contexte ni transition ;
  - long : un premier enseignement utile dans les **60 premières secondes**, sans donner d'emblée le plus gros ;
  - intro éducative : Call out → Proof → Promise → Plan → Core learning, dans l'ordre le plus fort pour ce contenu
    (`frameworks/intro-proof-promise-plan-et-4c.md`).
- **Ajout du 2026-10-25 (le « bon moment »)** : Hormozi précise dans son cadre Hook → Retain → Reward qu'on tient la
  promesse « élégamment et au bon moment » ; les trois erreurs sont de la tenir **trop tôt** (plus de raison de
  rester), **jamais**, ou de tenir **la mauvaise** [fiche:k834E6OTGTM 00:45-00:46, framework D]. Règle maison : une
  première valeur tout de suite, la plus grosse plus tard, et la promesse du titre tenue avant la fin. En long format,
  la seule durée publiée par YouTube est la carte « Intro » à **30 s** de Studio [veille:youtube §9.3].
- **Sources** : [fiche:HzoQgQS8czE 01:33] [fiche:uJ8Pg6t_iho 02:16-02:19] [fiche:AA1LoZwW_2Y 02:39] [fiche:Jmkq5RLjm0U 00:54]
  [fiche:k834E6OTGTM framework D] [fiche:Z2uoA3bhJT0 01:44-01:47] [fiche:xf0Mli0LVgI 01:04-01:07] [veille:youtube §9.3].
- **Consensus** : 6 experts (Yuergens, Ralston, Mino, Hormozi, Galloway, MrBeast).
- **Confiance** : **moyenne** (heuristiques d'expérience ; cohérent avec les signaux officiels de rétention). Les durées
  « 15-20 s maximum » pour l'accroche YouTube sont **invérifiables** (registre P11) : ne pas en faire une règle chiffrée.

### H4. Parle à un inconnu à chaque contenu (« assume nothing »)
- **Pourquoi** : si le contenu marche, c'est qu'il est vu par des inconnus. Les marques finissent par écrire pour leurs
  fans (références internes, titres centrés sur leur nom) et les nouveaux décrochent.
- **Comment** :
  - dire à chaque fois qui parle et pourquoi l'écouter **sur ce sujet** (crédibilité contextuelle) ;
  - expliquer chaque nom propre et chaque référence ; aucune blague interne ;
  - titrer par **rôle + résultat + bénéfice**, jamais par le nom de la marque ;
  - prévoir quand même des contenus de fidélisation dans le calendrier (sinon « seau percé »).
- **Pour une marque sans visage** : l'intro rituelle d'Hormozi (générique de série) se transpose **sans musique ni jingle** :
  signature visuelle animée + signature sonore en effets + une phrase fixe en voix off + un détail qui varie.
- **Ajouts du 2026-10-25** : Galloway veut une vidéo appréciable à la fois par le noyau dur, les occasionnels et les
  nouveaux (CCN), sans jamais perdre l'inconnu, mais en glissant le contexte **dans l'action** plutôt qu'en
  réintroduisant lourdement (technique « Katie ») ; il bannit « you probably saw my last video »
  [fiche:Z2uoA3bhJT0 00:21-00:27, 00:38]. Synthèse retenue entre Hormozi (se présenter à chaque fois) et Galloway :
  **contexte minimal mais systématique, intégré à l'action**. YouTube confirme en 2026 que chaque vidéo est jugée seule
  et servie hors ordre [veille:youtube §9.1] (détail : `youtube-long.md` YT1).
- **Sources** : [fiche:Jmkq5RLjm0U 01:12-01:20] [fiche:uJ8Pg6t_iho 00:55-01:01] [fiche:Ch4Sl0POBhU 02:20]
  [fiche:AA1LoZwW_2Y 02:26 (« pourquoi un inconnu regarderait-il ? »)] [fiche:Z2uoA3bhJT0 00:21-00:38]
  [fiche:xf0Mli0LVgI 00:10-00:13] [veille:youtube §1.1, §9.1].
- **Consensus** : 5 experts (Hormozi, Ralston, Mino, Galloway, MrBeast) + déclaration officielle relayée.
- **Confiance** : **moyenne**. Hormozi balaie le risque de perte de rétention par un raisonnement, sans donnée.

### H5. Aligne les trois canaux (visuel, écrit, verbal) sur une seule promesse, en commençant par le visuel
- **Pourquoi** : le feed est saturé et le son n'est pas garanti. Un hook travaillé sur un seul canal gaspille les deux
  autres.
- **Comment** :
  1. **visuel** (priorité 1) : sans son ni texte, l'image donne-t-elle envie de rester ? Pas besoin d'effet spectaculaire
     (un geste, un avant/après, une plongée, une révélation) ;
  2. **écrit** : très court, lisible en moins d'1 s, hors des zones d'interface ;
  3. **verbal** : la première phrase porte la promesse ;
  4. les trois disent la même chose, sans se répéter mot pour mot.
- **Pour une marque sans visage** : le visuel **est** le hook ; l'écrit tient en ~5 mots (règle Sillage : 3-4 messages par
  vidéo) ; le verbal n'existe que s'il y a une voix off. Le premier mouvement est synchronisé à un effet sonore.
- **Ajout du 2026-10-25** : Google demande que la marque soit à la fois **visible et audible** (YouTube est « almost
  entirely a sound-on experience », registre PA28 confirmé : 95 % des pubs YouTube audibles, définition peu exigeante)
  [fiche:google-abcd-youtube-ads § A, § B]. Pour la place de la musique, voir D7.
- **Sources** : [fiche:HzoQgQS8czE 00:17-00:20] [fiche:AA1LoZwW_2Y 00:33] [fiche:uJ8Pg6t_iho 01:54]
  [fiche:google-abcd-youtube-ads § A, § B] ; `frameworks/hook-trois-canaux.md`.
- **Consensus** : 4 experts (Yuergens, Mino, Ralston via le « wrapping paper », Google).
- **Confiance** : **moyenne** pour l'alignement ; **faible** pour « le visuel est devenu le plus important » (registre P19).
  Attention : la justification d'Ava, « 80 à 90 % regardent sans le son », est **contredite** (registre P02). Voir H6.

### H6. Ne publie jamais une vidéo muette ; prévois une lecture possible sans le son, sans concevoir pour le muet
- **Pourquoi** : c'est la **correction** d'une croyance répandue. Le « 85 % sans le son » date de Facebook en 2016. Sur
  Instagram, les Reels muets sont officiellement moins diffusés et la part de visionnage **avec le son** entre dans le
  classement ; sur TikTok, 88 % des utilisateurs jugent le son essentiel (enquête Kantar pour TikTok).
- **Comment** :
  - toujours une piste audio (voix et/ou effets sonores), publiée comme **son original** nommé ;
  - le sens reste compréhensible sans le son (visuel autoportant, ou sous-titres sobres s'il y a une voix off) ;
  - LinkedIn : sous-titres incrustés recommandés officiellement quand il y a une voix.
- **Pour une marque sans visage** : les effets sonores synchronisés **sont** un audio au sens des plateformes. Jamais de
  musique (règle Sillage) : aucune pénalité officielle constatée, et aucun risque de droits ni de blocage Content ID.
- **Ajout du 2026-10-25** : Google fait de l'audio (voix off, effets sonores, musique) un levier d'attention et de
  marque ; « audio is your superpower » en notoriété, avec une insistance sur la **voix humaine**
  [fiche:google-abcd-playbook-2022 p. 12]. Ce qu'on en garde et ce qu'on refuse (la musique chez Sillage) : D7.
- **Sources** : [registre:P02] [registre:PA28] [veille:instagram §5, §8 règle 6] [veille:tiktok §8] [veille:linkedin §2.4, §7 règle 19]
  [veille:youtube §6 règle 6] [fiche:google-abcd-youtube-ads § A] [fiche:google-abcd-playbook-2022 p. 12].
- **Consensus** : un expert (Google) ; Ava dit l'inverse. **La veille et le registre tranchent.**
- **Confiance** : **haute** sur « muet = moins diffusé » (officiel Instagram) ; moyenne sur le reste.

### H7. Tiens exactement la promesse de l'emballage : jamais d'appât à clic
- **Pourquoi** : en éducation, le spectateur vérifie que la vidéo tient la promesse du clic. YouTube pondère le temps de
  visionnage par la **satisfaction** (sondages, regret) et son test A/B choisit le gagnant au **temps de visionnage**,
  pas au CTR. Une curiosité trompeuse gagne un clic et perd la suite.
- **Comment** :
  - miniature, titre, couverture et première slide disent **exactement** ce que le contenu livre ;
  - la curiosité reste permise **dans la structure** (boucle ouverte, « ça va paraître contre-intuitif »), jamais comme
    fausse promesse ;
  - relire le contenu final contre l'emballage avant publication (`controleur-qualite-marketing`).
- **Ajouts du 2026-10-25** :
  - MrBeast : le spectateur doit être convaincu de **tout** ce que promettent le titre et la miniature (« look, I
    promise what I put in the title thumbnail is real ») ; plus la promesse est grosse, plus la preuve doit être lourde
    [fiche:xf0Mli0LVgI 01:04-01:07] ; Galloway : les 10 premières secondes disent « you made the right choice »
    [fiche:Z2uoA3bhJT0 01:47] ;
  - Halbert : l'attention doit être **du bon type**, reliée à l'offre et justifiée tout de suite ; « A Submarine That
    Flies? … No » est « a cheap shot. People resent this kind of fraud » [fiche:halbert-boron-letters ch. 14] ;
  - Hopkins : un titre mystérieux attire du monde, mais les vrais prospects ne comprennent pas qu'il les concerne
    [fiche:hopkins-scientific-advertising p. 26-27] ;
  - contre-exemple : un titre qui emprunte une autorité (« Harvard, FBI, GIGN ») que le contenu n'étaye pas
    [fiche:aGI7puAXf6w, Leçons de format 6] ;
  - la règle complète du couple titre + miniature est dans `packaging.md` K1.
- **Sources** : [fiche:Jmkq5RLjm0U 00:49-00:53] [fiche:Ch4Sl0POBhU 02:09] [fiche:uJ8Pg6t_iho 01:54]
  [fiche:xf0Mli0LVgI 01:06] [fiche:Z2uoA3bhJT0 01:47] [fiche:halbert-boron-letters ch. 14]
  [fiche:hopkins-scientific-advertising p. 26-27] [fiche:aGI7puAXf6w] [veille:youtube §1.1, §2.1, §6 règle 2].
- **Consensus** : 7 experts (Hormozi, Ralston, MrBeast, Galloway, Halbert, Hopkins, Despas en contre-exemple) + règle
  officielle YouTube.
- **Confiance** : **haute** (source officielle YouTube, revalidée le 2026-10-22).

### H8. Emprunte la structure des accroches qui ont déjà marché, jamais la valeur
- **Pourquoi** : chaque niche contient déjà des accroches validées par le marché. Inventer seul revient à parier ; copier la
  valeur ruine la crédibilité et, depuis 2026, l'éligibilité (originalité exigée par Instagram, TikTok et YouTube Shorts).
- **Comment** :
  - tenir la **bibliothèque d'emballages** (`swipe-file/hooks.md`) : capturer chaque semaine ce qui accroche, **y compris
    hors de la niche et l'absurde**, puis le transformer en gabarit avec sa mécanique ;
  - repérer les outliers (contenu qui surperforme par rapport à la taille **ou** à la moyenne du compte) ;
  - remplir le gabarit avec **sa propre** expertise, ses résultats réels, ou au moins 3 sources recoupées ;
  - jamais de repost, de compilation ni de texte repris.
- **Ajouts du 2026-10-25** : Galloway relève les outliers à au moins **3× la moyenne de leur chaîne** (niche et niches
  adjacentes), puis écrit « my spin / my twist » pour chacun ; il tient des playlists d'étude revues 3 à 5 h par semaine
  [fiche:Z2uoA3bhJT0 00:40-00:52, 02:33] ; Koe réutilise la structure des posts qui marchent comme « soft structure »,
  jamais leur texte (« imitate then innovate ») [fiche:SUzKZfyaAK8 02:01-02:03] ; Leloup relit des annonces vintage
  quand l'angle manque [fiche:1N2XALudegQ 00:00-00:33] ; Halbert recopie à la main et lit à voix haute les textes
  gagnants [fiche:halbert-boron-letters ch. 16-17, ch. 22]. Toujours préciser la base d'un outlier (moyenne de la
  chaîne, médiane, abonnés) et la plateforme.
- **Sources** : [fiche:HzoQgQS8czE 00:16, 00:41, 01:58] [fiche:uJ8Pg6t_iho 01:54-02:05] [fiche:Ch4Sl0POBhU 02:00]
  [fiche:Z2uoA3bhJT0 00:40-00:52, 02:33] [fiche:SUzKZfyaAK8 02:01-02:03] [fiche:1N2XALudegQ 00:00-00:33]
  [fiche:halbert-boron-letters ch. 10, ch. 16-17] [veille:instagram §3] [veille:tiktok §3] [veille:youtube §1.1].
- **Consensus** : 6 experts (Yuergens, Ralston, Galloway, Koe, Leloup, Halbert) ; Hormozi nuance (packaging clair).
  Ralston rejette la **copie assistée par IA** des vidéos concurrentes : la règle commune est « structure empruntée,
  valeur propre » (`ia-creation.md`).
- **Confiance** : **moyenne** (seuils « 3x » et « 5x » empiriques) ; **haute** pour l'interdiction du repost (officielle).

### H9. Préfère l'affirmation à contre-courant et le résultat chiffré réel, sans perdre la nuance
- **Pourquoi** : ce sont les deux types d'accroche que les experts citent comme les plus efficaces. Le contre-courant fait
  réagir ; le résultat chiffré répond tout de suite à « pourquoi t'écouter ? ».
- **Comment** :
  - ordre de préférence (Ralston) : affirmation à contre-courant > rupture de schéma > question qui fait réfléchir >
    fait inattendu (« un peu usé ») ;
  - résultat **précis**, chiffré et daté (« de [A] à [B] en [durée] ») ;
  - contrarien = conviction sincère ; **controversé** (fait pour choquer) = interdit ;
  - toute variable chiffrée est une **donnée réelle et vérifiée** de la marque. À défaut de résultat, la preuve par le
    labeur (« nous avons décortiqué [N] lancements ») si N est vrai.
- **Ajouts du 2026-10-25** :
  - précision : un chiffre exact est cru, un superlatif fait décompter toutes les autres affirmations ; un chiffre non
    rond suggère un test réel, à condition qu'il **le soit** [fiche:hopkins-scientific-advertising p. 37-40] ; Koe
    accroche par le problème, les nombres et les statistiques, mais ses propres statistiques sont fausses ou sans
    source (V4B-DK01 contredit, V4B-DK02 invérifiable, « 99 % de regrets » non sourcé) [fiche:SUzKZfyaAK8 framework J] ;
  - contre-courant mesuré : le playbook Scale VP vise la « prolific zone » entre l'évident et le délirant, avec un
    thermomètre de 10 à 30 % de commentaires négatifs (repère de Gal Aga, non vérifié)
    [fiche:scalevp-founder-led-growth-2025 p. 15] ; Raskin donne une famille d'accroches « Goodbye X, hello Y »
    [fiche:U1b1o-m5bpI framework A] ;
  - **limite de nuance** (Welsh) : le ton outrancier « marche » aujourd'hui mais supprime la nuance et fait perdre la
    confiance (« when I see someone remove nuance from a topic that requires nuance… I just lose trust »)
    [fiche:DJLtwT1Z0eo 00:32-00:34]. Voir D10.
- **Sources** : [fiche:Ch4Sl0POBhU 02:09] [fiche:uJ8Pg6t_iho 00:22] [fiche:Jmkq5RLjm0U 00:54, 02:36]
  [fiche:HzoQgQS8czE 01:39] [fiche:AA1LoZwW_2Y 01:16] [fiche:hopkins-scientific-advertising p. 37-40]
  [fiche:SUzKZfyaAK8 01:23-01:26, 01:58-02:00] [fiche:scalevp-founder-led-growth-2025 p. 15] [fiche:DJLtwT1Z0eo 00:32-00:34]
  [registre:V4A-T01, V4B-DK01, V4B-DK02].
- **Consensus** : 7 experts sur le résultat précis et réel (Ralston, Hormozi, Yuergens, Mino, Hopkins, Koe, playbook
  Scale VP) ; 1 sur le classement des types (Ralston) ; Welsh pose la limite de nuance.
- **Confiance** : **faible à moyenne** (opinions d'expérience, aucune donnée comparative).

### H10. Retiens par l'apprentissage et la structure, pas par l'accumulation d'effets
- **Pourquoi** : en éducatif, « le meilleur hack de rétention, c'est que l'audience apprenne ». Selon Hormozi, 9 de ses
  12 meilleurs Reels misaient sur le message, 8 des 12 pires sur les effets (affirmation, n = 24).
- **Comment** :
  - hiérarchie : hook > script > format > montage ; le montage amplifie, il ne remplace pas ;
  - chaque effet doit **servir la compréhension** (texte clarifiant, schéma, visualisation de données) ou le moment fort ;
  - le rythme vient de l'**information nouvelle**, pas d'un effet ajouté à intervalle fixe.
- **Pour une marque sans visage** : c'est la règle Sillage « un seul vrai moment waouh, construit et mis en scène » ;
  pas d'effets partout, pas d'hyper-cut.
- **Ajouts du 2026-10-25** : Hormozi résume la rétention par « listes, étapes, histoires » (Retain) [fiche:k834E6OTGTM
  framework D] ; Despas structure chaque vidéo en « technique + parade » avec des relances entre les items
  [fiche:aGI7puAXf6w, Leçons de format 1-2] ; Hopkins : une image ou un effet ne se justifie que s'il argumente mieux que
  le même espace en texte (« they forget they are salesmen and try to be performers »)
  [fiche:hopkins-scientific-advertising p. 15, p. 45]. Pour la vidéo longue : `youtube-long.md` YT4.
- **Sources** : [fiche:Jmkq5RLjm0U 00:56-01:00] [fiche:uJ8Pg6t_iho 02:15] [fiche:HzoQgQS8czE 00:20]
  [fiche:k834E6OTGTM framework D] [fiche:aGI7puAXf6w] [fiche:hopkins-scientific-advertising p. 15, p. 45].
- **Consensus** : 5 experts (Hormozi, Ralston, Yuergens, Despas, Hopkins) contre Mino (voir désaccord D2).
- **Confiance** : **moyenne** pour le principe ; **faible** pour le chiffre 9/12 (registre C16).

### H11. Annonce le plan comme une boucle ouverte et traite l'objection du spectateur avant qu'il parte
- **Pourquoi** : annoncer la structure réduit l'incertitude ; nommer l'objection, avec les mots du spectateur, crée la
  proximité et désamorce la raison de partir.
- **Comment** :
  - long : « Il y a [N] étapes, je vais les détailler » (Plan / Compass), formulé comme une **promesse à suspense**
    (« …et la troisième va contre tout ce qu'on vous a dit »), jamais comme une table des matières (« In this video
    we're going to cover this, this and this », que Galloway bannit) [fiche:Z2uoA3bhJT0 01:47-01:50] (D8) ;
  - lever l'**objection suivante** juste après la preuve (MrBeast : « vont-ils juste rester plantés là ? », réponse par
    la règle et l'enjeu) [fiche:xf0Mli0LVgI framework A] ;
  - court : hook → solution → « Je sais, tu te dis sûrement que… » → réponse chiffrée → retour au hook ;
  - long et court : traiter dans le contenu les objections récurrentes relevées en commentaires.
- **Sources** : [fiche:Jmkq5RLjm0U 00:54] [fiche:uJ8Pg6t_iho 02:16] [fiche:AA1LoZwW_2Y 01:09, 02:39]
  [fiche:Ch4Sl0POBhU 00:21-00:25] [fiche:Z2uoA3bhJT0 01:47-01:50] [fiche:xf0Mli0LVgI 01:05-01:06] ;
  `frameworks/script-educatif-court.md`, `frameworks/message-a-mon-moi-passe.md`.
- **Consensus** : 5 experts (Hormozi, Ralston, Mino, MrBeast, Galloway sur la forme du plan).
- **Confiance** : **faible à moyenne** (heuristiques, petit échantillon : les 35 vidéos d'Hormozi).

### H12. Choisis une durée que le spectateur va finir
- **Pourquoi** : la complétion est jugée **par rapport aux vidéos de même durée** (Instagram) ; finir une vidéo longue est un
  signal fort (TikTok). Une vidéo de 12 s vue en entier vaut mieux qu'une vidéo de 40 s abandonnée à mi-chemin.
- **Comment** :
  - écrire la durée cible dans le script ;
  - TikTok (étude Socialinsider 2026, 6 M de vidéos) : **15-30 s** pour l'engagement (démo, pub, logo), **60-180 s** pour
    l'éducatif ou le making-of ; éviter 30-60 s sans raison ;
  - Instagram : aussi court que le message le permet, jamais plus de 3 min (au-delà, pas de recommandation aux
    non-abonnés) ; cible Sillage 8-30 s, 60 s maximum pour un making-of ;
  - LinkedIn : 20-60 s, 90 s maximum en organique ;
  - format long : relance visuelle ou sonore toutes les 5 à 8 s, et une boucle possible (le dernier plan raccorde au
    premier).
- **Sources** : [veille:instagram §2.1, §8 règle 2] [veille:tiktok §4, §13] [veille:linkedin §7 règle 17]
  [fiche:HzoQgQS8czE 01:39 (réponse en moins de 60 s)] [fiche:AA1LoZwW_2Y 02:26 (boucle)].
- **Ajout du 2026-10-25** : MrBeast rappelle que le rythme dépend du « contrat d'attention » de la plateforme (« what
  in YouTube you have to do in 20 seconds, in streaming you can do in 3 minutes ») **[DATÉ]** ; les « 20 s » n'ont
  aucune source YouTube [fiche:xf0Mli0LVgI 01:07] [veille:youtube §9.2]. YouTube ne publie aucune durée idéale pour le
  long format : la durée suit la matière, jamais rallongée pour « plaire à la TV » (`youtube-long.md` YT9).
- **Consensus** : la veille porte ce principe ; les experts ne se prononcent que par format (MrBeast sur le contrat
  d'attention).
- **Confiance** : **moyenne** (officiel pour le mécanisme, études corrélationnelles pour les tranches).

### H13. Supprime chaque temps mort, et fais démarrer chaque plan sur l'action
- **Pourquoi** : un blanc, une respiration ou un plan statique qui « ressemble à une photo » fait décrocher. Couper les
  micro-silences ne fait gagner que quelques secondes, mais change le rythme perçu.
- **Comment** :
  - dérushage au mot près, pauses coupées ;
  - un plan par phrase ou demi-phrase, qui colle au propos et démarre en mouvement ;
  - sous-titres d'une ligne, ~4 mots, hors des zones d'interface (valeurs à jour dans `veille/plateformes/`).
- **Pour une marque sans visage** : en motion design, « démarrer sur l'action » = courbes easeOut et springs dès la
  première image, aucun élément figé ; pas de B-roll « aléatoire » : chaque plan sert le message.
- **Ajouts du 2026-10-25** : MrBeast relit son montage en cherchant ce qu'on regarderait « en vitesse ×2 » et le coupe
  [fiche:xf0Mli0LVgI 00:59] ; Galloway bannit les marqueurs de conclusion (« at the end of the day ») hors de la vraie
  fin : ils font partir tout le monde [fiche:Z2uoA3bhJT0 01:42] ; en long, chaque dip de la courbe de rétention est
  noté avec la phrase ou le plan en cause [veille:youtube §9.3].
- **Sources** : [fiche:AA1LoZwW_2Y 02:04-02:07, 01:26] [fiche:HzoQgQS8czE 00:21] [fiche:xf0Mli0LVgI 00:59]
  [fiche:Z2uoA3bhJT0 01:42] [veille:youtube §9.3] ; `frameworks/montage-court-clarte-et-vitesse.md`.
- **Consensus** : 4 experts (Mino, Yuergens, MrBeast, Galloway).
- **Confiance** : **moyenne** pour le principe ; **faible** pour les seuils « quelque chose toutes les 3 s », « blanc de
  0,5 s » (registre P37).

### H14. Produis plusieurs accroches pour le même contenu, et laisse l'audience trancher
- **Pourquoi** : on ne sait pas d'avance quelle accroche gagne. Ralston passe environ 12 h sur un hook ; Mino tourne 2 ou
  3 variantes d'affilée ; les plateformes fournissent désormais des outils natifs de test.
- **Comment** :
  - au moins 15 variantes écrites, notées par `critique-hook`, 2 ou 3 retenues ;
  - Instagram : publier les variantes en **Trial Reels** (non-abonnés seulement), puis mettre à niveau la gagnante ;
  - YouTube long : 3 paires titre + miniature dans **Test & Compare** ; la **variante n°1 est notre favorite** (elle reste
    si le test n'est pas concluant) ; ne rien modifier pendant le test (détail : `packaging.md` K5) ;
  - Shorts et vidéos verticales de 3 min ou moins : **non testables** nativement ; le test de **montages** (3 accroches)
    n'arrivera qu'en 2027 pour une sélection de créateurs : d'ici là, variantes publiées séparément et consignées dans
    `experiences/` [veille:youtube §6 règle 20] ;
  - LinkedIn (playbook Scale VP) : observer les 15 à 30 premières minutes et réécrire l'accroche si le post décroche
    (repère de 1 à 2 likes par minute d'un compte à environ 700 000 lecteurs par semaine, **inapplicable tel quel**)
    [fiche:scalevp-founder-led-growth-2025 p. 13] ;
  - logique de Hopkins : tester les angles **par l'accroche, à corps constant** [fiche:hopkins-scientific-advertising
    p. 28-29] ;
  - protocole et lecture des résultats : `analyse-et-iteration.md` (A10).
- **Sources** : [fiche:uJ8Pg6t_iho 04:11] [fiche:AA1LoZwW_2Y 02:07] [fiche:Z2uoA3bhJT0 01:14-01:21]
  [fiche:hopkins-scientific-advertising p. 28-29] [fiche:scalevp-founder-led-growth-2025 p. 13]
  [veille:instagram §4 Trial Reels, §8 règle 9] [veille:youtube §2.1, §6 règles 3-4 et 20].
- **Consensus** : 5 experts (Ralston, Mino, Galloway, Hopkins, playbook Scale VP) + outils officiels.
- **Confiance** : **haute** pour les outils (officiels) ; moyenne pour le volume de variantes.

### H15. Ferme la boucle : la fin renvoie à l'accroche ou au contenu suivant, jamais à « like et abonne-toi »
- **Pourquoi** : une fin qui reboucle sur le début favorise la relecture ; une fin qui mène au contenu suivant prolonge la
  session. Demander des likes fait chuter les interactions sur TikTok (−60 % selon Metricool) et peut rendre le contenu
  inéligible (manipulation) ; LinkedIn pénalise les appâts à engagement.
- **Comment** :
  - conclusion qui reprend le hook en une phrase ; dernier plan qui raccorde au premier ;
  - transition vers la suite (« si tu as aimé ceci, regarde cela ») ou question ouverte sur le sujet ;
  - le CTA de conversion se règle ailleurs (voir `monetisation-et-offre.md` et `communaute.md`).
- **Ajouts du 2026-10-25** : Despas récompense ceux qui restent par un **bonus** final (« si vous êtes encore là… ») et
  transforme une liste de 10 en **une** action (le défi du post-it) [fiche:aGI7puAXf6w, Leçons de format 2 et 4] ;
  Welsh termine par une question à méditer et un appel explicite à répondre, honnête sur ses limites (« I can't reply
  to every single email that I get, but I read them all ») [fiche:DJLtwT1Z0eo framework D]. Le CTA « abonne-toi,
  sinon like » de Despas (grosse demande puis petite) relève de l'ancrage : à éviter sur TikTok (manipulation, règle
  officielle). Expérience en attente sur la forme du CTA final : `2026-10-22-cta-contenu-oui-vs-non`.
- **Sources** : [fiche:AA1LoZwW_2Y 02:44] [fiche:Jmkq5RLjm0U 00:37] [fiche:uJ8Pg6t_iho 02:20] [fiche:aGI7puAXf6w]
  [fiche:DJLtwT1Z0eo framework D] [veille:tiktok §3, §13] [veille:linkedin §2.3].
- **Consensus** : 5 experts (Mino, Hormozi, Ralston, Despas, Welsh) + règles officielles TikTok et LinkedIn.
- **Confiance** : **haute** pour l'interdit (officiel) ; moyenne pour la boucle.

### H16. Confirme le choix dans les 10 premières secondes : promesse et preuve visibles, intro sans sommaire (ajout 2026-10-25)
- **Pourquoi** : tous les experts de la vidéo longue veulent que le spectateur sache très vite qu'il a bien choisi.
  MrBeast : « A big problem with my YouTube videos is people just don't think they're real » ; il prouve d'abord la
  réalité de la promesse (les 100 paires de jumeaux, l'argent réel), lève l'objection suivante, et seulement ensuite
  prend « permission to slow down » [fiche:xf0Mli0LVgI 01:04-01:07]. Galloway : tenir la promesse du titre et de la
  miniature dans les 10 premières secondes, en image si possible, puis intrigue avec le minimum de contexte, intro de
  moins de 45 s [fiche:Z2uoA3bhJT0 01:43-01:52]. Hormozi : Proof-Promise-Plan en éducatif, « why should I listen to
  you? » [fiche:Jmkq5RLjm0U 00:54] ; Ralston : premier enseignement dans les 60 s [fiche:uJ8Pg6t_iho 02:16-02:19].
- **Comment** :
  1. dans les 10 premières secondes : la promesse **et** une preuve visible (résultat montré, chiffre réel, démonstration) ;
     l'ordre des deux est le désaccord D6, en test ;
  2. « The best intro doesn't feel like an intro. It just feels like the video started » : pas de « Today we sat down
     with X », pas de « Um, anyway, let's get into it » ; une phrase-pont écrite en dernier [fiche:Z2uoA3bhJT0 01:49-01:50] ;
  3. le mot « réel » peut devancer le doute quand la promesse est extraordinaire (« I am standing on $5 million of real
     money ») ; plus la promesse est grosse, plus la preuve est lourde ;
  4. lecture officielle : carte « Intro » de Studio (part encore là **après 30 s**) et dips, par rapport à nos vidéos
     de même durée [veille:youtube §9.3] ; les « 20 s » (MrBeast), « 45 s » et « 60-70 % perdus en 10 s » (Galloway)
     sont des repères de praticien sans source YouTube.
- **Pour une marque sans visage (Sillage)** : la preuve est **en image** dès le premier plan : le produit réel, le rendu,
  l'avant/après. Aucun composite qui pourrait passer pour une prise de vue réelle sans signalement (`ia-creation.md` I5).
- **Sources** : [fiche:xf0Mli0LVgI 01:04-01:07, framework A] [fiche:Z2uoA3bhJT0 01:43-01:52, framework Q]
  [fiche:Jmkq5RLjm0U framework I] [fiche:uJ8Pg6t_iho 02:16-02:19] [veille:youtube §6 règle 19, §9.3].
- **Consensus** : 4 experts + outil officiel de lecture. Détail long format : `youtube-long.md` YT2.
- **Confiance** : **moyenne** (convergence forte sur le but ; durées non officielles sauf les 30 s de Studio).

### H17. Donne un enjeu à chaque contenu, vrai et conforme à son contrat (ajout 2026-10-25)
- **Pourquoi** : « People don't care unless you make them care » [fiche:Z2uoA3bhJT0 01:59]. Un enjeu donne une raison
  de rester jusqu'au résultat ; un dilemme que le spectateur se pose à lui-même fait parler le lendemain
  [fiche:xf0Mli0LVgI 00:07-00:08].
- **Comment** :
  - choisir parmi les cinq enjeux de Galloway (adversaire ou sceptique, limite de temps, récompense, punition, peur de
    rater), ou poser une **règle simple avec sanction** (« if either twin crosses the red line they'll both be
    eliminated ») [fiche:Z2uoA3bhJT0 framework R] [fiche:xf0Mli0LVgI framework A] ;
  - pour un contenu informatif : le coût réel de l'inattention, chiffré et sourcé, jamais un gadget ;
  - poser la fin heureuse **et** ce qui arrive si rien ne change, sans peur infondée [fiche:S8lH_TdQZgs 00:42-00:44] ;
    en B2B, relier le sujet à « qui gagne, qui perd » sur le marché [fiche:U1b1o-m5bpI framework A] ;
  - escalader d'une partie à l'autre (« la prochaine est beaucoup plus méchante ») [fiche:aGI7puAXf6w] ;
  - **vrai** : aucun sceptique inventé, aucun défi mis en scène présenté comme réel.
- **Sources** : [fiche:Z2uoA3bhJT0 01:57-02:01] [fiche:xf0Mli0LVgI 00:07-00:08, 01:05] [fiche:S8lH_TdQZgs 00:42-00:44]
  [fiche:U1b1o-m5bpI 00:25-00:27] [fiche:aGI7puAXf6w, Leçons de format 2]. Récit : `storytelling.md` ST4.
- **Consensus** : 5 experts. **Confiance** : **moyenne**.

### H18. Romps la convention du support : différent bat meilleur (ajout 2026-10-25)
- **Pourquoi** : « The mind is a pattern machine » : une vingtième pub semblable se fond dans le papier peint, une forme
  différente se détache (« not by being better, just by being different », chiffres illustratifs que Trott dit lui-même
  incertains) [fiche:rl3SELihHqs 00:21-00:26]. Sugarman ouvre un catalogue en démolissant son propre produit, et
  **nomme** l'attente avant de la contredire (« Vous vous attendez probablement à notre pitch habituel… »)
  [fiche:1N2XALudegQ 03:17-04:24]. Ralston classe la rupture de schéma juste après l'affirmation à contre-courant (H9) ;
  Koe utilise les nombres comme « pattern interrupt » dans un fil chargé [fiche:SUzKZfyaAK8 01:24-01:25] ; Halbert
  agrafe un objet en tête de lettre, relié au message [fiche:halbert-boron-letters ch. 11, ch. 14] ; Vaynerchuk annonce
  un secret puis tombe sur une chute brutale [fiche:IWuVEcQexWo framework I].
- **Comment** :
  1. relever la convention du support (ce que tout le fil ou toute la niche fait à cet endroit), puis choisir une forme
     qui n'y ressemble pas, sans viser la meilleure version de la même chose ;
  2. la rupture **sert le message** (elle annonce le sujet) et repose sur des faits réels : défauts avoués réels, rejet
     initial réel (`storytelling.md` ST13) ; jamais de fausse notification ni de faux élément d'interface ;
  3. pour une marque premium, éviter l'autodénigrement fort (« détruire sans pitié ») : la rupture passe par la forme
     (cadrage, rythme, silence) plutôt que par le dénigrement.
- **Sources** : [fiche:rl3SELihHqs 00:21-00:26, framework G] [fiche:1N2XALudegQ 03:17-04:24, framework A]
  [fiche:Ch4Sl0POBhU 02:09] [fiche:SUzKZfyaAK8 01:24-01:25] [fiche:halbert-boron-letters ch. 11, ch. 14]
  [fiche:IWuVEcQexWo framework I] ; swipe-file `hooks.md` § 11 (rupture de schéma).
- **Consensus** : 6 experts (Trott, Leloup, Ralston, Koe, Halbert, Vaynerchuk). **Confiance** : **moyenne** (aucune
  mesure ; l'efficacité de l'annonce MagicStat n'est pas démontrée, registre V4A-M05).

### H19. Juge l'accroche à son vrai emplacement, dans le fil, jamais sur l'écran de montage (ajout 2026-10-25)
- **Pourquoi** : « Everything only works in context » : on juge les pubs à la table du conseil, en plein écran et
  attentivement, alors qu'elles sont vues en passant, entourées de « 50 other identical things » ; une annonce vide
  domine son vrai emplacement, une annonce chargée devient du papier peint [fiche:rl3SELihHqs 00:48-00:51]. Galloway fait
  regarder quelqu'un faire défiler YouTube sur une TV ou un téléphone [fiche:Z2uoA3bhJT0 framework E] ; Halbert juge le
  pli au premier regard, dans la pile du courrier [fiche:halbert-boron-letters ch. 11, ch. 19].
- **Comment** : maquetter chaque accroche ou couverture dans un vrai fil (Instagram, TikTok, LinkedIn, page d'accueil
  YouTube sur téléphone **et** sur TV), entre des contenus réels ; demander à des non-professionnels « de quelle marque
  était-ce ? » ; refuser le remplissage qui fait rentrer le contenu dans le papier peint.
- **Sources** : [fiche:rl3SELihHqs 00:48-00:51, framework K] [fiche:Z2uoA3bhJT0 00:33-00:39, framework E]
  [fiche:halbert-boron-letters ch. 11, ch. 19].
- **Consensus** : 3 experts. **Confiance** : **moyenne** ; expérience en attente `2026-10-22-revue-in-situ-vs-ecran-montage`
  (Sillage en priorité).

### H20. Relance l'attention par des boucles ouvertes, et récompense ceux qui restent (ajout 2026-10-25)
- **Pourquoi** : une boucle ouverte donne une raison de rester jusqu'à sa fermeture. Despas place un teaser entre
  chaque item, relance à mi-parcours et récompense la fin par un bonus [fiche:aGI7puAXf6w, Leçons de format 2] ;
  Galloway remplace le sommaire par des boucles et distille le contexte [fiche:Z2uoA3bhJT0 01:47-01:50] ; Sugarman ne
  ferme son « …jusqu'à ce que » qu'après la liste des défauts [fiche:1N2XALudegQ 02:44-03:50] ; MrBeast finit l'épisode
  d'avant le seuil sur un cliffhanger visuel [fiche:xf0Mli0LVgI framework C] ; Miller : « open a story loop, the
  product closes the story loop » [fiche:S8lH_TdQZgs 00:57] ; Yuergens coupe une étape en pleine phrase, Mino annonce
  le paradoxe (D3).
- **Comment** : une boucle par transition (« la prochaine, vous n'en avez jamais entendu parler ») ; toute boucle ouverte
  est **fermée** dans le même contenu (sinon promesse non tenue, H7) ; le bonus final est réel et livré.
- **Sources** : [fiche:aGI7puAXf6w] [fiche:Z2uoA3bhJT0 01:47-01:50] [fiche:1N2XALudegQ 02:44-03:50]
  [fiche:xf0Mli0LVgI framework C] [fiche:S8lH_TdQZgs 00:57] [fiche:HzoQgQS8czE] [fiche:AA1LoZwW_2Y] ;
  swipe-file `hooks.md` § 1 (curiosité / boucle ouverte).
- **Consensus** : 7 experts. **Confiance** : **moyenne** (aucune donnée comparative).

### H21. En organique, ne ressemble pas à une pub dans la première seconde, mais rends la marque indispensable au moment fort (ajout 2026-10-25)
- **Pourquoi** : deux constats qui se complètent. (1) Ce qui a l'air de vendre est trié et jeté : « Our first objective
  is to get our envelope into the "A" pile » [fiche:halbert-boron-letters ch. 11] ; la belle écriture publicitaire
  « révèle l'hameçon » [fiche:hopkins-scientific-advertising p. 13] ; un post qui se lit comme une brochure perd face à
  une histoire [fiche:scalevp-founder-led-growth-2025 p. 10]. (2) Mais un fort impact sans marque identifiable est un
  échec (« Who was that even for? ») [fiche:rl3SELihHqs 00:16-00:20], et une histoire dont on peut retirer la marque se
  partage sans elle [fiche:FN4eDk1pq6U 00:25-00:29].
- **Comment** : pas de logo en ouverture, pas de ton de réclame ; le produit ou la marque est **dans** le moment fort
  (la transformation, l'objet, le geste), pas plaqué à côté. En **publicité payante**, la règle de Google s'applique :
  marque tôt, souvent, sous plusieurs formes (D9).
- **Pour Sillage** : le produit est le moment fort ; le logo arrive en signature à la fin (tableau ci-dessous) ;
  la signature d'effets sonores et le nom en voix off sont en test comme repères d'attribution (D7).
- **Sources** : [fiche:halbert-boron-letters ch. 11, ch. 18] [fiche:hopkins-scientific-advertising p. 13]
  [fiche:scalevp-founder-led-growth-2025 p. 10] [fiche:rl3SELihHqs 00:16-00:20] [fiche:FN4eDk1pq6U 00:25-00:29]
  [fiche:google-abcd-youtube-ads § B].
- **Consensus** : 5 experts ; Google défend l'inverse pour la pub (D9). **Confiance** : **moyenne**.

---

## Désaccords entre experts

### D1. Largeur de l'accroche : spécifique (Mino) ou large (Ava) ?
- **Mino Lee** : la spécificité fait la viralité ; viser tout le monde est « la pire façon » de faire un hook. On ajoute
  contexte, émotion précise et chiffre jusqu'à ce que la cible se dise « c'est moi » [fiche:AA1LoZwW_2Y 02:13].
- **Ava Yuergens** : en organique, un hook de niche (« Tu habites à [petite ville] ? ») fait scroller tout le monde et tue
  le temps de visionnage. Hook large, valeur ciblée, CTA de niche [fiche:HzoQgQS8czE 01:38].
- **Recommandation de l'agence** : les deux ont raison sur des choses différentes.
  - Rendre l'accroche spécifique par la **situation, l'émotion ou le chiffre** (beaucoup de gens de la cible s'y
    reconnaissent) ;
  - ne jamais la rendre étroite par **exclusion géographique, administrative ou de métier rare** en organique : ce filtre
    va dans le CTA ;
  - en **publicité payante**, le ciblage est fait par l'achat : l'accroche peut et doit être spécifique.
  - Statut : déduction à tester (`concepteur-experiences`).

### D2. Rythme de montage : stimuler toutes les 3 secondes (Mino) ou couper les effets (Ralston, Hormozi) ?
- **Mino Lee** : quelque chose de nouveau à l'écran au moins toutes les 3 s, hyper-cut de plans de moins d'1 s sur la
  première phrase, B-roll à chaque phrase [fiche:AA1LoZwW_2Y 01:58, 02:47].
- **Caleb Ralston** : les effets de montage toutes les ~13 s relèvent du divertissement ; en éducatif, on retient par
  l'apprentissage [fiche:uJ8Pg6t_iho 02:15]. **Hormozi** : effets et « whiz bangs » distraient une audience B2B
  [fiche:Jmkq5RLjm0U 00:56-01:00].
- **Recommandation de l'agence** : le rythme se fait par **l'information nouvelle** (un plan par idée, aucun temps mort),
  pas par des effets ajoutés à intervalle fixe. **Pas d'hyper-cut** pour Sillage ni pour une marque premium : il est
  remplacé par **un seul** effet d'accroche fort. Les seuils de Mino (3 s, 0,5 s) restent des heuristiques UGC
  (registre P37, faible). Expérience proposée : même contenu, montage « une idée par plan » contre « stimulation
  toutes les 3 s », mesuré au temps de visionnage moyen.

### D3. Curiosité : interdite (Hormozi) ou moteur de l'accroche (Ava, Mino) ?
- **Hormozi** : pas de curiosité gratuite dans la miniature et le titre d'un contenu éducatif ; « s'ils veulent cette
  chose, ils cliquent, et tu leur donnes cette chose » [fiche:Jmkq5RLjm0U 00:50]. Il ouvre pourtant ses conférences par
  « Vous voulez entendre un truc complètement fou ? ».
- **Ava** utilise la boucle ouverte (« Étape 3, je… » coupé) ; **Mino** annonce le paradoxe (« ça va paraître
  contre-intuitif »).
- **Recommandation de l'agence** : curiosité **dans la structure et le hook oral**, oui ; curiosité **comme promesse
  trompeuse** dans le packaging, non. La règle YouTube (satisfaction, test A/B au temps de visionnage) va dans le sens
  d'Hormozi sur le packaging (H7).

### D4. Le son : « 80 à 90 % regardent sans le son » (Ava) contre les données
- **Ava** en tire que le hook visuel prime [fiche:HzoQgQS8czE 00:20-00:22].
- **Registre et veille** : chiffre contredit (Facebook 2016) ; les Reels muets sont moins diffusés ; le son est un signal
  mesuré [registre:P02] [veille:instagram §5].
- **Recommandation de l'agence** : on garde la priorité au visuel (le feed est saturé), on **abandonne** l'argument du
  muet. Toujours un audio ; une lecture possible sans le son ; jamais conçu « pour le muet » (H5, H6).

### D5. Durée de l'accroche en format long : 15-20 s (Ralston) ou 30 s (« l'industrie ») ?
- **Ralston** conteste les « 30 s » du secteur et vise 15-20 s maximum [fiche:Ch4Sl0POBhU 02:09, 04:13].
- **Registre** : aucune pondération par segment publiée par YouTube ; ces chiffres sont invérifiables [registre:P11].
- **Recommandation de l'agence** : aucun chiffre en règle. La promesse est visible **dès la première image**, la preuve
  suit immédiatement, un premier enseignement arrive dans la première minute (H1, H3). On mesure sur nos courbes de
  rétention (vues engagées).

---

## Application Sillage et marques sans visage (récapitulatif)

| Règle générale | Transposition sans visage, premium, sans musique |
|---|---|
| Hook en 3 canaux | Visuel = transformation produit ; écrit = un carton de ~5 mots ; verbal seulement si voix off |
| Hook visuel « simple » (s'asseoir, plongée) | Objet qui entre en spring, révélation par masque, avant/après en morphing, légère caméra 3D |
| Montage serré, hyper-cut | Aucun temps mort, aucun hyper-cut ; un seul moment « waouh » construit |
| Sous-titres partout | Seulement s'il y a une voix off ; sinon 3-4 messages courts |
| Son tendance / musique | Jamais. Effets sonores synchronisés, publiés comme son original nommé |
| Intro rituelle (générique) | Signature visuelle + signature sonore en effets + phrase fixe en voix off |
| « Hey guys », présentation | Jamais de logo en ouverture : le logo arrive en signature, à la fin |
| Durée | 8-30 s (démo, pub, logo) ; 60-180 s seulement pour un making-of éducatif |

Structure de référence : `swipe-file/structures.md` R9 (reel 30 s motion, sans visage).

## Expériences proposées au labo (`concepteur-experiences`)
1. Largeur du hook (D1) : même reel, hook « situation précise » contre hook « large », mesuré en envois/portée et DM
   qualifiés.
2. Rythme (D2) : « une idée par plan » contre « nouveauté toutes les 3 s », mesuré au temps de visionnage moyen.
3. Voix off ou 100 % visuel + effets sonores, pour les reels Sillage, mesuré en DM qualifiés par 1 000 vues.
4. Trial Reels : 3 hooks visuels différents sur la même animation.

## Journal
| Date | Modification |
|---|---|
| 2026-10-20 | Création : 15 principes, 5 désaccords tranchés, tableau de transposition Sillage, 4 expériences proposées. Sources : 5 fiches, 11 frameworks, swipe-file, registre (P02, P10, P11, P19, P37, G04, C16), veille des 4 plateformes. Aucun apprentissage du labo disponible. |
