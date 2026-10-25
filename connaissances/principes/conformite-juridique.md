# Principes : conformité juridique (droit, règles des plateformes, mentions obligatoires)

> Tenu par `synthetiseur-connaissances`. Création : 2026-10-25 (grande synthèse, équipe S4 « publicité et mesure »).
> **Ce fichier n'est pas un avis juridique.** Il range, pour les agents de création, ce que disent les textes lus par
> `verificateur-faits` (registre, sections A, E à O, et « Conséquences pour les agents »). Chaque principe cite
> l'**identifiant du registre** qui le fonde ; une fiche d'expert n'est jamais la seule source d'une règle de droit.
> Les points ouverts restent ouverts : ils renvoient aux questions n° 2, 4 et 5 de `journal/questions-utilisateur.md`.
>
> **Hiérarchie** : (1) la loi et la règle de plateforme vérifiées ; (2) la checklist offres de
> `.claude/agents/garde-offres.md` (15 lignes) et la grille de `.claude/agents/garde-conformite.md`, qui les appliquent ;
> (3) les experts. Quand un expert recommande une pratique que (1) ou (2) interdit, le principe le dit et l'écarte.
> Un livrable qui enfreint une « règle sans condition » du registre est **Bloqué** par `garde-offres`,
> `garde-conformite` et `controleur-qualite-marketing`.
>
> Libellés « conformité juridique / droit de l'influence » (Bpifrance) et « conformité juridique et emailing » (CNIL),
> signalés « hors liste » dans ces fiches avant la création du tag : rangés ici (le tag existe désormais dans `agents.md`).
>
> **Sources** : `connaissances/verifications/registre.md` (sections A2, E, F, G, H à O ; « Règles sans condition du droit
> des offres » ; « Conséquences pour les agents ») et passe 4a (V4A-H02) · fiches juridiques
> `cnil-prospection-electronique` (CNIL, autorité) et `bpifrance-influenceur-reglementation` (source secondaire,
> **inexacte sur l'emailing** [verif:JI24 ❌]) · `barometre-numerique-2026` (comportements déclarés) · fiches d'experts
> citées comme **cas** (pratique recommandée puis écartée) : `au0-dI_wjI8` (Kennedy), `k834E6OTGTM` et `6_CCutkM11g`
> (Hormozi), `rPZG5xfN7vI` (Brunson, élève de Kennedy : sources non indépendantes), `LJVP2wRk7Cc` (Priestley),
> `11rNI6BUey4` (Marketing Mania), `hopkins-scientific-advertising`, `dAJyqo6wnq4` (Heath), `google-abcd-playbook-2022`,
> `_hem3-8XbEI` (Cialdini), `halbert-boron-letters`, `Ge8xTCIP0Zw` (Abraham), `buAY7UtjCb4` (Séguéla),
> `yRgPbqywUJ8` (Denney) ; soit 17 fiches au total ·
> `veille/plateformes/meta-ads.md` §5, §7 bis.
> **Frameworks** : `conformite-influence-commerciale.md` · `arbre-regime-message-electronique-cnil.md` ·
> `filtre-humain-ia-et-enhancements-meta.md`. **Swipe-file** : `swipe-file/hooks.md`, « Hooks interdits ou bloqués ».
>
> **Labo** : sans objet (le droit ne se teste pas en A/B). `experiences/apprentissages.md` est vide au 2026-10-25.

## Légende

- **Fondement** : identifiants du registre, avec leur verdict. Pour les sections juridiques, la **confiance** est celle
  du registre : **haute** = texte primaire lu (JO, Curia, Code consolidé) ; **moyenne** = reprise officielle ou
  déduction directe d'un texte lu ; **faible** = presse ou blogs seulement.
- **Experts concernés** : ceux qui appuient la règle et ceux qui recommandent l'inverse (pratique écartée).
- **Statut** : *Bloquant* (règle sans condition, aucune exception au cas par cas) · *À vérifier* (point ouvert, renvoi
  à un juriste) · *Règle maison* (choix prudent de l'agence en attendant).

## Résumé (13 principes)

| # | Principe | Fondement principal | Confiance | Statut |
|---|---|---|---|---|
| J1 | Signale l'intention commerciale sur le contenu lui-même | JI06, JI01, Q3 | haute (Q3 ouverte) | Bloquant + à vérifier |
| J2 | Ne mens jamais sur le prix : référence à 30 jours, aucune « valeur » fictive, « gratuit » s'il n'y a rien d'autre à payer | OP01-OP07, OP10 | haute | Bloquant |
| J3 | Urgence et rareté vraies, datées, tenues, en B2B comme en B2C | OU01-OU04, OP08 | haute | Bloquant |
| J4 | Ne vends jamais un droit légal comme un avantage ; toute garantie annoncée t'engage | OG01, OG02 | haute | Bloquant |
| J5 | Preuve sociale réelle : aucun faux avis, faux témoin, faux client, ni humain IA présenté comme réel | OU06, JI07, PC03 | haute | Bloquant |
| J6 | Une pub ou un e-mail qui vend donne accès aux informations obligatoires | OV06, OV05, OP09 | haute | Bloquant |
| J7 | Qualifie chaque message électronique avant de l'écrire ; consentement par défaut en B2C | JP01-JP09, JI19, JI24 | haute | Bloquant |
| J8 | Pas d'enrichissement de données par défaut ; informe la personne et respecte son opposition | OD01-OD07 | moyenne à haute | Bloquant |
| J9 | Influence : mentions, contrat écrit, secteurs interdits ; aucune collaboration rémunérée montée par l'agence pour l'instant | JI02-JI19, Q2 | haute (Q2 ouverte) | Bloquant + règle maison |
| J10 | Applique les règles propres à chaque plateforme avant la création | PA07, PA08, veille Meta §5 | moyenne à haute | Bloquant |
| J11 | Toute allégation se prouve ; l'hyperbole n'est permise que manifeste et adossée à un atout réel ; comparatif selon L. 122-1 | OC01-OC04 | haute | Bloquant |
| J12 | Prévente et formation : règles d'attente tant que les questions n° 5 sont ouvertes | OV01-OV08, OQ1-OQ3 | haute (OQ ouvertes) | Bloquant + à vérifier |
| J13 | Un point ouvert reste ouvert : il va en question à l'utilisateur, jamais en interprétation favorable | G, O | — | Règle maison |

---

## Principes

### J1. Signale l'intention commerciale sur le contenu lui-même
- **Fondement** : l'absence de mention « claire, lisible et compréhensible, sur tout support » (« Publicité »,
  « Collaboration commerciale » ou équivalent) est une pratique commerciale trompeuse (L. 121-3 C. conso), sauf si
  l'intention ressort du contexte [verif:JI06 ✅ haute] ; l'activité d'influence couvre personnes physiques et morales,
  contrepartie en nature comprise [verif:JI01 ✅ haute]. Pour un **compte de marque** ou un **fondateur** qui promeut sa
  propre entreprise, l'application de la loi influence n'est pas tranchée (critère « à titre onéreux ») ; la Commission
  européenne considère l'autopromotion comme du contenu commercial à signaler, et le droit commun des pratiques
  trompeuses s'applique dans tous les cas [verif:Q3 ❓] (question n° 4 de `journal/questions-utilisateur.md`).
- **Comment l'appliquer** : outil natif de partenariat de la plateforme **et** mention dans le contenu (incrustée en
  vidéo) ; sur le compte personnel d'un fondateur ou d'un salarié, mention explicite du lien avec l'entreprise par
  prudence (règle maison en attendant la question n° 4) ; une pub payante porte toujours la mention de la plateforme.
