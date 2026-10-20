# Instagram — fiche algorithme

> Tenue par `veilleur-algorithmes`. Dernière mise à jour : **2026-10-20**.
> Fenêtre « nouveautés 90 jours » : 2026-07-22 → 2026-10-20.

Niveaux de preuve utilisés dans la fiche :
- **[OFFICIEL]** : page Instagram, Meta ou Mosseri consultée directement.
- **[OFFICIEL-relayé]** : déclaration officielle (vidéo ou post de Mosseri, post @creators) qu'on n'a pas pu lire en direct parce qu'Instagram bloque la lecture automatique. Elle est donc rapportée par une source presse fiable (Social Media Today, TechCrunch, PetaPixel…).
- **[SUPPOSÉ]** : créateurs, agences, outils, études. À traiter comme une *affirmation*.

---

## 1. Comment Instagram distribue (vue d'ensemble)

- **Il n'y a pas « un » algorithme.** Feed, Stories, Explore et Reels ont chacun leur classement, et des milliers de signaux entrent en jeu. [OFFICIEL] [Instagram Ranking Explained, Mosseri, 31/05/2023](https://about.instagram.com/blog/announcements/instagram-ranking-explained)
- **Diffusion par paliers pour les non-abonnés.** Un Reel est d'abord montré à une petite audience de non-abonnés. S'il performe, il est montré à des cercles de plus en plus larges, selon l'engagement et non selon le nombre d'abonnés. Instagram regarde aussi ce qu'aiment les personnes aux intérêts similaires (« audience matching »). [OFFICIEL] [Improving how reels are ranked and recommended, @creators, 26/02/2025](https://creators.instagram.com/blog/helping-creators-of-all-sizes-break-through)
- **Contenu « breaking ».** Les posts publics des petits comptes sont montrés en partie à des non-abonnés pour tester la réaction, ce qui aide les nouveaux comptes (cas de Sillage). [OFFICIEL-relayé] Série vidéo de Mosseri, sept. 2026, relayée par [Social Media Today, 24/09/2026](https://www.socialmediatoday.com/news/instagram-chief-shares-algorithm-insights-and-posting-tips/831326/)
- **Plus de 50 % du temps passé dans l'app l'est sur les Reels.** Instagram teste une ouverture de l'app directement sur les Reels (voir §4). [SUPPOSÉ : chiffre repris par la presse, non vu sur une page officielle]

## 2. Signaux de classement

### 2.1 Confirmés (sources officielles)

| Signal | Ce qu'on sait | Source |
|---|---|---|
| **Temps de visionnage / rétention** | Premier des 3 signaux les plus importants selon Mosseri. L'indicateur à suivre est le **temps de visionnage moyen**. | [OFFICIEL-relayé] vidéo Mosseri, janv. 2025, relayée par [Social Media Today](https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/) |
| **Envois en DM par portée (« sends per reach »)** | Dans le top 3. Selon Mosseri, les envois pèsent **un peu plus** que les likes pour toucher les **non-abonnés**. | idem |
| **Likes par portée** | Dans le top 3. Les likes pèsent un peu plus que les envois auprès des **abonnés**. On raisonne en **ratio**, pas en volume brut. | idem |
| **Ratio d'engagement plutôt que vues totales** | Mosseri (sept. 2026) conseille de suivre le **taux d'engagement**, pas les vues ni les likes totaux. | [OFFICIEL-relayé] [Social Media Today, 24/09/2026](https://www.socialmediatoday.com/news/instagram-chief-shares-algorithm-insights-and-posting-tips/831326/) |
| **Prédictions du modèle Reels (fiche système Meta)** | 1) utiliser l'audio du Reel ; 2) regarder **moins de 3 s**. Entrées de cette prédiction : part des personnes qui regardent ≥ 3 s, rejets, part de visionnage **avec le son**, abandons en **moins de 2 s**. 3) cliquer sur « Intéressé » ; 4) commenter ; 5) regarder **plus de 95 %** du Reel, *comparé aux Reels de même durée* ; 6) ouvrir en plein écran depuis Explore ; 7) repartager ; 8) partager hors d'Instagram ; 9) s'abonner à l'auteur. | [OFFICIEL] [Meta Transparency, Instagram Reels Chaining, mis à jour le 11/11/2025](https://transparency.meta.com/features/explaining-ranking/ig-reels-chaining/) |
| **Prédictions du Feed** | Les plus pondérées : rester quelques secondes sur le post, commenter, liker, partager, toucher la photo de profil. | [OFFICIEL] [Ranking Explained, 2023](https://about.instagram.com/blog/announcements/instagram-ranking-explained) |
| **Explore** | Likes, enregistrements et partages sont les prédictions les plus importantes. La popularité du post y pèse plus qu'ailleurs. | idem |
| **Stories** | Taper sur la story, y répondre, passer à la suivante. Comptent aussi la proximité avec l'auteur et l'historique de visionnage. | idem |
| **Principes de 2026 (au-delà de l'engagement)** | **Originalité**, **fraîcheur** (le feed reste « à peu près chronologique »), contenu **breaking** montré aux non-abonnés, **modèles d'IA plus gros** qui prennent en compte plus de facteurs. | [OFFICIEL-relayé] Mosseri, épisode 2 de la série (post `DdENi2fP59I`), relayé par [SMT](https://www.socialmediatoday.com/news/instagram-chief-shares-algorithm-insights-and-posting-tips/831326/) |
| **Originalité** | Les comptes qui republient surtout le contenu des autres sont **exclus des recommandations** : Reels depuis 2024, **photos et carrousels depuis le 30/04/2026**. Évaluation sur 30 jours glissants (voir §3). | [OFFICIEL] [Rewarding original creators on Instagram, @creators, 30/04/2026](https://creators.instagram.com/blog/rewarding-original-creators-on-instagram) |
| **Facteurs qui réduisent la visibilité des Reels** | Reel **basse résolution**, **muet**, **avec bordure**, **majoritairement du texte**, **filigrane** visible (TikTok, CapCut…), Reel **déjà publié** sur Instagram. | [OFFICIEL] [Ranking Explained](https://about.instagram.com/blog/announcements/instagram-ranking-explained) + [Tips for improving your reach, 31/05/2023](https://creators.instagram.com/blog/tips-for-improving-your-reach) |
| **Hashtags** | **5 hashtags maximum** par post ou Reel (déploiement progressif, déc. 2025). Ils aident la **recherche** mais n'augmentent **pas la portée** (Mosseri). | [OFFICIEL-relayé] [post @creators sur Threads](https://www.threads.com/@creators/post/DSalXGPCWM4), relayé par [BDM, 19/12/2025](https://www.blogdumoderateur.com/instagram-limite-hashtags-5-par-publication/) |
| **Mots-clés** | Les mots-clés dans le contenu, la légende, la bio et les hashtags rendent le compte trouvable par la recherche, y compris par les non-abonnés. | [OFFICIEL] [Tips for improving your reach](https://creators.instagram.com/blog/tips-for-improving-your-reach) |
| **Recommendation Guidelines** | Un contenu qui les enfreint reste visible des abonnés mais n'est pas recommandé (Explore, Reels, Recherche, suggestions). Le statut se vérifie dans **Statut du compte**. | [OFFICIEL] idem |
| **Contrôles côté utilisateur** | Favoris, « Pas intéressé » et **« Your Algorithm »** (sujets d'intérêt modifiables, générés par IA). Lancé sur les Reels le 10/12/2025, étendu à Explore le 15/04/2026, puis à **toute l'app le 10/06/2026**. Un post recommandé via un intérêt affiche un libellé du type « From Running ». | [OFFICIEL] [Reels algorithm control](https://about.instagram.com/blog/announcements/reels-algorithm-control) |
| **Profils IA non déclarés** | Depuis le 31/08/2026, le libellé « AI-generated profile » est obligatoire pour les comptes **dont la personne mise en avant est générée par IA**. Sans ce libellé : portée limitée et possible exclusion des recommandations. L'usage ordinaire de l'IA (retouche, graphisme, légendes) n'est **pas** concerné. | [OFFICIEL-relayé] blog @creators relayé par [TechRepublic](https://techrepublic.com/article/news-instagram-ai-generated-profile-label-recommendations/) / [Khaleej Times](https://www.khaleejtimes.com/business/tech/instagram-ai-generated-profile-label-reach-restrictions) |

### 2.2 Supposés ou non vérifiés (à ne pas citer comme faits)

- « Un envoi vaut 3 à 5 likes » : **aucune source**. Instagram n'a jamais publié de pondération chiffrée. [SUPPOSÉ, réfuté comme chiffre]
- « Seuil de 10 reposts en 30 jours » pour être classé agrégateur : non confirmé. Le texte officiel parle de la **majorité** des posts récents sur 30 jours. [SUPPOSÉ]
- « 5 Trial Reels par jour maximum » : non confirmé. [SUPPOSÉ]
- « Les sons tendance donnent +29 % de portée » : chiffre sans source. [SUPPOSÉ]
- « Instagram pénalise le contenu léché en 2026 » : c'est une **lecture** du mémo de fin d'année de Mosseri (voir §6), pas un signal de classement annoncé. [SUPPOSÉ]
- Étude Socialinsider, T2 2026 (taux d'engagement par format) : **carrousels 0,50 %**, Reels 0,48 %, images 0,33 %. Les carrousels mènent la plupart des trimestres, et l'engagement des images recule de 17 % sur un an. [SUPPOSÉ : étude sérieuse mais externe] [Socialinsider](https://www.socialinsider.io/instagram-benchmarks)

## 3. Originalité et pénalité des reposts (détail)

Source : [OFFICIEL] [@creators, 30/04/2026](https://creators.instagram.com/blog/rewarding-original-creators-on-instagram)

- **Compte visé** : celui qui republie principalement le travail des autres. La sanction porte sur **tout le compte** : il disparaît des surfaces de recommandation. Les abonnés continuent de voir ses posts.
- **Retour en grâce** : il faut que la majorité des photos, carrousels et Reels récents soient jugés originaux sur une **période glissante de 30 jours**. On vérifie dans « Statut du compte », avec possibilité de faire appel.
- **Ce qui compte comme original** : ce que l'on a filmé ou photographié, ce que l'on a conçu (série, tutoriel, récit visuel), ce que l'on a **édité en profondeur**. Exemples d'édition suffisante : texte qui apporte un contexte nouveau, graphisme qui apporte une information nouvelle, Remix qui transforme l'original.
- **Ce qui ne suffit pas** : ajouter une bordure, un filigrane, des sous-titres ou un crédit en légende.
- **Alternatives prévues** : Collab, Remix, mention « partenariat rémunéré », partage en Story, bouton Republier (l'attribution reste à l'auteur original).
- **Republier son propre Reel** déjà présent sur Instagram : il est rendu moins visible. [OFFICIEL] (Ranking Explained). Exception : la mise à niveau d'un **Trial Reel** n'est pas un repost.

## 4. Formats, durées, limites techniques

| Format | Spécifications | Niveau |
|---|---|---|
| **Reel : durée** | Enregistrement et montage jusqu'à **20 min** dans l'app (caméra Reels, nov. 2025). **Au-delà de 3 min, le Reel n'est pas recommandé aux non-abonnés.** De 0 à 3 min, il est éligible au Reels tab et à Explore depuis janv. 2025 (avant : 90 s). | [OFFICIEL] [@creators, 21/01/2025](https://creators.instagram.com/blog/the-latest-with-instagram) ; 20 min : [OFFICIEL-relayé] [PetaPixel, 25/11/2025](https://petapixel.com/2025/11/25/instagram-updates-camera-so-you-can-film-20-minute-reels) |
| **Reel : durée d'import** depuis la pellicule | Les sources se contredisent (15 ou 20 min). Sans importance pour nous, puisque nous restons sous 3 min. | [SUPPOSÉ] |
| **Reel : format** | 9:16, 1080×1920. Prévoir des marges de sécurité en haut et en bas pour l'interface : en pratique, rien d'important dans les ~250 px du haut ni les ~350 px du bas. | Ratio : standard. Zones de sécurité : [SUPPOSÉ] (convention d'outils) |
| **Photo / carrousel dans le feed** | Portrait 4:5 (1080×1350) ou **3:4 (1080×1440)**. Depuis début 2025, la grille du profil affiche des vignettes **3:4** (fin des carrés, pas de retour possible). Tous les slides d'un carrousel ont le **même ratio**. | Grille 3:4 : [OFFICIEL-relayé] annonce de Mosseri en story, relayée par [Engadget](https://www.engadget.com/social-media/instagrams-experimental-profile-grid-has-rectangular-images-instead-of-squares-160007086.html) / [Kapwing](https://www.kapwing.com/resources/instagrams-new-grid-layout-size-and-dimensions-2025/) |
| **Carrousel : nombre de slides** | **20** dans l'app (depuis mi-2024), mélange photos et vidéos possible. **Via l'API de publication : 10 maximum.** | 20 : centre d'aide, cité par la presse. 10 (API) : [OFFICIEL] [Meta, Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/) |
| **Carrousel avec audio** | Ajouter un audio à une photo ou à un carrousel peut le rendre **éligible au Reels tab** et aider à toucher de nouvelles personnes. | [OFFICIEL] [@creators, 21/01/2025](https://creators.instagram.com/blog/the-latest-with-instagram) et 26/02/2025 |
| **Story** | 9:16, 1080×1920. | Standard |
| **API de publication** | JPEG uniquement pour les images. Le conteneur expire après 24 h. Plafond de publication à vérifier via `GET /<IG_ID>/content_publishing_limit` (la doc indique 100, ailleurs 50, par 24 h glissantes). **Les Trial Reels sont publiables par API** avec `trial_params.graduation_strategy` = `MANUAL` ou `SS_PERFORMANCE` (passage automatique aux abonnés si le Reel performe). | [OFFICIEL] [Meta, Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/) |
| **Liens cliquables dans les posts et Reels** | Réservés aux abonnements payants **Meta One** (à partir de la formule Advanced), avec un quota mensuel de posts et de Reels à lien selon la formule : chiffres divergents, 4/8/12 ou 12. Sans abonnement, le seul lien reste celui de la bio ou des stories. | [OFFICIEL] [Meta, About Meta One plans](https://www.meta.com/help/subscriptions/960854640235758/) + presse (quotas à revérifier) |

### Trial Reels
- Le Reel est montré **d'abord et uniquement aux non-abonnés**. On regarde les résultats, puis on le « met à niveau » : il apparaît alors chez les abonnés et sur le profil (Mosseri). Lancés en déc. 2024. Chiffres Instagram : 40 % des créateurs qui les utilisent publient plus souvent, et la portée des Reels auprès des non-abonnés a augmenté de 80 %. [OFFICIEL-relayé] [SMT, 02/04/2026](https://www.socialmediatoday.com/news/instagram-allows-creators-to-schedule-trial-reels/816549/)
- **Programmation des Trial Reels** possible depuis le 02/04/2026. [OFFICIEL-relayé] idem
- Mosseri (sept. 2026) recommande de **s'en servir pour expérimenter** : ce qui marche une semaine peut ne plus marcher la suivante. [OFFICIEL-relayé] [SMT, 24/09/2026](https://www.socialmediatoday.com/news/instagram-chief-shares-algorithm-insights-and-posting-tips/831326/)

## 5. Musique et audio : nos contenus sans musique sont-ils pénalisés ?

**Réponse courte : non, l'absence de musique n'est pas pénalisée. Un Reel silencieux l'est.**

Ce qui est confirmé :
1. Les Reels **muets** sont rendus moins visibles. [OFFICIEL] [Ranking Explained](https://about.instagram.com/blog/announcements/instagram-ranking-explained)
2. La **piste audio** est un signal d'entrée du classement des Reels, et « utiliser l'audio de ce Reel » est une prédiction du modèle. [OFFICIEL] [Reels Chaining](https://transparency.meta.com/features/explaining-ranking/ig-reels-chaining/)
3. La part de visionnage **avec le son** entre dans la prédiction « moins de 3 s ». [OFFICIEL] idem
4. Instagram conseille d'**ajouter de l'audio** aux Reels, aux photos et aux carrousels pour toucher plus de monde. [OFFICIEL] [@creators, 26/02/2025](https://creators.instagram.com/blog/helping-creators-of-all-sizes-break-through)
5. Un mix d'audio personnel (plusieurs pistes superposées) est **attribué au créateur** : il apparaît comme « son original », et d'autres peuvent l'enregistrer ou le réutiliser. [OFFICIEL] [@creators, 21/01/2025](https://creators.instagram.com/blog/the-latest-with-instagram)

Ce qui n'existe pas : **aucune** source officielle ne dit que la *musique* (ou un son tendance) est un signal de classement en tant que tel. L'effet « son tendance = plus de portée » vient de blogs. Le mécanisme plausible : la page audio du son, et la prédiction « utiliser l'audio ». [SUPPOSÉ]

Conséquences pour Sillage :
- Nos **effets sonores, avec ou sans voix off**, forment un **son original** : c'est un audio au sens d'Instagram. Le Reel n'est pas muet, donc pas de pénalité.
- Ce que l'on perd **peut-être** : la découverte via la page d'un son tendance. [SUPPOSÉ] Impact non mesuré, à tester (voir règles).
- **Carrousels** : le levier officiel « audio sur carrousel → éligibilité au Reels tab » passe dans l'app par la **bibliothèque musicale**. Nous n'avons pas confirmé qu'on puisse y mettre un audio original (effets sonores ou voix). Avec la règle « jamais de musique », nos carrousels se privent de ce levier. → **Question remontée à l'orchestrateur** (voir rapport).
- Les comptes professionnels ont de toute façon un accès restreint à la musique commerciale (bibliothèque libre de droits Meta). Ne pas avoir de musique nous évite aussi le risque de Reel rendu muet pour raison de droits. [SUPPOSÉ : connu, non revérifié lors de cette passe]

## 6. Contexte stratégique (déclarations, pas des signaux)

- **Mémo de fin d'année de Mosseri (carrousel de 20 slides, 31/12/2025)** : « l'authenticité devient reproductible à l'infini ». « Dans un monde où l'IA génère des images parfaites, le look professionnel devient l'indice » (slide 9). « L'imperfection devient un signal » (slide 10). Priorités 2026 : « Surface credibility signals about who's posting. **Continue to improve ranking for originality** », « Label AI-generated content and verify authentic content » (slide 19). [OFFICIEL-relayé] citations relevées par [Om Malik, 01/01/2026](https://om.co/2026/01/01/what-is-instagrams-adam-mosseri-really-saying-in-his-year-end-memo/)
  → Pour Sillage, studio premium et donc « léché » par nature : ce n'est **pas** une pénalité algorithmique annoncée. C'est en revanche une tendance de perception à surveiller (voir règle 12).
- **Fréquence** : publier autant que possible pour multiplier les chances de succès, sans s'épuiser (Mosseri, sept. 2026). Aucun chiffre donné. [OFFICIEL-relayé]

## 7. Nouveautés des 90 derniers jours (2026-07-22 → 2026-10-20)

| Date | Nouveauté | Statut | Source |
|---|---|---|---|
| juil. 2026 | Traduction IA des Reels étendue au **français**, à l'allemand, à l'italien, au japonais et au coréen | Lancé | [SMT](https://www.socialmediatoday.com/news/instagram-reels-adds-more-ai-translations/825258/) [OFFICIEL-relayé] |
| juil. 2026 | Possibilité de **changer la musique** d'un post déjà publié | Lancé | [post Instagram officiel](https://www.instagram.com/p/DbD7E7eG_x8/) (via SocialBee) |
| août 2026 | Programme de **bonus pour les photos et carrousels** (créateurs éligibles) | Non vérifié | [SUPPOSÉ] SocialBee, sans source |
| 31/08/2026 | Libellé **« AI-generated profile »** et portée réduite pour les profils IA non déclarés | Lancé | [OFFICIEL-relayé] (§2.1) |
| 03→24/09/2026 | **Série de 4 vidéos de Mosseri sur le classement** : 1) pourquoi le classement existe ; 2) **originalité, fraîcheur, breaking, modèles plus gros** ; 3) contrôles utilisateur ; 4) **expérimenter avec les Trial Reels, suivre le taux d'engagement** | Publié | [SMT, 24/09/2026](https://www.socialmediatoday.com/news/instagram-chief-shares-algorithm-insights-and-posting-tips/831326/) |
| ~05/10/2026 | **Test : ouvrir l'app sur les Reels** (option à activer, iOS ; stories en haut, feed classique accessible d'un glissement) | Test | [SMT](https://www.socialmediatoday.com/news/instagram-tests-option-to-open-to-reels/) [OFFICIEL-relayé] |
| ~07/10/2026 | **Éditeur de carrousels dans Edits** (iOS ; Android à venir) : mises en page, détourage, titre ou photo qui « débordent » d'un slide à l'autre, styles enregistrés (dont l'audio), publication directe | Lancé | [PetaPixel, 07/10/2026](https://petapixel.com/2026/10/07/instagram-edits-now-lets-you-make-custom-photo-and-video-carousels/) |
| oct. 2026 | **Liens cliquables dans les posts et Reels** pour les abonnés **Meta One** (quotas mensuels) | Lancé (payant) | [Meta Help](https://www.meta.com/help/subscriptions/960854640235758/) |
| oct. 2026 | Onglet profil « Longform » et commentaires horodatés en développement | Fuite (pas un test public) | [SUPPOSÉ] rétro-ingénieurs (via SocialBee) |
| 15/10/2026 | Nouveaux formats publicitaires Meta (Ads Super Burst, First Impression Ads, Reels Trending Ads étendus) | Lancé (pub payante) | [Search Engine Land](https://searchengineland.com/meta-introduces-new-brand-advertising-formats-across-facebook-and-instagram-496608) |

Faits marquants de 2026, antérieurs à la fenêtre (rappel) : programmation des Trial Reels (02/04) ; « Your Algorithm » étendu à Explore (15/04) puis à toute l'app (10/06) ; **originalité étendue aux photos et carrousels (30/04)** ; Instants, photos éphémères en DM (13/05).

## 8. Ce que ça change pour nos agents (règles à appliquer)

Destinataires : `ideateur`, `redacteur-hooks`, `scenariste-reel`, `redacteur-carrousel`, `redacteur-legende`, `specialiste-seo-social`, `planificateur-calendrier`, `publicateur`, `pont-motion-design` (et, par lui, le studio Sillage).

1. **Accroche avant 2 s.** Le modèle prédit l'abandon en moins de 3 s à partir des abandons en moins de 2 s [OFFICIEL]. Le premier plan doit déjà être le moment fort, sans logo ni carton d'intro.
2. **Durée : aussi courte que le message le permet, et jamais plus de 3 min** (au-delà, aucune recommandation aux non-abonnés). La complétion est jugée *par rapport aux Reels de même durée* : un Reel de 12 s regardé en entier vaut mieux qu'un Reel de 40 s abandonné à mi-chemin. Cible Sillage : 8 à 30 s pour les démos, 30 à 60 s au maximum pour un « making-of ». [Règle de travail, fondée sur l'OFFICIEL]
3. **Concevoir pour l'envoi en DM.** Chaque post doit avoir une réponse claire à « à qui le spectateur va-t-il l'envoyer ? » (un cofondateur, un responsable marketing, un ami designer). Les envois pèsent le plus auprès des non-abonnés [OFFICIEL-relayé]. Les CTA de type « Envoie ça à… » restent sobres, pas plus d'un par post.
4. **Mesurer en ratios** : temps de visionnage moyen, envois/portée, likes/portée, taux d'engagement. Jamais les vues brutes. → `analyste-performance`, `predicteur-performance`.
5. **100 % original.** Pas de republication d'un Reel déjà en ligne (le nôtre ou celui d'un autre). Aucun filigrane TikTok ou CapCut : exporter des fichiers propres depuis Remotion. Pas de bordure ajoutée. Pour montrer le travail d'un client : **Collab** (avec son accord), ou contenu retravaillé en profondeur (contexte, analyse, avant/après). Ne pas se contenter d'un crédit.
6. **Jamais de Reel silencieux.** Toujours une piste audio : effets sonores synchronisés, avec ou sans voix off. Musique : jamais (règle studio, pas de pénalité constatée). Donner un nom reconnaissable au son original (ex. « Sillage — son original ») pour qu'il puisse être réutilisé. Prévoir aussi la lecture **sans le son** (sous-titres ou visuel autoportant), puisque le visionnage avec le son est mesuré mais pas garanti.
7. **Pas de Reel « majoritairement texte »** [OFFICIEL : moins visible]. C'est cohérent avec le style maison (3 à 4 messages, environ 5 mots chacun).
8. **Qualité technique** : 1080×1920, sans compression excessive (la basse résolution réduit la visibilité [OFFICIEL]). Rien d'important dans les zones couvertes par l'interface.
9. **Trial Reels systématiques pour tester les accroches.** Publier 2 ou 3 variantes d'accroche du même Reel en Trial (programmées), puis mettre à niveau la gagnante. Par API : `trial_params.graduation_strategy = "MANUAL"` (on garde la main), ou `"SS_PERFORMANCE"` seulement si l'utilisateur a validé à l'avance toutes les variantes. → `publicateur`, `experiences/`.
10. **Hashtags : 5 au maximum**, ciblés (ex. #motiondesign #remotion). Jamais #reels ni #explore. Le travail de découvrabilité passe par les **mots-clés** dans la légende, le texte à l'écran et la bio (recherche Instagram). → `specialiste-seo-social`.
11. **Carrousels** : ratio **3:4 (1080×1440)** ou 4:5, identique sur tous les slides. Contenu important dans le cadre central, pour que la vignette 3:4 de la grille reste lisible. Jusqu'à 20 slides dans l'app, **10 si publication par API**, donc concevoir en ≤ 10. Ce format reste le plus engageant d'après Socialinsider [SUPPOSÉ].
12. **Premium sans artifice** : le mémo de Mosseri fait de l'imperfection un signal d'authenticité. Sans renoncer au rendu premium, glisser dans le calendrier une part de contenus « preuve humaine » : coulisses, écran de travail, voix réelle, avant/après. → `strategiste-contenu`, `planificateur-calendrier`. [Recommandation fondée sur une déclaration, pas sur un signal]
13. **IA** : les plans Higgsfield sont autorisés. Déclarer l'IA quand Meta le demande (libellé « AI info » sur un contenu photoréaliste généré). **Jamais de « personne IA » présentée comme réelle** (libellé de profil obligatoire, sinon perte de portée). → `garde-conformite`.
14. **Liens** : pas de lien cliquable dans les posts sans abonnement Meta One payant. CTA vers la bio ou par mot-clé en DM.
15. **Régularité** : un rythme tenable plutôt que des pics. Mosseri conseille de publier « autant que possible sans s'épuiser ». → `planificateur-calendrier`.
16. **Traduction IA des Reels (fr ↔ en)** : piste de test pour toucher un public anglophone avec un seul Reel. Éligibilité de notre compte à vérifier.

## 9. Questions ouvertes / à vérifier à la prochaine passe

- Un carrousel peut-il porter un **son original** (effets sonores ou voix) plutôt qu'une musique de la bibliothèque, par exemple via l'éditeur de carrousels d'Edits ? Si oui, cela débloque le levier « Reels tab » pour nos carrousels.
- Quotas exacts des liens Meta One par formule.
- Plafond réel de l'API de publication (50 ou 100 par 24 h).
- Le test « ouvrir sur les Reels » sera-t-il généralisé ?
- Effet mesuré des sons tendance comparé au son original : à tester nous-mêmes (`experiences/`).

---

## Journal des modifications

| Date | Modification |
|---|---|
| 2026-10-20 | **Création de la fiche.** Signaux confirmés (top 3 de Mosseri, fiche système Reels Chaining du 11/11/2025, facteurs de visibilité réduite), originalité étendue aux photos et carrousels (30/04/2026), Trial Reels (programmation, API), durées (20 min dans l'app, 3 min pour les recommandations), 5 hashtags maximum, grille 3:4, carrousels 20 (app) / 10 (API), « Your Algorithm » sur toute l'app, série de Mosseri de sept. 2026, mémo du 31/12/2025, libellé profil IA, nouveautés des 90 jours, analyse musique et audio, 16 règles pour les agents. |
