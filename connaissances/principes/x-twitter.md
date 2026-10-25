# Principes : X (ex-Twitter)

> Tenu par `synthetiseur-connaissances`. Création : 2026-10-25 (grande synthèse, équipe S5b).
> Périmètre : codes, formats et algorithme de X (posts, threads, posts longs, Articles). Tag `x-twitter` ; alias
> « twitter », « X », « threads X » (table « Alias » d'`agents.md`). Rédaction des threads : agent `redacteur-thread-x`.
>
> **Source qui prime** : `veille/plateformes/x.md` (création 2026-10-22), fondée sur le **code ouvert** de X
> (`xai-org/x-algorithm`, poids lus le 2026-10-22), la documentation de l'API et des déclarations de dirigeants,
> citée `[veille:x §x]`. Elle prime sur toutes les fiches : la plupart des conseils d'experts sur X datent de
> 2021-2023, avant le passage au modèle Phoenix (janvier 2026).
>
> Sources traitées (5 fiches, 4 experts) : `SUzKZfyaAK8` (Dan Koe, compilation publiée en 2024, conseils X **[DATÉ]**
> 2021-2022 ; seule fiche dont X est un thème central, signalé « hors liste » et rangé ici par l'alias) ·
> `hdjlCLb9Hl8` (April Dunford, remarque de 2023) · `Z2uoA3bhJT0` (Paddy Galloway, 2026) · `k834E6OTGTM` (Alex
> Hormozi, X comme canal parmi d'autres, 2023) · `IWuVEcQexWo` (Gary Vaynerchuk, fréquence multi-plateforme).
> Registre : lignes V4B-DK01 à DK06 (passe 4b fusionnée le 2026-10-25) ; exclusion de la tactique de Koe « payer pour
> des retweets ». Question utilisateur n° 6 (X Premium) **en attente** (`journal/questions-utilisateur.md`).
> Frameworks liés : `frameworks/contenu-pilier-et-cascade.md` · `decliner-un-contenu-gagnant.md` ·
> `bibliotheque-d-emballages.md`.
>
> **Labo** : `experiences/apprentissages.md` est vide au 2026-10-25 ; aucune expérience X n'est encore conçue dans
> `experiences/index.md` (les trois tests proposés par la veille sont demandés à `concepteur-experiences`, voir
> « Tests »).

## Légende

- **Consensus** : nombre d'experts distincts. Sur X, l'expertise disponible est **datée** : elle compte moins que le
  code de 2026.
- **Confiance** : **haute** = code ouvert ou documentation officielle [OFFICIEL] ; **moyenne** = déclaration de
  dirigeant relayée par la presse [OFFICIEL-relayé], ou observation de tiers sérieuse (Buffer) ; **faible** = expert
  seul, conseil daté, [RUMEUR].
- Les poids du code sont des **valeurs par défaut** que la production peut modifier ; ils multiplient des probabilités
  prédites, pas des compteurs (« une réponse ne vaut pas 7,5 likes ») [veille:x §2.2].
- Chiffres de Koe : tous autodéclarés et contradictoires d'un segment à l'autre (abonnés, revenus) ; « 230 000 abonnés
  Instagram grâce aux captures de tweets » est une affirmation non vérifiée. Statistiques à ne jamais reprendre :
  « 60 % des emplois de demain n'existent pas » (V4B-DK01 ❌), « 62 % des emplois menacés » (V4B-DK02 ❓), « 99 % des
  gens ont un regret » (exemple de hook, sans source). Galloway : « environ 200 000 vues par tweet » (affirmation).

## Résumé (12 principes)

| # | Principe | Consensus | Confiance |
|---|---|---|---|
| X1 | Écris pour être partagé et pour qu'on te réponde, pas pour être liké | officiel | haute |
| X2 | Ne provoque jamais le rejet : signaler, masquer et « pas intéressé » écrasent tout | officiel | haute |
| X3 | Écris pour la lecture jusqu'au bout ; chaque post se suffit à lui-même | officiel + 1 | moyenne |
| X4 | 1 à 3 posts originaux par jour au maximum, espacés de plusieurs heures | officiel + 2 | haute (mécanisme) |
| X5 | Fenêtre de 48 h : reprends un sujet fort sous un nouvel angle, jamais en copier-coller | officiel + 1 | moyenne |
| X6 | Thread : le premier post doit tenir seul ; avec Premium, préfère le post long ou l'Article | officiel + 1 | moyenne |
| X7 | Construis la distribution par de vraies conversations, jamais en série | officiel + 1 | moyenne |
| X8 | Sers-toi de X comme banc d'essai d'idées, puis développe les gagnantes en format long | 2 | moyenne |
| X9 | Mets un lien seulement si le trafic est l'objectif, dans un post qui donne déjà la valeur | officiel | moyenne |
| X10 | N'achète jamais d'engagement, ne coordonne jamais de partages | officiel + règle | haute |
| X11 | Ne republie jamais une capture de post X ailleurs : recrée le texte en visuel natif | règle maison + officiel IG | haute |
| X12 | Juge un post X aux partages, réponses de fond, abonnements et temps de lecture | officiel | moyenne |

---

## Principes

### X1. Écris pour être partagé et pour qu'on te réponde, pas pour être liké
- **Pourquoi** : poids par défaut du fil « Pour toi » (code lu le 2026-10-22) : copier le lien du post 20, réponse 5,
  citation 5, envoi en message privé 5, s'abonner à l'auteur 4, partage 2, repost 1, like 0,66 ; clic sur le profil 0
  [veille:x §2.3]. Le conseil de Koe « le retweet est le moteur de la croissance », « le clic sur le profil mène à
  l'abonnement » [fiche:SUzKZfyaAK8 01:20] est **dépassé** : le repost ne pèse que 1 et le clic sur le profil ne compte
  plus [veille:x §7].
- **Comment l'appliquer** : chaque post a une réponse claire à « à qui le lecteur va-t-il l'envoyer ? » ou une raison
  de répondre sur le fond ; CTA de réponse formulés comme de vraies questions.
- **Pour une marque d'entreprise / un studio B2B** : un décodage de lancement qu'un fondateur enverra à son associé
  vaut plus qu'une maxime à liker.
- **Consensus** : officiel (code). **Confiance** : haute.

### X2. Ne provoque jamais le rejet : signaler, masquer et « pas intéressé » écrasent tout
- **Pourquoi** : signalement −234, masquer l'auteur −58,8, « pas intéressé » −52,3, bloquer −31,2 [veille:x §2.3] ; un
  post qui agace fait plus de dégâts qu'un post neutre. Welsh voit le ton outrancier « marcher » aujourd'hui sur X,
  mais détruire la confiance [fiche:DJLtwT1Z0eo 00:31-00:34].
- **Comment l'appliquer** : pas de provocation gratuite, pas d'appât (« BREAKING » systématique), rien hors de la
  promesse du compte ; la conviction contrarienne sincère reste possible (`personal-branding.md` P12). Contrôle par
  `critique-hook` et `controleur-qualite-marketing`.
- **Consensus** : officiel + 1 (Welsh). **Confiance** : haute.

### X3. Écris pour la lecture jusqu'au bout ; chaque post se suffit à lui-même
- **Pourquoi** : le temps de lecture entre dans les poids ; X a annoncé le 2026-10-20 un modèle qui prédit le temps
  passé et une récupération entraînée sur les posts « lus jusqu'au bout » [veille:x §1, §2.1] ; Nikita Bier : « the post
  should stand alone as great content so write a solid caption » [veille:x §4.1].
- **Comment l'appliquer** : première ligne forte ; une idée par phrase ; couper plutôt qu'allonger. Gabarits de Koe
  réutilisables pour la **structure** seulement : PPP (Pull, Perspective, Punchline), « hook → 3 puces actionnables →
  conclusion avec un point de douleur », tweet liste « How to [résultat] » [fiche:SUzKZfyaAK8 frameworks P, Q, 01:55].
- **Consensus** : officiel (annonce relayée) + 1 (Koe pour les gabarits). **Confiance** : moyenne (le modèle du
  2026-10-20 est annoncé, son déploiement non précisé).

### X4. Publie 1 à 3 posts originaux par jour au maximum, espacés de plusieurs heures
- **Pourquoi** : le code ne pénalise pas le compte qui publie plusieurs fois par jour, mais dans le fil de chaque
  lecteur, chaque post après le premier d'un même auteur est multiplié par un facteur décroissant jusqu'à un plancher
  (diversité d'auteur) [veille:x §2.4, §4.2]. Le conseil de Koe « Twitter ne pénalise pas plusieurs posts par jour »
  [fiche:SUzKZfyaAK8 03:05] est donc globalement exact, avec un rendement décroissant. Vaynerchuk prescrit « every
  single day, multiple times a day » [fiche:IWuVEcQexWo 00:05], mais ajoute que la constance ne paie qu'une fois le
  savoir-faire acquis [00:48].
- **Comment l'appliquer** : 1 post original par jour par défaut, jusqu'à 3 si chacun tient seul ; jamais de rafale ;
  des posts faibles ou répétitifs exposent aux signaux négatifs (X2) et aux libellés anti-spam. Règle de travail,
  pas un chiffre de X (D1).
- **Consensus** : officiel + 2 (Koe, Vaynerchuk). **Confiance** : haute sur le mécanisme ; règle de travail à valider.

### X5. Fenêtre de 48 h : reprends un sujet fort sous un nouvel angle, jamais en copier-coller
- **Pourquoi** : les posts de plus de 48 h sortent des candidats « Pour toi » ; les auteurs sous un seuil d'impressions
  reçoivent un coup de pouce pendant leurs 2 premières heures (paramètres lus : 200 impressions, 50 000 abonnés,
  7 200 s) [veille:x §2.4]. Koe : « say one validated valuable thing 1,000 different ways from 1,000 different
  angles » [fiche:SUzKZfyaAK8 02:40].
- **Comment l'appliquer** : pas d'espoir de longue traîne sur X ; un sujet gagnant revient après 48 h sous un autre
  angle, un autre format (liste, histoire, contre-exemple) ; `decliner-un-contenu-gagnant.md`.
- **Consensus** : officiel + 1 (Koe). **Confiance** : moyenne.

### X6. Thread : le premier post doit tenir seul ; avec Premium, préfère le post long ou l'Article
- **Pourquoi** : `DedupConversationFilter` retire les branches supplémentaires d'une même conversation : un thread
  n'occupe en principe qu'**une** place dans « Pour toi », celle de son premier post ; avec Premium, un post long
  (jusqu'à 25 000 caractères) est une seule unité dont le clic « Afficher plus » et le temps passé lui reviennent ; les
  Articles sont réservés à Premium [veille:x §2.4, §4.3]. Koe tirait un thread hebdomadaire de sa newsletter (partie
  actionnable) [fiche:SUzKZfyaAK8 framework N]. Le « thread format roi » n'est pas démontré en 2026 [veille:x §3.2].
- **Comment l'appliquer** : sans Premium (situation par défaut tant que la question n° 6 est ouverte) : thread de 4 à 8
  posts, premier post = promesse + valeur, chaque post lisible seul, pas de lien avant la fin, dernier post = synthèse
  ou question de fond [veille:x §8 règles 5-6]. Avec Premium : post long par défaut, Article pour un contenu de fond.
- **Consensus** : officiel + 1 (Koe). **Confiance** : moyenne (aucune comparaison officielle thread / post long).

### X7. Construis la distribution par de vraies conversations, jamais en série
- **Pourquoi** : une réponse entre deux comptes qui se suivent mutuellement reçoit un bonus de 15 ; les réponses des
  comptes payants passent devant dans les conversations ; un classifieur IA de réponses spam existe depuis septembre
  2026 [veille:x §2.3, §3.1, §4.4, §2.1]. Koe : commentaires à valeur ajoutée sous les gros comptes (le profil soigné
  fait vitrine) et cercle de 3 à 5 créateurs du même niveau, en rejetant les « engagement groups »
  [fiche:SUzKZfyaAK8 framework O] ; ces conseils restent pertinents avec cette limite [veille:x §7].
- **Comment l'appliquer** : répondre vite et vraiment pendant les 2 premières heures ; quelques réponses de fond par
  jour sous des comptes de la niche, rédigées ou validées par la personne ; profil (photo, nom, bio) aligné sur le sujet ;
  le « cercle d'amis » qui se partage n'est acceptable qu'occasionnel et sincère (X10).
- **Consensus** : officiel + 1 (Koe). **Confiance** : moyenne.

### X8. Sers-toi de X comme banc d'essai d'idées, puis développe les gagnantes en format long
- **Pourquoi** : Koe lance beaucoup d'idées en court, garde les meilleures et les développe en newsletter, vidéo ou
  podcast ; « A good tweet that went viral is the perfect newsletter, blog, YouTube headline » [fiche:SUzKZfyaAK8
  02:03, 03:01, framework Z]. Dunford teste ses idées « half-baked » sur X parce qu'on y conteste ce qu'elle dit, alors
  que LinkedIn applaudit [fiche:hdjlCLb9Hl8 01:03] (avis de 2023). Galloway prévient qu'une compétence X ne se transfère
  pas d'elle-même à YouTube [fiche:Z2uoA3bhJT0 framework U].
- **Comment l'appliquer** : tenir la liste des posts X qui surperforment (en partages et réponses, X12) comme
  bibliothèque de titres et d'angles ; recréer chaque idée **nativement** sur la plateforme suivante, avec son métier
  propre (packaging YouTube, document LinkedIn).
- **Consensus** : 2 (Koe, Dunford) ; Galloway nuance. **Confiance** : moyenne (aucune mesure).

### X9. Mets un lien seulement si le trafic est l'objectif, dans un post qui donne déjà la valeur
- **Pourquoi** : plus de pénalité officielle des liens depuis environ mi-2025 (Bier, Musk, juillet 2026 : « We haven't
  for over a year ») ; le clic de lien a un poids positif (0,2) ; mais les posts à lien des comptes gratuits restaient
  faibles chez Buffer en 2025 (données antérieures aux déclarations) et **un post à lien coûte 0,200 $ via l'API contre
  0,015 $** [veille:x §4.1, §5]. Mécanisme plausible : le lecteur qui sort de X produit moins de signaux. Le lien « en
  réponse » de Koe n'est plus nécessaire [veille:x §7].
- **Comment l'appliquer** : le texte donne déjà la valeur ; lien seulement quand le trafic est l'objectif ; test « lien
  dans le post / en réponse / sans lien » (Tests).
- **Consensus** : officiel. **Confiance** : moyenne (effet 2026 non chiffré).

### X10. N'achète jamais d'engagement, ne coordonne jamais de partages
- **Pourquoi** : la politique « manipulation de la plateforme et spam » interdit l'engagement inauthentique et
  l'activité coordonnée [veille:x §4.5]. La tactique de Koe « payer pour obtenir des retweets, des partages ou des
  commentaires » [fiche:SUzKZfyaAK8 01:58, 03:05] est **exclue** : manipulation, fausse preuve sociale, partenariat non
  signalé [fiche:SUzKZfyaAK8 « Ce qui est discutable »]. `garde-offres` règle 9 et `gestionnaire-communaute` la
  bloquent. X coupe aussi la rémunération des agrégateurs et des posts appâts (avril 2026), sans réduire la portée par
  principe [veille:x §4.5].
- **Comment l'appliquer** : refus par `garde-conformite` de tout achat de reposts, likes ou abonnés, de tout groupe
  d'engagement coordonné, de toute automatisation de réponses ; un partenariat rémunéré est **déclaré** (distribution
  achetée, `croissance-audience.md` D6).
- **Consensus** : officiel + règle du repo. **Confiance** : haute.

### X11. Ne republie jamais une capture de post X ailleurs : recrée le texte en visuel natif
- **Pourquoi** : Koe republiait ses tweets viraux en captures **avec les compteurs visibles** sur Instagram
  [fiche:SUzKZfyaAK8 01:46, 03:06]. En 2026 : non pénalisé en photo ou carrousel si c'est notre post, pénalisé en Reel
  (« majoritairement texte », logo d'une autre app), interdit pour les posts d'autrui (originalité contrôlée sur les
  photos et carrousels depuis le 2026-04-30) ; le logo et l'interface de X sont une **marque tierce** (règle du
  `CLAUDE.md`) ; des compteurs figés dans une image deviennent faux [veille:x §4.6, §8 règles 11-12]
  [veille:instagram §3].
- **Comment l'appliquer** : recréer le texte dans la charte de la marque (carrousel 3:4 ou 4:5 sur Instagram, document
  PDF sur LinkedIn) ; si l'on veut dire qu'un texte a marché sur X, le dire en légende avec des chiffres réels et datés.
- **Consensus** : règle maison + règle officielle Instagram. **Confiance** : haute.

### X12. Juge un post X aux partages, réponses de fond, abonnements et temps de lecture
- **Pourquoi** : ce sont les actions qui pèsent (X1) ; l'outil « Under the Hood » (test depuis le 2026-08-13, comptes de
  plus d'un an ayant publié au moins 10 fois le mois précédent) montre les libellés de visibilité appliqués
  [veille:x §1, §4.2]. Koe diagnostiquait une promotion qui ne vend pas par la chaîne clics → visites → post porteur →
  sujet, en changeant un élément par jour [fiche:SUzKZfyaAK8 framework U].
- **Comment l'appliquer** : pas de pilotage aux likes ni aux impressions brutes ; rapport « Under the Hood » mensuel si
  le compte y a accès ; diagnostic d'une promotion élément par élément.
- **Consensus** : officiel + 1 (Koe). **Confiance** : moyenne.

**Vidéo pour X** : une vidéo par post, aucun bonus de classement documenté (la « vue vidéo de qualité » a été retirée
des poids en août 2026) ; livrables MP4 H.264/AAC, 720×1280 ou 1280×720 recommandés par l'API, sous 140 s ; limite de
résolution de l'API à vérifier avec `publicateur` avant livraison [veille:x §4.7, §5, §8 règle 14]. Renvoi
`formats-courts.md`.

---

## Désaccords entre experts

### D1. Volume (« post every day », plusieurs posts par jour) ou métier d'abord, et rendement décroissant ?
| Position | Qui | Arguments |
|---|---|---|
| **Plusieurs posts par jour** | Koe (stade 1 : « plusieurs posts par jour sur X » [03:05]) ; Vaynerchuk (« every single day, multiple times a day » [00:05]) | Plus de tirages, apprentissage rapide ; pas de pénalité de compte |
| **Le métier d'abord** | Vaynerchuk lui-même (« Then it will be consistency once you're good at the craft », 10 à 20 h d'étude [00:48]) ; Welsh (« sniper » plutôt que « machine gunner » [00:15]) | Publier sans savoir-faire ne marche pas ; le public se lassera du volume dopé à l'IA (souhait, pas donnée) |
| **Code 2026** | `veille/plateformes/x.md` §2.4, §4.2 | Pas de pénalité de compte, mais facteur décroissant par post supplémentaire dans le fil de chaque lecteur ; posts faibles = signaux négatifs |

**Recommandation de l'agence** : 1 post original par jour par défaut, 3 au maximum, espacés ; le volume n'augmente
qu'une fois les premiers posts jugés bons aux partages et aux réponses. **Ce qui la ferait changer** : le test « 1 post
par jour contre 3 pendant 2 semaines » (portée totale et par post) [veille:x §9], à concevoir par
`concepteur-experiences`.

### D2. Le retweet est-il le moteur de la croissance ?
- **Koe** (2021-2022) : oui, et le clic sur le profil mène à l'abonnement [fiche:SUzKZfyaAK8 01:20].
- **Code 2026** : repost 1, clic sur le profil 0 ; partages (copie du lien 20, message privé 5, citation 5) et réponses
  (5, +15 entre abonnés mutuels) pèsent bien plus [veille:x §2.3].
- **Recommandation de l'agence** : le code tranche. On conçoit pour le partage et la réponse (X1).

### D3. Faut-il X Premium pour un compte de marque ? (question utilisateur n° 6, **en attente**)
- **Pour** : Buffer mesure une portée médiane environ ×10 pour les comptes Premium (18,8 M de posts, 2024-2025 ;
  corrélation, les comptes payants sont aussi plus actifs) [OBSERVÉ] ; réponses Premium prioritaires dans les
  conversations selon le centre d'aide (relayé, à revérifier) ; posts longs, Articles et vidéos longues réservés à Premium
  [veille:x §4.4].
- **Contre ou incertain** : aucun multiplicateur Premium dans le code de 2026 ; coût mensuel par compte ; l'effet passe
  peut-être par d'autres chemins, non démontré [veille:x §2.5].
- **Recommandation de l'agence** : décision de l'**utilisateur** (coût). En attendant : aucun Premium supposé, threads
  dont le premier post tient seul (X6), aucune campagne X qui dépendrait du post long. **Ce qui la ferait changer** :
  la réponse de l'utilisateur à la question n° 6 ; puis, si Premium est pris, le test « thread contre post long sur le
  même contenu ».

### D4. Lien dans le post, en réponse, ou pas de lien ?
- **Koe** : lien vers la newsletter archivée **en réponse** [fiche:SUzKZfyaAK8 01:54] ; **X** (2026) : plus besoin, pas
  de pénalité ; **Buffer** (2025) : posts à lien faibles chez les comptes gratuits ; **API** : 13 fois plus cher.
- **Recommandation de l'agence** : X9 ; test à trois branches avant toute règle.

Le débat « distribution construite, empruntée ou achetée » de Koe, qui dépasse X, est tranché dans
`croissance-audience.md` D6.

---

## Tests proposés au labo (à concevoir par `concepteur-experiences`)
1. Lien dans le post, lien en réponse, sans lien (même sujet, même heure) (X9, D4).
2. Thread contre post long Premium sur le même contenu, si Premium est pris (X6, D3).
3. 1 post par jour contre 3 posts par jour pendant 2 semaines (D1).

## Journal
| Date | Modification |
|---|---|
| 2026-10-25 | Création (grande synthèse, S5b) : 12 principes, 4 désaccords tranchés (volume, retweet, Premium en attente de l'utilisateur, lien), à partir de 5 fiches, de `veille/plateformes/x.md` (2026-10-22, code ouvert) et du registre fusionné ; tactique « payer des retweets » de Koe exclue. |
