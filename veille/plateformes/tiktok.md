# TikTok : comment la plateforme distribue le contenu (fiche de veille)

- **Dernière mise à jour :** 2026-10-20 (agent `veilleur-algorithmes`)
- **Fenêtre « nouveautés » :** du 2026-07-22 au 2026-10-20 (90 jours)
- **Prochaine revue conseillée :** 2026-11-20, ou plus tôt si TikTok publie une annonce officielle sur le classement, sur la durée des vidéos ou sur le Creator Rewards Program.

**Niveaux de confiance utilisés dans cette fiche**
- **[OFFICIEL]** : texte publié par TikTok (Newsroom, Règles de la communauté, docs développeurs, Creator Academy, Help Center), lu à la source.
- **[ÉTUDE]** : étude chiffrée d'un tiers sérieux, avec échantillon déclaré (Buffer, Socialinsider, Metricool…). Il s'agit de corrélations, pas de preuves de causalité.
- **[SECONDAIRE]** : blogs, agrégateurs ou observations de créateurs. Ce sont des *affirmations* à faire vérifier par `verificateur-faits` avant de les citer comme des faits.

---

## 0. L'essentiel en 7 règles

1. **Le premier plan décide de tout.** TikTok confirme officiellement qu'un visionnage complet est un signal **fort**, et qu'un visionnage complet d'une vidéo *longue* l'est encore plus. Le nombre d'abonnés n'est **pas** un facteur direct. [OFFICIEL]
2. **L'originalité conditionne l'éligibilité au fil Pour toi.** Depuis le 2026-09-24, un contenu « non original ou réutilisé sans rien apporter de nouveau » est **inéligible au fil Pour toi**. [OFFICIEL]
3. **Plus d'une minute, mais seulement si la rétention suit.** Les vidéos de plus de 60 s obtiennent en médiane plus de vues : de 2 à 3 minutes, c'est la tranche la plus vue en 2026. Les vidéos de 15 à 30 s ont en revanche le meilleur taux d'engagement. [ÉTUDE]
4. **La recherche compte.** TikTok rémunère explicitement la « search value », c'est-à-dire l'alignement sur des requêtes populaires. Le mot-clé doit donc être dit, écrit à l'écran et placé dans la première ligne de la légende. [OFFICIEL + SECONDAIRE]
5. **La vidéo bat le carrousel photo en portée.** Le carrousel garde un intérêt pour le contenu « à sauvegarder ». [ÉTUDE]
6. **Son original obligatoire chez nous.** Jamais de musique (règle Sillage), seulement de la voix off et des effets sonores. Cela tombe bien : les comptes professionnels n'ont de toute façon pas accès à la musique tendance, seulement à la Commercial Music Library. Avec l'API, il faut forcer `auto_add_music=false`.
7. **Étiqueter l'IA réaliste.** Tout plan IA réaliste (Higgsfield) doit être étiqueté « contenu généré par IA » (`is_aigc=true` via l'API). [OFFICIEL]

---

## 1. Signaux de recommandation confirmés [OFFICIEL]

