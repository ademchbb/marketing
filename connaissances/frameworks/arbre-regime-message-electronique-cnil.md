# Quel régime pour ce message ? Arbre de décision CNIL (prospection / transactionnel / relationnel, B2C / B2B) et checklists

> Famille : conformité · Niveau : contrôle de tout email, SMS ou séquence avant validation
> **Ce n'est pas un avis juridique.** En cas de doute sur un cas réel, la question va dans `journal/questions-utilisateur.md`.

## Origine
- **CNIL**, *Communications par voie électronique aux prospects et clients : quelles règles respecter ?*, mise à jour du 2026-06-10 [fiche:cnil-prospection-electronique] :
  - arbre de décision (framework A, **ordre déduit** par la fiche) ;
  - typologie des messages (framework B) ; jurisprudence de la page (framework C) ;
  - checklist officielle en 11 points (framework D) ; double test de qualification (framework E) ;
  - checklists B2B et B2C (fin de fiche).
- Textes : CPCE art. L.34-5, RGPD, loi Informatique et Libertés ; CJUE 13 nov. 2025 *Inteligo Media* (C-654/23) ; CNIL SAN-2021-008, SAN-2022-017, SAN-2024-002.
- **Étiquettes reprises de la fiche, sans les renforcer** :
  - **[LOI]** obligation légale ou interprétation par un juge ou par la CNIL en sanction ;
  - **[RECO]** bonne pratique recommandée par la CNIL, pas formellement obligatoire ;
  - **[USAGE]** pratique du métier absente de la source ;
  - **(déduction)** application de l'agence, non écrite dans la source.
- Fiabilité : **5/5** sur son périmètre (autorité compétente), **couverture partielle**. **Prime sur Bpifrance** [fiche:bpifrance-influenceur-reglementation], qui écrit à tort que le consentement est « systématiquement requis » pour la prospection par courriel.

## Problème résolu
Les tactiques « posséder l'audience » (lead magnets, séquences de bienvenue, cold email) des fiches de créateurs ne parlent jamais de consentement. Or en France tout dépend de **l'objectif** du message, pas de son ton : une newsletter « éducative » qui vise à faire acheter est de la prospection. L'arbre qualifie chaque message avant de l'écrire.

## Périmètre
Courriel, SMS, MMS, automates d'appel, « autres technologies » électroniques. **Hors périmètre** de la source : messages privés LinkedIn et autres messageries sociales (zone grise), adresses génériques, achat ou location de fichiers, cookies et pixels, durées de conservation chiffrées, téléphone, courrier.

## Étapes : l'arbre de décision
1. **Canal** : électronique (courriel, SMS, MMS, automate, autre) ? Sinon, autres règles, hors fiche.
2. **Destinataire** : adressé directement à une personne identifiée ? Sinon (post public), ce régime ne s'applique pas a priori **(déduction)**.
3. **Objectif** (et non apparence) — **double test** [LOI, CJUE] :
   - exécuter ou informer sur un service demandé → **transactionnel** ;
   - accompagner l'usage sans aucune promotion → **relationnel** ;
   - promouvoir, directement ou indirectement, produits, services **ou l'image de l'entreprise**, ou pousser à consommer davantage → **prospection**.
