# État de l'agence — file de tâches

> Toute session ou reprise commence ici. Mettre à jour après chaque étape, puis commit + push
> sur la branche `claude/marketing-agent-hierarchy-gm2c4k` (repo `ademchbb/marketing`).
> (Ancienne branche de travail : `claude/stoic-brown-bol5m5`.)

## Contexte
- 2026-10-19 ~23h30 (heure FR) : l'utilisateur crée l'agence. Il envoie 5 vidéos (personal branding,
  croissance d'audience, reels viraux). Il dort ; reprises programmées à 00:05 UTC et 02:30 UTC.
- Le quota de session coupe tout après ~45 min de travail parallèle intense (reset toutes les 5 h :
  00h, 05h, 10h UTC…). Reprises de secours programmées à 10h10 et 15h10 UTC le 2026-10-20.
- Transcription YouTube : fonctionne depuis le cloud via `yt-dlp` (l'API youtube-transcript est
  souvent bloquée, yt-dlp passe). Script : `outils/youtube/transcrire.py`.

## Fait
- [x] Structure du repo, `CLAUDE.md`, outils de transcription et de découpe.
- [x] 5 vidéos transcrites et découpées en 17 parties (`sources/index.md`).
- [x] 58 agents écrits en 9 pôles (`agents.md`).
- [x] 17 notes d'analyse (`connaissances/fiches/<id>/notes-partie-NN.md`). (1re tentative à 21h30 UTC
      coupée par la limite de quota ; relancée à 00h07 UTC.)

## En cours (lancés vers 00h45 UTC ; coupés par la limite de quota vers 01h ; repris à 07h47 UTC)
- [x] 5 fiches consolidées (`connaissances/fiches/<id>/fiche.md`).
- [x] `extracteur-hooks` → swipe-file (82 hooks, 14 structures, 30 CTA) · `extracteur-frameworks` → 47 frameworks
- [x] `verificateur-faits` → registre (120 affirmations : 10 ✅ 76 🟡 12 ❌ 22 ❓)
- [x] `cartographe-lacunes` → `connaissances/lacunes.md`
- [ ] 4 × `synthetiseur-connaissances` (par groupe de thèmes) → `connaissances/principes/` — lancés 08h30 UTC
- [ ] `chercheur-sources` → `sources/a-traiter.md`
- [ ] ensuite : 1 synthétiseur pour `connaissances/index.md` + désaccords transverses ; `architecte-agents` (renvois agents → frameworks, règle tiret long) ; `rapporteur`
- [x] 4 × `veilleur-algorithmes` → `veille/plateformes/{instagram,tiktok,youtube,linkedin}.md`

## Session du 2026-10-21 (demande : « te former au maximum, hiérarchie stricte d'agents »)
- Vérifié : un sous-agent n'a pas l'outil Agent → la sous-délégation passe par l'orchestrateur
  (section « Demandes de délégation » à la fin de chaque rapport).
- [x] Lot 2 découpé (`decouper.py`) : 6 vidéos, 7 parties + 4 sources web.
- [x] 8 × `analyste-transcription` sur le lot 2 → 10 notes
- [x] 10 × `consolidateur-fiche` → 10 fiches
- [ ] extracteur-hooks, extracteur-frameworks, 3 × verificateur-faits (passe 2) — lancés
- [x] `architecte-agents` : section « Sous-délégation » dans tous les agents, hiérarchie dans `agents.md`,
      règle tiret long, renvois frameworks/principes (lancé)
- [ ] `chercheur-sources` : « Lot 3 — Canon du marketing » (Hormozi, Ogilvy, Schwartz, Cialdini, Ries & Trout,
      Sharp, Godin, Sutherland…) + programme de formation dans `sources/a-traiter.md` (lancé)
- [x] `architecte-agents` : créer `extracteur-pdf` (59 agents) ; `lecteur-images` en cours
- [ ] 4 × `extracteur-pdf` (ABCD, Binet & Field, Baromètre 2026, Hopkins) lancés
- Délégations demandées par les agents : `journal/delegations.md`
- ensuite : → hooks/frameworks/vérif → synthétiseur (principes + `index.md`)
  → `extracteur-youtube` sur le lot 3 → même pipeline.

## À faire (dans l'ordre)
4. `synthetiseur-connaissances` → `connaissances/principes/` + `index.md`.
5. `cartographe-lacunes` → `connaissances/lacunes.md` ; puis `chercheur-sources` → `sources/a-traiter.md`.
6. Ingérer les 5 premières sources de `sources/a-traiter.md` (même pipeline).
7. `architecte-agents` : relire les principes et créer/améliorer les agents qui manquent.
8. Préparer pour l'utilisateur un résumé « ce que l'agence a appris cette nuit » (`journal/rapport-<date>.md`).

## Prochaines étapes (quand la file est vide)
- Créer `marques/sillage/` (le studio motion design de l'utilisateur) et dérouler le pipeline
  « Promouvoir une marque » jusqu'au calendrier + 3 premiers posts (sans publier).
- Idée (rapport consolidateur HzoQgQS8czE) : le tiret long « — » est perçu comme marqueur de texte IA ; règle à ajouter aux rédacteurs pour les textes publiés (architecte-agents).