- **Experts** : Ralston et Hormozi demandent une mention claire des partenariats (`monetisation-et-offre.md` M11).
- **Sources** : [verif:JI01, JI06, Q3] · [fiche:bpifrance-influenceur-reglementation enseignements 1, 2] ·
  `conformite-influence-commerciale.md`.
- **Confiance** : **haute** pour la règle ; Q3 **à vérifier** par un juriste.

### J2. Ne mens jamais sur le prix : référence à 30 jours, aucune « valeur » fictive, « gratuit » s'il n'y a rien d'autre à payer
- **Fondement** : toute annonce de réduction (pourcentage, prix barré ou mention vantant l'avantage du prix) se calcule
  sur le **prix le plus bas pratiqué pendant les 30 jours** précédents (L. 112-1-1 ; CJUE *Aldi Süd*, 26/09/2024)
  [verif:OP01 ✅ haute] ; **aucune exemption « produit nouveau »** en France [verif:OP03 ❌ de la croyance contraire] ;
  appliquée par prudence aux offres numériques [verif:OP04 🟡]. « Valeur totale 2 000 €, aujourd'hui 297 € » avec une
  valeur jamais pratiquée est un faux prix de référence (L. 121-2, 2°, c) [verif:OP06 ❌ de la méthode Kennedy] ; une
  comparaison avec les prix d'autres prestataires doit être exacte, sourcée et présentée comme telle [verif:OP05 ✅,
  OP07 ✅]. « Gratuit » est réputé trompeur si le client doit payer autre chose que les coûts inévitables (L. 121-4, 19°)
  [verif:OP10 ✅ haute]. Sanctions : jusqu'à 5 ans et 750 000 € quand l'infraction passe par un service en ligne
  (L. 132-2) [verif:OP08 ✅ haute].
