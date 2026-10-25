# X (ex-Twitter) : fiche algorithme et formats

> Tenue par `veilleur-algorithmes`. **Dernière mise à jour : 2026-10-22** (création).
> Fenêtre « nouveautés 90 jours » : 2026-07-24 → 2026-10-22.
>
> Niveaux de preuve utilisés partout :
> - **[OFFICIEL]** : X l'a publié et je l'ai lu directement (code du dépôt `xai-org/x-algorithm`, documentation développeurs `docs.x.com`).
> - **[OFFICIEL-relayé]** : déclaration d'un dirigeant de X (Elon Musk, Nikita Bier, Keith Coleman, comptes @XCreators, @XEng…) ou page du centre d'aide que je n'ai pas pu ouvrir (x.com et help.x.com bloquent la lecture automatique). Le contenu est connu par une presse qui la cite.
> - **[OBSERVÉ par des tiers]** : étude ou lecture du code par un tiers (Buffer, analyses de dépôt…). C'est une *affirmation* tant que `verificateur-faits` ne l'a pas vérifiée.
> - **[RUMEUR]** : circule chez des créateurs ou des blogs sans source retrouvée. Ne jamais citer comme un fait.
>
> Particularité de X : les annonces passent par des **posts de dirigeants**, pas par un blog. Elles sont rapides, parfois contradictoires, et le principal responsable produit (Nikita Bier) a quitté son poste en août 2026. Le **code ouvert** est donc la source la plus solide, avec une réserve : il fixe des valeurs par défaut que des réglages de production peuvent modifier.

---

## 1. L'essentiel en 10 points

