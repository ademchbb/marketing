# Agence marketing autonome — règles du projet

Ce repo est **le cerveau marketing** de l'utilisateur : une agence entière faite d'agents IA
spécialisés. Objectif à long terme : quand l'utilisateur dit « fais connaître la marque X » ou
« crée-moi les posts de la semaine », tout est automatisé **de A à Z** — apprentissage, veille,
stratégie, création, contrôle qualité, tests, publication, analyse.

Repo frère : **`ademchbb/motion-design`** (studio *Sillage*) — fabrique les vidéos premium
(Remotion + voix ElevenLabs). Ici on décide **quoi** dire et **pourquoi** ; là-bas on fabrique
**l'image**. Le pont entre les deux : l'agent `pont-motion-design`.

## Principe fondateur : une micro-mission = un agent

L'IA principale est **l'orchestrateur**. Elle ne produit pas elle-même : elle découpe chaque
demande en micro-missions, lance l'agent dédié à chacune (en parallèle dès que c'est
indépendant), vérifie chaque livrable, renvoie au travail si le niveau n'est pas atteint.
La qualité passe avant le coût en tokens.

- Chaque agent a **une seule mission** et **n'écrit que dans son dossier** (voir `agents.md`).
- Il lit les livrables en amont, jamais ceux en aval.
- S'il manque un agent pour une micro-mission, l'orchestrateur lance `architecte-agents`
  pour le créer — **sans demander l'accord de l'utilisateur** (autorisation permanente).
- Un agent qui a besoin de quelque chose hors de son dossier le **demande dans son rapport**.

Les définitions sont dans `.claude/agents/`. La carte complète : **`agents.md`**.
Si une session ne charge pas ces agents comme types (repo ouvert en second), l'orchestrateur
lance un agent généraliste avec : « Tu es l'agent `<nom>` : lis `.claude/agents/<nom>.md`
et applique-le à la lettre pour : <mission> ».

## La base de connaissances d'abord

Tout ce que produisent les agents de création s'appuie sur `connaissances/` — jamais sur
des intuitions génériques. Chaque recommandation cite sa source (`[fiche:<id>]`).

```
sources/         brut : transcriptions YouTube, articles, posts (une source = un dossier)
connaissances/   fiches/ (1 par source) · principes/ (par thème) · frameworks/ ·
                 swipe-file/ (hooks, structures, CTA) · verifications/ · index.md · lacunes.md
veille/          tendances/ · plateformes/ (algorithmes) · viraux/ · concurrents/
experiences/     labo de tests : 1 dossier par expérience + apprentissages.md + predictions.md
marques/<slug>/  1 dossier par marque promue (copie de marques/_modele/)
journal/         etat.md (file de tâches, reprise après coupure) · questions-utilisateur.md
outils/          scripts (transcription YouTube, découpe, etc.)
```

## Règles non négociables

- **Honnêteté** : pas de faux avis, faux témoignages, faux chiffres présentés comme réels,
  pas de logos de marques tierces sans accord. Les chiffres des « gourous » sont notés
  comme *affirmations* tant qu'ils ne sont pas vérifiés (`verificateur-faits`).
- **Rien n'est publié sans validation explicite de l'utilisateur** (`publicateur`).
- **Pas de robots avec mots de passe** : publication via API officielles ou outils de
  programmation, jamais d'automatisation qui se connecte avec les identifiants.
- **Secrets** (clés API) : jamais dans le repo — variables d'environnement uniquement.
- **Vidéos/audios** : jamais commités (le code et les scripts sont la source de vérité).
- Pour les contenus du studio Sillage : **jamais de musique** (effets sonores oui), style
  clair, sobre, peu de texte (voir le `CLAUDE.md` de `motion-design`).

## Autonomie et reprise

- `journal/etat.md` est **toujours à jour** : ce qui est fait, en cours, à faire. Toute
  session (ou reprise programmée) commence par le lire et reprend la file.
- Commit + push après chaque étape terminée (le conteneur cloud est éphémère).
- Ce qui bloque et nécessite l'utilisateur va dans `journal/questions-utilisateur.md`
  — on continue le reste en attendant.

## Commandes

```bash
pip install yt-dlp youtube-transcript-api          # une fois
python3 outils/youtube/transcrire.py <url> [<url>…] # -> sources/youtube/<id>/
python3 outils/youtube/decouper.py <id> 15000       # -> sources/youtube/<id>/parties/
```

## Pipelines types (détail dans `agents.md`)

- **Apprendre d'une vidéo / d'un lien** : extracteur → (découpe) → analyste-transcription ×N
  → consolidateur-fiche → extracteur-hooks + extracteur-frameworks + verificateur-faits
  → synthetiseur-connaissances → cartographe-lacunes → chercheur-sources.
- **Promouvoir une marque** : analyste-marque → veilleur-concurrence → analyste-concurrent ×N
  → ecouteur-audience → architecte-persona → strategiste-positionnement → strategiste-contenu
  → planificateur-calendrier → (par post) ideateur → redacteur-hooks → critique-hook
  → scenariste-reel / redacteur-carrousel / redacteur-linkedin… → redacteur-legende
  → specialiste-seo-social → correcteur → garde-conformite → simulateur-audience
  → controleur-qualite-marketing (veto) → validation utilisateur → publicateur.
- **Apprendre de ses résultats** : predicteur-performance (avant) → analyste-performance
  (après) → analyste-resultats → mise à jour de `experiences/apprentissages.md`.