- **Comment l'appliquer** : checklist `garde-offres` lignes 1 à 3 ; preuve du prix pratiqué conservée ; un bonus
  « d'une valeur de X € » seulement si la marque vend réellement ce bonus seul à X € ; pas de setup « offert » sous une
  pub « paiement unique » (bait and switch, ligne 3).
- **Experts qui recommandent l'inverse (écartés)** : Kennedy, valeur de remplacement (« le système vaut 100 000 $ »)
  [fiche:au0-dI_wjI8 framework K] ; Hormozi, value stack au lancement de *$100M Leads* [fiche:k834E6OTGTM] et setup à
  10 000 $ « offert » contre engagement [fiche:6_CCutkM11g enseignement 4] (licite seulement si le setup est réellement
  facturé 10 000 $ à qui ne s'engage pas, et si la pub annonce les conditions) ; Brunson, même école que Kennedy
  [fiche:rPZG5xfN7vI].
- **Sources** : [verif:OP01-OP08, OP10] · `.claude/agents/garde-offres.md` lignes 1-3 · registre, règles sans
  condition n° 1 et 2.
- **Confiance** : **haute**. **Statut** : Bloquant.

### J3. Urgence et rareté vraies, datées, tenues, en B2B comme en B2C
- **Fondement** : déclarer faussement qu'un produit ne sera disponible que très peu de temps est **réputé** trompeur
  (L. 121-4, 7° ; directive 2005/29, annexe I, point 7) [verif:OU01 ✅ haute] ; un compte à rebours qui repart ou une
  promo « limitée » renouvelée en continu est une fausse urgence (CA Paris, 02/04/2025 ; balayage UE : 42 sites sur 399)
  [verif:OU02 ✅ moyenne] ; fausse rareté de quantité (« plus que 3 places ») : L. 121-2 et L. 121-4, 17° [verif:OU03 ✅] ;
  **en B2B aussi** (L. 121-5) [verif:OU04 ❌ de la croyance contraire].
- **Comment l'appliquer** : checklist `garde-offres` lignes 4 et 5 ; date limite réelle, jamais prolongée en silence ;
  N places = N réel au moment de la publication ; une capacité de production vraie et maintenue est une rareté
  permise (`monetisation-et-offre.md` D1) ; hooks « dernière chance », « plus que N places » interdits sans preuve datée
  (swipe-file, « Hooks interdits »).
- **Experts dont la tactique ne vaut que si elle est vraie** : Heath met la rareté parmi ses 7 cases et l'urgence en
  description [fiche:dAJyqo6wnq4 enseignement 8] ; Hopkins, « tell what delay may cost » [fiche:hopkins-scientific-advertising
  p. 89-90] ; Google, « plant the seed of urgency » [fiche:google-abcd-playbook-2022 p. 18] ; Hormozi, « Fast Cash » en
  compte à rebours de 7 jours sur la base clients [fiche:6_CCutkM11g enseignement 7] ; Priestley, scripts de capacité et
  de refus [fiche:LJVP2wRk7Cc]. Ralston juge l'urgence inutile si la relation existe.
- **Sources** : [verif:OU01-OU04, OP08] · `.claude/agents/garde-offres.md` lignes 4-5 · règle sans condition n° 3.
- **Confiance** : **haute**. **Statut** : Bloquant.

### J4. Ne vends jamais un droit légal comme un avantage ; toute garantie annoncée t'engage
- **Fondement** : présenter les droits légaux comme une caractéristique propre de l'offre est réputé trompeur
  (L. 121-4, 10°) : « satisfait ou remboursé 14 jours » pour une vente à distance redit la rétractation légale
  [verif:OG01 ✅ haute] ; la garantie commerciale lie le garant aux conditions de la publicité si elles sont plus
  favorables (L. 217-21, L. 217-22 ; services : L. 121-2, 2°, e) [verif:OG02 ✅ haute].
- **Comment l'appliquer** : seule une garantie **plus large** que la loi, dite « en plus du droit légal », est un
  argument ; elle est écrite mot pour mot dans `conditions-vente.md` et tenable (checklist `garde-offres` lignes 6 et 7).
- **Experts** : Hopkins, « Pay in a week if you like them » bat « remboursé si non satisfait » : licite si le client a
  commandé, l'envoi non sollicité suivi d'une demande de paiement est interdit [verif:OG03 🟡 efficacité / ✅ droit] ;
  « What do you have to lose? » n'est licite que si le risque est réellement levé [verif:OG04 🟡].
- **Sources** : [verif:OG01-OG04] · règles sans condition n° 4 et 6.
- **Confiance** : **haute**. **Statut** : Bloquant.

### J5. Preuve sociale réelle : aucun faux avis, faux témoin, faux client, ni humain IA présenté comme réel
- **Fondement** : nombre de clients faux : L. 121-2 ; avis présentés comme venant de vrais acheteurs sans vérification
  raisonnable, ou faux avis : **réputés** trompeurs (L. 121-4, 27° et 28°) ; dire **si et comment** on vérifie les avis
  est une information substantielle (L. 121-3) [verif:OU06 ✅ haute]. Visage ou silhouette retouchés : « Images
  retouchées » ; générés par IA : « Images virtuelles » (1 an et 4 500 €) [verif:JI07 ✅, JI08 ✅]. Les témoignages chiffrés
  du visuel de Heath sont invérifiables : ne jamais les reprendre, même comme modèle [verif:PC03 ❓]. Meta appose un
  libellé « AI info » et un libellé visible pour un humain photoréaliste généré [veille:meta-ads §5].
- **Comment l'appliquer** : témoignage = client réel, résultat vérifié, accord écrit ; méthode de vérification des avis
  mentionnée ; aucun pod, retweet payé ni engagement acheté (checklist `garde-offres` ligne 9) ; jamais d'humain généré
  dans le rôle d'un client ou d'un témoin, même étiqueté (`meta-ads.md` MA9) ; un personnage fictif n'est admis que
  présenté **explicitement** comme fictif (mascotte).
- **Experts qui recommandent l'inverse (écartés)** : Hopkins, une « personnalité créée » signataire d'annonces
  [fiche:hopkins-scientific-advertising p. 35-36, p. 83] ; Halbert, lettres laissant croire qu'un parent recommande
  l'offre : la Poste américaine a ordonné à son entreprise de cesser cette fausse recommandation en novembre 1995
  (source secondaire [verif:V4A-H02 🟡]) [fiche:halbert-boron-letters]. Cialdini : la preuve sociale doit être « vraie et
  représentative », ce qui est aussi une règle de droit [verif:OU06] [fiche:_hem3-8XbEI].
- **Sources** : [verif:OU06, JI07, JI08, PC03, V4A-H02] · [veille:meta-ads §5, §10 règle 9] · règle d'honnêteté de
  `CLAUDE.md`.
- **Confiance** : **haute**. **Statut** : Bloquant.

### J6. Une pub ou un e-mail qui vend donne accès aux informations obligatoires
- **Fondement** : dans une « invitation à l'achat » (prix + caractéristiques), sont substantielles : caractéristiques
  principales, identité du professionnel, prix TTC et frais, modalités inhabituelles, **existence d'un droit de
  rétractation** ; le texte tient compte des limites d'espace du support si l'information est disponible ailleurs
  (L. 121-3) [verif:OV06 ✅ haute]. Depuis le 19/06/2026, toute vente en ligne offre une **fonctionnalité de
  rétractation** gratuite (L. 221-21, ord. 2026-2) [verif:OV05 ✅ moyenne]. Une offre promotionnelle par e-mail est
  identifiable dès réception et renvoie à des conditions claires (L. 122-8, L. 122-9) [verif:OP09 ✅ haute].
- **Comment l'appliquer** : checklist `garde-offres` ligne 12 ; un Reel ou une pub avec prix et lien renvoie à une page
  qui porte ces informations ; objet d'e-mail qui dit l'offre.
- **Sources** : [verif:OV05, OV06, OP09].
- **Confiance** : **haute**. **Statut** : Bloquant.

### J7. Qualifie chaque message électronique avant de l'écrire ; consentement par défaut en B2C
- **Fondement** : c'est la finalité commerciale qui fait la prospection, même si le contenu est aussi informatif (CJUE,
  13/11/2025, *Inteligo Media*, C-654/23) [verif:JP03 ✅ haute]. B2C : consentement préalable, sauf **exception client**
  à quatre conditions cumulatives (coordonnées recueillies lors d'une vente, produits analogues, même entreprise,
  opposition à la collecte et dans chaque message) [verif:JP01 ✅ haute]. B2B : pas de consentement systématique si le
  message est lié à l'activité professionnelle et si la personne est informée et peut s'opposer (doctrine CNIL)
  [verif:JP02 ✅ moyenne]. Offres de partenaires : consentement obligatoire (Accor, 600 000 €) [verif:JP05 ✅] ; case
  pré-cochée interdite [verif:JP07 ✅] ; expéditeur identifiable et adresse valable pour l'arrêt [verif:JP08 ✅] ; contrat
  art. 28 RGPD avec le routeur [verif:JP09 ✅]. **Démarchage des titulaires de CPF** par téléphone, e-mail, SMS ou réseau
  social : interdit à tous, sans exception B2B ni de consentement (jusqu'à 375 000 € pour une société) [verif:JI19 ✅
  haute]. « Le consentement est toujours requis » (Bpifrance) est faux [verif:JI24 ❌] : pour l'emailing, la fiche CNIL
  fait foi.