1. **Le fil « Pour toi » est classé par un modèle de type Grok (Phoenix)** qui prédit la probabilité d'une vingtaine d'actions pour chaque post, puis fait une **somme pondérée**. Le code est public depuis le **2026-01-20** et les poids sont lisibles dans le dépôt. [OFFICIEL]
2. **Ce qui pèse le plus (poids par défaut lus le 2026-10-22)** : copier le lien du post (20), réponse (5), citation (5), envoi en message privé (5), s'abonner à l'auteur (4), partage (2), repost (1), like (0,66). Une réponse entre deux comptes qui se suivent mutuellement reçoit un bonus de 15. [OFFICIEL]
3. **Les signaux négatifs écrasent tout** : signalement (−234), masquer l'auteur (−58,8), « pas intéressé » (−52,3), bloquer (−31,2). Un post qui agace fait plus de dégâts qu'un post neutre. [OFFICIEL]
4. **Le temps de lecture monte en importance** : X a annoncé le **2026-10-20** un modèle qui prédit le temps passé sur un post et un modèle de récupération entraîné à remonter les posts **lus jusqu'au bout**. [OFFICIEL-relayé]
5. **Liens externes : plus de pénalité officielle** depuis environ mi-2025 (Musk, juillet 2026 : « We haven't for over a year »). Mais les posts à lien restent faibles chez les comptes gratuits d'après les données de tiers, et **un post à lien coûte 13 fois plus cher via l'API**. [OFFICIEL-relayé + OBSERVÉ + OFFICIEL]
6. **Plusieurs posts par jour : pas de pénalité de compte**, mais un **rendement décroissant** : dans le fil d'un même lecteur, chaque post après le premier d'un même auteur est multiplié par un facteur qui décroît jusqu'à un plancher. [OFFICIEL]
7. **Fraîcheur courte** : les posts de plus de **48 h** sont exclus des candidats du fil « Pour toi ». [OFFICIEL]
8. **Les comptes Premium touchent beaucoup plus de monde** (environ ×10 de portée médiane selon Buffer) et leurs réponses sont prioritaires dans les conversations. Le code de 2026 ne montre pas de multiplicateur Premium explicite. [OBSERVÉ + OFFICIEL-relayé]
9. **Contenu recyclé et agrégateurs** : X ne réduit pas la portée par principe (« X will never infringe on speech or reach ») mais **coupe la rémunération** des agrégateurs et des posts appâts (avril 2026). Acheter de l'engagement est interdit. [OFFICIEL-relayé]
10. **Transparence nouvelle** : l'outil « Under the Hood » (test depuis le 2026-08-13) permet à certains comptes de télécharger les **libellés de visibilité** appliqués à leurs posts. [OFFICIEL-relayé]

---

## 2. Comment le fil « Pour toi » fonctionne (code ouvert)

### 2.1 Historique des publications de code
| Date | Événement | Statut |
|---|---|---|
| 2023-03-31 | Twitter publie `twitter/the-algorithm` et `twitter/the-algorithm-ml`. Le classeur principal (« Heavy Ranker ») pondère des probabilités d'engagement (poids au 2023-04-05, § 2.3). Les tiers y lisent aussi un multiplicateur pour les comptes vérifiés payants : ×4 dans le réseau, ×2 hors réseau. | [OFFICIEL] pour les poids (README de `the-algorithm-ml`, https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md) ; [OBSERVÉ par des tiers] pour le multiplicateur ([blckalpaca](https://blckalpaca.at/en/knowledge-base/social-media/social-media-algorithms-distribution/x-twitter-algorithm-open-source)) |
| Oct. 2025 | Musk annonce que la recommandation passera à Grok, que « all heuristics » seront supprimées en 4 à 6 semaines et que Grok lira chaque post et regardera chaque vidéo. | [OFFICIEL-relayé] [Social Media Today](https://socialmediatoday.com/news/x-formerly-twitter-switching-to-fully-ai-powered-grok-algorithm/803174) |
| 2026-01-10 → 2026-01-20 | Musk promet d'ouvrir « all code used to determine what organic and advertising posts are recommended » ; X publie `xai-org/x-algorithm` le 2026-01-20 (modèle Phoenix dérivé de Grok-1). | [OFFICIEL] dépôt · [OFFICIEL-relayé] [PPC Land](https://ppc.land/xs-algorithm-source-code-drops-what-it-reveals-about-the-platforms-feed-mechanics/) |
| 2026-05-15 | Grosse mise à jour (pipeline d'inférence, service de compréhension de contenu Grox, insertion des pubs). | [OBSERVÉ par des tiers] [Keywords Everywhere](https://keywordseverywhere.com/news/social-algorithm-updates/x-algorithm-open-source/) |
| 2026-08-13 | Publication des **poids de score**, du code de **filtrage de visibilité** et du code d'entraînement de Phoenix ; lancement de l'outil « Under the Hood ». | [OFFICIEL] dépôt · [OFFICIEL-relayé] [GIGAZINE](https://gigazine.net/gsc_news/en/20260814-x-timeline-algorithm/) |
| 2026-08-17 → 2026-09-04 | Mises à jour fréquentes : comptage des répétitions de sujets, **temps de lecture (dwell) dans les poids et retrait des « vues vidéo de qualité »** (25 août), agrégation Phoenix par défaut sur une variante « long dwell » (2 sept.), classifieur IA de réponses spam (4 sept.). | [OBSERVÉ par des tiers] Keywords Everywhere. Recoupé : le poids `VqvWeight` vaut bien 0 dans le code lu le 2026-10-22. |
| 2026-10-20 | Musk : « New AI/SI ranking model that predicts probable time spent much better » et « Retrieval model trained to surface posts people read all the way through ». | [OFFICIEL-relayé] [IBTimes, 2026-10-21](https://www.ibtimes.co.uk/elon-musk-x-algorithm-reading-time-recommendations-1826986) |

### 2.2 Architecture 2026 (README du dépôt, lu le 2026-10-22)
Source : https://github.com/xai-org/x-algorithm [OFFICIEL]
- **Home Mixer** assemble le fil.
- **Sources de candidats** : *Thunder* (posts récents des comptes suivis, en mémoire) ; *Phoenix retrieval* (posts hors réseau trouvés par similarité d'embeddings lecteur ↔ post) ; *SimClusters* (groupes d'intérêts) ; une liste de posts populaires.
- **Classement** : *Phoenix* prédit une probabilité par action ; un réordonnancement final (*vm-ranker*) diversifie le fil.
- **Compréhension du contenu** : plusieurs services d'étiquetage (Grox, modèles d'images, crédibilité du compte, contenu adulte…).
- **Visibilité** : un module décide « autoriser, avertir, interstitiel ou retirer » ; des systèmes anti-abus posent des libellés.
- **Score final** : `Σ (poids × P(action))`. Le README précise que les poids multiplient des **probabilités prédites**, « not the raw engagement counts » : on ne peut pas lire « une réponse = 7,5 likes ».
- **Production** : « we run cron scripts that set the defaults in this repository's code to be the primary production values » ; des expériences peuvent tourner sur une part du trafic. Les modèles entraînés et les classifieurs anti-spam ne sont pas publiés.

### 2.3 Les poids publiés : 2023 contre 2026
Fichier `home-mixer/params/param.rs`, branche principale, lu le 2026-10-22 [OFFICIEL]. Valeurs par défaut, modifiables en production.

| Action prédite | Poids 2026 | Poids 2023 (Heavy Ranker) |
|---|---|---|
| Copier le lien du post | **20,0** | (absent) |
| Réponse | **5,0** | 13,5 |
| Bonus réponse entre abonnés mutuels | **+15** (`BidirectionalFollowReplyWeightBoost`) | Réponse à laquelle l'auteur répond : 75 |
| Citation | 5,0 | (absent) |
| Envoi en message privé | 5,0 | (absent) |
| S'abonner à l'auteur | 4,0 | (absent) |
| Partage | 2,0 | (absent) |
| Repost | 1,0 | 1,0 |
| Vidéo ouverte depuis un carrousel vidéo | 1,0 | (absent) |
| Like | 0,66 | 0,5 |
| Temps passé après un clic (continu) | 0,4 | (absent) |
| Clic sur le post | 0,3 | « good click » 11 / 10 |
| Clic sur un lien externe | **0,2 (positif)** | (absent) |
| Clic sur le profil | **0,0** | « good profile click » 12 |
| Arrêt sur le post (dwell) | 0,05 | (absent) |
| Agrandir une photo | 0,05 | (absent) |
| Vidéo ouverte | 0,02 | lecture vidéo à 50 % : 0,005 |
| Temps d'arrêt (continu) | 0,006 | (absent) |
| Vue vidéo « de qualité » | **0** (retiré en août 2026) | (absent) |
| Post vu sans arrêt | −0,02 | (absent) |
| Bloquer l'auteur | −31,2 | « negative feedback » −74 |
| « Pas intéressé » | −52,3 | (idem) |
| Masquer l'auteur | −58,8 | (idem) |
| Signalement | **−234** | −369 |

Lecture :
- **Ce qui a changé depuis l'époque des conseils de Dan Koe (2021-2022)** : la réponse pèse moins en relatif, le **partage** (copie du lien, message privé, citation) est devenu le signal positif le plus lourd, le clic sur le profil ne compte plus directement, et l'abonnement à l'auteur est récompensé.
- Le bonus de 15 sur les réponses entre abonnés mutuels favorise les **vraies conversations** entre comptes qui se connaissent.
- Le poids de 0,2 sur le clic de lien est **positif** : le code ne pénalise pas les liens (§ 4.1).

### 2.4 Ajustements et filtres (README) [OFFICIEL]
- **Diversité d'auteur** : « each post after an author's first is multiplied by a decaying factor, down to a floor ». Valeurs du facteur et du plancher non retrouvées dans le fichier de paramètres.
- **Décote hors réseau** : les posts de comptes que le lecteur ne suit pas sont multipliés par un facteur inférieur à 1, tout comme les réponses et reposts venant de comptes suivis.
- **Coup de pouce aux nouveaux auteurs** : un post d'auteur sous un seuil d'impressions est remonté vers une position cible. Paramètres lus : `ColdStartImpressionThreshold` = 200, `ColdStartFollowerCap` = 50 000, `ColdStartMaxPostAgeSecs` = 7 200 (2 h).
- **Filtres avant score** : mots masqués, auteurs bloqués ou masqués, **posts de plus de 48 h** (`AgeFilter`), posts déjà vus, ses propres posts.
- **Filtres après sélection** : visibilité, et `DedupConversationFilter` qui retire les « additional branches of the same conversation ». Un fil de posts (thread) n'occupe donc en principe **qu'une place** dans « Pour toi ».
- Un post dont le post parent, cité ou reposté a été retiré est retiré aussi.

### 2.5 Ce que le code ne dit pas
- Aucune règle explicite sur les **liens**, la **longueur** du texte ou la **fréquence** de publication par jour.
- Aucun paramètre **Premium** ou « vérifié » dans le fichier de poids 2026. L'effet Premium passe peut-être par d'autres chemins (classement des réponses, libellés de crédibilité, données d'entraînement) : non démontré.
- Les modèles entraînés, les seuils anti-spam réels et les réglages de production en cours.

---

## 3. Signaux de classement : confirmés et supposés

### 3.1 Confirmés
| Signal | Ce qui est confirmé | Source |
|---|---|---|
| Partages (copie du lien, message privé, citation, partage) | Poids les plus lourds parmi les actions positives | [OFFICIEL] `param.rs`, 2026-10-22 |
| Réponses, surtout entre abonnés mutuels | Poids 5, bonus +15 si abonnement mutuel | idem |
| S'abonner à l'auteur depuis le post | Poids 4 | idem |
| Temps de lecture | Actions « dwell » au code ; nouveau modèle de temps passé et récupération « lu jusqu'au bout » annoncés le 2026-10-20 | [OFFICIEL] + [OFFICIEL-relayé] |
| Signaux négatifs (signaler, masquer, bloquer, pas intéressé) | Poids très négatifs | [OFFICIEL] |
| Fraîcheur | Exclusion au-delà de 48 h ; coup de pouce des 2 premières heures pour les petits auteurs | [OFFICIEL] |
| Diversité d'auteur | Rendement décroissant des posts d'un même auteur dans un même fil | [OFFICIEL] README |
| Hors réseau | Décote, mais récupération par similarité d'intérêts | [OFFICIEL] README |
| Libellés de visibilité | Retrait, interstitiel, profil seul ou masquage aux non-abonnés selon le libellé (18 libellés de post, 12 de compte dans la liste publique) | [OFFICIEL] code · [OFFICIEL-relayé] [tech-ish, 2026-08-14](https://tech-ish.com/2026/08/14/inside-xs-newly-published-visibility-filtering-code/) |
| Lien avec peu de texte | « Posting a link with almost no description will get weak distribution » (Musk) | [OFFICIEL-relayé] [SMT, 2025-10-19](https://www.socialmediatoday.com/news/x-formerly-twitter-testing-links-in-app-link-post-penalties/803176/) |
| Réponses Premium prioritaires | Le centre d'aide citerait, pour le classement des réponses : l'auteur a-t-il répondu, suivez-vous la personne, a-t-elle un abonnement payant (priorité maximale pour Premium+) | [OFFICIEL-relayé] texte du centre d'aide capturé par un tiers le 2026-10-14, cité par [SocialPilot](https://socialpilot.co/blog/twitter-algorithm) (à revérifier) |

### 3.2 Supposés ou contestés
| Affirmation | Source | Statut |
|---|---|---|
| « Les comptes Premium ont ×10 de portée » | Buffer, 18,8 M de posts, 71 000 comptes, août 2024 → août 2025 : portée médiane < 100 impressions sans abonnement, > 600 avec | [OBSERVÉ par des tiers] [Buffer](https://buffer.com/resources/x-premium-review/) |
| « Les posts à lien des comptes gratuits ont un engagement médian nul depuis mars 2025 » | Buffer, même base | [OBSERVÉ par des tiers] [Buffer, 2025-10-14](https://buffer.com/resources/links-on-x/), antérieur aux déclarations de 2026 |
| « Un post à lien perd 94 % de vues » | Blog d'éditeur | [RUMEUR] |
| « Publier en rafale fait perdre de la portée par lots de 35 » attribué à Nikita Bier | Sujet tendance sur X, introuvable ailleurs | [RUMEUR] |
| « Les "gm" et réponses en masse gaspillent la portée » (Bier, début 2026) | Paraphrases de presse crypto | [RUMEUR] proche d'une déclaration, wording non retrouvé |
| « La réponse vaut 13,5 likes, la réponse avec réponse de l'auteur 75 » | Poids de **2023** | Dépassé (§ 2.3) |
| « Le thread est le format roi » | Créateurs 2020-2023 | Non démontré en 2026 (§ 4.3) |

---

## 4. Thème par thème

### 4.1 Liens externes
- **Officiel** :
  - Octobre 2025, Nikita Bier (responsable produit) : les posts à lien ont moins de portée parce que « the web browser covers the post and people forget to Like or Reply, so X doesn't get a clear signal whether the content is any good ». Test d'un navigateur intégré où le post reste visible en bas pendant la lecture. Conseil : « the post should stand alone as great content so write a solid caption ». [OFFICIEL-relayé] [SMT, 2025-10-19](https://www.socialmediatoday.com/news/x-formerly-twitter-testing-links-in-app-link-post-penalties/803176/)
  - Avril 2026 (date déduite de l'identifiant du post), Bier à Nate Silver : « Links are not deboosted. We fixed that issue last year. » Le même mois, nouvelle expérience de lien testée sur iOS. [OFFICIEL-relayé] post `x.com/nikitabier/status/2040968250604102105`
  - 2026-07-28/29, Bier à Mark Zuckerberg : « you do not need to put the links in replies anymore ». Musk : « We haven't for over a year. » [OFFICIEL-relayé] [Free Press Journal, 2026-07-29](https://www.freepressjournal.in/tech/x-product-head-nikita-bier-confirms-link-penalty-removed-over-a-year-ago-tells-mark-zuckerberg-he-can-post-them-directly)
  - Code 2026 : aucun filtre sur les liens ; le clic de lien a un poids **positif** (0,2). [OFFICIEL]
  - **API** : créer un post coûte 0,015 $ sans URL et **0,200 $ avec URL**. [OFFICIEL] https://docs.x.com/x-api/getting-started/pricing
- **Observé** : chez Buffer, en août 2025, engagement médian des posts à lien **0 %** pour les comptes gratuits, environ 0,28 % en Premium, contre 0,40 % (gratuit) et 0,90 % (Premium) pour le texte seul. Ces données datent d'**avant** les déclarations de 2026 et ne mesurent pas le lien en réponse. [OBSERVÉ par des tiers]
- **Mécanique plausible** (déduction du code) : un clic sortant fait quitter X. Le lecteur produit alors moins de likes, de réponses et de temps de lecture, qui pèsent bien plus que le clic de lien (0,2). Ce n'est pas une pénalité, c'est un **manque à gagner** de signaux.
- **Lien en réponse** : plus nécessaire selon X. Aucune mesure publique ne compare « lien dans le post » et « lien en réponse » en 2026. Une réponse est elle-même un candidat moins bien placé (décote des réponses hors réseau).
- **Verdict** : *pas de pénalité officielle depuis environ mi-2025, effet négatif probable mais non chiffré en 2026*. On teste.

### 4.2 Plusieurs posts par jour
- **Officiel (code)** : pas de plafond ni de pénalité de compte. Mais dans le fil de chaque lecteur, le 2e, 3e… post d'un même auteur est multiplié par un facteur décroissant (diversité d'auteur). Chaque post est jugé seul et disparaît des candidats « Pour toi » après 48 h.
- **Officiel (accès)** : l'outil « Under the Hood » est réservé aux comptes de plus d'un an qui ont publié **au moins 10 fois le mois précédent**. C'est une condition d'accès, pas un signal de classement. [OFFICIEL-relayé]
- **Rumeurs** : « rafales pénalisées par lots de 35 », « les "gm" gaspillent la portée » : non vérifiées.
- **Verdict sur Dan Koe** (« Twitter ne pénalise pas plusieurs posts par jour ») : **globalement exact en 2026**, avec deux nuances : les posts suivants d'une même journée se concurrencent dans le fil de chaque abonné, et des posts faibles ou répétitifs exposent aux signaux négatifs (masquer, « pas intéressé ») et aux libellés anti-spam.

### 4.3 Threads, posts longs (Premium) et Articles
- **Limites** : 280 caractères en standard ; **jusqu'à 25 000 caractères** pour un post long avec Premium. [OFFICIEL-relayé] centre d'aide https://help.x.com/en/using-x/how-to-post (page bloquée en lecture directe ; la même page mentionnerait encore une limite de 4 000, sans doute un reste d'une version ancienne)
- **Articles** (texte long mis en forme) ouverts à **tous les abonnés Premium** en janvier 2026. [OFFICIEL-relayé] [Storyboard18](https://www.storyboard18.com/amp/digital/x-expands-long-form-articles-access-to-all-premium-subscribers-87544.htm)
- **Rémunération** (2026-01-16, @XCreators) : les gains dépendent des impressions de comptes Premium dans leur fil d'accueil, et X « may weight formats like Articles more heavily than short-form content ». Concours d'un million de dollars (16 au 28 janvier 2026, États-Unis seulement, 1 000 mots minimum, jugé sur les impressions « Verified Home Timeline »). [OFFICIEL-relayé] [PPC Land](https://ppc.land/x-doubles-creator-revenue-pool-and-offers-1m-for-top-article-but-why/). C'est la **monétisation**, pas la portée.
- **Classement** :
  - le temps de lecture entre dans les poids ; le nouveau modèle du 2026-10-20 vise le temps passé et les posts **lus jusqu'au bout** [OFFICIEL + OFFICIEL-relayé] ;
  - un thread ne prend en principe qu'une place dans « Pour toi » (`DedupConversationFilter`), donc c'est son **premier post** qui est jugé et diffusé ; chaque post du thread reste un candidat séparé [OFFICIEL, lecture du code] ;
  - un post long est un seul candidat ; le clic « Afficher plus » et le temps passé ensuite (poids 0,3 et 0,4) lui reviennent [déduction du code].
- **Aucune déclaration officielle** ne compare la portée d'un thread et d'un post long.
- **Verdict** : le thread n'est plus le seul moyen de faire long. Avec Premium, le **post long** colle mieux au virage « temps de lecture » annoncé le 2026-10-20, mais rien ne le démontre encore. Sans Premium, le thread reste la seule option longue, et il vit ou meurt sur son premier post. À tester.

### 4.4 Premium et portée
- Buffer mesure environ ×10 de portée médiane pour les comptes Premium. C'est une corrélation : les comptes payants sont aussi souvent plus actifs. [OBSERVÉ par des tiers]
- Réponses des abonnés payants prioritaires dans les conversations, au maximum pour Premium+. [OFFICIEL-relayé]
- Depuis mars 2026, les abonnés Premium ont un bouton « vote négatif » sur les réponses, qui alimenterait le classement des réponses. [OBSERVÉ par des tiers]
- Les vidéos longues, le texte long, les Articles et la rémunération exigent Premium (§ 5).
- **Conséquence** : un compte de marque sans Premium part avec un handicap net sur X. La décision d'abonnement revient à l'utilisateur (coût).

### 4.5 Contenu recyclé, agrégateurs, achat d'engagement
- 2026-04-11, Bier : « All aggregators had their payouts reduced to 60% this cycle », 20 % de plus au cycle suivant ; « flooding the timeline with 100 stolen reposts and clickbait everyday crowded-out real creators and hurt new author growth » ; même chose pour les posts « 🚨BREAKING » systématiques. Mais : « X will never infringe on speech or reach — but we will not compensate for manipulation of the program ». [OFFICIEL-relayé] [TechCrunch, 2026-04-12](https://techcrunch.com/2026/04/12/x-says-its-reducing-payments-to-clickbait-accounts/)
- **Règles** : la politique « manipulation de la plateforme et spam » interdit les engagements inauthentiques visant à rendre un compte ou un contenu plus populaire qu'il ne l'est, et l'activité coordonnée par plusieurs comptes ou par automatisation. [OFFICIEL-relayé] https://help.x.com/rules-and-policies/platform-manipulation
- **Verdict sur Dan Koe** (« payer pour obtenir des retweets ») : **interdit** sur X, et contraire à nos règles d'honnêteté. Le « cercle de 3 à 5 amis qui se partagent mutuellement » est une zone grise : s'il devient systématique et coordonné, c'est de l'engagement inauthentique.

### 4.6 Captures de posts X reprises sur Instagram (croisement avec `instagram.md`)
Tactique de Dan Koe [fiche:SUzKZfyaAK8, 01:46:30, 03:06:19] : capturer ses tweets viraux **avec les likes et reposts visibles** et les publier sur Instagram. Il annonce 230 000 abonnés Instagram ainsi (affirmation, vers 2021-2023).

Ce qui est vrai en 2026 côté Instagram (sources dans `veille/plateformes/instagram.md`, § 2.1 et § 3) :
| Point | État 2026 | Niveau |
|---|---|---|
| Republier le contenu **des autres** | Le compte qui republie surtout le travail d'autrui sort des recommandations ; depuis le **2026-04-30**, la règle couvre aussi les **photos et carrousels**. Un crédit, une bordure ou un filigrane ajoutés ne suffisent pas. | [OFFICIEL] Instagram @creators |
| Capture de **son propre** post X | C'est notre propre texte : la règle d'originalité vise le travail d'autrui. Aucune source ne la classe comme repost. | Déduction d'un texte [OFFICIEL] |
| Filigrane | La liste officielle des facteurs qui réduisent la visibilité porte sur les **Reels** : filigrane d'une autre app (TikTok, CapCut…), Reel **majoritairement texte**, bordure, basse résolution. Une capture de tweet transformée en Reel cumule « texte » et, si le logo X est visible, « filigrane ». Pour les **photos et carrousels**, aucune pénalité de filigrane n'est documentée. | [OFFICIEL] Instagram (Ranking Explained, 2023) + déduction |
| « Instagram classe les captures de posts d'autrui comme du contenu peu travaillé » | Repris par un blog, texte officiel non retrouvé | [RUMEUR] |
| Efficacité du format image | L'engagement des images seules recule (−17 % sur un an, T2 2026) ; les carrousels mènent | [OBSERVÉ par des tiers] Socialinsider |

**Verdict** : la tactique n'est **pas pénalisée en soi** si la capture est la nôtre et publiée en photo ou en carrousel. Elle l'est en Reel (texte, logo d'une autre app). Elle est **interdite chez nous pour les posts d'autrui** (originalité et droits). Elle pose aussi deux problèmes maison : le logo et l'interface de X sont une **marque tierce** (règle du `CLAUDE.md`), et les compteurs affichés figent une preuve sociale qui doit rester exacte. On recrée le texte en visuel natif (§ 7, règle 11).

### 4.7 Vidéo
- Une vidéo par post (ou 4 images, ou 1 GIF). [OFFICIEL] docs.x.com
- Le code compte les ouvertures de vidéo (poids faibles) ; la « vue vidéo de qualité » a été **retirée** des poids en août 2026. Rien n'indique un bonus vidéo en soi. [OFFICIEL + OBSERVÉ]
- Buffer (août 2025) : la vidéo engage moins que le texte seul, chez les comptes gratuits comme chez les Premium. [OBSERVÉ par des tiers]

---

## 5. Formats et limites techniques

| Élément | Valeur | Niveau |
|---|---|---|
| Texte | 280 caractères ; **25 000** avec Premium (post long) | [OFFICIEL-relayé] centre d'aide |
| Articles | Réservés aux abonnés Premium | [OFFICIEL-relayé] |
| Médias par post | Jusqu'à **4 photos**, ou 1 GIF animé, ou 1 vidéo | [OFFICIEL] https://docs.x.com/x-api/media/quickstart/best-practices |
| Images | JPG, PNG, GIF, WEBP ; **5 Mo** maximum | [OFFICIEL] idem |
| GIF animé | 15 Mo, 1280×1080 maximum, 350 images maximum | [OFFICIEL] idem |
| Vidéo via l'API | 0,5 s à **20 min** (compte standard) ou **125 min** (Premium/vérifié) ; 8 Go ou 16 Go ; ratio entre **1:3 et 3:1** ; 60 i/s maximum ; résolution entre 32×32 et 1280×1024 ; recommandé : 1280×720 (paysage), **720×1280 (portrait)**, 720×720 (carré), 16:9 ou 1:1 ; débit conseillé ≥ 5 000 kbit/s vidéo, 128 kbit/s audio | [OFFICIEL] idem |
| Vidéo dans l'app | 140 s pour tous ; Premium jusqu'à **4 h en 1080p** sur web et iOS, 10 min sur Android. Un tiers a observé environ 10 min pour les comptes gratuits sur le web dès avril 2025. **Les chiffres de l'aide, de l'API et des observations ne concordent pas.** | [OFFICIEL-relayé] https://help.x.com/using-x/premium-longer-videos · [OBSERVÉ] [RouteNote, 2025-04-15](https://routenote.com/blog/x-increases-video-length/) |
| API de publication | Paiement à l'usage (abonnement gratuit fermé aux nouveaux développeurs début 2026) : **0,015 $** par post sans URL, **0,200 $** avec URL ; lecture 0,005 $ par post | [OFFICIEL] https://docs.x.com/x-api/getting-started/pricing (date de fermeture du gratuit : [OBSERVÉ], plusieurs blogs) |

---

## 6. Nouveautés des 90 derniers jours (2026-07-24 → 2026-10-22)

| Date | Nouveauté | Statut | Source |
|---|---|---|---|
| 2026-10-20 | Nouveau modèle de classement qui prédit le **temps passé** ; récupération entraînée sur les posts **lus jusqu'au bout** | Annoncé (déploiement non précisé) | [IBTimes](https://www.ibtimes.co.uk/elon-musk-x-algorithm-reading-time-recommendations-1826986) [OFFICIEL-relayé] |
| 2026-10-02 | Nikita Bier confirme la fin de son passage chez X (il avait annoncé le 2026-08-05 quitter le poste de responsable produit, en restant conseiller) | Confirmé | [SMT](https://www.socialmediatoday.com/news/head-of-product-at-x-steps-down/827289/), [wwwhatsnew](https://wwwhatsnew.com/2026/08/08/nikita-bier-deja-x-twitter-head-product-agosto-2026/) [OFFICIEL-relayé] |
| 2026-09-21 | « Under the Hood » étendu : on voit si un post a été retenu dans un pays sur demande légale | Test | [SMT](https://socialmediatoday.com/news/x-shares-more-insight-into-penalties-impacting-post-reach/830972) [OFFICIEL-relayé] |
| 2026-08-17 → 09-04 | Série de mises à jour du code : temps de lecture dans les poids, « vues vidéo de qualité » retirées, agrégation « long dwell » par défaut, classifieur IA de réponses spam | Publié | [Keywords Everywhere](https://keywordseverywhere.com/news/social-algorithm-updates/x-algorithm-open-source/) [OBSERVÉ], recoupé en partie dans `param.rs` |
| 2026-08-13 | Publication des poids, du filtrage de visibilité et du code d'entraînement ; test de « Under the Hood » (libellés de visibilité téléchargeables en JSON ; comptes de plus d'un an avec au moins 10 posts le mois précédent) | Publié / test | dépôt [OFFICIEL] ; Keith Coleman (VP Produit) via [GIGAZINE](https://gigazine.net/gsc_news/en/20260814-x-timeline-algorithm/) |
| 2026-07-28/29 | Bier et Musk : plus besoin de mettre les liens en réponse, pas de pénalité « depuis plus d'un an » | Déclaration | [Free Press Journal](https://www.freepressjournal.in/tech/x-product-head-nikita-bier-confirms-link-penalty-removed-over-a-year-ago-tells-mark-zuckerberg-he-can-post-them-directly) [OFFICIEL-relayé] |

Avant la fenêtre (rappel 2026) : rémunération indexée sur les impressions Premium et poids accru des Articles (16 janv.) ; concours d'Article à 1 M$ (16-28 janv.) ; code ouvert (20 janv.) ; API à l'usage (début 2026) ; vote négatif sur les réponses pour Premium (mars) ; baisse de rémunération des agrégateurs (11 avril) ; test du navigateur de liens sur iOS (avril) ; grosse mise à jour du dépôt (15 mai).

---

## 7. Confrontation avec les conseils de Dan Koe (~2021-2022)

Source : `[fiche:SUzKZfyaAK8]`, notes des parties 02 et 03 (compilation publiée le 2024-02-06, segments enregistrés plus tôt).

| Conseil de la fiche | État en 2026 | Niveau | Confiance |
|---|---|---|---|
| Lien vers la newsletter archivée **en réponse** sous ses tweets [01:54:21] | Plus nécessaire selon X (pas de pénalité depuis environ mi-2025). Le post à lien reste faible chez les comptes gratuits d'après Buffer (2025), et il coûte 13 fois plus cher via l'API. | [OFFICIEL-relayé] + [OBSERVÉ] + [OFFICIEL] | Moyenne |
| « Twitter ne pénalise pas plusieurs posts par jour » [03:05:47] | Vrai pour le compte ; rendement décroissant dans le fil de chaque lecteur (diversité d'auteur), fenêtre de 48 h | [OFFICIEL] code | Élevée |
| Thread hebdomadaire tiré de la newsletter [01:54:21], tweet liste quotidien [01:55:26] | Le thread fonctionne encore mais n'occupe qu'une place dans « Pour toi » et se joue sur son premier post. Avec Premium, le post long (25 000 caractères) ou l'Article sont des alternatives ; X valorise désormais le temps de lecture et les posts lus jusqu'au bout. | [OFFICIEL] + [OFFICIEL-relayé] | Moyenne |
| Le retweet est le moteur de la croissance [01:20:12] | Le repost ne vaut que 1 ; le **partage** (copie du lien 20, message privé 5, citation 5) et la **réponse** (5, +15 entre abonnés mutuels) pèsent bien plus | [OFFICIEL] | Élevée |
| Les commentaires sous les gros comptes servent de vitrine (photo, nom) [01:21:18 ; 01:57:41] | Toujours pertinent, avec une limite : les réponses des comptes payants passent devant. Les réponses en masse peu utiles exposent au classifieur IA de réponses spam (sept. 2026). | [OFFICIEL-relayé] + [OBSERVÉ] | Moyenne |
| Le clic sur le profil mène à l'abonnement [01:20:12] | Le clic sur le profil ne pèse plus directement (0) ; l'abonnement depuis le post pèse 4 | [OFFICIEL] | Élevée |
| Payer pour obtenir des retweets [03:05:47] | Interdit (manipulation de la plateforme) et contraire à nos règles | [OFFICIEL-relayé] | Élevée |
| Captures de tweets reprises sur Instagram avec likes visibles [01:46:30 ; 03:06:19] | Non pénalisé en photo ou carrousel si c'est notre post ; pénalisé en Reel (texte, logo d'une autre app) ; interdit pour les posts d'autrui ; logo X = marque tierce (§ 4.6) | [OFFICIEL] Instagram + déduction | Moyenne |
| Les signaux de classement (époque 2021-2022) | Code ouvert en 2023 (poids publiés), remplacé en janvier 2026 par Phoenix (Grok) dont les poids sont publics depuis août 2026 | [OFFICIEL] | Élevée |

---

## 8. Ce que ça change pour nos agents (règles concrètes)

### Pour tous les agents de création qui écrivent pour X
1. **Écrire pour être partagé et pour qu'on y réponde, pas pour être liké.** Le like pèse 0,66, la réponse 5, le message privé 5, la copie du lien 20. Chaque post doit avoir une raison claire d'être envoyé à quelqu'un (« à qui le lecteur va-t-il l'envoyer ? ») ou de recevoir une réponse de fond. → `ideateur`, `redacteur-hooks`, `redacteur-thread-x`.
2. **Ne jamais provoquer de rejet.** Signaler (−234), masquer (−58,8) et « pas intéressé » (−52,3) effacent des dizaines de réactions positives. Pas de provocation gratuite, pas d'appât (« 🚨BREAKING » systématique), pas de sujet hors de la promesse du compte. → `critique-hook`, `controleur-qualite-marketing`.
3. **Écrire pour la lecture jusqu'au bout.** Depuis le 2026-10-20, X vise le temps passé et les posts lus en entier. Première ligne forte, puis une idée par phrase, sans remplissage. Couper ce qui ne sert pas plutôt qu'allonger. → `redacteur-thread-x`, `correcteur`.
4. **Le post se suffit à lui-même**, même s'il contient un lien (conseil officiel : « write a solid caption »).

### `redacteur-thread-x`
5. **Choisir le format selon l'abonnement du compte.** Avec Premium : par défaut un **post long** (une seule unité lue, le clic « Afficher plus » et le temps passé lui reviennent), ou un **Article** pour un contenu de fond. Sans Premium : thread, en sachant que **seul le premier post est diffusé** dans « Pour toi ». Le premier post d'un thread doit donc tenir seul (promesse + valeur), les suivants livrent. Le choix thread ou post long est une variable à tester (§ 9).
6. Thread : 4 à 8 posts maximum, chacun lisible seul, pas de « 1/ » sans contenu, dernier post = synthèse ou question ouverte de fond. Pas de lien avant la fin.

### `planificateur-calendrier`, `strategiste-contenu`
7. **Fréquence : 1 à 3 posts originaux par jour au maximum par compte**, espacés de plusieurs heures. Il n'y a pas de pénalité de compte, mais chaque post supplémentaire concurrence le précédent dans le fil des abonnés. Règle de travail, pas un chiffre X.
8. **Fenêtre de vie de 48 h** : un sujet important se republie sous un nouvel angle (pas un copier-coller) après 48 h plutôt que d'espérer une longue traîne.
9. **Répondre vite et vraiment** pendant les 2 premières heures (coup de pouce aux petits auteurs, bonus des conversations entre abonnés mutuels). → `gestionnaire-communaute`.

### `redacteur-legende`, `specialiste-seo-social`, `publicateur`
10. **Liens** : plus besoin de les mettre en réponse. Mais un post à lien coûte **0,20 $** via l'API contre 0,015 $ : on ne met un lien que quand le trafic est l'objectif, et on rend le post autonome (le texte donne déjà la valeur). La comparaison « lien dans le post » / « lien en réponse » / « sans lien » passe par `concepteur-experiences`.

### `adaptateur-multiplateforme`, `redacteur-carrousel`, `directeur-creatif-visuel`
11. **Jamais de capture d'écran d'un post X sur Instagram ou LinkedIn.** On **recrée** le texte en visuel natif dans la charte de la marque (carrousel 3:4 ou 4:5 sur Instagram, document PDF sur LinkedIn). Raisons : logo et interface X = marque tierce, Reel « majoritairement texte » ou avec logo d'une autre app = moins visible, et l'originalité est contrôlée sur les photos et carrousels depuis le 2026-04-30. Les posts d'autrui ne sont jamais repris, même crédités.
12. Si l'on veut montrer qu'un texte a marché sur X, on le dit en légende avec des chiffres **réels et datés** (« 1 200 partages sur X en octobre 2026 »), jamais avec des compteurs figés dans une image. → `garde-conformite`.

### `garde-conformite`
13. **Refuser** : achat de reposts, de likes ou d'abonnés ; groupes d'engagement coordonnés ; automatisation de réponses ; réponses en série sous des gros comptes. Un « cercle d'amis » qui se partage mutuellement reste acceptable seulement s'il est occasionnel et sincère.

### `scenariste-reel`, `pont-motion-design` (vidéo pour X)
14. Livrer en **MP4 H.264/AAC**, **720×1280 (portrait) ou 1280×720 (paysage)** recommandés par la documentation API, 30 i/s, débit ≥ 5 000 kbit/s. Un rendu 1080×1920 est accepté dans l'app, mais pour la publication **par API** on vérifie la limite de résolution (1280×1024 dans la documentation) avec `publicateur` avant de livrer. Durée : sous **140 s** (limite sûre pour tous les comptes). La vidéo n'a pas de bonus de classement : elle doit être aussi forte que le texte qui l'accompagne.

### `analyste-performance`, `predicteur-performance`
15. Juger un post X sur les **partages** (copies de lien, envois), les **réponses de fond**, les **abonnements générés** et le temps de lecture si disponible, pas sur les likes ni les impressions brutes. Si le compte y a accès, télécharger chaque mois le rapport « Under the Hood » pour vérifier qu'aucun libellé ne limite la visibilité.

### Pour l'utilisateur (via l'orchestrateur)
16. **Premium** : sans abonnement, un compte de marque sur X part avec un handicap net (portée médiane environ ×10 plus faible selon Buffer, réponses moins bien placées, pas de post long ni d'Article). Décision à remonter dans `journal/questions-utilisateur.md` avant toute campagne X.

---

## 9. Lacunes et vérifications à lancer
- **Centre d'aide X** : x.com et help.x.com bloquent la lecture automatique. À relire par un humain ou un outil autorisé : limites de texte (25 000 contre 4 000), vidéo (140 s, 4 h), classement des réponses Premium.
- **Valeurs de la diversité d'auteur et de la décote hors réseau** : présentes dans le README, introuvables dans `param.rs`. À chercher dans le dépôt lors de la prochaine passe.
- **Déploiement réel** des modèles annoncés le 2026-10-20.
- **Après le départ de Nikita Bier** : qui porte désormais la parole produit ? Les déclarations de 2025-2026 sur les liens tiennent-elles toujours ?
- **Expériences proposées à `concepteur-experiences`** :
  1. lien dans le post, lien en réponse, sans lien (même sujet, même heure) ;
  2. thread contre post long Premium (même contenu) ;
  3. 1 post par jour contre 3 posts par jour pendant 2 semaines (portée totale et par post).

---

## 10. Sources

**Officielles (lues directement)**
- Dépôt `xai-org/x-algorithm`, README et `home-mixer/params/param.rs`, lus le 2026-10-22 : https://github.com/xai-org/x-algorithm
- README `the-algorithm-ml` (poids 2023) : https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md
- Documentation API, tarifs : https://docs.x.com/x-api/getting-started/pricing
- Documentation API, médias : https://docs.x.com/x-api/media/quickstart/best-practices

**Officielles relayées (posts de dirigeants, pages d'aide bloquées)**
- Musk, 2026-10-20, via [IBTimes](https://www.ibtimes.co.uk/elon-musk-x-algorithm-reading-time-recommendations-1826986)
- Bier et Musk sur les liens : [SMT, 2025-10-19](https://www.socialmediatoday.com/news/x-formerly-twitter-testing-links-in-app-link-post-penalties/803176/) ; [Free Press Journal, 2026-07-29](https://www.freepressjournal.in/tech/x-product-head-nikita-bier-confirms-link-penalty-removed-over-a-year-ago-tells-mark-zuckerberg-he-can-post-them-directly)
- Bier sur les agrégateurs : [TechCrunch, 2026-04-12](https://techcrunch.com/2026/04/12/x-says-its-reducing-payments-to-clickbait-accounts/)
- Rémunération et Articles : [PPC Land](https://ppc.land/x-doubles-creator-revenue-pool-and-offers-1m-for-top-article-but-why/)
- Code ouvert de janvier 2026 : [PPC Land](https://ppc.land/xs-algorithm-source-code-drops-what-it-reveals-about-the-platforms-feed-mechanics/)
- Passage à Grok (oct. 2025) : [SMT](https://socialmediatoday.com/news/x-formerly-twitter-switching-to-fully-ai-powered-grok-algorithm/803174)
- Under the Hood : [GIGAZINE, 2026-08-14](https://gigazine.net/gsc_news/en/20260814-x-timeline-algorithm/) ; [SMT, 2026-09-21](https://socialmediatoday.com/news/x-shares-more-insight-into-penalties-impacting-post-reach/830972) ; [tech-ish, 2026-08-14](https://tech-ish.com/2026/08/14/inside-xs-newly-published-visibility-filtering-code/)
- Centre d'aide (non lu directement) : https://help.x.com/en/using-x/how-to-post · https://help.x.com/using-x/premium-longer-videos · https://help.x.com/rules-and-policies/platform-manipulation

**Tiers (affirmations)**
- Buffer, liens : https://buffer.com/resources/links-on-x/ ; Premium : https://buffer.com/resources/x-premium-review/
- Journal des versions du dépôt : [Keywords Everywhere](https://keywordseverywhere.com/news/social-algorithm-updates/x-algorithm-open-source/)
- Multiplicateur Premium de 2023 : [blckalpaca](https://blckalpaca.at/en/knowledge-base/social-media/social-media-algorithms-distribution/x-twitter-algorithm-open-source)
- Classement des réponses : [SocialPilot](https://socialpilot.co/blog/twitter-algorithm)
- Vidéo, comptes gratuits : [RouteNote, 2025-04-15](https://routenote.com/blog/x-increases-video-length/)

---

## Journal des modifications
| Date | Auteur | Modification |
|---|---|---|
| 2026-10-22 | veilleur-algorithmes | **Création de la fiche.** Historique du code ouvert (2023, puis `xai-org/x-algorithm` de janvier 2026 et ses mises à jour d'août-septembre) ; poids 2026 lus dans `param.rs` et comparés à 2023 ; ajustements (diversité d'auteur, décote hors réseau, coup de pouce aux nouveaux auteurs, 48 h, un thread = une place) ; liens (plus de pénalité officielle, données Buffer 2025, 0,20 $ par post à lien via l'API) ; fréquence ; threads, posts longs et Articles ; Premium ; agrégateurs et achat d'engagement ; captures reprises sur Instagram (croisement avec `instagram.md`) ; limites techniques ; nouveautés des 90 jours (modèle de temps passé du 2026-10-20, Under the Hood, départ de Nikita Bier) ; confrontation avec les conseils de Dan Koe `[fiche:SUzKZfyaAK8]` ; 16 règles pour les agents. |
