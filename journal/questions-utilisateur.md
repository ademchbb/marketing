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
