# Archives : contrôles de l'archiviste

> Tenu par `archiviste`. Liens `[fiche:<id>]` cassés, fichiers orphelins, doublons et écarts d'index.
> L'archiviste ne supprime ni ne corrige rien hors de son périmètre : chaque ligne nomme le propriétaire qui doit agir.

## Contrôle du 2026-10-22

### Gabarit `marques/_modele/`
- Ajouté : `emails/` (+ `.gitkeep`), pour `marques/<slug>/emails/<sequence>/` (`redacteur-newsletter`,
  `garde-conformite`, `controleur-qualite-marketing`). Les sous-dossiers variables (`<sequence>`, `<post>`) ne sont
  pas créés dans le gabarit.
- Déjà présents : `01-brief` à `10-ads`, `06-performance/donnees`, `veille/concurrents`, `commande.md`.
  Le gabarit couvre tous les dossiers `marques/<slug>/…` déclarés dans `agents.md` et `.claude/agents/`.
- Aucune marque réelle dans `marques/` (seulement `_modele/` et `index.md`).

### Index manquants
- `connaissances/index.md` **n'existe pas** (jamais créé dans l'historique git). Propriétaire : `synthetiseur-connaissances`.
  La section « Carte des fichiers » (archiviste) ne peut pas être remplie tant que le fichier n'existe pas.
- `sources/podcast/` **n'existe pas** (seul `outils/podcast/` existe). Aucune source podcast à indexer.

### `sources/index.md` (mis à jour)
- 4 sources web absentes de l'index, ajoutées : `meta-andromeda`, `google-abcd-youtube-ads`,
  `cnil-prospection-electronique`, `bpifrance-influenceur-reglementation`.
- Statuts recalculés d'après les fichiers présents :
  - `intégré` (fiche citée dans `connaissances/principes/`) : les 5 sources du lot 1.
  - `fiché` : 29 sources (lot 2, canon, PDF, web ; dont `Z2uoA3bhJT0` et `JE2_7elAcxM`, fiches arrivées pendant le contrôle).
  - partiels : `6_CCutkM11g` (notes 4/6, pas de `fiche.md`), `halbert-boron-letters` (notes 2/3, pas de `fiche.md`).
  - Les 15 autres sources restent `transcrit` (aucune note).
  - Total : 51 sources indexées, 34 `fiche.md` présentes.
- Aucune source du lot 2 ni du canon n'est encore citée dans `connaissances/principes/` : aucune n'est `intégré`.

### Liens `[fiche:<id>]`
- Aucun lien cassé : chaque identifiant cité correspond à un dossier `connaissances/fiches/<id>/` avec `fiche.md`.
  `[fiche:<id>]` dans `frameworks/index.md` et `swipe-file/*.md` est un exemple de format, pas un lien.
- Aucune citation ne vise une source sans `fiche.md` (`6_CCutkM11g`, `halbert-boron-letters`).

### Fichiers orphelins
- Aucun fichier `.md` ou `.py` orphelin trouvé (chacun est cité au moins une fois ailleurs).
- Aucune fiche sans source, aucune source sans entrée d'index (après mise à jour). Aucun média commité.

### Doublons
- Aucun doublon exact (empreintes md5 des `.md`).
- Doublon de contenu voulu : `connaissances/verifications/passe-2-publicite.md`, `passe-2-b2b.md` et `passe-2-droit.md`
  sont fusionnés dans `registre.md`, qui fait foi, mais restent en archive. Renvois encore dirigés vers les
  archives et non vers `registre.md` :
  - `connaissances/frameworks/conformite-influence-commerciale.md` l. 15 → `passe-2-droit.md` (propriétaire : `extracteur-frameworks`) ;
  - `veille/plateformes/meta-ads.md` l. 13 et 216 → `passe-2-publicite.md` (propriétaire : `veilleur-algorithmes`).
- Proximité à surveiller (pas un doublon) : `google-abcd-playbook-2022` (PDF 2022) et `google-abcd-youtube-ads`
  (article 2022) traitent du même cadre ABCD ; un seul framework (`abcd-pub-video.md`) les réunit.

### `agents.md` / `.claude/agents/`
- Cohérent : 61 agents des deux côtés, mêmes noms ; chaque `name:` correspond à son nom de fichier.

## Contrôle du 2026-10-22 (2e passage)

### Gabarit `marques/_modele/`
- Ajouté : `conditions-vente.md` (squelette vide, en-tête « PROJET, non rédigé », propriétaire `redacteur-conditions-vente`,
  validation de l'utilisateur obligatoire avant toute offre payante, jamais un avis juridique ; 9 sections vides
  reprises de `.claude/agents/redacteur-conditions-vente.md`). Pas de tiret long dans le fichier (règle [fiche:HzoQgQS8czE]).
- Le gabarit couvre désormais tous les chemins `marques/<slug>/…` déclarés dans `agents.md` et `.claude/agents/`.
- La section « Gabarit des marques » de `agents.md` ne liste pas les fichiers : aucune mise à jour nécessaire.

### `sources/index.md` (mis à jour)
- 17 sources passées à `fiché` (`fiche.md` présente) : `6_CCutkM11g`, `halbert-boron-letters`, `OgRgbar2dOQ`,
  `k834E6OTGTM`, `guZa7mQV1l0`, `DJLtwT1Z0eo`, `FN4eDk1pq6U`, `1N2XALudegQ`, `Ge8xTCIP0Zw`, `rl3SELihHqs`,
  `Br2KSsaTzUc`, `xf0Mli0LVgI`, `buAY7UtjCb4`, `IWuVEcQexWo`, `rPZG5xfN7vI`, `SUzKZfyaAK8`, `aGI7puAXf6w`.
- Bilan : 51 sources, 51 `fiche.md` ; 5 `intégré` (lot 1), 46 `fiché`. Aucune source sans fiche, aucune fiche sans
  source, aucune source hors index.
- 46 fiches ne sont citées dans aucun fichier de `connaissances/principes/` : à intégrer (propriétaire :
  `synthetiseur-connaissances`).

### Liens `[fiche:<id>]`
- Aucun lien cassé dans le repo (chaque identifiant cité a sa `fiche.md`).

### Index manquant (toujours ouvert)
- `connaissances/index.md` n'existe toujours pas. Propriétaire : `synthetiseur-connaissances`.

### `agents.md` / `.claude/agents/`
- Cohérent : 62 agents des deux côtés (ajout de `redacteur-conditions-vente`), mêmes noms.
