# Séquence payante LinkedIn : Thought Leader Ads → Message Ad au nom du même dirigeant (et variante multi-étapes)

> Famille : publicité payante B2B / LinkedIn · Niveau : campagne de bout en bout (réchauffer puis convertir)

## Origine
- **The LinkedIn Ads Show**, ép. 167, AJ Wilcox (B2Linked) avec Ruby James (LinkedIn) [fiche:pILj7t-qQhs] :
  - séquence TLA → Sponsored Messaging (framework I [00:30]-[00:32]) ;
  - séquence de TLA en plusieurs étapes, « hack Fibbler » (framework J [00:33]-[00:34]) ;
  - pas besoin d'audience pour sponsoriser (enseignement 8 [00:41]) ;
  - échelle d'engagement du comité d'achat, cas Sendoso (framework B [00:15]-[00:16]), usage CRM **déduit**.
- **Même mécanisme ailleurs dans la base** : le funnel « shorts larges → retargeting payant **au même visage** » d'Hormozi (voir `role-des-formats-courts-et-longs.md`). Ici, la version B2B : le message de retargeting part **au nom de la personne** avec qui le prospect a interagi.
- Fiabilité : **2,5/5** pour la source (tactiques ≈ 3,5/5, chiffres ≈ 1,5/5). **Conflit d'intérêts majeur** : l'invitée est salariée de LinkedIn, l'animateur vend des LinkedIn Ads. Le « ×6 », le « +24 % / +120 % » et le « 33 % » sont des **corrélations sans méthode publiée**, avec biais de sélection probables : à présenter au mieux « selon LinkedIn », jamais comme des faits.

## Problème résolu
Un message privé sponsorisé envoyé à froid convertit mal ; un post de dirigeant crée de la confiance mais pas de rendez-vous. La séquence combine les deux : les TLA construisent une audience de retargeting « very cheap but very engaged », puis un message signé par **le même dirigeant** propose l'étape de bas d'entonnoir. Les deux formats sont « intensely personal », d'où la cohérence.

## Prérequis
- Marque B2B, un dirigeant qui publie (voir `journee-du-journaliste-et-production-dirigeant.md`), budget LinkedIn Ads, CRM.
- **Mesure installée avant de payer** : voir `cac-blended-et-mesure-du-mix.md` (Revenue Attribution Report, Conversions API, outil tiers).
- Validation explicite de l'utilisateur avant tout lancement (`publicateur`, API officielle).

## Étapes

### 1. Le dirigeant publie en organique
Choisir ses meilleurs posts (pédagogiques, voir la règle 80/20).
- Question : le post tient-il seul, sans contexte, devant un inconnu de l'ICP ?

### 2. Sponsoriser en Thought Leader Ads, ciblés sur l'ICP
- Les TLA ressemblent à de l'organique (mention « promoted by » + nom de l'entreprise).
- **Sans attendre d'avoir une audience** : « With thought leader ads, we can take someone who has no following and still put their content in front of exactly the right people. »
- Question : le ciblage correspond-il au best-fit (critères de compte, voir `cinq-composantes-du-positionnement.md`) ?

### 3. Créer l'audience « a interagi avec les TLA »

### 4. Envoyer une Message Ad (ou Conversation Ad) **au nom du même dirigeant**
- Offre de bas d'entonnoir : démo, rendez-vous.
- Le texte n'est pas donné par l'épisode : à écrire à partir du TLA vu par le prospect (`redacteur-linkedin`).
- Format : AJ préfère aujourd'hui les **Message Ads** (données non montrées) ; Ruby les met au même niveau. « Age-old debate » → **tester les deux**.
- Questions :
  - Le message fait-il référence, honnêtement, au sujet du post vu (sans prétendre à un échange qui n'a pas eu lieu) ?
  - L'offre est-elle la prochaine étape réelle et une seule ?

### 5. Mesurer soi-même le gain du réchauffement
Groupe « TLA puis message » contre groupe « message seul », même offre, même période. Ne pas reprendre le ×6 de LinkedIn.
- Question : a-t-on contrôlé le biais de sélection (ceux qui interagissent étaient déjà plus intéressés) ? Idéalement, un groupe exposé aux TLA mais **sans** message en plus.

### 6. Variante pour une marque jeune : séquence de 2 à 4 TLA
1. TLA éducatifs de haut d'entonnoir.
2. Retargeting des personnes touchées avec un TLA « set up a meeting with me ».
3. Pour N étapes : à chaque étape, une audience de retargeting de l'étape précédente **et** une exclusion des personnes déjà passées à l'étape suivante (montage manuel dans Campaign Manager, lourd).
- Tension assumée : plus direct que la règle 80/20, justifié par le stade précoce de l'entreprise.

### 7. Exploiter le signal CRM (déduction)
Repérer dans les opportunités ouvertes qui like, commente ou **suit** les dirigeants ; traiter l'abonnement comme un signal fort de priorité commerciale. Le cas Sendoso (+24 % / +120 % de taille de deal) porte sur **une seule entreprise**, avec causalité inverse probable.

## Exemple appliqué (illustratif : Sillage, B2B)
- Post organique du fondateur : « Ce qu'on a appris en refaisant 30 vidéos de lancement : on coupe la moitié des messages. »
- TLA ciblé : fondateurs et responsables marketing de startups SaaS de 5 à 50 personnes.
- Message Ad signé par le fondateur aux personnes ayant interagi : « Vous avez lu notre post sur les vidéos de lancement. Si vous lancez dans les 2 prochains mois, je peux regarder votre landing et vous dire en 15 minutes quel moment mettre en avant. » Une offre, un lien.
- Test : 50 % des personnes engagées reçoivent la Message Ad, 50 % non ; on compare les rendez-vous pris (protocole par `concepteur-experiences`).
- Le message ne doit pas être envoyé à quelqu'un qui a demandé à ne plus être sollicité ; pour une prospection par e-mail en parallèle, voir `arbre-regime-message-electronique-cnil.md` (les messages LinkedIn ne sont **pas couverts** par la fiche CNIL : zone grise).

## Erreurs fréquentes
- Envoyer le message au nom de la marque au lieu du dirigeant vu dans le TLA.
- Attendre d'avoir des abonnés pour sponsoriser.
- Une offre de bas d'entonnoir dans le TLA lui-même (sauf variante multi-étapes assumée).
- Oublier les exclusions dans une séquence multi-étapes (le même prospect reçoit tout).
- Citer le ×6 comme une preuve.
- Faux prétexte dans le message (« suite à notre échange » sans échange réel).

## Agents qui doivent l'utiliser
`strategiste-ads` (propriétaire), `redacteur-linkedin` (posts et Message Ad), `redacteur-ads`, `architecte-personal-brand` (le dirigeant), `analyste-performance` (groupes comparés, CRM), `concepteur-experiences` (test Message Ad / Conversation Ad, test de réchauffement), `garde-conformite`, `publicateur`.

## Voir aussi
`journee-du-journaliste-et-production-dirigeant.md` · `crawl-walk-run-voix-sponsorisees.md` · `cac-blended-et-mesure-du-mix.md` · `role-des-formats-courts-et-longs.md`
