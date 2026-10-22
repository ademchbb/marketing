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
