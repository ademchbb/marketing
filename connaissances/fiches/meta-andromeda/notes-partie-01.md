# Notes — Meta Andromeda: Supercharging Advantage+ automation with the next-gen personalized ads retrieval engine — partie 01 (article complet)
Source : https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/ · Intervenant(s) : 8 ingénieurs de Meta (Chonglin Sun, Nancy Yu, Haiyu Lu, Liang Wang, Yunchen Pu, Gaoxiang Liu, Neeraj Bhatia, GP Musumeci), blog *Engineering at Meta*, publié le 2024-12-02 (1 626 mots, anglais).

> **Repère de position** : source écrite, donc pas d'horodatage. `[§ …]` renvoie à l'intertitre de
> l'article (ex. `[§ Hierarchical indexing]`) et `[§ chapô]` aux trois puces d'introduction.
> **Nature de la source** : billet d'ingénierie **de l'éditeur de la régie lui-même**. Tout chiffre de
> performance est une **affirmation d'éditeur** (auto-déclarée, sans méthodologie publiée, Meta vend la
> publicité et les outils d'IA générative dont elle vante l'effet). L'article est **technique** : il ne
> donne **aucune consigne aux annonceurs**. Toute conséquence pratique pour l'achat média ou la
> création est marquée « (déduction) ».
> Daté de décembre 2024 : l'état de déploiement en octobre 2026 n'est pas couvert par la source.

## Idées clés (dans l'ordre de la source)

- **[§ chapô] Andromeda = le moteur de « retrieval » (présélection) des pubs Meta** — Andromeda est le système d'apprentissage automatique propriétaire de Meta pour l'étape de *retrieval* de la recommandation publicitaire. Il tourne sur des puces NVIDIA Grace Hopper et sur les accélérateurs maison MTIA. Meta annonce une « step-function improvement » (un saut, pas une amélioration graduelle) de la valeur pour les annonceurs et les utilisateurs, grâce à un travail conjoint sur le modèle, le système et le matériel.

- **[§ intro] Le système publicitaire est en plusieurs étages : retrieval puis ranking** — Le retrieval est la **première** étape : il réduit **des dizaines de millions** de pubs candidates à **quelques milliers** de candidates pertinentes. Ensuite, des modèles de *ranking* plus gros et plus sophistiqués prédisent la valeur pour la personne et pour l'annonceur et choisissent les pubs finalement affichées. Conséquence (déduction) : une pub qui n'est pas retenue au retrieval n'a aucune chance d'être affichée, quelle que soit sa qualité aux étages suivants ; le retrieval décide donc de l'éligibilité réelle d'une créative face à une personne donnée.

- **[§ Challenges] Deux contraintes : le volume de pubs candidates et la latence** — Le retrieval traite **trois ordres de grandeur** (×1 000) de pubs de plus que les étages suivants. Des fonctions comme le *predictive targeting* (ciblage prédictif) améliorent beaucoup les résultats mais coûtent cher en calcul. La suite Advantage+ **augmente le nombre de pubs éligibles** en automatisant la création d'audience, l'allocation du budget, le placement dynamique et la génération de créatives ; les outils d'IA générative vont faire « croître fortement » le nombre de créatives dans le système. En parallèle, il faut sélectionner très vite (toute latence dégrade l'expérience) et suivre en quasi temps réel les mises à jour de diffusion et d'intérêts de chaque personne.

- **[§ Deep neural networks] Un réseau neuronal profond plus complexe pour mieux personnaliser dès le retrieval** — Le modèle apprend des « higher-order interactions » entre les données des personnes et celles des pubs. Déployé sur Instagram et Facebook, il annonce **+6 % de rappel (recall)** du système de retrieval et **+8 % de qualité des pubs** (« ads quality », notion de Meta) **sur des segments sélectionnés**. Sens (déduction) : le système retrouve davantage les pubs réellement pertinentes pour chaque personne.

- **[§ Hierarchical indexing to support exponential ad creatives growth] Andromeda est conçu pour absorber l'explosion du nombre de créatives** — Meta relie explicitement Andromeda à la croissance « exponentielle » des créatives produites par Advantage+ creative et par l'IA générative. Il cite trois chiffres d'adoption et d'effet (voir la section Chiffres) : +22 % de ROAS, +7 % de conversions estimées avec la génération d'images, plus d'un million d'annonceurs et plus de 15 M de pubs créées en un mois avec ses outils d'IA générative. Andromeda introduit un **index hiérarchique** pour monter en volume de créatives et « empowering the adoption of GenAI technologies by advertisers ». Lecture (déduction) : Meta construit son infrastructure en partant du principe que les annonceurs vont fournir **beaucoup plus de variantes créatives**, et qu'il saura les exploiter.