4. **Transactionnel** → base « exécution du contrat », pas de consentement. Vérifier l'absence de contenu promotionnel, sinon retour à 3 en prospection [LOI].
5. **Relationnel** → base « intérêt légitime » : information, opposition quand c'est applicable, fréquence raisonnable, clients uniquement. Même vérification qu'en 4 [LOI].
6. **Prospection vers un professionnel**, en lien avec son activité → pas de consentement systématique ; exiger origine des données + finalité indiquées, opposition simple [LOI] [§ B to B].
7. **Prospection vers un particulier déjà client**, pour des produits **similaires** de **la même entreprise** → pas de nouveau consentement ; exiger information et opposition facile **à la collecte et dans chaque message** (4 conditions cumulatives) [LOI].
8. **Tous les autres cas** → **consentement préalable** libre, spécifique et éclairé : prospects, comptes créés sans achat, offres de partenaires, produits non similaires [LOI].
9. **Dans tous les cas** : information dès la collecte, liste repoussoir [RECO, au service de l'opposition durable LOI], prestataires encadrés, sécurité, durées de conservation, preuves documentées [§ Checklist].
- Questions à chaque nœud : l'ai-je écrit dans le brief ? Dans un cas limite, ai-je tranché dans le sens le plus prudent (prospection) **(déduction)** ?

## Typologie et jurisprudence (rappel)
| Type | Exemples cités | Base | Consentement ? |
|---|---|---|---|
| Prospection | Offres, newsletter visant l'abonnement | Consentement (B2C) sauf exception client ; régime B2B | Oui en B2C sauf exception client ; pas systématique en B2B |
| Transactionnel | Bienvenue, alertes de compte, expédition, confirmation, facture, rappels, mot de passe | Exécution du contrat | Non, si aucun contenu promotionnel |
| Relationnel | Biens similaires d'une alerte immobilière, sondages anonymes, conseils d'usage, alertes de sécurité | Intérêt légitime (raisonnable, non intrusif) | Non, mais information et opposition quand c'est applicable |

| Cas | Régime retenu | Référence |
|---|---|---|
| Compte gratuit presse freemium, lettre du même éditeur | **Peut** relever de l'exception client (« dans certains cas ») | CJUE C-654/23 |
| Compte e-commerce créé sans achat | Consentement préalable | SAN-2021-008 |
| Client d'hôtel → offres de partenaires | Consentement préalable | SAN-2022-017 |
| Alerte immobilière → biens similaires, sondages anonymes | Peut ne pas être de la prospection | SAN-2024-002 |
Frontière freemium : **non tracée par la CNIL** ; notre lecture (service réel rendu, intégré au modèle économique) est une **déduction**. Ne jamais généraliser « freemium = client ».

## Checklist officielle CNIL (11 points, dans l'ordre)
1. Identifier la nature du message. 2. Pas de contenu promotionnel significatif dans le transactionnel et le relationnel. 3. Déterminer la base juridique. 4. Informer clairement à la collecte. 5. Consentement valide quand il est requis. 6. Opposition ou désinscription simple à la collecte et dans chaque message, quand c'est requis. 7. Liste d'opposition à jour. 8. Encadrer les prestataires. 9. Sécurité des données. 10. Durées de conservation adaptées. 11. Documenter (preuves de consentement, procédures).

## Checklist B2B (BLOQUANT / À CORRIGER / À VÉRIFIER, niveaux repris de la fiche)
- **BLOQUANT** — Type de message écrit dans le brief, jugé sur l'objectif [LOI].
- **BLOQUANT** — Destinataire contacté à titre professionnel ; sinon checklist B2C [LOI].
- **BLOQUANT** — Message en lien avec l'activité professionnelle (fonction ↔ offre) [LOI].
- **À CORRIGER** — Cibles à fonction éloignée exclues (déduction).
- **BLOQUANT** — Aucun contact de la liste repoussoir dans la campagne [LOI : opposition durable ; RECO : liste repoussoir].
- **À VÉRIFIER** — Origine de chaque adresse connue ; fichier acheté, loué ou scrapé : zone non couverte, à faire trancher (déduction ; lacune).
- **BLOQUANT** — Le message dit d'où vient l'adresse [LOI].
- **BLOQUANT** — Le message dit pourquoi on écrit [LOI].
- **BLOQUANT** — Moyen simple de ne plus être sollicité dans chaque message [LOI].
- **BLOQUANT** — Expéditeur clairement identifié [LOI : information sur l'identité ; obligation **par message** à vérifier dans L.34-5].
- **BLOQUANT** — Aucun faux prétexte (« suite à notre échange » sans échange, faux « Re: ») (déduction ; règle d'honnêteté du projet).
- **À CORRIGER** — Offre de partenaire retirée ou envoyée à part, sur une base adaptée (déduction).
- **BLOQUANT** — Toute demande d'arrêt ajoutée le jour même à la liste repoussoir et propagée [LOI ; RECO].
- **À CORRIGER** — Relance arrêtée dès qu'une opposition est exprimée (déduction).
- Socle : **BLOQUANT** prestataire d'envoi encadré par contrat [LOI, point 8] ; **À CORRIGER** durée de conservation fixée et purge (durée non chiffrée par la source) ; **À CORRIGER** sécurité ; **À CORRIGER** procédure écrite.

## Checklist B2C (même convention)
- **BLOQUANT** — Type écrit dans le brief, jugé sur l'objectif ; faire acheter, consommer davantage, revenir sur la plateforme ou valoriser l'image = prospection, même au ton éducatif [LOI, CJUE].
- **BLOQUANT** — Base identifiée : consentement préalable, ou exception client avec ses 4 conditions ; aucune autre base [LOI].
- Consentement : **BLOQUANT** case décochée [LOI] ; **BLOQUANT** consentement spécifique, non noyé dans les CGV ni conditionné [LOI] ; **BLOQUANT** lead magnet : consentement newsletter **distinct** de la ressource (déduction de [LOI]) ; **BLOQUANT** information dès la collecte [LOI] ; **BLOQUANT** preuve conservée (date, formulaire, texte) ; **BLOQUANT** compte sans achat ≠ client [LOI, SAN-2021-008] ; **À VÉRIFIER** double opt-in [USAGE], non exigé par la source.
- Exception client : **BLOQUANT** achat réel (freemium : au cas par cas) ; **BLOQUANT** produits similaires ; **BLOQUANT** même entreprise (partenaires : consentement) [LOI, SAN-2022-017] ; **BLOQUANT** information et opposition facile dès la collecte [LOI] ; **À CORRIGER** case d'opposition décochée [RECO].
- Chaque message de prospection : **BLOQUANT** désinscription simple (email et SMS) [LOI] ; **BLOQUANT** expéditeur identifiable [LOI ; obligation par message à vérifier] ; **BLOQUANT** liste repoussoir vérifiée avant envoi et à chaque import [LOI ; RECO] ; **À VÉRIFIER** désinscription en un clic dans l'en-tête [USAGE], hors source.
- Transactionnel et relationnel : **BLOQUANT** aucune offre, code promo ou incitation à l'achat sauf consentement ou exception client [LOI] ; **BLOQUANT** relationnel aux seuls clients, sans autre offre [LOI, SAN-2024-002] ; **À CORRIGER** fréquence raisonnable fixée [LOI : intérêt légitime « raisonnable »] ; **À CORRIGER** information et opposition aux relationnels quand c'est applicable [LOI].
- Socle : **BLOQUANT** prestataires encadrés ; **BLOQUANT** liste repoussoir centralisée et synchronisée [RECO, au service d'une obligation] ; **À CORRIGER** durée de conservation et purge ; **À CORRIGER** sécurité et procédure.

## Exemple appliqué (illustratif)
- **Cold email Sillage** à la responsable marketing d'une startup : prospection B2B, fonction liée à l'offre → possible sans opt-in **si** le message dit d'où vient l'adresse, pourquoi on écrit, et permet de se désinscrire (« répondez stop »). Le même email à un développeur de la startup : lien professionnel fragile → exclure (déduction).
- **Lead magnet** d'une marque promue B2C : l'envoi de la checklist est transactionnel ; l'inscription à la newsletter promotionnelle demande une case **décochée distincte**.
- **Email de bienvenue** avec code promo à un inscrit sans consentement promotionnel : n'est plus transactionnel → illicite hors exception client (déduction).
- Gabarits de mentions (déduction de la fiche, à adapter) : « ☐ J'accepte de recevoir par email les nouveautés et offres de [marque]. Désinscription possible à tout moment. » ; « Nous pourrons vous envoyer par email des offres sur des produits similaires de [marque]. ☐ Je ne souhaite pas les recevoir. »

## Erreurs fréquentes
- Juger un message sur son ton (« c'est juste une newsletter informative »).
- Glisser une offre dans un email transactionnel ou relationnel.
- Envoyer des offres de partenaires à sa base clients sans consentement spécifique.
- Traiter un compte sans achat (ou un freemium, sans examen) comme un client.
- Ne pas synchroniser la liste repoussoir lors d'un import ou d'un changement d'outil.
- Citer Bpifrance au lieu de la CNIL pour l'emailing.
- Présenter un [USAGE] (double opt-in, désinscription en un clic) comme une obligation de cette source.

## Agents qui doivent l'utiliser
`garde-conformite` (propriétaire), `redacteur-newsletter` (séquences, bienvenue, relances), `strategiste-offre` (lead magnets, formulaires), `strategiste-contenu`, `prospecteur-collaborations` (co-marketing), `publicateur` (aucun envoi sans feu vert), `gestionnaire-communaute` (quand un DM renvoie vers une inscription email), `strategiste-ads` (formulaires instantanés et retargeting vers une inscription).

## Voir aussi
`conformite-influence-commerciale.md` · `funnel-cta-commentaire.md` · `offer-stack.md`