- **Comment l'appliquer** : arbre `arbre-regime-message-electronique-cnil.md` puis checklist B2B ou B2C ; liste
  repoussoir centrale ; un compte gratuit ne vaut relation client que s'il est financé indirectement par une offre
  payante, à examiner au cas par cas [verif:JP03, JP04] ; « 3 ans sans contact » est un repère CNIL non contraignant,
  relancé seulement par un contact **venant du prospect** [verif:JI23 🟡].
- **Pratique** : près de 4 utilisateurs sur 10 disent limiter qui peut leur envoyer des messages privés (déclaratif)
  [fiche:barometre-numerique-2026 enseignement 6] : le DM non sollicité est aussi un mauvais canal.
- **Sources** : [verif:JP01-JP09, JI19, JI23, JI24] · [fiche:cnil-prospection-electronique enseignements 1-10] ·
  `arbre-regime-message-electronique-cnil.md`. Méthode de l'emailing : `email.md`.
- **Confiance** : **haute** (JP02 moyenne : doctrine d'autorité qu'un juge pourrait lire autrement). **Statut** :
  Bloquant.

### J8. Pas d'enrichissement de données par défaut ; informe la personne et respecte son opposition
- **Fondement** : enrichissement automatique de leads : base légale, information, minimisation, conservation et
  opposition (CNIL, KASPR, 240 000 €, 05/12/2024 : masquer ses coordonnées vaut opposition) [verif:OD01 ✅ moyenne] ;
  information au plus tard dans le mois et au **premier contact**, avec la **source** des données (RGPD art. 14)
  [verif:OD02 🟡 haute] ; intérêt commercial légitime possible mais soumis au test de mise en balance (CJUE *KNLTB*)
  [verif:OD03 ✅] ; opposition à tout moment, présentée dès la première communication (art. 21) [verif:OD04 ✅ haute] ;
  le scoring est du profilage, et peut devenir une décision si un tiers s'y fie fortement (CJUE *SCHUFA*) [verif:OD05 🟡].
