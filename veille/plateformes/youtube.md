# YouTube : fiche algorithme et formats (long format + Shorts)

> Tenue par `veilleur-algorithmes`. **Dernière mise à jour : 2026-10-22** (passe de revalidation des fiches MrBeast `xf0Mli0LVgI` et Galloway `Z2uoA3bhJT0`, voir § 9).
> Niveaux de preuve utilisés partout :
> **[OFFICIEL]** = YouTube l'a écrit ou dit (blog, centre d'aide, TeamYouTube, Creator Insider).
> **[OFFICIEL, relayé]** = source YouTube que je n'ai pas pu ouvrir moi-même (page bloquée ou vidéo) : contenu connu par une presse sérieuse qui la cite.
> **[ÉTUDE]** = étude tierce avec méthode publiée, mais corrélationnelle sauf mention contraire.
> **[SUPPOSÉ]** = créateurs, gourous, outils SaaS, rien de vérifiable.
> Règle : un chiffre [ÉTUDE] ou [SUPPOSÉ] n'est jamais présenté comme une règle de YouTube.

---

## 1. Comment YouTube classe les vidéos : signaux confirmés

### 1.1 Ce que YouTube affirme officiellement

| Signal | Ce que YouTube dit | Source |
|---|---|---|
| **Satisfaction (sondages)** | Des sondages post-visionnage demandent de noter les vidéos. Ils « aident le système à comprendre la satisfaction, pas seulement le temps de visionnage ». | [OFFICIEL] Centre d'aide, *How YouTube recommendations work* : https://support.google.com/youtube/answer/16089387 (page non datée, consultée le 2026-10-20) |
| **« Valued watch time »** | Seul le temps passé sur des vidéos notées 4 ou 5 étoiles compte comme du temps « valorisé ». Un modèle prédit la réponse au sondage pour tous les spectateurs, même ceux qui n'ont pas répondu. Objectif : « We don't want viewers regretting the videos they spend time watching. » | [OFFICIEL] Cristos Goodrow (VP Engineering), blog YouTube, 2021-09-15 : https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/ |
| **Temps de visionnage, en absolu et en relatif** | Todd Beaupré (Senior Director, Growth & Discovery) : on regarde le temps absolu et le pourcentage vu ; « We don't want to just assume that all time is valuable, which is why we bring in those surveys. » | [OFFICIEL, relayé] Creator Insider, interview de Todd Beaupré, 2026-09-01 : https://www.youtube.com/watch?v=rHLjxrbXmmY (citations horodatées relayées par OutlierKit, vidéo non ouverte par moi) |
| **Pas de pondération universelle** | « The system doesn't even work such that there's a weighting for each of these that is the same for everyone. » Les poids varient selon le spectateur, le moment, l'appareil. | [OFFICIEL, relayé] même interview, 2026-09-01 |
| **Contexte d'écran** | « Watch time may be more important in television versus mobile. » | [OFFICIEL, relayé] Beaupré, interview relayée le 2025-03-14 |
| **TV : le spectateur tire les vidéos longues** | Beaupré (2026-09-01) : les gens croient que YouTube « pousse » les vidéos longues, alors que ce sont les spectateurs sur TV qui en veulent, et YouTube les recommande en conséquence. Sur TV, « viewers don't want to be picking up the remote every five to 10 minutes to make a new video decision », ce qui explique selon lui que les formats en série tiennent. | [OFFICIEL, relayé] Creator Insider 2026-09-01 (https://www.youtube.com/watch?v=rHLjxrbXmmY), citations relayées par [PPC Land, 2026-09-02](https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/) |
| **Jugement par vidéo, pas par chaîne ; pas sur les premiers instants seuls** | « We're not basing decisions just on those initial moments. » Chaque vidéo est évaluée individuellement ; « each viewer gets a different ranking » ; les recommandations sont « pulled » par chaque spectateur (seules les notifications sont « poussées »). Les abonnés ignorent normalement la plupart des mises en ligne (« maybe a 10% or less click-through rate » dans le fil abonnements). | [OFFICIEL, relayé] même interview, PPC Land et [SEJ, 2026-09-02](https://www.searchenginejournal.com/youtube-bigger-thumbnails-long-form-engagement/588102/) |
| **Historiques Shorts et long format séparés** | Beaupré (VidCon 2022) : YouTube a séparé l'historique Shorts de l'historique long format pour la recommandation du long format : « we're not going to pay attention to what Shorts they watch because we don't want the algorithm to get the wrong idea. » Conséquence : les vues Shorts ne « poussent » pas les vidéos longues d'une chaîne, et ne les pénalisent pas non plus. Aucune annonce contraire depuis. | [OFFICIEL, relayé] [vidIQ, 2022-07-27](https://vidiq.com/blog/post/youtube-shorts-long-form-viewers-algorithm/) (vidéo de la session : https://youtu.be/qM_l7KAoNX0?t=13680) |
| **CTR seul = piège** | Beaupré : « Would you rather have a video that has a 20% CTR and 10,000 views or a 5% CTR and 100,000 views? » | [OFFICIEL, relayé] même source, 2025-03-14 |
| **Signaux négatifs** | Les « Je n'aime pas », « Pas intéressé » et « Ne pas recommander la chaîne » servent à éviter des recommandations similaires. | [OFFICIEL] answer/16089387 |
| **Historique, recherches, abonnements, likes** | Ce sont les entrées explicites citées par YouTube (plus de « 80 milliards de signaux »). | [OFFICIEL] answer/16089387 |
| **Surfaces différentes** | Accueil = surtout l'historique personnel. « À suivre » = la vidéo en cours est « le signal principal ». Le fil Shorts est personnalisé à part. | [OFFICIEL] answer/16089387 |
| **Contenu IA** | Les vidéos faites avec l'IA peuvent être recommandées aussi largement que les autres. | [OFFICIEL] answer/16089387 |
| **Originalité dans les Shorts** | Depuis le 2026-10-01, les recommandations Shorts favorisent le contenu original. Les chaînes « identified as primarily aggregating or re-uploading other creators' videos without significant changes » auront moins de distribution dans le fil Shorts. Pour réutiliser un clip, il faut ajouter une vraie valeur (commentaire, montage, narration), pas un simple retouche technique ou de template. | [OFFICIEL, relayé] TeamYouTube, communauté d'aide, 2026-10-01 : https://support.google.com/youtube/blog/470890423/prioritizing-original-content-on-shorts (page tronquée chez moi, contenu cité par [Android Authority](https://www.androidauthority.com/youtube-shorts-promoting-original-content-reposts-3718668/), [Social Media Today](https://www.socialmediatoday.com/news/youtube-updates-shorts-algorithm-to-put-more-focus-on-original-content/831976), [9to5Google](https://9to5google.com/?p=732354)) |
| **Contenu « inauthentique »** | L'ancienne politique « contenu répétitif » s'appelle « contenu inauthentique » depuis le 2025-07-15 : contenu produit en masse, répétitif, sur un même gabarit, non monétisable. Reformulation en juillet 2026 qui nomme trois groupes (répétitif, insatisfaisant, personas IA donnant des conseils sensibles), d'après la presse. | [OFFICIEL] https://support.google.com/youtube/answer/1311392 · reformulation 2026 : [SUPPOSÉ/presse] [Tubefilter, 2026-07-13](https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/) |

