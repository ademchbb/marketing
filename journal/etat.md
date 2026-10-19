# État de l'agence — file de tâches

> Toute session ou reprise commence ici. Mettre à jour après chaque étape, puis commit + push
> sur la branche `claude/stoic-brown-bol5m5` (repo `ademchbb/marketing`).

## Contexte
- 2026-10-19 ~23h30 (heure FR) : l'utilisateur crée l'agence. Il envoie 5 vidéos (personal branding,
  croissance d'audience, reels viraux). Il dort ; reprises programmées à 00:05 UTC et 02:30 UTC.
- Transcription YouTube : fonctionne depuis le cloud via `yt-dlp` (l'API youtube-transcript est
  souvent bloquée, yt-dlp passe). Script : `outils/youtube/transcrire.py`.

## Fait
- [x] Structure du repo, `CLAUDE.md`, outils de transcription et de découpe.
- [x] 5 vidéos transcrites et découpées en 17 parties (`sources/index.md`).
- [x] Agents du pôle Apprentissage écrits.

## En cours
- [ ] 17 × `analyste-transcription` (une partie chacun) → `connaissances/fiches/<id>/notes-partie-NN.md`
- [ ] Écriture des agents des autres pôles (veille, stratégie, création, qualité, labo, diffusion, méta)

## À faire (dans l'ordre)
1. Vérifier que les 17 notes existent (sinon relancer l'analyste manquant).
2. 5 × `consolidateur-fiche` → `connaissances/fiches/<id>/fiche.md`.
3. En parallèle : `extracteur-hooks`, `extracteur-frameworks`, `verificateur-faits`.
4. `synthetiseur-connaissances` → `connaissances/principes/` + `index.md`.
5. `cartographe-lacunes` → `connaissances/lacunes.md` ; puis `chercheur-sources` → `sources/a-traiter.md`.
6. Ingérer les 5 premières sources de `sources/a-traiter.md` (même pipeline).
7. `architecte-agents` : relire les principes et créer/améliorer les agents qui manquent.
8. Préparer pour l'utilisateur un résumé « ce que l'agence a appris cette nuit » (`journal/rapport-<date>.md`).

## Prochaines étapes (quand la file est vide)
- Créer `marques/sillage/` (le studio motion design de l'utilisateur) et dérouler le pipeline
  « Promouvoir une marque » jusqu'au calendrier + 3 premiers posts (sans publier).