- **Comment l'appliquer** : enrichissement **désactivé par défaut**, activé seulement avec base légale documentée et
  durée de conservation fixée (règle sans condition n° 7 ; grille `garde-conformite`, ligne « Données ») ; aucune
  donnée que la personne a masquée.
- **Expert dont la tactique est encadrée** : Abraham propose la **copropriété des fichiers** recrutés avec un
  partenaire [fiche:Ge8xTCIP0Zw enseignement 5] : partager des contacts avec un tiers demande une base légale,
  l'information des personnes (source comprise) et, pour la prospection électronique B2C par le partenaire, leur
  consentement (déduction de JP05, OD02 et OD04 ; à faire valider par `garde-conformite`). Priestley : enrichissement
  automatique à partir de l'e-mail [fiche:LJVP2wRk7Cc] (OD01).
- **Sources** : [verif:OD01-OD07, JP05].
- **Confiance** : **moyenne à haute** selon les lignes. **Statut** : Bloquant.

### J9. Influence : mentions, contrat écrit, secteurs interdits ; aucune collaboration rémunérée montée par l'agence pour l'instant
- **Fondement** : **6** catégories de promotions interdites aux influenceurs (art. 4 I-VI) [verif:JI02 ✅ haute], crypto
  sous condition [verif:JI03 🟡], jeux d'argent avec exclusion des mineurs selon le référentiel Arcom [verif:JI05 ✅] ;
  contrat écrit dès **1 000 € HT cumulés** par annonceur, par an et par objectif [verif:JI11 ✅] avec 5 rubriques
  [verif:JI12 ✅] ; annonceur, mandataire, influenceur et agent **solidairement responsables** [verif:JI13 ✅] ; formation
  financée (CPF compris) : promotion **encadrée** (bandeau ≥ 7 % de la surface, ≥ 90 % de la durée, phrase et lien
  officiels) [verif:JI09 ✅, JI10 ✅], contrepartie liée à l'inscription interdite à tous [verif:JI17 ❌ de la croyance
  « CPF interdit », JI18 ✅] ; créateur établi dans un autre État de l'EEE : art. 4 et 5 non applicables [verif:JI16 ✅] ;
  hors UE / EEE / Suisse : représentant écrit et RC pro UE [verif:JI15 ✅].