- **[§ AI development efficiency] Moins de règles manuelles, plus d'optimisation de bout en bout** — Andromeda réduit le nombre de composants et la logique à base de règles (« rule-based logic ») pour permettre l'optimisation de bout en bout et accélérer l'adoption de futures innovations. Conséquence possible (déduction) : moins l'annonceur contraint le système (règles de ciblage, exclusions), plus le modèle a de latitude ; cela va dans le sens de l'automatisation Advantage+, mais l'article ne le dit pas pour l'achat média.

- **[§ Meta's new personalized ads retrieval paradigm] Avant Andromeda : personnalisation limitée et heuristiques** — L'ancien retrieval n'appliquait qu'une **personnalisation limitée**, avec des étages de modèles isolés et de nombreuses heuristiques à base de règles pour gérer le volume. Cela empêchait l'optimisation globale et l'allocation efficace des ressources, faisait un usage intensif de la bande passante mémoire et sous-utilisait le matériel.

- **[§ A state-of-the-art deep neural network for retrieval] Capacité ×10 000 avec un coût d'inférence sous-linéaire** — Le réseau est conçu pour un coût d'inférence **sous-linéaire** (le coût croît moins vite que le nombre de pubs), ce qui permet d'augmenter la capacité du modèle de **10 000×**. Il capte des « complex latent relationships » entre les intérêts des personnes et les produits et services proposés dans les pubs. Techniquement : prétraitement des features sur GPU, embeddings et features des pubs précalculés et stockés dans la mémoire locale de la puce, ce qui contourne les goulots CPU-GPU.

- **[§ Hierarchical indexing for efficiency and scalable retrieval] Les pubs sont rangées dans un index hiérarchique entraîné avec le modèle** — Les pubs sont organisées en un index à plusieurs niveaux ; l'inférence ne parcourt que les nœuds les plus pertinents. L'index et les modèles de retrieval sont **entraînés conjointement**, ce qui améliore précision et rappel par rapport aux approches courantes (réseaux *two-tower*, recherche de plus proches voisins approchée). Lecture (déduction) : le système regroupe les pubs par proximité de représentation ; des créatives très semblables tomberaient dans les mêmes régions de l'index. L'article **ne dit pas** que des créatives similaires sont pénalisées.

- **[§ Model elasticity] Plus de puissance de calcul pour les segments de pubs à forte valeur** — Une conception « segment-aware » sert les **segments de pubs à forte valeur** avec des modèles plus complexes, pour maximiser le retour sur l'infrastructure. La complexité du modèle et le nombre d'étapes d'inférence s'ajustent en temps réel selon les ressources disponibles. Avec l'index hiérarchique, cela multiplie par **10** l'efficacité d'inférence. L'article ne définit pas ce qu'est un « high value ads segment » (enchère ? valeur prédite ? annonceur ?) : point opaque.

- **[§ An optimized retrieval model] Signaux d'interaction reconstruits à la volée, sans features écrites à la main** — Contrairement aux modèles classiques fondés sur des features conçues par des experts, Andromeda reconstruit **à la volée** les signaux latents d'interaction personne-pub grâce au parallélisme GPU : plus de **100×** de gain en latence et en débit d'extraction des features par rapport aux composants CPU, et plus de **3×** de requêtes par seconde (QPS) de bout en bout. Le reste de la section est de l'optimisation GPU (fusion de noyaux, pipelines logiciels, limitation des échanges mémoire HBM-SRAM), sans enjeu marketing direct.

- **[§ Advancing the state of art] Synthèse : personnalisation au retrieval et meilleur ROAS** — Andromeda améliore la personnalisation dès le retrieval et le retour sur dépenses publicitaires, et répond à la croissance exponentielle des créatives sous des contraintes strictes de latence et de coût. Meta dit capitaliser sur « la rapide adoption » d'Advantage+ et de l'IA générative.

- **[§ Advancing the state of art, perspectives] Prochaine étape : une fonction de perte autorégressive et plus de diversité** — L'architecture doit passer à une **fonction de perte autorégressive**, pour une inférence plus rapide qui fournit **un ensemble plus diversifié de pubs candidates**. Meta affirme que plus de diversité améliore l'expérience des utilisateurs et les résultats des annonceurs. Intégration future avec MTIA et les GPU suivants : Meta **estime** un nouveau gain de **1 000×** en complexité de modèle.

## Frameworks / méthodes nommées

- **Chaîne de recommandation publicitaire Meta** [§ intro] : 1) **Retrieval** (Andromeda) : des dizaines de millions de pubs → quelques milliers de candidates, personnalisées pour la personne ; 2) **Ranking** : modèles plus gros qui prédisent la valeur pour la personne et pour l'annonceur → sélection finale des pubs affichées. (L'enchère et le reste du ranking ne sont pas détaillés ici.)
- **Leviers Advantage+ qui gonflent le nombre de pubs éligibles** [§ Challenges] : création d'audience automatisée, allocation optimale du budget, placement dynamique sur les surfaces Meta, génération de créatives. [§ Hierarchical indexing to support…] reformule : allocation de budget, ciblage d'audience, ajustement des enchères.
- **Les 4 briques techniques d'Andromeda** [§ Meta's new paradigm → § An optimized retrieval model] : 1) réseau neuronal profond à coût sous-linéaire (capacité ×10 000) ; 2) index hiérarchique entraîné avec le modèle ; 3) élasticité du modèle (plus de calcul pour les segments à forte valeur, ×10 d'efficacité) ; 4) modèle optimisé GPU (features ×100, QPS ×3).

## Tactiques concrètes (checklist actionnable)

> La source ne donne aucune tactique. Les lignes ci-dessous sont **toutes des déductions** à confronter
> aux docs officielles annonceurs de Meta (Business Help Center, Blueprint) et aux praticiens, avant
> d'entrer dans `principes/`.

- [ ] (déduction) Fournir à chaque campagne **plusieurs créatives réellement différentes** (angle, format, accroche, visuel), pas des variantes cosmétiques : le système est conçu pour un grand volume de créatives et va vers « a more diverse set of ad candidates » [§ Hierarchical indexing to support… ; § perspectives].
- [ ] (déduction) Ne pas supposer que dupliquer une même pub en 10 versions quasi identiques multiplie les chances : rien dans la source ne le soutient, et l'index regroupe les pubs par proximité [§ Hierarchical indexing for efficiency].
- [ ] (déduction) Tester Advantage+ (ciblage et créative automatisés) en A/B contre une campagne manuelle plutôt que de croire le +22 % de ROAS, chiffre auto-déclaré par Meta [§ Hierarchical indexing to support…].
- [ ] (déduction) Si l'on utilise les outils d'IA générative de Meta (génération d'images), mesurer l'effet sur les conversions dans nos propres comptes ; le +7 % est une estimation de Meta [§ Hierarchical indexing to support…].
- [ ] (déduction) Garder des contraintes de ciblage minimales sauf raison métier, puisque le système est construit pour l'optimisation de bout en bout et la personnalisation [§ AI development efficiency] ; à valider par la doc annonceur.
- [ ] Demander à `verificateur-faits` la doc officielle Meta pour annonceurs sur Andromeda et la diversité créative (voir Demandes).

## Hooks, formules et scripts cités mot pour mot

> Source technique : pas de hooks. Formules utiles pour comprendre le discours de Meta (et pour
> argumenter auprès d'un client) :

- « Retrieval is the first step in our multi-stage ads recommendation system. » [§ intro] — résume l'architecture en une phrase.
- « the number of ads creatives in Meta's recommendation systems is expected to grow significantly » [§ Challenges] — la régie elle-même anticipe l'inflation créative : argument pour une production créative en volume (utile pour Sillage, déduction).
- « Increased ad diversity can improve people's experience with ads and drive better advertiser outcomes. » [§ perspectives] — seule phrase de la source qui relie diversité et performance ; c'est une affirmation prospective, pas une mesure.

## Chiffres et affirmations (à vérifier)

- Retrieval : de « tens of millions » de pubs à « a few thousand » candidates [§ intro] · type : donnée d'éditeur (ordre de grandeur).
- Le retrieval traite **3 ordres de grandeur** de pubs de plus que les étages suivants [§ Challenges] · type : donnée d'éditeur.
- **+6 %** de recall du retrieval ; **+8 %** d'« ads quality » **sur des segments sélectionnés** (Instagram et Facebook) [§ Deep neural networks] · type : affirmation d'éditeur (segments non précisés, pas de méthodologie).
- **+22 % de ROAS** pour les annonceurs qui n'utilisaient pas Advantage+ creative et ont activé « its AI-driven targeting features » [§ Hierarchical indexing to support…] · type : affirmation d'éditeur (périmètre flou : la phrase mêle « Advantage+ creative » et « targeting features » ; période, échantillon et groupe de contrôle non donnés ; biais de sélection possible des annonceurs qui activent).
- **+7 % de conversions** « estimées » pour les entreprises qui utilisent la génération d'images [§ Hierarchical indexing to support…] · type : estimation d'éditeur.
- **Plus d'un million** d'annonceurs ont créé **plus de 15 millions** de pubs en un mois avec les outils d'IA générative de Meta [§ Hierarchical indexing to support…] · type : donnée d'adoption d'éditeur (mois non précisé, vers fin 2024).
- Capacité du modèle **×10 000** [§ A state-of-the-art deep neural network] · type : donnée technique d'éditeur.
- Élasticité + index hiérarchique : efficacité d'inférence **×10** [§ Model elasticity] · type : donnée technique d'éditeur.
- Extraction des features : **plus de 100×** en latence et débit vs composants CPU ; **plus de 3×** de QPS de bout en bout [§ An optimized retrieval model] · type : donnée technique d'éditeur.
- Prochaine génération : **+1 000×** de complexité de modèle « what we estimate » [§ perspectives] · type : projection d'éditeur.

## Exemples de créateurs/marques cités

- **Meta (Advantage+, Advantage+ creative, outils GenAI)** — suite d'automatisation (audience, budget, placements, enchères, créatives) dont Andromeda est le moteur de présélection.
- **NVIDIA (Grace Hopper Superchip, GPU Hopper)** et **MTIA** (puce maison Meta) — matériel sur lequel le système est co-conçu.
- Aucune marque annonceuse ni étude de cas n'est citée.

## Contradictions ou nuances

- **Ce que la source ne dit pas, alors que les praticiens le lui attribuent** : depuis 2025, beaucoup de media buyers résument Andromeda par « la créative est le nouveau ciblage », « il faut des dizaines de créatives différentes », « les créatives trop semblables sont regroupées ou pénalisées ». La source dit seulement : (1) le système est conçu pour un volume de créatives en forte croissance, (2) la personnalisation se fait dès la présélection, (3) la prochaine version vise plus de **diversité** de candidates. Les consignes de diversité créative relèvent donc de l'interprétation des praticiens ou d'autres communications Meta, **à sourcer séparément** avant d'en faire un principe.
- **Conflit d'intérêts** : tous les chiffres de performance viennent de Meta, qui vend la publicité et promeut ses outils d'IA générative et Advantage+. Aucun chiffre indépendant.
- **« Selected segments »** : le +8 % de qualité ne vaut que sur des segments choisis par Meta, non décrits.
- **Ambiguïté du +22 %** : la phrase attribue le gain à l'activation des « AI-driven targeting features » d'**Advantage+ creative**, alors que la créative et le ciblage sont deux leviers différents. Impossible de savoir lequel est mesuré.
- **Segments à forte valeur** [§ Model elasticity] : les « high value ads segments » reçoivent des modèles plus complexes, ce qui suggère (déduction) que tous les annonceurs ne bénéficient pas du même niveau de personnalisation ; la source ne dit pas comment on entre dans ces segments.
- **Date** : article de décembre 2024, partiellement prospectif (perte autorégressive, ×1 000). L'état réel en 2026 est à vérifier (`veille/plateformes/` ne couvre pas encore la pub Meta).
- **Lien avec la base** : contredit en partie l'idée, présente dans les fiches organiques, que « une niche par compte » ou un ciblage fin est la clé : côté pub Meta, c'est le système qui cible, et la créative porte une part de la sélection (déduction, cohérent avec la lacune n°1 de `lacunes.md`).

## Citations fortes

- « Retrieval is the first step in our multi-stage ads recommendation system. This stage is tasked with selecting ads from tens of millions of ad candidates into a few thousand relevant ad candidates. » [§ intro]
- « With the adoption of powerful new tools based on generative AI for creating and optimizing ad creative content, the number of ads creatives in Meta's recommendation systems is expected to grow significantly. » [§ Challenges]
- « Andromeda is designed to maximize ads performance by utilizing the exponential growth in volume of eligible ads available to the retrieval stage. » [§ Hierarchical indexing to support…]
- « Before Andromeda, Meta's retrieval systems were only able to apply limited personalization, relying on a process with isolated model stages and numerous rule-based heuristics. » [§ Meta's new paradigm]
- « Looking forward, the Andromeda model architecture is expected to transition to support an autoregressive loss function, leading to a more efficient and faster inferencing solution that delivers a more diverse set of ad candidates. » [§ perspectives]

## Rattachement aux lacunes

- **L1 (publicité payante)** : premier élément officiel sur le **fonctionnement** du système publicitaire Meta (retrieval → ranking, rôle d'Advantage+). Ne couvre **pas** la structure de campagne, le budget, la mesure (pixel, CAPI) ni les consignes créatives : la lacune reste ouverte.
- **L2 (création publicitaire vidéo)** : justifie (indirectement) l'intérêt d'un **volume de créatives variées**, argument commercial pour Sillage ; ne dit rien sur ce qui fait convertir une créative.

## Passages douteux / limites d'extraction

- Le schéma « Personalized Ads Retrieval Paradigm » est une image non lue : son contenu n'est pas exploité.
- Remerciements en fin d'article ignorés.