**Ce que YouTube n'a jamais publié :** aucun poids chiffré pour un signal. Les affirmations « les 30 premières secondes pèsent 40 % », « un partage vaut 5 à 8 likes » ou « la satisfaction a remplacé le temps de visionnage en 2026 » n'ont **aucune source YouTube**. OutlierKit les a retirées de sa propre page le 2026-10-03 faute de source ([OutlierKit](https://outlierkit.com/resources/youtube-viewer-satisfaction-algorithm-2026/)). La bonne formulation est : **temps de visionnage pondéré par la satisfaction**, pas l'un à la place de l'autre.

### 1.2 Ce qui circule sans preuve officielle (à ne pas traiter comme règle)

- [SUPPOSÉ] Beaupré aurait dit en septembre 2026 que des vidéos atteignent des non-abonnés dès la première heure, et que beaucoup de vidéos font l'essentiel de leurs vues un mois ou plus après publication. C'est relayé par des agrégateurs ([AIR](https://air.io/en/trending/youtube-algorithm-in-2026-month-by-month-changes-that-affect-your-views)), sans transcription vérifiée. Cohérent avec ce qu'il disait en 2025 (« many waves of interest in channels »).
- [SUPPOSÉ] « Creator Authenticity Framework » (janvier 2026), « déclassement des tutoriels » (septembre 2026), « chute de vues de 30 à 70 % en 2026 » : **non confirmés** par YouTube ([OutlierKit](https://outlierkit.com/resources/youtube-algorithm-updates/)).
- [SUPPOSÉ] Une règle d'heures de visionnage propre aux Shorts, ou un « nouvel algorithme de vidéos suggérées » en 2026 : **aucune source de niveau 1** ([OneTube](https://onetube.io/blog/youtube-algorithm-change-2026)).
- [OFFICIEL] Septembre 2025 : de grosses chaînes ont signalé des baisses de vues, et YouTube a répondu que ses systèmes fonctionnaient normalement (https://support.google.com/youtube/thread/373195597).

---

## 2. Test A/B natif : titres, miniatures et bientôt montages

### 2.1 Ce qui existe aujourd'hui : « Test & Compare » (long format)
[OFFICIEL] Centre d'aide : https://support.google.com/youtube/answer/13861714
- On peut tester **jusqu'à 3 variantes** : titres seuls, miniatures seules, ou paires titre + miniature.
- Uniquement **sur ordinateur** (YouTube Studio), avec les **fonctionnalités avancées** activées (compte vérifié).
- Le test dure **de quelques jours à 2 semaines** selon les impressions. Modifier un titre ou une miniature en cours de test l'arrête.
- **Critère du gagnant : la part de temps de visionnage, pas le CTR.** « The option with the highest watch time will be shown to all viewers. » YouTube : « we're optimizing for overall watch time over other metrics like CTR » (Creator Insider, déc. 2025, relayé par [Search Engine Journal, 2025-12-04](https://www.searchenginejournal.com/youtube-title-a-b-testing-rolls-out-globally-to-creators/562571/), vidéo https://www.youtube.com/watch?v=Ef9vcwon10s).
- Résultats possibles : **Winner** (gagnant statistiquement significatif), **Performed Same** (équivalents, on choisit), **Inconclusive** (la variante n°1 reste par défaut). **La variante n°1 doit donc toujours être notre favorite.**
- Non disponible pour : **les Shorts**, les vidéos « conçues pour les enfants », le contenu pour public averti, les vidéos privées, les Premieres et lives programmés (les archives de live sont testables). **Toute vidéo de 3 min ou moins en format carré ou vertical est traitée comme un Short, donc non testable** (revérifié le 2026-10-22).
- **Groupe témoin** (revérifié le 2026-10-22) : un petit groupe ne voit que le titre et la miniature par défaut ; ses données sont exclues des résultats.
- Volume : plus de 40 millions d'expériences titres/miniatures lancées depuis 2024 [OFFICIEL] (blog, 2026-09-23 : https://blog.youtube/news-and-events/made-on-youtube-new-tools-power-creation-journey/).
- Si une miniature fait moins de 720p, toutes les miniatures du test sont réduites à 480p.
- Historique : miniatures depuis 2024 ; titres testés sur un petit échantillon à partir de sept. 2025, puis ouverts à tous les créateurs ayant les fonctionnalités avancées en **décembre 2025**.

### 2.2 Annoncé, pas encore disponible (Made on YouTube, 2026-09-23)
[OFFICIEL, relayé] Vidéo *Video A/B Testing & Dynamic Thumbnails* (hub officiel https://blog.youtube/madeonyoutube/) et démo Creator Insider du 2026-09-25, détaillées par [PPC Land](https://ppc.land/youtube-to-test-up-to-3-versions-of-one-video-on-real-viewers-shorts-too/) et [TubeBuddy](https://www.tubebuddy.com/blog/youtube-creator-tools-ab-testing-feedback-dynamic-thumbnails/) :
- **A/B test de la vidéo elle-même** : jusqu'à **3 montages** de la même vidéo pour trouver quelle accroche marche le mieux (« test up to three video cuts to see which hook performs best », billet officiel du 2026-09-23). **Calendrier précisé le 2026-10-22 : « Launching to select creators in 2027 »**, Shorts **et** vidéos longues (« YouTube Shorts or videos »), d'après les posts @YouTubeCreators du 2026-09-23 relayés par [GIGAZINE, 2026-09-24](https://www.gigazine.net/gsc_news/en/20260924-made-on-youtube-2026-new-function) [OFFICIEL, relayé]. Le rapport afficherait la part de temps de visionnage par montage ([80.lv, 2026-09-24](https://80.lv/articles/youtube-adds-a-b-testing-for-video-cuts-expanding-studio-s-toolkit)). [SUPPOSÉ] Un filtre de similarité entre montages (seules des versions proches seraient admises) circule sans source officielle.
- **Miniatures dynamiques** : jusqu'à 3 miniatures choisies par le créateur ; « our system dynamically match the most compelling one to specific audiences » (pas de gagnant unique). Statut : « soon to select creators » [OFFICIEL, relayé] (même source). La base des segments n'est pas expliquée. Ask Studio pourra aussi proposer et tester des miniatures rafraîchies pour les anciennes vidéos [OFFICIEL] (billet du 2026-09-23).
- **Nouveaux espaces Studio « Insights » et « Research »** pour comprendre la performance passée et repérer des vidéos outliers [OFFICIEL] (billet du 2026-09-23). Disponibilité non précisée.
- **Retour IA sur brouillon** (Ask Studio) : on importe un brouillon non publié, l'outil commente le rythme, la structure et la rétention (exemple de la démo : « tighten up the first bit »).

---

## 3. Shorts

### 3.1 Limites techniques
| Élément | Valeur | Source |
|---|---|---|
| Durée max | **3 minutes** pour toute vidéo verticale (ou carrée) importée depuis le **2024-10-15** (avant : 60 s) | [OFFICIEL] https://support.google.com/youtube/answer/15424877 · https://support.google.com/youtube/answer/10059070 |
| Réclamation Content ID | Un Short **de plus d'1 minute** avec une réclamation Content ID active, de n'importe quel type (même manuelle), est **bloqué dans le monde entier** : ni visible, ni recommandé, ni monétisé. Pas de changement pour les Shorts d'1 minute ou moins. | [OFFICIEL] answer/15424877 |
| Musique de la bibliothèque Shorts | En général 90 s maximum dans un Short de 3 min, parfois 60 ou 30 s selon le titre | [OFFICIEL] answer/15424877 |
| Création | La caméra Shorts mobile ne filme pas 3 min : on importe via YouTube Studio | [OFFICIEL] answer/15424877 |
| Format | Vertical 9:16 (carré accepté), import Shorts jusqu'à 1080p | [OFFICIEL] answer/10059070 |
| Titre | 100 caractères maximum | [OFFICIEL] answer/10059070 |
| Miniature personnalisée | **Nouvelle depuis le 2026-07-24** : réservée au YPP au départ, élargie « over time ». Import **sur ordinateur uniquement**. Sur ordinateur, on peut aussi choisir parmi 3 images proposées ; sur mobile, n'importe quelle image de la vidéo. Spécifications : 2160×3840 recommandé, 9:16, hauteur minimale de 640 px, 50 Mo. **Pas de test A/B pour les Shorts.** | [OFFICIEL] blog, 2026-07-24 : https://blog.youtube/news-and-events/youtube-studio-custom-thumbnail-updates/ · https://support.google.com/youtube/answer/72431 (cette page indique « compte vérifié ») |
| Où la miniature apparaît | Accueil, onglets Accueil et Shorts de la chaîne. **Pas dans le fil Shorts**, d'où vient l'essentiel des vues. Rene Ritchie (Creator Liaison YouTube) : la zone visible est plus proche du **3:2** sur certaines surfaces, donc le texte et les éléments clés restent au centre. | [OFFICIEL, relayé] [PPC Land, 2026-07-26](https://ppc.land/youtube-ends-2-year-wait-for-shorts-thumbnails-but-blocks-a-b-testing/) |
| Lien « vidéo associée » | On peut lier un Short à une vidéo longue (ou à un autre Short) ; le lien s'affiche dans le lecteur Shorts | [OFFICIEL] article d'aide lié depuis answer/10059070 (*Add a related video to your YouTube Shorts*) |
| Séries Shorts | **Lancé le 2026-09-23, déploiement en cours** : saisons et épisodes de Shorts, sur web, mobile et TV. Les créateurs **YPP** ont la miniature de série personnalisée et la **lecture séquentielle** (les épisodes s'enchaînent dans l'ordre). @YouTubeCreators parle d'une disponibilité « globally in YouTube Studio » ; TechCrunch d'un déploiement « now » aux créateurs YPP. Le fonctionnement dans la recommandation (épisode 1 mis en avant ? « Continuer à regarder » ?) **n'est pas documenté**. Contexte : microdrames à 6,5 Md de vues au 1er semestre 2026, vues sur TV +90 % sur un an (chiffres YouTube relayés). | [OFFICIEL] https://blog.youtube/madeonyoutube/ · [OFFICIEL, relayé] [TechCrunch, 2026-09-23](https://techcrunch.com/2026/09/23/youtubes-new-short-series-feature-brings-episodic-viewing-to-shorts/), [MediaPost](https://www.mediapost.com/publications/article/418231/), [GIGAZINE](https://www.gigazine.net/gsc_news/en/20260924-made-on-youtube-2026-new-function) |
| Montage conversationnel (Gemini) | Annoncé le 2026-09-23 : couper la parole, synchroniser, ajouter des accroches texte, réordonner par instructions texte (Shorts et app YouTube Create) | [OFFICIEL] https://blog.youtube/madeonyoutube/ |
| Bouton « Je n'aime pas » | Retiré du lecteur Shorts le 2026-06-25 (lecture ×2 ajoutée) | [presse] [Engadget](https://www.engadget.com/2202221/youtube-shorts-nixes-dislikes-adds-double-playback-speed/) |

### 3.2 Comptage des vues : deux ruptures de série
1. **2025-03-31 (Shorts)** : une vue Shorts est comptée **à chaque lancement ou relecture, sans durée minimale**. L'ancien compteur devient « **vues engagées** » dans Analytics. Les revenus et l'éligibilité au YPP restent calculés sur les vues engagées. [OFFICIEL] annonce TeamYouTube du 2025-03-26 dans la communauté d'aide ([TechCrunch](https://techcrunch.com/2025/03/26/youtube-is-changing-how-youtube-shorts-views-are-counted/), [PPC Land](https://ppc.land/youtube-changes-how-shorts-views-are-counted-from-march-31/))
2. **2026-08-24 (tous formats)** : les vues publiques sont comptées **dès la première image** sur tous les formats (Shorts, long format, podcasts, live), y compris la lecture automatique sur l'accueil et le survol d'une miniature qui se lance. L'ancienne définition devient la « vue engagée » : clic pour regarder, ou visionnage au-delà des premières secondes. Une miniature vue sans interaction reste une impression. **Le CTR, la durée moyenne de visionnage et la rétention restent calculés sur les vues engagées.** YouTube : aucun changement de l'algorithme de recommandation ni du YPP. [OFFICIEL] blog YouTube, 2026-08-19 : https://blog.youtube/inside-youtube/engaged-views-youtube-explained/ · TeamYouTube : https://support.google.com/youtube/blog/433409976/an-update-to-how-we-count-public-views-across-youtube

> **Conséquence pour l'analyse :** les vues publiques d'avant et d'après le 2025-03-31 (Shorts) et le 2026-08-24 (long format) **ne sont pas comparables**. On compare uniquement des **vues engagées**.

### 3.3 Les Shorts amènent-ils au long format ? Vérification de l'affirmation Hormozi
**Ce que dit Hormozi** [fiche:Jmkq5RLjm0U, 01:09:48] : dans ses données internes, les spectateurs de Shorts regardent d'autres Shorts et ceux du long format regardent du long format. Ce sont des audiences différentes, et l'entonnoir Shorts → long → clients est un mythe. Il nuance lui-même : la passerelle « Short sur une plateforme → long format sur une autre » semble fonctionner, et c'est « for now, as far as we have data ». Ses données ne sont pas publiées.

**Ce qu'on trouve :**
| Source | Niveau | Ce qu'elle montre |
|---|---|---|
| Pierce Vollucci (chef de produit YouTube), 2022-07-29 : « The channels that made Shorts actually seem to be growing faster. » | [OFFICIEL] mais **sans aucun chiffre publié**, et c'est une corrélation | [Social Media Today](https://www.socialmediatoday.com/news/youtube-shares-new-insight-into-how-to-use-shorts-to-boost-your-channel-per/628491) |
| YouTube : les chaînes qui publient Shorts et long format ont plus de temps de visionnage et d'abonnés que celles qui ne font que du long format | [OFFICIEL, relayé], données sous-jacentes introuvables | [Tubefilter](https://www.tubefilter.com/?p=167699) |
| Metricool, 2026-07-29 : 799 718 vidéos, 71 177 comptes. Long format sans Shorts : 4 364 vues par vidéo. Avec environ 5 Shorts par mois : 8 789 (+46 % par rapport à la moyenne de 5 985). Au-delà de 35 Shorts par mois : retour au niveau « sans Shorts ». | [ÉTUDE] corrélationnelle, sélection des comptes non décrite | [Metricool](https://metricool.com/youtube-trends/) |
| AIR Media-Tech, données de mars 2025 à mars 2026 : environ 18 000 chaînes anglophones. Effet très variable selon la niche : le mix est associé à plus d'abonnés en fitness (+41 %), **business (+39 %)**, éducation (+37 %) ; le long format seul l'emporte en gaming (+85 %), beauté et grand divertissement. Repère « 25-40 % de Shorts » ; au-delà de 55 %, le long format décline. 1 247 chaînes qui ont basculé brutalement vers les Shorts ont eu de mauvais résultats. | [ÉTUDE] corrélationnelle. Vendeur d'audits. Seuil de 55 % non démontré dans la page. Le taux de conversion Shorts → long « de 0,04 % à 0,5 % » cité **n'a pas de source** | [AIR](https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels) |
| Rajendran, Creusy, Garnes (Upfluence), arXiv 2024 : 250 grands créateurs. Baisse significative des vues et de l'engagement du long format après l'arrivée des Shorts. | [ÉTUDE] prépublication, design non vérifié | https://arxiv.org/abs/2402.18208 |
| Violot, Elmas, Bilogrevic (Google), Humbert (Univ. Lausanne), arXiv 2024 : 70 712 chaînes, 16,7 M de vidéos (2021-2022). Les Shorts **complètent** le long format plutôt qu'ils ne le remplacent au niveau de la plateforme. Ne mesure pas la circulation des spectateurs. | [ÉTUDE] | https://arxiv.org/abs/2403.00454 |
| vidIQ, juillet 2026 : 448 413 nouvelles chaînes. Les Shorts donnent plus de chances d'un premier succès ; le long format progresse au fil des 10 premières vidéos (+51 %), pas les Shorts. | [ÉTUDE] observationnelle | [vidIQ](https://vidiq.com/research/youtube-first-10-videos-study/) |

**Verdict :**
- **« Aucune preuve que les Shorts amènent au long format » : globalement exact.** Personne, ni YouTube ni un chercheur, n'a publié de mesure **causale** du passage d'un spectateur de Short vers une vidéo longue. YouTube n'a publié qu'une corrélation au niveau des chaînes, sans chiffres.
- **Mais « aucune donnée » serait exagéré.** Il existe des corrélations publiques, contradictoires. Une dose modérée de Shorts est associée à un long format plus performant (Metricool, AIR en business et éducation), un volume massif est associé à une stagnation ou à un déclin (Metricool, AIR, Upfluence). Rien ne sépare l'effet des Shorts de l'effet « chaîne plus active ».
- **Statut :** *affirmation partiellement corroborée, non réfutée*. À transmettre au `verificateur-faits` avec ce tableau. Seul un test sur nos propres chaînes permettra de trancher (voir § 6, règle 10).

---

## 4. Long format : limites techniques
| Élément | Valeur | Source |
|---|---|---|
| Durée et poids max | 12 h ou 256 Go (le plus petit des deux). Plus de 15 min seulement avec un compte vérifié (téléphone). | [OFFICIEL] https://support.google.com/youtube/answer/71673 |
| Miniature | 16:9, 3840×2160 recommandé, largeur minimale de 640 px, JPG ou PNG, **50 Mo sur ordinateur et 2 Mo sur mobile**, compte vérifié | [OFFICIEL] https://support.google.com/youtube/answer/72431 |
| Miniatures multilingues | Depuis août 2026, on peut importer une miniature par langue ; le spectateur voit celle de sa langue | [OFFICIEL] https://support.google.com/youtube/answer/13338784 |
| Doublage automatique | Ouvert à tous les créateurs en 27 langues (2026-02-04, presse) ; doublage auto en live annoncé pour début 2027 | [presse] [gHacks](https://www.ghacks.net/2026/02/05/youtube-makes-auto-dubbing-available-to-all-creators-worldwide/) · [OFFICIEL] https://blog.youtube/madeonyoutube/ |
| Titre | 100 caractères | [OFFICIEL] (limite Studio, identique aux Shorts) |
| Playlist « série officielle » | Option « Set as official series for this playlist » (ordinateur, compte vérifié). Effet officiel : « Adding videos to a series playlist allows other videos in the playlist to be featured and recommended » quand quelqu'un regarde une vidéo de la série ; « YouTube may use this info to modify how the videos are presented or discovered ». Une vidéo ne peut appartenir qu'à **une** série ; uniquement nos propres vidéos. | [OFFICIEL] https://support.google.com/youtube/answer/6084043 (consulté le 2026-10-22) |
| Saisons et épisodes long format (« Creator Shows ») | Pilote annoncé au Brandcast de mai 2025 : sélecteur d'épisodes façon plateforme de streaming sur TV, pour **certains créateurs** seulement. Pas d'ouverture générale documentée. | [OFFICIEL, relayé] [TechCrunch, 2025-05-14](https://techcrunch.com/2025/05/14/youtube-targets-tv-dollars-with-nfl-deal-bingeable-shows-from-creators/), [Tubefilter](https://www.tubefilter.com/2025/05/14/youtube-brandcast-2025/) |
| Conseils TV officiels | Miniatures « supersized, front and center », nettes, lisibles de loin, haute résolution ; bannière lisible à distance (2560×1440) ; **épisodes rangés en playlists** pour le visionnage à la suite, titres d'épisode homogènes (« Titre d'épisode \| Nom de l'émission ») ; formats récurrents, thèmes ou personnages familiers. Sessions plus longues sur TV que sur les autres appareils. | [OFFICIEL] blog YouTube, 2024-11-27 : https://blog.youtube/creator-and-artist-stories/tv-tips/ |
| Durée idéale | **YouTube ne publie aucune durée idéale.** Metricool 2026 : la durée moyenne de visionnage du long format est passée de 3,98 à 2,51 min (−37 %), mais c'est à lire avec le nouveau comptage des vues. | [ÉTUDE] [Metricool](https://metricool.com/youtube-trends/) |

---

## 5. Monétisation et RPM

### 5.1 Définitions officielles
[OFFICIEL] https://support.google.com/youtube/answer/9314357
- **RPM** = revenu du créateur pour 1 000 vues, **après** la part de YouTube. Il inclut la publicité, Premium, les abonnements à la chaîne, les Super Chat et les Super Stickers. **Pour les Shorts, seules les vues engagées comptent.** Pour les vidéos, toutes les vues comptent, y compris les non monétisées.
- **CPM** = ce que paie l'annonceur pour 1 000 impressions publicitaires, **avant** la part de YouTube (publicité et Premium uniquement).

### 5.2 Partage des revenus Shorts
[OFFICIEL] https://support.google.com/youtube/answer/12504220
- Les revenus des pubs diffusées **entre** les Shorts du fil sont mis en commun chaque mois. La part qui revient aux créateurs est répartie selon leur part de **vues engagées** dans chaque pays. **Le créateur garde 45 %**, qu'il ait utilisé de la musique ou non. S'il y a de la musique, une partie du revenu de ce Short va aux ayants droit avant le pot commun : la moitié avec 1 titre, les deux tiers avec 2 titres.
- Long format : le créateur garde 55 % (Premium Lite : 55 % en long format, 45 % en Shorts).

### 5.3 Changement majeur annoncé le 2026-08-10 (effet au 2027-02-01)
[OFFICIEL] https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/
- **Entrée au YPP pour les nouveaux** : **8 000 heures** de visionnage qualifiées sur 365 jours **ou 20 M** de vues Shorts qualifiées sur 90 jours. Avant : 4 000 heures ou 10 M ([presse](https://tbreak.com/youtube-partner-program-8000-watch-hours/)). Le seuil de 1 000 abonnés est reconduit selon la plupart des médias, mais le billet ne le répète pas.
- **Revenus des Shorts** : à partir du 2027-02-01, il faut **10 M de vues Shorts qualifiées sur les 90 derniers jours** pour toucher les revenus pub et abonnements des Shorts, **même pour les chaînes déjà au YPP**. En dessous, la chaîne reste au YPP et monétise son long format.
- Nouveaux programmes à paliers pour les chaînes sous le seuil (bonus Shopping, partenariats de marque, tendances), détails « soon ». Nouvelles conditions à accepter dans Studio.

### 5.4 Ordres de grandeur du RPM (non officiels)
[ÉTUDE] AIR Media-Tech, 274 chaînes, 3 044 mois-chaîne, mise à jour le 2026-09-16 ([AIR](https://air.io/en/air-data-findings/youtube-shorts-rpm-vs-long-form-how-much-do-shorts-earn-in-2026)) :
- Le RPM Shorts vaut **3 à 14 % du RPM long format** dans la plupart des niches (musique : 41 à 60 %). La plupart des niches tournent entre **0,07 et 0,20 $** pour 1 000 vues Shorts. États-Unis : environ 0,33 $.
- **1 M de vues Shorts ≈ 150 à 250 $** (audience mondiale) ; **1 M de vues long format ≈ 2 300 $** (médiane). Il faut 11 000 à 26 000 vues Shorts pour gagner autant que 1 000 vues long format.
- RPM long format le plus élevé : éducation (15 à 18 $).
- Vendeur d'audits, échantillons parfois très petits, corrélationnel.

**Lien avec Hormozi** [fiche:Jmkq5RLjm0U, 01:06:31] : utiliser le revenu pub (vues × RPM) comme indicateur avancé de la qualité d'audience n'a de sens que si l'on est monétisé, en long format, et dans une niche où le RPM reflète la valeur de l'audience. Pour une marque qui cherche des clients (Sillage), **le RPM n'est pas notre indicateur** : on mesure les demandes et les prospects générés.

---

## 6. Ce que ça change pour nos agents (règles à appliquer)

1. **`ideateur`, `redacteur-hooks`, `scenariste-reel`** : la vue compte dès la première image (2026-08-24) mais la performance se lit en **vues engagées** (le spectateur reste au-delà de quelques secondes). Le premier plan doit montrer tout de suite la promesse. C'est cohérent avec la règle Sillage « accroche < 2 s ».
2. **Pas d'appât à clics.** YouTube pondère le temps de visionnage par la satisfaction (sondages, regret) et le test A/B natif choisit selon le **temps de visionnage**, pas le CTR. La miniature et le titre doivent promettre **exactement** ce que livre la vidéo (même conclusion que Hormozi, « clarté > curiosité », [fiche:Jmkq5RLjm0U, 00:49:30]).
3. **Long format, `redacteur-hooks` + `pont-motion-design`** : livrer **3 paires titre + miniature** par vidéo pour Test & Compare. La **variante n°1 est notre favorite** (c'est elle qui reste si le test n'est pas concluant). Ne rien modifier pendant les 2 semaines du test. Miniature en 3840×2160.
4. **Shorts sans test A/B possible** : le packaging se joue sur l'accroche. Quand le test de montages annoncé sera disponible, prévoir **3 versions de l'accroche** (les 2-3 premières secondes) du même Short. À surveiller.
5. **Miniature de Short** (si la chaîne y a accès) : 2160×3840, avec le texte et le sujet **dans la zone centrale au format 3:2**. Elle sert surtout sur la page de chaîne (vitrine pour les prospects), pas dans le fil.
6. **Durée des Shorts** : jusqu'à 3 min, mais **au-delà d'1 min, la moindre réclamation Content ID bloque le Short partout**. Notre règle « jamais de musique » nous protège. Effets sonores : uniquement ceux générés par `motion-design/scripts/generate-sfx.py` (aucune banque tierce). YouTube ne publie aucune durée idéale, on la teste.
7. **Originalité (2026-10-01)** : ne jamais republier de clips d'autres créateurs ni de compilations. Les rendus Sillage sont originaux. Pour réutiliser une vidéo client, ajouter une vraie valeur (coulisses, avant/après, explication). Ne pas produire en série sur un gabarit unique (risque « contenu inauthentique »).
8. **`analyste-performance`, `predicteur-performance`** : comparer uniquement des **vues engagées**. Les vues publiques ont deux ruptures de série (2025-03-31 pour les Shorts, 2026-08-24 pour tous les formats). Le CTR, la durée moyenne et la rétention restent sur la base des vues engagées. Pour les Shorts, suivre aussi le ratio « regardé / balayé » dans Studio.
9. **`strategiste-contenu`** : **ne pas supposer d'entonnoir Shorts → long format** (§ 3.3). Si on fait les deux formats, les données publiques (corrélationnelles) invitent à une **dose modérée** de Shorts (environ 25-40 % des publications ou environ 5 par mois), pas une bascule massive. C'est une hypothèse, pas une règle.
10. **`concepteur d'expériences` (labo)** : créer une expérience dans `experiences/` qui mesure le passage Shorts → long format sur nos chaînes. Lien « vidéo associée » sur chaque Short, puis comparaison du trafic venant des Shorts (sources de trafic dans Analytics) entre Shorts avec lien et sans lien, et avec ou sans appel oral à l'action.
11. **Monétisation** : ne jamais bâtir une stratégie Sillage sur les revenus pub des Shorts (RPM d'environ 0,07 à 0,20 $, seuil de 10 M de vues sur 90 jours dès février 2027). Indicateur maison : **prospects ou demandes par vidéo**, pas les vues ni le RPM.
12. **Visuels IA (Higgsfield)** : cocher « contenu modifié ou synthétique » dans Studio quand un plan photoréaliste généré par IA pourrait passer pour réel (politique de divulgation en vigueur depuis 2024). Les vidéos IA ne sont pas défavorisées dans les recommandations (answer/16089387). L'étiquetage IA automatique (mai 2026) reste **non vérifié** dans une source officielle.
13. **Bilingue FR/EN** : en long format, utiliser les **miniatures multilingues** et les titres et descriptions traduits plutôt que deux vidéos séparées.
14. **Formats récurrents** (exemple : « Avant / après motion ») : les ranger en **séries Shorts** (saisons et épisodes) dès que la fonction est visible dans Studio (déploiement depuis le 2026-09-23, YPP en priorité pour la lecture séquentielle).

*Ajouts du 2026-10-22 (revalidation des fiches MrBeast et Galloway, détail § 9) :*

15. **`ideateur`, `scenariste-reel`, `strategiste-contenu` : chaque épisode reste autonome, même dans une série.** YouTube peut recommander n'importe quel épisode à un inconnu ; seule une playlist « série officielle » ou une série Shorts aide à pousser les autres épisodes. Règle : un épisode = une promesse tenue en entier, avec un contexte minimal intégré à l'action ; la série est un **bonus** de découverte, jamais un prérequis pour comprendre.
16. **`publicateur`, `specialiste-seo-social` : tout format récurrent en long format va dans une playlist marquée « série officielle »** (une vidéo, une seule série), titres d'épisode homogènes « Titre | Nom de la série », la meilleure porte d'entrée en tête de playlist (pas forcément la plus ancienne).
17. **`pont-motion-design`, `directeur-creatif-visuel` : concevoir aussi pour la TV.** Miniature lisible de loin (un sujet, peu ou pas de texte, contraste fort), texte et éléments clés au centre. Pour une vidéo longue Sillage, vérifier le rendu sur grand écran avant livraison. YouTube n'impose aucune durée : la durée suit la matière, mais un format long est **plus naturel sur TV** (Beaupré 2026). On ne rallonge jamais pour « plaire à la TV ».
18. **`analyste-performance` : lire la TV et les recouvrements dans nos propres données, pas dans les chiffres d'experts.** Studio → Analytics → Audience : « Type d'appareil » (part de la durée de visionnage par mobile, ordinateur, TV, tablette, filtrable par type de contenu) et « Formats que regardent vos spectateurs ». Les 50-60 % de TV de Galloway et le « peu de recouvrement » de MrBeast ne s'appliquent pas tels quels à nos chaînes.
19. **`analyste-performance`, `critique-hook` : la rétention d'intro se lit sur la carte « Intro » de Studio** (« moments clés pour la rétention », part des spectateurs encore là **après 30 s**) et sur la « rétention typique » (comparaison avec nos 10 dernières vidéos de durée similaire). Une **chute** (« dip ») signale un abandon ou un saut à un endroit précis : on note la phrase ou le plan en cause. YouTube ne dit nulle part qu'un abandon à mi-vidéo « coupe » la recommandation : il compte le temps absolu et relatif, pondéré par la satisfaction.
20. **Test & Compare** : rien ne change (3 variantes, critère = temps de visionnage, variante n°1 = favorite). Nouveau : ne pas livrer au test une vidéo de 3 min ou moins en format vertical ou carré (traitée comme Short, non testable). Le test de **montages** (3 accroches) n'arrivera qu'en **2027** et d'abord pour certains créateurs : d'ici là, on teste les accroches de Shorts par publications séparées dans `experiences/`, pas en attendant l'outil.

---

## 7. Nouveautés des 90 derniers jours (2026-07-24 → 2026-10-22)
| Date | Nouveauté | Statut | Source |
|---|---|---|---|
| 2026-10-22 (revérif.) | Calendrier de l'A/B test de montages : **sélection de créateurs en 2027**, Shorts et long format ; miniatures dynamiques « soon to select creators » | Annoncé, daté | @YouTubeCreators via [GIGAZINE](https://www.gigazine.net/gsc_news/en/20260924-made-on-youtube-2026-new-function) |
| 2026-09-23 | **Séries Shorts lancées** (saisons, épisodes, lecture séquentielle et miniature de série pour le YPP ; web, mobile, TV) | Déploiement en cours | [TechCrunch](https://techcrunch.com/2026/09/23/youtubes-new-short-series-feature-brings-episodic-viewing-to-shorts/) |
| 2026-09-01 | Beaupré : sur TV le spectateur veut du long et des séries (« remote every five to 10 minutes ») ; jugement vidéo par vidéo | Déclaration | Creator Insider, relayé par [PPC Land](https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/) |
| Juillet 2026 | YouTube à **14,2 % de l'écoute TV aux États-Unis** (record Nielsen *The Gauge*) | Mesure tierce (Nielsen) | [Parasocial](https://www.parasocialmagazine.com/news/youtube-hits-14-2-of-u-s-tv-viewing-a-nielsen-record/) |
| 2026-10-01 | Recommandations Shorts favorables au contenu original ; moins de distribution pour les chaînes de reposts | Confirmé | TeamYouTube (voir § 1.1) |
| 2026-09-25 | Démo Creator Insider : A/B test de montages, miniatures dynamiques, retour IA sur brouillon | Annoncé, « coming soon » | [PPC Land](https://ppc.land/youtube-to-test-up-to-3-versions-of-one-video-on-real-viewers-shorts-too/) |
| 2026-09-23 | Made on YouTube : séries Shorts, montage conversationnel Gemini, flux d'accueil personnalisés (États-Unis, cet automne), Ask YouTube, détection de ressemblance étendue | Annoncé, déploiement progressif | https://blog.youtube/madeonyoutube/ · [Google](https://blog.google/products-and-platforms/products/youtube/made-on-youtube-updates-2026/) |
| 2026-09-03 | Contrôles d'âge et de pays pour les contenus sponsorisés ; détection auto des partenariats non déclarés à venir | Confirmé | [TeamYouTube](https://support.google.com/youtube/blog/458476782/giving-you-tools-to-easily-disclose-paid-partnerships-with-new-controls-automated-disclosures) |
| 2026-09-01 | Interview Creator Insider de Todd Beaupré : fonctionnement des recommandations, **aucune règle modifiée** | Confirmé | https://www.youtube.com/watch?v=rHLjxrbXmmY |
| 2026-08-24 | Vue publique dès la première image, tous formats ; « vue engagée » = ancienne vue | Confirmé | blog YouTube, 2026-08-19 |
| 2026-08-10 | YPP 2027 : 8 000 h ou 20 M de vues Shorts pour entrer ; 10 M de vues Shorts sur 90 jours pour monétiser les Shorts | Annoncé, effet au 2027-02-01 | blog YouTube |
| Août 2026 | Miniatures multilingues pour le long format | Confirmé | answer/13338784 |
| 2026-07-24 | Miniatures personnalisées pour les Shorts (YPP d'abord) ; génération de miniatures long format par Ask Studio | Confirmé, déploiement progressif | blog YouTube |

Juste avant la fenêtre : retrait du « Je n'aime pas » dans les Shorts (2026-06-25) ; Ask YouTube sur ordinateur aux États-Unis (2026-07-07, [TeamYouTube](https://support.google.com/youtube/blog/448540943/try-a-new-conversational-search-experience-with-ask-youtube)) ; I/O 2026 (2026-05-19) avec le remix Gemini Omni des Shorts ([blog](https://blog.youtube/news-and-events/youtube-news-google-io-2026/)).

---

## 8. À surveiller (prochaine mise à jour)
- **A/B test de montages** (sélection de créateurs en 2027) et **miniatures dynamiques** (« soon ») : critères d'éligibilité, et si les miniatures dynamiques remplacent ou complètent Test & Compare.
- **Séries Shorts** : page d'aide officielle (introuvable le 2026-10-22), effet réel sur la recommandation (épisode 1 recommandé ? « Continuer à regarder » ?), ouverture hors YPP.
- **Saisons et épisodes long format** (« Creator Shows ») : ouverture au-delà du pilote de 2025.
- Un chiffre **officiel** de part de la TV dans la durée de visionnage (mondial ou France). À ce jour : TV = 1er appareil aux États-Unis (lettre de Neal Mohan, 2025-02-11), plus d'1 milliard d'heures par jour sur TV (2024), 14,2 % de l'écoute TV américaine (Nielsen, juillet 2026). Aucun pourcentage de la durée de visionnage YouTube publié.
- Transcription complète de l'interview Beaupré du 2026-09-01 (vérifier les citations relayées).
- Texte exact du billet TeamYouTube du 2026-10-01 (seuil « significant changes »).
- Éventuelle « activité minimale » exigée des partenaires YPP actuels (rapportée par OutlierKit seulement).
- Fiches à créer pour le `chercheur-sources` : interview Beaupré 2026, billet Goodrow 2021, étude Metricool 2026.

---

## Journal des modifications
| Date | Auteur | Modification |
|---|---|---|
| 2026-10-20 | veilleur-algorithmes | **Création de la fiche** (pas de version antérieure). Couvre : satisfaction et temps valorisé ; Test & Compare titres et miniatures (critère : temps de visionnage) ; annonces A/B de montages et miniatures dynamiques ; Shorts 3 min et blocage Content ID au-delà d'1 min ; miniatures Shorts (2026-07-24) ; deux ruptures de comptage des vues (2025-03-31, 2026-08-24) ; originalité des Shorts (2026-10-01) ; vérification de l'affirmation Hormozi sur Shorts → long format (partiellement corroborée, aucune preuve causale publique) ; RPM et partage Shorts 45 % ; YPP 2027. |