- **Point ouvert** : une agence qui organise une collaboration est-elle « mandataire » (art. 8) ou « agent d'influenceur »
  (art. 7, mise en relation à titre onéreux) ? [verif:Q2 ❓] (questions n° 2 et 4).
- **Règle maison en attendant** : l'agence ne monte **aucune collaboration rémunérée** avec un créateur, ne joue ni le
  rôle de mandataire ni celui d'agent, et ne fait aucune promotion de formation CPF (questions n° 2 et 4) ; toute
  collaboration rémunérée est ❌ dans la grille `garde-conformite`. Cela vaut aussi pour les **partnership ads** de Meta,
  les créateurs sponsorisés en TLA LinkedIn et le whitelisting (`publicite.md` P8, P12).
- **Sources** : [verif:JI01-JI19, Q1, Q2] · [fiche:bpifrance-influenceur-reglementation] ·
  `conformite-influence-commerciale.md`.
- **Confiance** : **haute** pour les règles lues ; Q1 et Q2 **à vérifier**. **Statut** : Bloquant + règle maison.

### J10. Applique les règles propres à chaque plateforme avant la création
- **Fondement** : Meta ne diffuse plus aucune pub sur un sujet social, électoral ou politique dans l'UE depuis le
  06/10/2025 (règlement TTPA) ; catégories spéciales (Financial Products and Services, Employment, Housing, Social Issues,
  Elections or Politics) à déclarer, sous peine de rejet voire de fermeture du compte [verif:PA07 ✅ moyenne] ;
  vérification des pubs « typically completed within 24 hours » [verif:PA08 🟡] ; libellés IA et détection des outils
  tiers [veille:meta-ads §5]. Restriction éventuelle des messages sponsorisés LinkedIn dans l'UE : signalée de mémoire
  dans un protocole, **non vérifiée** (prérequis de `2026-10-22-linkedin-tla-puis-message-ad`).
- **Comment l'appliquer** : une marque à message engagé passe par l'organique ; catégorie spéciale déclarée dès la
  création ; « add music », musique IA, texte IA dans l'image, traduction automatique et personne IA coupés (grille
  `garde-conformite`, ligne « Plateforme ») ; contenus restreints et concours selon les règles de chaque réseau.
- **Sources** : [verif:PA07, PA08] · [veille:meta-ads §5, §7 bis, §10 règles 9 et 14] · `meta-ads.md` MA4, MA9.
- **Confiance** : **moyenne à haute**. **Statut** : Bloquant.

