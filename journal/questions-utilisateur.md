# Questions pour l'utilisateur

(Ce qui bloque et nécessite une réponse. L'agence continue le reste en attendant.)

## 2026-10-20
1. **Rapport LinkedIn de Richard van der Blom (payant)** : c'est la référence sur l'algorithme LinkedIn.
   Veux-tu l'acheter et le déposer dans `sources/` ? (Sinon on s'appuie sur ses résumés publics.)

## 2026-10-21
2. **Responsabilité légale de l'agence (question pour un juriste)** : la loi influence du 9 juin 2023
   rend l'annonceur, son mandataire, l'influenceur et son agent solidairement responsables. Si l'agence
   organise une collaboration entre une marque et un créateur, est-elle « mandataire » ? Tant qu'on n'a
   pas de réponse, l'agence ne monte aucune collaboration rémunérée avec un créateur
   ([fiche:bpifrance-influenceur-reglementation]).
3. **Clé API YouTube (facultatif, confort)** : pour vérifier les métadonnées des vidéos (vues, durée, date),
   l'agence passe aujourd'hui par un relais public tiers. Une clé YouTube Data API v3 (gratuite, Google
   Cloud) stockée en variable d'environnement de l'environnement cloud (`YOUTUBE_API_KEY`, jamais dans
   le repo) rendrait la vérification plus fiable. Sans elle, on continue comme aujourd'hui.

4. **Questions juridiques précisées (pour un juriste)**. L'état des sources est dans `connaissances/verifications/passe-2-droit.md` (Q1-Q3).
   - **Agence « mandataire » ou « agent d'influenceur » ?** La loi ne définit pas le mandataire (→ art. 1984 du Code civil :
     agir au nom et pour le compte de la marque). Nouveau risque : l'art. 7 de la loi 2023-451 définit l'agent d'influenceur
     comme celui qui « met en relation, à titre onéreux » créateurs et annonceurs. Une agence payée pour trouver des
     créateurs pourrait donc être qualifiée d'agent, avec la même responsabilité solidaire. Aucune jurisprudence trouvée.
   - **Compte de marque ou fondateur qui parle de ses propres produits** : relève-t-il de la loi influence ? Aucun texte lu
     ne tranche (critère « à titre onéreux » de l'art. 1). Le droit commun des pratiques commerciales trompeuses s'applique
     dans tous les cas, et la Commission européenne considère que l'autopromotion doit être signalée comme commerciale.
   - **Formation CPF** : la promotion est encadrée. La contrepartie liée à l'inscription et le démarchage individuel des titulaires
     (email, DM, SMS, téléphone) sont interdits à tous (jusqu'à 375 000 € pour une société). Question ouverte : un post sponsorisé public
     compte-t-il comme démarchage ?
   En attendant : l'agence ne joue ni le rôle de mandataire ni celui d'agent pour une collaboration rémunérée, et ne fait
   aucune promotion de formation CPF.

5. **Droit des offres : 3 questions pour un juriste** (détail : `connaissances/verifications/passe-3-droit-offres.md`, OQ1-OQ3).
   - **Formation en ligne vendue à un particulier** : relève-t-elle du Code du travail (L6353-3 et s. : 10 jours de rétractation,
     rien à payer pendant ce délai, puis 30 % du prix au maximum) ou du Code de l'éducation (L444-1 et s.) ? Si c'est le Code du
     travail, une prévente payée à 100 % d'avance est impossible.
   - **Prévente** : peut-on annoncer « −X % sur le prix final » alors que ce prix n'a encore jamais été pratiqué ?
   - **Cours livré par étapes** : le droit de rétractation tombe-t-il dès l'accès au premier module ?
   - **Cumul** : une formation éligible au CPF vendue en prévente avec réduction cumule deux questions ouvertes (Q1 c du n° 4 et OQ2) ; aucune ne tranche l'autre.
   - **Engagement et frais de sortie** : une offre « frais d'installation offerts contre 6 mois d'engagement, dus en cas de résiliation anticipée » (Hormozi) est-elle licite en B2C ? en B2B ? (`connaissances/principes/monetisation-et-offre.md` D9). En attendant : pas de pénalité de sortie (défaut Sillage).
   En attendant : l'agence ne propose aucune prévente de formation payée à plus de 30 % d'avance, n'affiche aucun prix barré
   sans prix réellement pratiqué sur 30 jours, et ne présente jamais la rétractation légale de 14 jours comme un avantage.

6. **X Premium pour les comptes de marque ?** (détail : `veille/plateformes/x.md` § 4.4 et § 8). Premium débloque les posts longs
   (jusqu'à 25 000 caractères), les Articles et les réponses prioritaires ; un relevé tiers (Buffer) annonce une portée médiane
   environ 10 fois supérieure (non vérifié, et aucun multiplicateur Premium n'apparaît dans le code publié en 2026). Coût :
   abonnement mensuel par compte. En attendant : threads dont le premier post tient seul (pas de Premium supposé).