| Signal | Ce que TikTok dit | Source (date) |
|---|---|---|
| Interactions de l'utilisateur | Vidéos aimées ou partagées, comptes suivis, commentaires, contenus créés. | [Newsroom « How TikTok recommends videos #ForYou »](https://newsroom.tiktok.com/how-tiktok-recommends-videos-for-you?lang=en) (2020-06-18, republié avec la même formulation en 2023 : [version 2023](https://newsroom.tiktok.com/how-tik-tok-recommends-video-for-you?lang=en-MY)) |
| Informations de la vidéo | Légendes, sons, hashtags. | Idem |
| Réglages de l'appareil et du compte (langue, pays, type d'appareil) | Poids **plus faible** que les autres signaux. | Idem |
| Pondération par force du signal | « A strong indicator of interest, such as whether a user finishes watching a longer video from beginning to end, would receive greater weight than a weak indicator. » | Idem |
| Nombre d'abonnés | « Neither follower count nor whether the account has had previous high-performing videos are direct factors. » | Idem |
| Signaux négatifs | « Pas intéressé » et filtres de mots-clés. Le curseur « contenu IA » dans *Gérer les sujets* permet de réduire la part d'IA dans le fil (en test). | [Newsroom AIGC](https://newsroom.tiktok.com/tiktok-ssa-shares-more-ways-to-spot-shape-and-understand-ai-generated-content?lang=en-ZA) (2026-03-10) ; [TechCrunch](https://techcrunch.com/2025/11/18/tiktok-now-lets-you-choose-how-much-ai-generated-content-you-want-to-see/) (2025-11-18) |
| Critères de rémunération (indicateur indirect de ce que TikTok valorise) | Originalité, durée de lecture (play duration), **search value** (« a metric assigned to content based on popular search terms »), engagement de l'audience. Seuls les contenus originaux de **plus d'une minute** sont rémunérés. | [Newsroom Creator Rewards](https://newsroom.tiktok.com/en-us/introducing-the-new-creator-rewards-program) (2024-03-18) |
| Fil Local (États-Unis) | Le classement tient compte de la localisation, du sujet et de la date de publication. Activation volontaire, localisation précise requise. | [MacRumors](https://www.macrumors.com/2026/02/11/tiktok-us-local-feed) (2026-02-11), qui relaie l'annonce de TikTok USDS |

> Note : la page du Help Center « How TikTok recommends content » redirige vers une page générée en JavaScript, illisible par nos outils (vérifié le 2026-10-20). À relire à la main si possible.

## 2. Signaux supposés (non confirmés par TikTok)

| Affirmation | Origine | Niveau |
|---|---|---|
| Ordre d'importance : taux de complétion et temps de visionnage, puis partages et sauvegardes, puis commentaires, puis likes. | Consensus des blogs marketing (SocialPilot, Sprout, etc.) | [SECONDAIRE] |
| Le relecture et la boucle (rewatch, loop) pèsent plus que la complétion simple. | Sprout Social, cité par des blogs | [SECONDAIRE] |
| Seuil de complétion pour devenir viral « autour de 70 % » (contre 50 % en 2024). | Blogs, sans source | [SECONDAIRE] : ne pas citer |
| Test d'abord auprès des abonnés, puis élargissement. | Blogs | [SECONDAIRE] |
| 96 % des vues et 98 % des interactions arrivent dans les 10 premiers jours ; 73 % des vues viennent du fil Pour toi. | [Metricool TikTok Study 2026](https://metricool.com/tiktok-trends/), 2,3 M de posts, 92 000 comptes (2026-05-13) | [ÉTUDE] |
| Les posts avec hashtags font environ 5 % de vues et près de 10 % d'interactions en plus ; le trafic venu des hashtags a progressé de 114 % sur un an. | Metricool 2026 | [ÉTUDE] |
| Une question en légende apporte 26 % de commentaires en plus ; demander des commentaires donne +14 % d'engagement ; demander des likes donne −60 % d'interactions. | Metricool 2026 | [ÉTUDE] |
| Pic d'activité entre 18 h et 21 h, maximum à 20 h. | Metricool 2026 (fuseau des comptes, non précisé) | [ÉTUDE] |
| L'algorithme américain a été « réentraîné » par Oracle, avec des baisses de portée en février-avril 2026. Les dates divergent selon les sources. | Blogs, [Seeking Alpha](https://seekingalpha.com/news/4496968-oracle-to-retrain-secure-tiktoks-us-algorithm---report) | [SECONDAIRE] |
| L'engagement global baisse. Rapporté aux vues, il passe d'environ 4,2-4,3 % (T1 2025 à T1 2026) à 3,85 % au T2 2026, soit −8 % sur un trimestre. | [Socialinsider benchmarks](https://www.socialinsider.io/de/social-media-benchmarks/tiktok) | [ÉTUDE] |

## 3. Ce qui coupe la distribution : éligibilité au fil Pour toi [OFFICIEL]

Ces règles viennent des Règles de la communauté **publiées le 2026-08-25 et en vigueur depuis le 2026-09-24** ([Intégrité et authenticité](https://www.tiktok.com/community-guidelines/en/integrity-authenticity), [Normes du fil Pour toi](https://www.tiktok.com/community-guidelines/en/fyf-standards)).

Un contenu est **inéligible au fil Pour toi** (il reste visible sur le profil et dans la recherche) dans les cas suivants :
- **contenu non original ou réutilisé sans rien de nouveau** (reposts, compilations sans apport) ;
- tentative de manipuler l'audience pour obtenir des cadeaux, des likes ou des abonnements (« like si… », « abonne-toi pour… » insistants) ;
- désinformation au préjudice modéré, information non vérifiée sur une crise, contenu en cours de vérification ;
- publicité politique payante suspectée ;
- contenus que le système évite de recommander en boucle : régimes ou fitness extrêmes, suggestivité sexuelle, tristesse, conseils de santé mentale trop généralisés.

Autres règles :
- **Contenu commercial non déclaré** : selon les analyses tierces de la version 2026, il n'est plus automatiquement inéligible. TikTok peut réduire sa visibilité ou activer d'office la mention. [SECONDAIRE, comparaison de textes par [Storika](https://www.storika.ai/guides/tiktok-community-guidelines-update-2026-brand-risk) et [Social Day](https://socialday.live/features/tiktoks-september-community-guidelines-formalise-off-platform-account-bans)]. Pour nous, la règle ne change pas : on active toujours la mention.
- **IA** : il faut étiqueter tout contenu IA, ou très retouché, qui montre des scènes ou des personnes **réalistes**. À défaut, TikTok peut supprimer le contenu, restreindre sa diffusion ou l'étiqueter lui-même. [OFFICIEL]
- **Diagnostic** : peu de vues ne veut pas dire infraction. Les statistiques de TikTok Studio indiquent si une vidéo a été rendue inéligible à la recommandation. [OFFICIEL]

## 4. Durées : ce qui est favorisé

### Limites techniques
| Élément | Valeur | Niveau |
|---|---|---|
| Enregistrement dans l'appli | Jusqu'à 10 min | [SECONDAIRE] (plusieurs guides concordants) |
| Import depuis l'appli | Jusqu'à 60 min (déploiement progressif selon les comptes) | [SECONDAIRE] |
| Content Posting API | Fichier envoyé jusqu'à **10 min**. Le plafond réel par créateur est renvoyé par `max_video_post_duration_sec` : 3 min pour tous, 5 ou 10 min pour certains. | [OFFICIEL, docs développeurs](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide) |
| Publicités In-Feed | 5 à 60 s (9 à 15 s recommandé par les guides) | [SECONDAIRE] |

### Ce que disent les données
- **Socialinsider, plus de 6 M de vidéos de marques, janvier à juin 2026** (publié le 2026-07-10, mis à jour le 2026-10-19) [ÉTUDE] ([lien](https://www.socialinsider.io/blog/how-long-are-tiktok-videos/)) :

  | Durée | Vues médianes | Taux d'engagement |
  |---|---|---|
  | 0-15 s | 1 274 | 5,90 % |
  | 15-30 s | 1 000 | **6,00 %** |
  | 30-60 s | 2 200 | 4,20 % |
  | 60-90 s | 7 200 | 4,80 % |
  | 90-120 s | 9 620 | 5,15 % |
  | 120-180 s | **11 136** | 5,50 % |
  | > 180 s | 10 150 | 5,90 % |

- **Buffer, 1,1 M de vidéos** (2025-03-17, données 2025) [ÉTUDE] ([lien](https://buffer.com/resources/longer-tiktoks-get-more-views-data/)) : au-delà de 60 s, la portée médiane est supérieure de 43,2 % à celle des vidéos de 30-60 s, et le temps de visionnage de 63,8 %. Seules 12,3 % des vidéos dépassent une minute, ce qui laisse moins de concurrence. Buffer précise lui-même que la durée n'est pas décisive : l'accroche et la qualité comptent davantage.
- **Côté officiel** : TikTok donne en exemple de signal fort le fait de finir une vidéo *longue*, et ne rémunère que les vidéos de plus d'une minute.

**Conclusion pratique :** la durée seule n'est pas favorisée. C'est le **temps de visionnage cumulé** qui l'est. Deux formats coexistent :
- **Format court, 15-30 s** : maximum d'engagement et de complétion. C'est le format idéal pour une démo Sillage ou une animation de logo.
- **Format long, 60-180 s** : maximum de vues médianes, et seul format éligible à la rémunération. À réserver aux formats éducatifs ou « coulisses » (making-of d'une animation, décryptage d'une pub), avec une relance d'attention toutes les 5 à 8 s.
- **Entre 30 et 60 s**, la tranche est la moins bonne sur les deux tableaux dans les données 2026. Il faut l'éviter, sauf si le script l'exige.

## 5. Formats et limites techniques

| Élément | Spécification | Source |
|---|---|---|
| Ratio | **9:16 plein écran, 1080×1920**. Les formats 1:1 et 16:9 s'affichent avec des bandes. | [SECONDAIRE] consensus |
| Vidéo via l'API | MP4 (recommandé), MOV ou WebM ; H.264 recommandé (H.265, VP8 et VP9 acceptés) ; 23 à 60 i/s ; 360 à 4096 px de côté ; 4 Go au maximum | [OFFICIEL](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide) |
| Photos via l'API | JPEG ou WebP, 1080p au maximum, 20 Mo par image | [OFFICIEL] idem |
| Nombre de photos par carrousel | **35 au maximum** | [OFFICIEL](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post) |
| Légende d'une vidéo | **2 200 caractères** UTF-16 au maximum | [OFFICIEL](https://developers.tiktok.com/doc/content-posting-api-reference-direct-post) |
| Carrousel photo | Titre de 90 caractères au maximum, description de 4 000 caractères au maximum | [OFFICIEL] (doc photo) |
| Couverture | Vidéo : `video_cover_timestamp_ms`, sinon la 1re image. Carrousel : `photo_cover_index`, obligatoire. | [OFFICIEL] |
| Zones de sécurité | Pas de texte ni de logo dans environ 130 px en haut, environ 480 px en bas et environ 140 px à droite (sur 1080×1920). Le gabarit officiel se trouve dans le Creative Center. | [SECONDAIRE] : valeurs prudentes, à vérifier sur le gabarit |
| Indicateurs à cocher | `brand_organic_toggle` (promotion de sa propre entreprise), `brand_content_toggle` (partenariat payé), `is_aigc` (étiquette IA) | [OFFICIEL] |

## 6. SEO et recherche TikTok

**Confirmé [OFFICIEL]**
- La « search value » est l'un des 4 critères du Creator Rewards Program ([Newsroom, 2024-03-18](https://newsroom.tiktok.com/en-us/introducing-the-new-creator-rewards-program)).
- **Creator Search Insights** est l'outil intégré qui montre ce que les gens recherchent, avec un filtre « Content gap » pour les sujets où la demande dépasse l'offre ([Newsroom](https://newsroom.tiktok.com/creator-search-insights?lang=en), page non datée).
- Les légendes, sons et hashtags font partie des « informations de la vidéo » utilisées par le système.
- Côté publicité : les **Search Hubs** permettent à une page de marque d'apparaître en tête des résultats ([TikTok World '26, 2026-05-13](https://newsroom.tiktok.com/tiktok-world-26-turning-discovery-into-business-growth-with-ai-powered-innovations-vertical-experiences-and-high-impact-brand-solutions?lang=en)), et la **campagne Search Ads pilotée par Smart+** automatise les mots-clés ([Newsroom, 2026-10-05](https://newsroom.tiktok.com/tiktok-unveils-ai-powered-updates-for-advertisers-driving-discovery-action-and-measurable-business-outcomes?lang=en)).

**Rapporté, non officiel [SECONDAIRE]**
- **« Gérer les mots-clés »** : depuis le menu « … » d'une vidéo publiée, le créateur peut proposer les mots-clés sur lesquels il veut ressortir et bloquer ceux qui ne conviennent pas. TikTok garde un contrôle anti-bourrage, et bloquer un terme peut bloquer aussi des termes voisins. Le déploiement est progressif ([Uppbeat](https://uppbeat.io/blog/creator-news/tiktok-now-lets-you-control-the-search-keywords-on-your-videos), [RouteNote](https://routenote.com/blog/tiktoks-new-keyword-tool-how-artists-can-boost-reach-and-get-discovered-faster/)).
- TikTok transcrit l'audio parlé et lit le texte à l'écran pour l'indexation. C'est le consensus des guides SEO, sans confirmation officielle retrouvée.
- AI Canvas, dans Creator Search Insights, générerait des mises en page de carrousels ([Metricool](https://metricool.com/tiktok-news/)).
- Les chiffres de type « 74 % de la génération Z cherche sur TikTok » ne sont **pas vérifiés** : ne pas les citer.

## 7. Carrousels photo (Photo Mode)

- **Limites** : 35 photos au maximum, 1080×1920 recommandé, JPEG ou WebP, 20 Mo par image [OFFICIEL] (docs API). Aucun minimum documenté côté API.
- **Rémunération** : les posts photo sont exclus du Creator Rewards Program [SECONDAIRE, consensus].
- **Performance** [ÉTUDE] :
  - [Buffer, 2026-03-19](https://buffer.com/resources/data-best-content-format-social-media/), plus de 45 M de posts, toutes plateformes : sur TikTok, engagement médian de **3,39 % pour la vidéo contre 1,92 % pour le carrousel ou la photo**, soit +77 % pour la vidéo.
  - [Metricool 2026](https://metricool.com/tiktok-trends/) : la vidéo obtient **5 fois plus de vues et 6 fois plus d'interactions** que le carrousel. Les marques ont pourtant publié 140 % de carrousels en plus sur un an, d'où une concurrence accrue.
  - [Fanpage Karma](https://www.fanpagekarma.com/insights/carousel-vs-video-performance-tiktok-instagram/) (janvier à mai 2025, environ 700 000 posts) trouvait l'inverse : +81 % d'engagement pour le carrousel. Ces données sont plus anciennes ; les études 2026 priment.
- **Son** : par l'API, `auto_add_music` (Direct Post uniquement) ajoute une musique recommandée. **Pour nous, toujours `false`**, et on ajoute un son original : effet sonore ou voix [OFFICIEL pour le paramètre].
- **Usage conseillé** : réserver le carrousel au contenu de référence qu'on sauvegarde (checklist, « 5 erreurs », avant/après de storyboard). La vidéo reste le format de portée.

## 8. Sons originaux ou musique tendance

- **Officiel** : les sons font partie des informations de la vidéo utilisées pour recommander. Les comptes qui font du marketing ou de la publicité doivent utiliser la **Commercial Music Library**. Pour une marque, un son tendance non commercial est un risque juridique ([guide](https://www.joinstatus.com/blog-for-brands/tiktok-commerical-music-library)) [SECONDAIRE sur le détail du catalogue].
- **Données** : on ne trouve **aucune donnée officielle** montrant un avantage de portée de la musique tendance. Les « +15-25 % » qui circulent ne sont pas sourcés [SECONDAIRE] ; ne pas citer.
- **Pour nous** : la règle Sillage (jamais de musique) est **compatible** avec TikTok. Notre son est soit de la voix off, soit des effets sonores synchronisés, soit le silence avec sous-titres. Publié comme *son original*, il peut être réutilisé par d'autres et devenir un actif de marque, et il évite tout risque de droits.
- Contexte musique 2026 : bouton « Play Full Song » avec Apple Music (annoncé le 2026-03-11, [Melodic](https://www.melodicmag.com/features/editorial/apple-music-now-plays-full-songs-inside-tiktok/)) ; retour de *Music on Stage* en LIVE (août 2026, [HeyOrca](https://www.heyorca.com/blog/tiktok-social-news)). Rien de tout cela ne nous concerne directement.

## 9. Contenus générés par IA [OFFICIEL]

- L'étiquetage est obligatoire pour l'IA réaliste (Règles de la communauté en vigueur depuis le 2026-09-24).
- TikTok lit les métadonnées **C2PA** et teste un filigrane invisible ([Newsroom, 2026-03-10](https://newsroom.tiktok.com/tiktok-ssa-shares-more-ways-to-spot-shape-and-understand-ai-generated-content?lang=en-ZA)). Un plan Higgsfield peut donc être étiqueté automatiquement s'il porte des métadonnées C2PA.
- Les utilisateurs peuvent **réduire la part d'IA** dans leur fil (curseur en test). Un contenu perçu comme « IA » peut donc perdre une partie de son audience potentielle. C'est une raison de plus pour que les plans IA restent des matériaux au service de l'animation Remotion, et pas le cœur visible du post.

## 10. Monétisation : Creator Rewards Program

- **Officiel** ([Newsroom, 2024-03-18](https://newsroom.tiktok.com/en-us/introducing-the-new-creator-rewards-program)) : contenus originaux de plus d'une minute ; critères = originalité, durée de lecture, search value, engagement.
- **Éligibilité (consensus des sources tierces, page d'aide officielle non lue)** : 18 ans et plus, compte personnel (les comptes professionnels sont exclus), 10 000 abonnés, 100 000 vues sur 30 jours. Une vue qualifiée dure au moins 5 s, vient du fil Pour toi et n'a pas été marquée « Pas intéressé ». Les duos, stitchs, posts photo et contenus sponsorisés sont exclus. La **France** figure dans toutes les listes de pays [SECONDAIRE].
- **Aucun changement officiel en 2026 n'a été trouvé.** Les RPM qui circulent (0,40 à 1 $ pour 1 000 vues) sont des estimations [SECONDAIRE].
- **Pour nous** : ce programme n'est pas un objectif, puisque notre compte de marque sera probablement professionnel. Il reste un **indicateur de ce que TikTok valorise** : originalité, durée, recherche.

## 11. Statut réglementaire

### États-Unis
- **2026-01-22 : naissance de TikTok USDS Joint Venture LLC.** Elle répond à la loi de 2024 « céder ou être interdit » et au décret de septembre 2025. Répartition du capital : Oracle, Silver Lake et MGX à 15 % chacun ; ByteDance à **19,9 %** ; d'autres investisseurs pour le reste. Adam Presser est directeur général et Will Farrell responsable de la sécurité. Le conseil de 7 membres est à majorité américaine ([TechCrunch, 2026-01-23](https://techcrunch.com/2026/01/23/heres-whats-you-should-know-about-the-us-tiktok-deal/), [Wikipedia](https://en.wikipedia.org/wiki/TikTok_USDS), [site officiel USDS](https://usdsjv.tiktok.com/)). **La période d'interdiction de droit est terminée** et aucune nouvelle appli n'est nécessaire.
- **Algorithme** : les données américaines sont hébergées sur le cloud Oracle. Une copie de l'algorithme est licenciée par ByteDance puis réentraînée sur les seules données américaines, sous audit d'Oracle, et ByteDance n'a plus accès aux données des utilisateurs américains (déclaration de la Maison-Blanche rapportée par TechCrunch). **Rien d'officiel sur ce que le réentraînement a changé dans le classement.** Les dates de bascule (février ou avril 2026) ne sont pas confirmées.
- **Incidents** : fin janvier 2026, une panne liée à une coupure de courant dans un centre de données a été suivie d'accusations de censure politique, démenties par TikTok, et d'une enquête annoncée par le gouverneur de Californie ([MacRumors, 2026-01-26](https://macrumors.com/2026/01/26/tiktok-outage-issue), [MediaPost](https://www.mediapost.com/publications/article/412310/tiktok-faces-backlash-outages-following-ownership.html)). Une nouvelle politique de confidentialité américaine élargit la collecte de localisation précise.
- **Situation au 2026-10-20** : aucune nouvelle mesure réglementaire américaine n'a été trouvée dans les 90 derniers jours. TikTok communique sur son poids économique : « 81 Md$ de PIB américain, 410 000 emplois » (Newsroom, 2026-10-13).
- **Conséquence pour nous** : le marché américain fonctionne avec un algorithme distinct. Les performances américaines et européennes ne sont pas comparables, et il faut séparer les données par marché dans les bilans.

### Union européenne (notre marché principal, en français)
- **2026-02-06** : constat **préliminaire** de la Commission européenne au titre du DSA sur le design addictif (défilement infini, lecture automatique, notifications, système de recommandation). L'amende possible va jusqu'à 6 % du chiffre d'affaires mondial ; TikTok conteste ([The Record](https://therecord.media/eu-threatens-tiktok-with-fine-over-addictive-features)). **Aucune décision finale trouvée** au 2026-10-20. À surveiller : un ajustement imposé du système de recommandation dans l'UE changerait la distribution.

## 12. Nouveautés des 90 derniers jours (2026-07-22 → 2026-10-20)

| Date | Nouveauté | Niveau | Impact pour nous |
|---|---|---|---|
| 2026-08-25, effet le 09-24 | **Nouvelles Règles de la communauté** : le contenu non original ou réutilisé est inéligible au fil Pour toi (règle reconduite et explicitée) ; règles IA ; le contenu commercial non déclaré voit sa portée réduite au lieu d'être inéligible d'office (selon les analyses tierces) ; les bannissements s'étendent aux comptes associés et aux comportements hors plateforme. | [OFFICIEL] + [SECONDAIRE] pour le comparatif | **Fort** : originalité, étiquette IA, mention commerciale |
| Août 2026 | Intros IA pour les LIVE, retour de *Music on Stage*, playlists des enregistrements LIVE, catégories et tendances dans la section Drama, appli séparée de contenus payants | [SECONDAIRE] | Faible |
| 2026-08-18 | TikTok étudierait un paiement entre utilisateurs par messages privés aux États-Unis (Bloomberg) | [SECONDAIRE] | Nul |
| 2026-09-03 (env.) | Réponses vocales jusqu'à 60 s et sondages dans les commentaires | [SECONDAIRE] | Moyen pour `gestionnaire-communaute` |
| Septembre 2026 | Accord pluriannuel avec la NFL ; renforcement de la protection des mineurs | [SECONDAIRE] | Nul |
| 2026-10-05 | Advertising Week : achat direct depuis le fil Pour toi (Buy Direct), assistant d'achat, Agentic Leads, **campagne Search Ads pilotée par Smart+**, TikTok Ad Network aux États-Unis, **connecteur MCP TikTok for Business** (compatible avec Claude) | [OFFICIEL](https://newsroom.tiktok.com/tiktok-unveils-ai-powered-updates-for-advertisers-driving-discovery-action-and-measurable-business-outcomes?lang=en) | Moyen pour `strategiste-ads` ; le MCP est une piste d'outillage |
| 2026-10-13 | Étude d'impact économique américaine (81 Md$, 410 000 emplois) | [OFFICIEL] (titre visible sur la Newsroom) | Nul |
| 2026-10-14 | Partenariat avec MADE BY US Studios pour des micro-séries verticales de créateurs (TikTok et PineDrama) ; post sur la saison des fêtes de TikTok Shop | [OFFICIEL](https://newsroom.tiktok.com/tiktok-and-made-by-us-studios-enter-partnership-to-co-produce-creator-led-micro-series?lang=en) | Faible : le format épisodique est poussé |
| 2026-07-10, mise à jour le 10-19 | Étude Socialinsider sur la durée (plus de 6 M de vidéos, 2026) | [ÉTUDE] | **Fort** : règle « 15-30 s ou 60-180 s » |
| Date non confirmée (2026) | « Gérer les mots-clés » sur les vidéos publiées | [SECONDAIRE] | Moyen pour `specialiste-seo-social` |

**Aucun changement de classement officiellement annoncé** par TikTok entre juillet et octobre 2026.

Repères plus anciens de 2026 : panne et polémique de fin janvier ; DSA (02-06) ; fil Local aux États-Unis (02-11) ; filigrane IA et curseur IA (03-10) ; Apple Music (03-11) ; étude Buffer sur les formats (03-19) ; TikTok World '26 (05-13) ; étude Metricool (05-13) ; Custom Creator Networks à Cannes (juin).

## 13. Ce que ça change pour nos agents : règles à appliquer

**`redacteur-hooks` / `critique-hook` / `scenariste-reel`**
- Le premier plan doit arrêter le scroll **avant 2 s**, comme le veut la règle Sillage. Le signal le plus pondéré est le visionnage complet.
- Choisir sa durée et l'écrire dans le script :
  - **15-30 s** pour une démo, une pub ou un logo animé ;
  - **60-180 s** seulement pour un contenu éducatif ou un making-of ;
  - ne pas viser 30-60 s sans justification.
- Pour le format long, prévoir une relance visuelle ou un effet sonore toutes les 5 à 8 s et une boucle possible : le dernier plan doit pouvoir s'enchaîner avec le premier.
- Dire le mot-clé principal **à l'oral dans les 5 premières secondes** quand il y a une voix off, et l'écrire à l'écran (court, conforme à la règle des 5 mots environ).

**`redacteur-legende` / `specialiste-seo-social`**
- Mettre le mot-clé de recherche dans la **première ligne** de la légende, en formulation naturelle. 2 200 caractères au maximum ; viser 1 à 3 phrases.
- Ajouter 3 à 5 hashtags précis : effet faible mais positif selon Metricool. Pas de bourrage.
- Terminer par une **question** (+26 % de commentaires). **Ne jamais demander de likes ou d'abonnements** : −60 % d'interactions selon Metricool, et risque d'inéligibilité au fil Pour toi pour manipulation.
- Valider les sujets avec Creator Search Insights (onglet « Content gap »). Après publication, utiliser « Gérer les mots-clés » si l'option est disponible.

**`redacteur-carrousel`**
- Le carrousel sert au contenu à sauvegarder, pas à la portée. Format 1080×1920, 35 slides au maximum ; viser 5 à 9 slides. Le texte reste hors des zones de sécurité.
- Toujours un son original (effet sonore ou voix), jamais de musique ajoutée automatiquement.

**`garde-conformite`**
- Bloquer tout repost ou compilation sans apport (inéligible au fil Pour toi).
- Exiger l'étiquette IA (`is_aigc=true`) dès qu'un plan IA est réaliste.
- Exiger la mention commerciale : `brand_organic_toggle=true` pour notre propre promotion ou celle d'une marque cliente sur son compte, `brand_content_toggle=true` pour un partenariat payé.
- Jamais de musique, même issue de la Commercial Music Library (règle Sillage).

**`publicateur`**
- Content Posting API : un client non audité ne peut publier **qu'en privé** (`SELF_ONLY`). Il faut un audit TikTok avant toute publication publique automatisée.
- Respecter le parcours imposé : interroger d'abord `creator_info`, proposer uniquement les niveaux de confidentialité renvoyés, recueillir le consentement explicite de l'utilisateur, ce qui rejoint notre règle de validation.
- Respecter les limites : 6 requêtes par minute et par jeton ; plafond quotidien par créateur (`spam_risk_too_many_posts`).
- Vidéo de 10 min au maximum via l'API ; fixer `video_cover_timestamp_ms` sur une image de couverture propre ; `auto_add_music=false`.

**`pont-motion-design` (commande au studio Sillage)**
- Livrable TikTok : 1080×1920, H.264, 30 ou 60 i/s, MP4.
- Prévoir une version courte (15-30 s) et, si le sujet le permet, une version longue (60-180 s) qui ne soit pas un simple étirement.
- Garder les textes et logos hors des zones de sécurité : haut environ 130 px, bas environ 480 px, droite environ 140 px.

**`predicteur-performance` / `analyste-performance` / `analyste-resultats`**
- Juger un post sur ses **10 premiers jours** (96 % des vues).
- Suivre le temps de visionnage moyen et le taux de complétion avant les likes.
- Vérifier dans TikTok Studio si un post a été jugé inéligible à la recommandation avant de conclure à un mauvais contenu.
- Séparer les marchés États-Unis et UE (algorithmes distincts).

**`strategiste-ads`**
- Les Search Ads avec Smart+ et les Search Hubs sont à évaluer pour les marques à forte intention de recherche.
- Le connecteur MCP TikTok for Business est à signaler à `architecte-agents` comme outil potentiel, en notant qu'il passe par une API officielle et non par des identifiants.

## 14. Lacunes et points à vérifier

- [ ] Lire à la main la page du Help Center « How TikTok recommends content » (illisible par nos outils) et la page d'aide officielle du Creator Rewards Program (pays, seuils 2026).
- [ ] Récupérer le gabarit officiel des zones de sécurité (Creative Center) et remplacer les valeurs approximatives.
- [ ] Confirmer officiellement la fonction « Gérer les mots-clés » et son déploiement en France.
- [ ] Confirmer les limites d'import (60 min) et d'enregistrement (10 min) sur une page officielle.
- [ ] Surveiller : décision finale de la Commission européenne au titre du DSA ; communication officielle de TikTok USDS sur l'algorithme réentraîné.
- [ ] Confirmer les réponses vocales et sondages dans les commentaires (septembre 2026) sur une source officielle.

## 15. Sources principales

**Officielles**
- [Newsroom : How TikTok recommends videos #ForYou](https://newsroom.tiktok.com/how-tiktok-recommends-videos-for-you?lang=en) (2020-06-18 ; [version 2023](https://newsroom.tiktok.com/how-tik-tok-recommends-video-for-you?lang=en-MY))
- [Règles de la communauté : Intégrité et authenticité](https://www.tiktok.com/community-guidelines/en/integrity-authenticity) et [Normes du fil Pour toi](https://www.tiktok.com/community-guidelines/en/fyf-standards) (publiées le 2026-08-25, en vigueur le 2026-09-24)
- [Newsroom : Creator Rewards Program](https://newsroom.tiktok.com/en-us/introducing-the-new-creator-rewards-program) (2024-03-18)
- [Newsroom : AIGC, filigrane, C2PA](https://newsroom.tiktok.com/tiktok-ssa-shares-more-ways-to-spot-shape-and-understand-ai-generated-content?lang=en-ZA) (2026-03-10)
- [Newsroom : Creator Search Insights](https://newsroom.tiktok.com/creator-search-insights?lang=en)
- [Newsroom : TikTok World '26](https://newsroom.tiktok.com/tiktok-world-26-turning-discovery-into-business-growth-with-ai-powered-innovations-vertical-experiences-and-high-impact-brand-solutions?lang=en) (2026-05-13)
- [Newsroom : Advertising Week 2026](https://newsroom.tiktok.com/tiktok-unveils-ai-powered-updates-for-advertisers-driving-discovery-action-and-measurable-business-outcomes?lang=en) (2026-10-05)
- [Newsroom : MADE BY US Studios](https://newsroom.tiktok.com/tiktok-and-made-by-us-studios-enter-partnership-to-co-produce-creator-led-micro-series?lang=en) (2026-10-14)
- Docs développeurs : [Media transfer](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide), [Direct Post](https://developers.tiktok.com/doc/content-posting-api-reference-direct-post), [Photo Post](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post), [Get started](https://developers.tiktok.com/doc/content-posting-api-get-started)
- [TikTok USDS Joint Venture](https://usdsjv.tiktok.com/)

**Études**
- [Socialinsider : durée des vidéos TikTok 2026](https://www.socialinsider.io/blog/how-long-are-tiktok-videos/) (plus de 6 M de vidéos, janvier à juin 2026)
- [Buffer : longer TikToks](https://buffer.com/resources/longer-tiktoks-get-more-views-data/) (1,1 M de vidéos, 2025-03-17)
- [Buffer : best content format 2026](https://buffer.com/resources/data-best-content-format-social-media/) (2026-03-19)
- [Metricool : TikTok Study 2026](https://metricool.com/tiktok-trends/) (2,3 M de posts, 2026-05-13)
- [Socialinsider : benchmarks TikTok](https://www.socialinsider.io/de/social-media-benchmarks/tiktok)

**Presse et secondaires**
- [TechCrunch : accord américain](https://techcrunch.com/2026/01/23/heres-whats-you-should-know-about-the-us-tiktok-deal/), [Wikipedia : TikTok USDS](https://en.wikipedia.org/wiki/TikTok_USDS), [MacRumors : panne](https://macrumors.com/2026/01/26/tiktok-outage-issue), [MacRumors : fil Local](https://www.macrumors.com/2026/02/11/tiktok-us-local-feed), [The Record : DSA](https://therecord.media/eu-threatens-tiktok-with-fine-over-addictive-features), [TechCrunch : curseur IA](https://techcrunch.com/2025/11/18/tiktok-now-lets-you-choose-how-much-ai-generated-content-you-want-to-see/), [Uppbeat : Gérer les mots-clés](https://uppbeat.io/blog/creator-news/tiktok-now-lets-you-control-the-search-keywords-on-your-videos), [Storika : CG 2026](https://www.storika.ai/guides/tiktok-community-guidelines-update-2026-brand-risk), [Metricool : chronologie](https://metricool.com/tiktok-news/), [HeyOrca : mises à jour](https://www.heyorca.com/blog/tiktok-social-news), [Fanpage Karma](https://www.fanpagekarma.com/insights/carousel-vs-video-performance-tiktok-instagram/)

---

## Journal des modifications

| Date | Changement | Agent |
|---|---|---|
| 2026-10-20 | **Création de la fiche.** Contenu : signaux confirmés et supposés ; éligibilité au fil Pour toi selon les Règles de la communauté du 2026-08-25 (effet 2026-09-24) ; durées (Socialinsider 2026, Buffer) ; limites techniques (docs API) ; SEO et recherche ; carrousels ; son original et règle « pas de musique » ; IA ; Creator Rewards ; statut réglementaire États-Unis et UE ; nouveautés des 90 jours ; règles par agent ; lacunes. | veilleur-algorithmes |