### J11. Toute allégation se prouve ; l'hyperbole n'est permise que manifeste et adossée à un atout réel ; comparatif selon L. 122-1
- **Fondement** : une allégation de supériorité (« n° 1 », « le meilleur ») doit être prouvable (L. 121-2, 2°, b et f)
  [verif:OC04 ✅ haute] ; publicité comparative licite seulement si non trompeuse, sur des produits répondant aux mêmes
  besoins, comparant objectivement des caractéristiques essentielles, pertinentes, vérifiables et représentatives ;
  ni dénigrement ni confusion ; preuve « dans un bref délai » (L. 122-1 à L. 122-5) [verif:OC01 ✅ haute] ; formats
  différents signalés clairement (CJUE *Carrefour*, C-562/15) [verif:OC03 ✅] ; une invitation générique (« essayez aussi
  les autres ») qui ne vise personne d'identifiable n'est probablement pas comparative [verif:OC02 🟡].
- **Comment l'appliquer** : checklist `garde-offres` lignes 8 et 10 ; contre une **méthode**, jamais contre une marque
  nommée ; l'hyperbole n'est acceptable que si (1) l'atout sous-jacent est réel et documenté, (2) l'exagération est
  manifeste pour tout spectateur raisonnable, (3) une démonstration présentée comme réelle l'est vraiment, (4) aucun
  chiffre, avis ou témoignage n'est inventé, (5) personne n'est mis en danger (conditions tirées de la confrontation de
  [fiche:buAY7UtjCb4 enseignement 3] avec la règle d'honnêteté, appuyées sur OC04) ; aucun résultat garanti en santé,
  finance ou revenus (grille `garde-conformite`, ligne « Allégations ») ; « pas de promesse de revenus » n'efface pas
  des résultats montrés (`garde-offres` ligne 10).
- **Experts** : Hopkins, « Try our rivals' too » [fiche:hopkins-scientific-advertising p. 34] (OC02) et « ne jamais
  attaquer un concurrent » ; Denney, angles « scam / worth it » sur **sa propre** marque, permis, à distinguer du
  dénigrement d'un tiers [fiche:yRgPbqywUJ8 enseignement 6].
- **Sources** : [verif:OC01-OC04, OP08].
- **Confiance** : **haute**. **Statut** : Bloquant.

### J12. Prévente et formation : règles d'attente tant que les questions n° 5 sont ouvertes
- **Fondement** : informer avant la commande de la date ou du délai de livraison (L. 221-5, 3°) [verif:OV01 ✅ haute] ;
  rétractation de 14 jours entière tant que rien n'est livré, exception numérique à trois conditions (accord exprès,
  reconnaissance, confirmation) [verif:OV02 ✅ haute] ; sommes versées d'avance = **arrhes** par défaut, restituées au
  double si la marque annule sans clause écrite [verif:OV03 🟡] ; formation achetée à titre individuel : 10 jours de
  rétractation, rien avant, **30 % maximum** ensuite, si le Code du travail s'applique [verif:OV07 ✅ texte] ; régime de
  l'enseignement à distance [verif:OV08 🟡]. Champ d'application et cas limites : [verif:OQ1, OQ2, OQ3 ❓].
- **Règles d'attente (question n° 5)** : aucune prévente de formation payée à plus de 30 % d'avance ; aucun « −X % sur
  le prix final » d'un produit jamais vendu ; la rétractation n'est pas présumée perdue au premier module ; toute
  prévente de formation part en renvoi à un juriste (`garde-offres` lignes 13 et 14).
- **Expert concerné** : Marketing Mania, prévente « éthique si on le dit » [fiche:11rNI6BUey4] : « le dire » est une
  obligation, et la clause de remboursement doit être écrite (OV01, OV03).
- **Sources** : [verif:OV01-OV08, OQ1-OQ3] · règle sans condition n° 5.
- **Confiance** : **haute** pour les textes ; OQ1-OQ3 **à vérifier**. **Statut** : Bloquant + à vérifier.

### J13. Un point ouvert reste ouvert : il va en question à l'utilisateur, jamais en interprétation favorable
- **Fondement** : les sections G (Q1-Q3) et O (OQ1-OQ4) du registre documentent sans trancher ; un verdict ❓ juridique
  « se fait trancher par un juriste » (légende du registre). Le Digital Fairness Act (comptes à rebours, dark patterns)
  n'est pas encore proposé au 22/10/2026 [verif:OQ4 ❓] : à suivre par la veille.
