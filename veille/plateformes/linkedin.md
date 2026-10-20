# LinkedIn : comment le fil distribue le contenu (fiche algorithme)

- **Dernière mise à jour :** 2026-10-20 (veilleur-algorithmes)
- **Période couverte :** décembre 2025 à octobre 2026. Les « nouveautés » portent sur la fenêtre du 2026-07-22 au 2026-10-20.
- **Légende de fiabilité :**
  - **[OFFICIEL]** : LinkedIn le dit lui-même (blog Engineering, Pressroom, centre d'aide, papier de recherche, dirigeant identifié).
  - **[ÉTUDE]** : étude tierce avec échantillon déclaré (van der Blom, Socialinsider, Ordinal…). C'est une *affirmation* tant que `verificateur-faits` ne l'a pas vérifiée.
  - **[RELAIS]** : chiffre repris par un média ou un blog, sans source primaire retrouvée. Ne pas citer comme un fait.
  - **[NON CONFIRMÉ]** : observation de créateurs, ou test pas encore officialisé.

---

## 1. L'essentiel en 10 points

1. **Le fil a été reconstruit en 2026** : récupération par embeddings LLM et classement par un modèle séquentiel de type transformer, qui lit ~1 000 interactions passées du membre. [OFFICIEL, 2026-03-12]
2. **Les relations comptent moins que les centres d'intérêt.** Le moteur de récupération unique remonte explicitement des posts d'auteurs que le lecteur ne suit pas, par proximité sémantique de sujet. [OFFICIEL]
3. **Le temps de lecture long (« long dwell ») est une cible de prédiction explicite**, au même titre que le clic, le scroll sans arrêt, la réaction, le commentaire et le partage. [OFFICIEL]
4. **Le profil de l'auteur fait partie du post** : titre (headline), entreprise et secteur sont donnés au modèle avec le texte et le format. [OFFICIEL]
5. **Pénalisés officiellement :** appâts à engagement (« Commentez OUI »), « thought leadership » recyclé sans substance, vidéos sans rapport avec le texte, pods, commentaires automatisés, « AI slop ». [OFFICIEL, 2026-03 et 2026-09]
6. **« AI slop » :** bouton de signalement depuis fin juillet / début août 2026, des classifieurs limitent la diffusion, et LinkedIn annonce -40 % de vues sur ce contenu. [OFFICIEL, 2026-09-15]
7. **Hashtags : aucun effet sur la distribution.** [OFFICIEL, 2025-12]
8. **Fréquence conseillée par LinkedIn : 2 à 5 posts par semaine**, en espaçant les sujets proches. [OFFICIEL, 2025-12]
9. **Liens externes :** LinkedIn n'a jamais annoncé de pénalité, mais les études mesurent une portée médiane plus faible (-18,8 % selon van der Blom, -26,5 % selon Ordinal). [ÉTUDE]
10. **Formats :** les documents PDF et les posts multi-images ont le meilleur taux d'engagement. La vidéo engage bien ceux qui la voient mais touche moins de monde, alors que LinkedIn pousse fortement le format (fil vidéo, rémunération des créateurs testée en octobre 2026). [ÉTUDE + OFFICIEL]

---

## 2. Comment fonctionne le fil aujourd'hui (sources officielles)

### 2.1 Architecture (blog LinkedIn Engineering, 2026-03-12)
Source : « Engineering the next generation of LinkedIn's Feed », Hristo Danchev, https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed

- **Avant :** une trentaine de sources de récupération distinctes (réseau, tendances, filtrage collaboratif, sujets), chacune avec son index, et un classement qui notait chaque impression isolément (« treated each impression independently »).
- **Maintenant :**
  - **Récupération :** un *dual encoder* LLM unique qui place membres et posts dans le même espace sémantique. Il fait le lien entre sujets voisins même sans mot-clé commun (exemple LinkedIn : « électrotechnique » rapproché de « petits réacteurs modulaires »).
  - **Classement :** un « Generative Recommender » séquentiel. Il comprend la *trajectoire* du membre (« a sequential model understands the trajectory »).
- **Entrées côté post :** format, texte, nom, titre, entreprise et secteur de l'auteur, compteurs d'engagement convertis en percentiles, métadonnées d'article.
  - LinkedIn qualifie la popularité de « such a strong relevance signal ».
- **Entrées côté membre :** parcours, compétences, formation, géographie, et historique chronologique des posts avec lesquels il a interagi positivement.
  - Démarrage à froid : le profil seul suffit pour un nouveau membre.
- **Fraîcheur :** les embeddings de posts et de membres sont rafraîchis « within minutes, not hours ». Un sujet qui monte peut être distribué vite.
- **Équité :** LinkedIn dit auditer les modèles pour que « posts from different creators compete on equal footing ». Aucun attribut démographique n'est utilisé.
- **Ce que LinkedIn ne publie pas :** aucun poids, seuil ou classement des signaux. Tout chiffre de type « un enregistrement vaut 5 likes » est **non officiel**.

### 2.2 Le papier de recherche (arXiv 2602.12354, 2026-02-12, accepté à CIKM '26)
Source : « An Industrial-Scale Sequential Recommender for LinkedIn Feed Ranking » (Feed-SR), https://arxiv.org/abs/2602.12354

- Feed-SR (un transformer) remplace l'ancien classeur DCNv2. Il est « currently the primary member experience on LinkedIn's Feed ».
  - Test A/B : +2,10 % de temps passé.
- Il prédit 6 actions en deux familles :
  - **passives :** clic, scroll sans arrêt, *Long Dwell* ;
  - **actives (« Contribution ») :** réaction, commentaire, partage.
- **Le seuil de « Long Dwell » varie selon le type de post** (valeurs non publiées). Les tranches de dwell vont de moins de 3 s à plus de 60 s. Chiffres repris de la synthèse fast-growth.fr, à recouper avec le PDF.
- L'historique couvre jusqu'à 1 000 posts vus sur environ un an, et les données perdent la moitié de leur poids tous les 60 jours. Autrement dit, l'activité récente pèse plus. [OFFICIEL via le papier, synthèse fast-growth.fr]

### 2.3 Ce que LinkedIn veut voir et ce qu'il freine (Tim Jurka, 2026-03-12)
Source : https://www.linkedin.com/pulse/updates-linkedin-feed-focusing-authentic-relevant-tim-jurka-umwnc/
- **Mis en avant :** « actionable insights » (analyses de tendances, points de vue de dirigeants), « a real person offering a real point of view ». Nouveaux membres : un sélecteur de centres d'intérêt (*Interest Picker*) dès l'inscription.
- **Réduit ou filtré :** « repetitive, click-driven posts », « engagement bait » (ex. « Comment 'Yes' if you agree »), thought leadership « recycled », vidéos sans rapport avec le texte (« should no longer gain additional reach »).
- **Combattus :** pods d'engagement et automatisation des commentaires. Les extensions et outils tiers sont « not allowed ».

### 2.4 FAQ officielle du fil (Gyanda Sachdeva, VP Product, 2025-12-18)
Source : https://www.linkedin.com/pulse/top-linkedin-feed-questions-2025-gyanda-sachdeva-anl2e/
- **Signaux cités :** utilité, originalité, actualité, pertinence, usage des médias, fréquence de publication, et un langage qui « semble promotionnel ou générique » (négatif).
- **Thèmes qui marchent :** actualité du secteur *avec votre point de vue*, contenu informatif travail/économie, leçons de carrière vécues.
- **Fréquence :** 2 à 5 posts par semaine. Publier 2 fois par semaine donne jusqu'à 5x plus de vues de profil en moyenne. Plus d'un post par jour ne nuit pas à la portée totale, mais il faut espacer les sujets similaires.
- **Hashtags :** n'influencent pas la distribution.
- **Vidéo :** les meilleures ont un *hook texte*, des sous-titres incrustés et des visuels engageants (graphismes, b-roll).
- **Commentaires :** apporter un vrai point de vue, poser des questions, taguer des personnes utiles. LinkedIn « investit dans l'expérience commentaires » en 2026.
- **IA :** « members, not AI, power the best engagement ». L'IA sert à augmenter, pas à remplacer.

### 2.5 Lutte contre l'« AI slop » (Pressroom LinkedIn, 2026-09-15)
Source : https://news.linkedin.com/2026/how-linkedin-is-tackling-ai-slop, plus le centre d'aide https://www.linkedin.com/help/linkedin/answer/a1481496
- **Définition :** « low-effort, likely AI-generated content that may sound polished on the surface », c'est-à-dire générique, répétitif, recyclé ou fait pour capter l'attention sans rien apporter.
- **Mécanique :**
  - option « Seems like AI slop » sur les posts **et les commentaires** ;
  - le post disparaît du fil de celui qui signale, et le signalement entraîne les classifieurs ;
  - au-delà d'un certain volume de signalements, l'auteur voit une indication dans ses statistiques de post.
- **Chiffres LinkedIn :** plus d'1 million de membres ont utilisé l'option en deux semaines, et le contenu classé AI slop fait -40 % de vues. Des centaines de milliers de tentatives de commentaires automatisés sont bloquées chaque jour.
- **Outillage :** « Enhance your post » (réécriture IA) est remplacé par un correcteur (*Post Proofreader*) qui garde la voix du membre.
- **Centre d'aide :** relire, éditer et valider tout contenu assisté par IA. Mentionner l'usage de l'IA quand on s'en est beaucoup servi, sauf si c'est évident.

---

## 3. Signaux de classement : confirmés et supposés

### 3.1 Confirmés [OFFICIEL]
| Signal | Ce qui est confirmé | Source (date) |
|---|---|---|
| Long dwell (lecture ou visionnage long) | Cible de prédiction, seuil propre à chaque format | Engineering 2026-03-12 ; arXiv 2026-02-12 |
| Clic, scroll sans arrêt | Signaux passifs prédits. Un post vu puis ignoré devient un « négatif dur » à l'entraînement | Engineering 2026-03-12 |
| Réaction, commentaire, partage | Signaux actifs (« Contribution ») | arXiv 2026-02-12 |
| Popularité (compteurs en percentiles) | « strong relevance signal » | Engineering 2026-03-12 |
| Pertinence sémantique sujet ↔ lecteur | Embeddings LLM, sujets voisins rapprochés | Engineering 2026-03-12 |
| Profil de l'auteur (titre, entreprise, secteur) | Entrée du modèle avec le texte | Engineering 2026-03-12 |
| Profil et historique récent du lecteur | Compétences, parcours, géographie, ~1 000 interactions. Le récent pèse plus | Engineering ; Jurka 2026-03-12 |
| Fraîcheur | Rafraîchissement en quelques minutes, actualité qui prend vite | Engineering 2026-03-12 |
| Format / médias | Le format est une entrée, et « media use » est un signal cité | Engineering ; Sachdeva 2025-12 |
| Langage promotionnel ou générique | Négatif | Sachdeva 2025-12 |
| Appâts à engagement, contenu recyclé, vidéo hors sujet | Réduits ou filtrés | Jurka 2026-03-12 |
| Pods, commentaires automatisés | Neutralisés. Risque de restriction et d'exclusion de programmes (Top Voices) | Jurka 2026-03 ; Oscar Rodriguez (VP Product) fin 2025 |
| AI slop (classifieurs + signalements) | Diffusion limitée, -40 % de vues | Pressroom 2026-09-15 |
| Hashtags | Sans effet sur la distribution | Sachdeva 2025-12 |
| Démographie de l'auteur | Non utilisée | Engineering 2026-03 ; Sachdeva 2025-12 |

### 3.2 Supposés (créateurs, études) : à traiter comme des affirmations
| Affirmation | Source | Fiabilité |
|---|---|---|
| Portée -60 % sur 2 ans pour les créateurs actifs, vues -50 %, engagement -20 à -25 %, croissance d'abonnés -59 % | Richard van der Blom, *Algorithm Insights 2026* (1,3 M posts, 50 000 créateurs), d'après le podcast Creator Science du 2026-06-02 | [ÉTUDE], rapport complet non consulté (payant) |
| Distribution « relations » 70 % (2024), 54 % (2025), 10 % (2026), et « intérêts » 5 %, 21 %, 50 % | Attribué à van der Blom 2026 par des blogs | [RELAIS], le sens va avec l'officiel, les chiffres sont non vérifiés |
| ~9 % du fil = posts suggérés hors réseau | Van der Blom (podcast) | [ÉTUDE] |
| Un lien dans le corps = -18,8 % de portée médiane | Van der Blom 2026 | [ÉTUDE] |
| Posts avec lien = -26,5 % de portée (p < 0,001) | Ordinal, 900 000+ posts 2023-2026 (vend un outil « lien en 1er commentaire » ; page devenue 404) | [ÉTUDE], conflit d'intérêts |
| Les posts avec plusieurs liens font mieux que ceux sans lien | Saywhat, *State of the Algorithm* T1 2026, 397 605 posts | [ÉTUDE], contredit les deux précédentes (effet qualité ?) |
| « Pénalité lien de 60 % » ; « lien en commentaire = -80 % » | Blogs, « Forbes » cité sans lien | [RELAIS], **ne pas utiliser** |
| « L'enregistrement vaut 5x un like / 2x un commentaire », « la sauvegarde est le 1er facteur » | Blogs (SocialPilot…) | [RELAIS], non officiel |
| Répondre dans l'heure +35 %, commenter avant de publier +21 % | Circule sans méthode publiée | [RELAIS] |
| Publier moins souvent quand on a quelque chose à dire = +10 à 15 % de portée | Van der Blom (podcast) | [ÉTUDE] |
| Publier tous les jours = -26 % de portée par post | Article M. Goodman 2026-05, « la recherche » non nommée | [RELAIS] |
| Sans hashtag = +5 à 10 % | Idem | [RELAIS], cohérent avec l'officiel « aucun effet » |
| Articles LinkedIn isolés ≈ 0,4x la portée normale ; newsletters en hausse | Van der Blom (podcast, « I think ») | [ÉTUDE], approximatif |
| Détection des pods ≈ 97 % | Van der Blom | [ÉTUDE] |

---

## 4. Thème par thème

### 4.1 Portée organique
- **Officiel :** pas de chiffre de portée publié. LinkedIn parle de portée « plus pertinente », pas « virale ».
  - L'activité augmente : posts originaux +14 % et commentaires « orientés connaissance » +11 % sur un an (T3 de l'exercice 2026, Pressroom 2026-04-30, https://news.linkedin.com/2026/Q3-Earnings-Highlights).
  - Plus d'1,3 milliard de membres.
- **Études :** la portée moyenne par post a baissé durablement (van der Blom : « reset to a lower baseline »). L'engagement *par vue* monte, car l'audience touchée est plus ciblée.
- **Lecture :** plus de concurrence (+14 % de posts) et un ciblage plus fin. Un post touche moins de monde, mais des gens plus pertinents, y compris hors réseau si le sujet colle à leurs intérêts.

### 4.2 Vidéo, et vidéo verticale dans le fil
- **Officiel :**
  - Expérience plein écran pour la vidéo verticale sur mobile, lancée à l'été 2024 : on balaie d'une vidéo à l'autre après un tap. Il y a aussi un module « Videos For You », un onglet vidéo mobile étendu au desktop, et des carrousels de vidéos dans la recherche. Dans le lecteur : aperçu du profil, bouton « Suivre » mis en avant, statistique de temps de visionnage moyen. (Lakshman Somasundaram, LinkedIn, 2025-02-04, https://www.linkedin.com/pulse/up-36-over-last-year-video-linkedin-booming-time-now-somasundaram-yqbzc ; vidéo regardée +36 % sur un an à cette date.)
  - La vidéo est « a key part of LinkedIn's content ecosystem ». Recette officielle : hook texte, sous-titres incrustés, b-roll ou graphismes (Sachdeva 2025-12).
  - Une vidéo sans rapport avec le texte du post ne gagne plus de portée supplémentaire (Jurka 2026-03-12).
  - Monétisation : test **In-Stream Ads** depuis le 2026-10-15, pré-rolls rémunérés pour des créateurs américains invités (Pressroom 2026-10-15). La vidéo payante croît de près de 30 % sur un an (T3 de l'exercice 2026). LinkedIn a donc un intérêt économique direct à la vidéo.
  - Limites techniques : voir la section 5.
- **Études :**
  - La vidéo engage bien ses spectateurs (Socialinsider T2 2026 : 5,90 % d'engagement).
  - Mais elle touche moins de monde : Magnettu donne ~887 vues moyennes contre ~2 639 pour un document.
  - Van der Blom (2026) déconseille la vidéo à la majorité des créateurs.
  - Durée souvent recommandée : 30 à 90 s (blogs, non officiel).
- **[NON CONFIRMÉ] (octobre 2026) :**
  - sur l'app mobile, un logo LinkedIn recouvrirait environ les 15 % supérieurs de chaque vidéo (observation d'un créateur, relayée par Influent) ;
  - zones d'interface en bas en plein écran (nom, légende, boutons) : un outil tiers recommande de laisser ~108 px en haut et ~320 px en bas sur du 1080x1920.
- **Recadrage :** pas de documentation officielle sur le recadrage du 9:16 dans le fil. L'usage le plus prudent est de garder l'essentiel dans la zone centrale 4:5.

### 4.3 Carrousels / documents PDF
- **Officiel (centre d'aide, https://www.linkedin.com/help/linkedin/answer/97459) :** PDF, PPT, PPTX, DOC ou DOCX, **100 Mo et 300 pages maximum**, conversion en PDF recommandée. Le document s'affiche en diapositives qu'on fait défiler.
- Le carrousel « natif » d'images a été retiré en 2023. Aujourd'hui, « carrousel » veut dire **document PDF**, ou post **multi-images** (jusqu'à 20 images, centre d'aide https://www.linkedin.com/help/linkedin/answer/100983).
- **Études :**
  - Socialinsider T2 2026 : documents natifs 6,60 % d'engagement (6,90 % au T1), multi-images 6,90 %, vidéo 5,90 %, image 5,20 %, sondage 4,50 %, texte 3,95 %, lien 3,30 % (https://www.socialinsider.io/social-media-benchmarks/linkedin).
  - Van der Blom recommande, pour une semaine à 2 ou 3 posts : texte + image, un carrousel, puis texte + image.
  - Ordinal : les carrousels ont le meilleur taux d'engagement médian, mais le texte seul a la meilleure portée. **Le gagnant dépend de la métrique.**
- **Lien avec le dwell :** un document fait passer du temps sur le post, et le long dwell est une cible officielle. C'est l'explication la plus plausible de sa performance (inférence).
- **Pratique courante (non officielle) :** 5 à 10 diapositives, format portrait 1080x1350 (4:5) ou carré 1080x1080.

### 4.4 Liens externes
- **Officiel :** **aucune** règle publiée qui pénalise les liens. Les guides LinkedIn ciblent le spam et la faible qualité, pas les URL.
- **Études :** -18,8 % (van der Blom) et -26,5 % (Ordinal) de portée médiane pour un lien dans le corps, mais Saywhat trouve l'inverse sur les posts à liens multiples.
  - L'effet du « lien en premier commentaire » est **incertain** : les sources se contredisent, et le -80 % qui circule n'a pas de source.
- **Lecture :** l'effet mesuré est une corrélation. Mécanique plausible : un clic sortant raccourcit le dwell sur la plateforme.
- **Conséquence :** par défaut, pas de lien dans le corps sauf objectif de trafic assumé, et à tester dans `experiences/`.

### 4.5 Commentaires
- **Officiel :**
  - le commentaire est une action « active » prédite ;
  - LinkedIn suit les commentaires « orientés connaissance » (+11 % sur un an, T3 de l'exercice 2026) et investit dans les commentaires en 2026 ;
  - les commentaires sont triés par pertinence ;
  - **les commentaires épinglés reviennent** pour les auteurs (annonce du 2026-10-15, déploiement progressif) ;
  - les pods et l'automatisation sont combattus (des groupes ont été supprimés, risque d'exclusion de Top Voices) ;
  - les commentaires eux-mêmes peuvent être signalés comme « AI slop ».
- **Études :** van der Blom traite les commentaires comme un signal du graphe d'intérêts. Il recommande ~15 minutes de disponibilité après publication pour répondre, et 5 à 10 commentaires de fond par jour sur des posts de pairs du même sujet.
  - Les bonus chiffrés (+35 %, +21 %…) n'ont **aucune méthode publiée**.

### 4.6 Expertise et sujets
- **Officiel :**
  - récupération par sujet sémantique ;
  - titre, entreprise et secteur de l'auteur en entrée du modèle ;
  - membres ciblés selon compétences et centres d'intérêt ;
  - *Interest Picker* à l'inscription ;
  - tests de fils thématiques : « suggested feeds » en juin 2026, construits sur les sujets avec lesquels le membre a interagi et sur l'actualité (Julia Cabral Flavin, LinkedIn, rapporté par Social Media Today le 2026-06-24) ;
  - *Creator Discovery* (bêta pour marques depuis le 2026-10-01) filtre les créateurs par expertise, audience, format et secteur (mise à jour agences LinkedIn, relayée par Influent).
- **Études :**
  - van der Blom parle d'une « empreinte de sujet » : un sujet principal, 2 ou 3 sous-sujets, ~80 % des posts dessus ;
  - il rapporte une hausse des visites de profil et de la portée environ 3 semaines après une refonte du profil centrée sur la cible ;
  - test conseillé : demander à une IA quels sont les sujets principaux de vos 20 derniers posts.
- **Lecture :** c'est le levier qui découle le plus directement du nouveau système. Si le modèle ne sait pas « de quoi parle » un auteur, il ne sait pas à qui le montrer hors réseau.

### 4.7 Fréquence
- **Officiel :** 2 à 5 posts par semaine, en espaçant les sujets proches. Juger sur l'engagement total, pas par post (Sachdeva 2025-12).
- **Études :** l'optimum est passé de 5-6 à 2-4 par semaine, et 2-3 suffisent pour la moyenne (van der Blom 2026). Publier tous les jours ferait baisser la portée par post [RELAIS].
- **Synthèse :** **3 posts par semaine** par compte, jamais deux posts sur le même sujet à moins de 48 h (règle maison issue de l'officiel « espacer »).

### 4.8 Newsletters et articles
- Les newsletters sont ouvertes à tous les membres, avec couvertures vidéo et statistiques e-mail (centre d'aide https://www.linkedin.com/help/linkedin/answer/a517925). Elles arrivent en notification et par e-mail, donc hors fil.
- Van der Blom : les newsletters progressent et portent l'essentiel de ses conversions. Les articles isolés ont une faible portée dans le fil [ÉTUDE].

---

## 5. Formats et limites techniques

| Élément | Limite / spécification | Statut |
|---|---|---|
| Vidéo : durée | 3 s min (desktop), 2 s (app) ; **15 min max** | [OFFICIEL] centre d'aide a548372 |
| Vidéo : fichier | 75 Ko à 5 Go | [OFFICIEL] |
| Vidéo : ratio | **1:2,4 à 2,4:1** (le 9:16, le 4:5, le 1:1 et le 16:9 passent tous) | [OFFICIEL] |
| Vidéo : résolution | 256x144 à 4096x2304 | [OFFICIEL] |
| Vidéo : images/s, débit | 10 à 60 fps ; 192 kbps à 30 Mbps | [OFFICIEL] |
| Vidéo : formats | MP4, MOV, AVI, WEBM, MKV, WMV… (MP4 H.264/AAC conseillé) | [OFFICIEL] (conseil MP4 = usage) |
| Vidéo : zones de sécurité | Le centre d'aide dit d'éloigner texte et logos des bords, sans marges chiffrées. Logo LinkedIn ~15 % en haut sur mobile [NON CONFIRMÉ] | mixte |
| Vidéo : sous-titres | Fichier .SRT accepté. Sous-titres incrustés recommandés par LinkedIn | [OFFICIEL] Sachdeva ; .SRT = [RELAIS] |
| Vidéo : durée efficace | 30 à 90 s | [RELAIS] |
| Document | PDF/PPT/PPTX/DOC/DOCX, **100 Mo, 300 pages** | [OFFICIEL] centre d'aide 97459 |
| Document : format conseillé | 1080x1350 (4:5) ou 1080x1080, 5 à 10 diapositives | [RELAIS] |
| Images | **Jusqu'à 20 par post** ; ~36 mégapixels max | [OFFICIEL] 100983 ; 36 MP = [RELAIS] |
| Image : dimensions usuelles | 1200x627 (1,91:1) ; 1080x1080 ; 1080x1350 | [RELAIS] |
| Texte du post | ~3 000 caractères ; coupure « …voir plus » après environ 2 à 3 lignes | usage largement documenté, page d'aide non revérifiée ce jour |
| Live | Chaque direct doit être rattaché à un événement programmé | [RELAIS] |

---

## 6. Nouveautés des 90 derniers jours (2026-07-22 → 2026-10-20)

| Date | Nouveauté | Statut | Source |
|---|---|---|---|
| 2026-07-30 (déploiement début août) | Option « Seems like AI slop » sur posts et commentaires ; classifieurs renforcés ; fin de « Enhance your post » | [OFFICIEL] | TechCrunch https://techcrunch.com/2026/07/30/linkedin-adds-a-button-to-report-ai-generated-slop/ ; Pressroom 2026-09-15 |
| Août 2026 | Post Proofreader (Premium) remplace la réécriture IA | [OFFICIEL] relayé | Social Media Today |
| Août 2026 | Clips et chapitres IA pour les replays LinkedIn Live (bêta publique) | [OFFICIEL] | LinkedIn for Marketing (Pulse) |
| ~2026-08-20 | Hari Srinivasan (CPO) : plus d'1 M de membres ont signalé, -40 % de vues sur l'AI slop | [OFFICIEL] | Engadget ; Pressroom 2026-09-15 |
| 2026-09-15 | Page officielle « How LinkedIn is tackling AI slop » ; une indication de signalement arrive dans les statistiques des auteurs | [OFFICIEL] | https://news.linkedin.com/2026/how-linkedin-is-tackling-ai-slop |
| 2026-09-18 | Test d'un onglet **« Network »** (posts des seules relations et abonnements), à côté d'un « For You » | [OFFICIEL] (post de H. Srinivasan), test | Social Media Today 2026-09-20 ; Pressroom 2026-10-15 (marchés : États-Unis, Inde, Australie, Royaume-Uni selon le texte) |
| 2026-09-23 | Recommandation par des collègues pour les membres vérifiés ; 115 M de membres vérifiés | [RELAIS] TechCrunch | TechCrunch |
| 2026-09-28 | Premiere Video Ads en bêta publique (Reserved Ads) | [OFFICIEL] | Centre d'aide LMS a9590437 |
| Sept. 2026 → janv. 2027 | 3 niveaux de Premium Company Page (Essentials, Plus, Pro) | [OFFICIEL] | premium.linkedin.com |
| 2026-10-01 | Creator Discovery (bêta marques) : recherche de créateurs par expertise, audience, format, secteur | [OFFICIEL] relayé | Influent / Social Media Today |
| 2026-10-15 | Communiqué Pressroom « New Ways to Build Meaningful Connections, Grow Your Side Hustle, and Earn on LinkedIn » : **In-Stream Ads** (test, créateurs américains invités), **tableau de bord créateur** unifié (déploiement mondial « in the coming weeks »), **commentaires épinglés**, **Advice Sessions** (conseil payant 1:1, Business Premium États-Unis), carte de visite numérique, notes privées sur les profils | [OFFICIEL] (URL du communiqué non récupérée) | PPC Land 2026-10-19 ; Engadget 2026-10-15 |
| Oct. 2026 | Logo LinkedIn incrusté sur ~15 % du haut des vidéos (app mobile) | [NON CONFIRMÉ] | Influent (analyse d'un créateur) |
| Oct. 2026 | Nouvelle interface iOS/Android en déploiement | [RELAIS] | SocialBee |

Pour mémoire, juste avant la fenêtre : test des « suggested feeds » thématiques (2026-06-24) ; rapport van der Blom 2026 (podcast du 2026-06-02).

**Ce qui n'a pas changé dans la fenêtre :** aucune nouvelle publication Engineering sur le classement depuis mars 2026, et aucune déclaration officielle sur les liens, les documents ou la durée des vidéos.

---

## 7. Ce que ça change pour nos agents (règles concrètes)

### Pour tous les agents de création
1. **Un vrai point de vue, un vécu ou une donnée propre dans chaque post.** C'est ce que LinkedIn promeut (« real person, real point of view ») et ce que les classifieurs anti-slop ciblent en creux. Pas de généralités recyclées. Test : « une autre entreprise aurait-elle pu écrire ce post mot pour mot ? » Si oui, on réécrit.
2. **Interdits** (refus par `garde-conformite`) :
   - « Commentez OUI / mettez un emoji pour recevoir… » ;
   - les pods ;
   - tout outil de commentaire automatisé ;
   - une vidéo sans rapport avec le texte ;
   - un texte IA non retravaillé.
   Toute demande de commentaire doit appeler un vrai contenu (une question ouverte sur le sujet), pas un mot-clé.
3. **Aucun hashtag pour la distribution.** 0 à 3 maximum, seulement pour le suivi ou la recherche (`specialiste-seo-social`).
4. **L'IA pour aider, jamais à la place.** Pas de tournures typiques d'IA en série. Si l'IA a fortement contribué, `garde-conformite` évalue s'il faut le mentionner (recommandation du centre d'aide).
5. **Les chiffres non officiels de cette fiche ne sont jamais présentés comme des faits** dans nos contenus (règle d'honnêteté). On les cite comme « selon <étude> ».

### `strategiste-contenu`, `architecte-personal-brand`, `planificateur-calendrier`
6. **Un sujet principal + 2 ou 3 sous-sujets par compte, ~80 % des posts dessus.** Le modèle doit pouvoir dire « de quoi parle » l'auteur.
7. **Le titre et le profil de l'auteur doivent annoncer ce sujet.** Le titre (headline) est une entrée officielle du modèle. Demander à l'utilisateur d'aligner son profil avant une campagne (via `journal/questions-utilisateur.md`).
8. **Cadence : 3 posts par semaine par compte** (fourchette officielle 2 à 5). Pas deux posts sur le même sous-sujet à moins de 48 h.
9. **Mix hebdomadaire par défaut :** 1 document PDF, 1 post texte + image (ou multi-images), 1 format libre (texte seul fort, vidéo, ou commentaire d'actualité). La vidéo n'est pas le format par défaut pour la portée. On l'utilise pour un objectif précis (démonstration du savoir-faire Sillage, notoriété), avec un suivi spécifique.
10. **Actualité du secteur + notre point de vue** = thème officiellement performant. Réagir vite, car les embeddings se rafraîchissent en quelques minutes.

### `redacteur-linkedin`, `redacteur-hooks`, `redacteur-legende`
11. **La première phrase porte tout** (recommandation officielle : « strong first sentence, clear point of view, simple narrative »). Elle doit tenir avant le « …voir plus », soit environ 2 lignes sur mobile.
12. **Écrire pour le temps de lecture, pas pour le clic** : une idée, une structure lisible, une fin qui donne envie de commenter avec du contenu. Le long dwell est une cible officielle.
13. **Pas de lien externe dans le corps par défaut.** Si un lien est indispensable (trafic), on le signale comme variable d'expérience, et `concepteur-experiences` compare « lien dans le corps », « lien en commentaire » et « sans lien ».

### `redacteur-carrousel`, `directeur-creatif-visuel`
14. **Document PDF en 4:5 (1080x1350)**, 6 à 10 diapositives. Diapo 1 = accroche visuelle (style Sillage : clair, sobre, ~5 mots). Dernière diapo = conclusion ou question, pas une publicité. Export en PDF (100 Mo et 300 pages max, sans risque).
15. Multi-images : jusqu'à 20 images, mais 3 à 6 suffisent. Même ratio partout.

### `scenariste-reel`, `pont-motion-design` (commandes au studio Sillage)
16. **Ratio de livraison LinkedIn : 4:5 (1080x1350)** pour le fil, ou **9:16 (1080x1920) avec tout l'essentiel dans la zone centrale 4:5**. Ne rien placer d'important dans les ~15 % du haut (logo LinkedIn possible) ni dans les ~17 % du bas (interface plein écran). Ces marges ne sont pas officielles : les valider au contrôle qualité sur un téléphone.
17. **Durée cible : 20 à 60 s** (le style Sillage est court). 90 s maximum en organique, et 15 min reste la limite technique.
18. **Hook visuel dès la 1re seconde, et un texte de post qui décrit vraiment la vidéo** (une vidéo sans rapport avec le texte ne gagne plus de portée).
19. **Lecture sans son par défaut.** Le studio Sillage n'utilise jamais de musique. Si la vidéo a une voix off, **sous-titres incrustés obligatoires** (recommandation officielle), sobres, dans la charte, compatibles avec la règle « peu de texte ». Sans voix off, les 3 ou 4 messages courts à l'écran suffisent. Les effets sonores sont un bonus, pas un porteur de sens.
20. Livrer en MP4 H.264/AAC 1080p, 30 fps, sous 5 Go (sans souci). Préparer aussi un .SRT si voix off.

### `gestionnaire-communaute`
21. **Être disponible ~15 à 30 min après publication** pour répondre à chaque commentaire par une vraie réponse (pas un « Merci ! »). Pratique d'étude, pas une règle officielle, mais cohérente avec l'officiel « Contribution ».
22. **Épingler** le meilleur commentaire de fond (ou notre commentaire de complément) dès que la fonction est disponible sur le compte.
23. **Commenter des pairs du même sujet chaque jour**, avec des commentaires de fond rédigés (jamais automatisés, jamais générés en série). Les commentaires peuvent eux aussi être signalés « AI slop ».

### `predicteur-performance`, `analyste-performance`
24. **Juger un post sur la portée hors réseau** (statistiques réseau / hors réseau), **les enregistrements, les envois et le temps de visionnage moyen** pour la vidéo, plutôt que sur les likes. Surveiller l'indication « signalé comme AI slop » dans les statistiques (à venir), et le tableau de bord créateur unifié (déploiement fin 2026).
25. Comparer à l'engagement total de la semaine, pas post par post (recommandation officielle).

### `publicateur`
26. Rien de nouveau côté publication : API officielle uniquement, et les documents PDF sont publiables via l'API (à confirmer selon le type de compte).

---

## 8. Lacunes et vérifications à lancer
- **`verificateur-faits` :**
  - obtenir le rapport van der Blom 2026 complet (portée par format, liens, dwell, durée vidéo, nombre de diapositives) ;
  - vérifier les chiffres « relations 10 % / intérêts 50 % ».
- **Recadrage officiel du 9:16 dans le fil et marges de sécurité** : aucune documentation LinkedIn. À mesurer nous-mêmes (capture sur iOS et Android).
- **Logo incrusté sur les vidéos mobiles :** à confirmer.
- **Expériences proposées à `concepteur-experiences` :**
  1. lien dans le corps, lien en commentaire, ou sans lien ;
  2. vidéo 4:5 ou 9:16 ;
  3. document 6 diapositives ou 12 diapositives ;
  4. même sujet en document ou en texte + image.
- **Onglet Network et In-Stream Ads :** surveiller l'extension hors test et les marchés (France ?).

---

## 9. Sources

**Officielles**
- LinkedIn Engineering, H. Danchev, 2026-03-12 : https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed
- Papier Feed-SR, arXiv 2602.12354, 2026-02-12 : https://arxiv.org/abs/2602.12354
- Tim Jurka (LinkedIn), 2026-03-12 : https://www.linkedin.com/pulse/updates-linkedin-feed-focusing-authentic-relevant-tim-jurka-umwnc/
- Gyanda Sachdeva (VP Product), 2025-12-18 : https://www.linkedin.com/pulse/top-linkedin-feed-questions-2025-gyanda-sachdeva-anl2e/
- Pressroom, AI slop, 2026-09-15 : https://news.linkedin.com/2026/how-linkedin-is-tackling-ai-slop
- Pressroom, résultats T3 de l'exercice 2026, 2026-04-30 : https://news.linkedin.com/2026/Q3-Earnings-Highlights
- Lakshman Somasundaram (LinkedIn), vidéo, 2025-02-04 : https://www.linkedin.com/pulse/up-36-over-last-year-video-linkedin-booming-time-now-somasundaram-yqbzc
- Centre d'aide, spécifications vidéo : https://www.linkedin.com/help/linkedin/answer/a548372
- Centre d'aide, documents : https://www.linkedin.com/help/linkedin/answer/97459
- Centre d'aide, images : https://www.linkedin.com/help/linkedin/answer/100983
- Centre d'aide, contenu assisté par IA : https://www.linkedin.com/help/linkedin/answer/a1481496
- Centre d'aide, newsletters : https://www.linkedin.com/help/linkedin/answer/a517925
- Centre d'aide LMS, Premiere Video Ads : https://www.linkedin.com/help/lms/answer/a9590437

**Médias (relais d'annonces officielles)**
- Social Media Today, refonte du fil, 2026-03-12 : https://www.socialmediatoday.com/news/linkedin-updates-its-feed-algorithm/814638/
- Social Media Today, suggested feeds, 2026-06-24 : https://www.socialmediatoday.com/news/linkedin-tests-suggested-feeds/823722/
- Social Media Today, conseils LinkedIn 2026 : https://www.socialmediatoday.com/news/linkedin-shares-tips-on-how-to-boost-your-in-app-performance-in-2026/808448/
- TechCrunch, bouton AI slop, 2026-07-30 : https://techcrunch.com/2026/07/30/linkedin-adds-a-button-to-report-ai-generated-slop/
- Engadget, annonce du 2026-10-15 : https://www.engadget.com/2287154/linkedin-is-adding-new-tools-to-help-people-with-their-side-hustles/
- PPC Land, refonte du fil, 2026-03-15 : https://ppc.land/linkedin-rebuilds-its-feed-from-scratch-with-llms-and-gpu-powered-ranking/
- PPC Land, In-Stream Ads, 2026-10-19 : https://ppc.land/linkedin-tests-paying-us-creators-for-pre-roll-ads-on-their-videos/

**Études et analyses (affirmations)**
- R. van der Blom, *Algorithm Insights 2026*, via le podcast Creator Science, 2026-06-02 : https://creatorscience.com/podcast/richard-van-der-blom-2/
- Synthèse sourcée (fast-growth.fr, livre blanc, mis à jour 2026-10-04) : https://fast-growth.fr/en/white-paper/linkedin-algorithm-2026/
- M. Goodman, 2026-05-07 : https://melaniegoodmanlinkedinconsultant.substack.com/p/linkedin-algorithm-2026-reach-topic-authority
- Socialinsider, benchmarks LinkedIn 2026 : https://www.socialinsider.io/social-media-benchmarks/linkedin
- Influent, récapitulatifs août et octobre 2026 : https://influent.co/blog/linkedin-updates-august-2026 , https://influent.co/blog/linkedin-updates-october-2026

---

## Journal des modifications
| Date | Auteur | Modification |
|---|---|---|
| 2026-10-20 | veilleur-algorithmes | Création de la fiche. Sources : refonte LLM du fil (Engineering + arXiv, fév.-mars 2026) ; signaux confirmés et supposés ; 8 thèmes (portée, vidéo verticale, documents, liens, commentaires, expertise, fréquence, newsletters) ; limites techniques officielles (vidéo, documents, images) ; nouveautés du 2026-07-22 au 2026-10-20 (AI slop, onglet Network, In-Stream Ads, commentaires épinglés, tableau de bord créateur, Creator Discovery) ; 26 règles pour les agents. |