- **Comment l'appliquer** : ⚠️ dans le rapport de `garde-conformite` ou `garde-offres`, question ajoutée à
  `journal/questions-utilisateur.md` par l'orchestrateur ; en attendant, la lecture la plus prudente.
- **Statut** : Règle maison.

---

## Désaccords entre experts (et avec le droit)

> Dans ce domaine, un désaccord se tranche par le texte vérifié, pas par le consensus des praticiens.

### D1. Afficher une « valeur » empilée pour faire paraître le prix bas ?
- **Positions** : Kennedy (valeur de remplacement « that's the truth »), Hormozi (value stack), Brunson (élève de
  Kennedy, non indépendant) pour ; droit : faux prix de référence (L. 121-2, 2°, c ; *Aldi Süd*) [verif:OP06 ❌, OP01].
- **Tranché** : interdit sauf valeur = prix réellement pratiqué pour l'élément vendu seul, ou comparaison externe sourcée
  et dite (J2). **Ce qui ferait changer** : seulement un texte ou une décision publiés (lignes directrices C/2021/526
  non lues, demande à `chercheur-sources`).

### D2. Urgence et rareté : levier à utiliser ou à éviter ?
- **Positions** : Heath, Hopkins, Google, Hormozi (Fast Cash), Priestley les utilisent ; Ralston les juge inutiles si
  la relation existe (`monetisation-et-offre.md` D1).
- **Tranché** : permises **seulement vraies, datées et tenues**, en B2B comme en B2C (J3) ; la confiance reste le levier
  par défaut.

### D3. « Satisfait ou remboursé » comme argument ?
- **Positions** : usage courant des offres numériques ; Hopkins préfère « paie dans une semaine si ça te plaît »
  [verif:OG03] ; droit : la rétractation légale ne s'affiche pas comme un avantage [verif:OG01 ✅].
- **Tranché** : seule une garantie plus large que la loi, dite comme un ajout, est un argument (J4).

### D4. Faut-il toujours le consentement pour envoyer un e-mail commercial ?
- **Positions** : Bpifrance : « systématiquement requis » ; CNIL : exception client et régime B2B.
- **Tranché** : la **CNIL** fait foi [verif:JI24 ❌, JP01, JP02] (J7). Déjà noté dans `frameworks/index.md`.

### D5. Porte-parole « créé » ou recommandation fabriquée ?
- **Positions** : Hopkins vante une signataire créée [p. 35-36, p. 83] ; Halbert a utilisé la fausse recommandation d'un
  parent [verif:V4A-H02 🟡].
- **Tranché** : interdit (règle d'honnêteté, OU06) ; mascotte explicitement fictive permise (J5).

### D6. Partager les contacts recrutés avec un partenaire (Abraham) ?
- **Positions** : Abraham négocie la copropriété des fichiers [fiche:Ge8xTCIP0Zw] ; RGPD et CPCE encadrent tout transfert
  et toute prospection par le partenaire.
- **Tranché** : possible seulement avec base légale, information des personnes (source) et consentement pour la
  prospection électronique B2C du partenaire ; validation `garde-conformite` avant tout accord (J8). **Ce qui ferait
  changer** : un avis de juriste sur un cas réel.

---

## Questions ouvertes renvoyées à l'utilisateur (`journal/questions-utilisateur.md`)
- **N° 2** : l'agence est-elle « mandataire » de la marque au sens de l'art. 8 ? (Q2) → J9.
- **N° 4** : agent d'influenceur (art. 7) ; compte de marque ou fondateur qui parle de ses produits (Q3) ; post sponsorisé
  public et démarchage CPF (Q1 a) → J1, J7, J9.
- **N° 5** : formation en ligne (Code du travail ou de l'éducation), « −X % sur le prix final » en prévente, rétractation
  au premier module, cumul CPF (OQ1-OQ3) → J12.

## Journal
| Date | Modification |
|---|---|
| 2026-10-25 | Création (grande synthèse, équipe S4) : 13 principes fondés sur le registre (sections A2, E à O, règles sans condition), la checklist `garde-offres` et la grille `garde-conformite` ; 6 désaccords tranchés par le texte ; renvoi aux questions n° 2, 4, 5. |
