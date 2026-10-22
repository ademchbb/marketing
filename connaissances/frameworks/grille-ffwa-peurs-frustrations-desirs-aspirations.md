# Grille FFWA (peurs, frustrations, désirs, aspirations) et « dans la peau du destinataire »

> Famille : recherche client / hooks · Niveau : générer des accroches et des angles par élément psychologique, pas « pour l'avatar en général »

## Origine
- **Alex Hormozi, *$100M Money Models*** (Q&A) [fiche:6_CCutkM11g], hooks par peurs, frustrations, désirs, aspirations, **FFWA** (framework H [04:22]-[04:24]) ; réserve sur l'IA [04:43] ; playbook, étape 15.
- **Variante, Jay Abraham** [fiche:Ge8xTCIP0Zw] : les questions de préparation d'une offre « dans la peau du destinataire » : espoirs · peurs · ce qui apaisera ces peurs · ce qui le fera se sentir spécial · ce que personne d'autre ne traite (framework N [00:35]) ; et l'ouverture « vers / loin de » : « I know what you're trying to get closer to or away from » (framework K [00:37]).
- **Variante, Daniel Priestley** [fiche:LJVP2wRk7Cc] : dans un formulaire de qualification, une question côté **« amour »** (ambition, nouveau public) et une côté **« peur »** (retard, IA) (framework G, étape 5 [00:26]).
- **Doublon fusionné** : FFWA (Hormozi), espoirs / peurs (Abraham) et amour / peur (Priestley) sont le même geste : découper la psychologie de la cible en éléments **vers** (désirs, aspirations, espoirs) et **loin de** (peurs, frustrations), et écrire pour chaque élément.
- Fiabilité : 3,5/5. Méthode simple, sans donnée de performance. Les hooks d'exemple de la source (coach en séduction) ont été **générés par IA en direct**. **Absent du registre** au 2026-10-22.

## Problème résolu
On écrit des accroches « pour l'avatar » en général, donc vagues. La grille oblige à écrire **au moins une accroche par élément psychologique précis**, et à vérifier qu'on couvre à la fois ce vers quoi la cible va et ce qu'elle fuit.

## Étapes

### 1. Définir l'avatar en profondeur
Partir du persona validé (`architecte-persona`) et des verbatims réels (`ecouteur-audience`, `analyse-de-reputation-et-minage-d-avis.md`).

### 2. Remplir la grille
| Élément | Direction | Question |
|---|---|---|
| **Peurs** | loin de | Qu'est-ce qu'elle redoute qu'il arrive ? |
| **Frustrations** | loin de | Qu'est-ce qui l'agace aujourd'hui, concrètement ? |
| **Désirs** | vers | Qu'est-ce qu'elle veut obtenir bientôt ? |
| **Aspirations** | vers | Qui veut-elle devenir ? |
| Ce qui apaisera ses peurs (Abraham) | pont | Quelle preuve, quelle garantie, quel geste la rassurerait ? |
| Ce qui la fera se sentir spéciale (Abraham) | pont | Qu'est-ce qui lui dirait « c'est pour moi » ? |
| Ce que personne d'autre ne traite (Abraham) | différenciation | Quel élément les concurrents ignorent-ils ? |

- Option IA (Hormozi) : donner l'avatar à un LLM (« assume you are this person… ») et lui faire lister chaque élément. **Réserve de l'auteur** : l'IA a « a bias for agreement » ; elle sert à **produire** et à **éclairer**, pas à trancher. Chaque élément retenu est confronté à un verbatim réel.

### 3. Écrire au moins un hook par élément
Pas « pour l'avatar », **par ligne de la grille**. Répéter pour chaque avatar.
- Formes d'exemple de la source (à adapter) : « n° 1 erreur + identité + conséquence immédiate » ; contraste compétence / blocage (« You can close million-dollar deals, but you freeze when… ») ; antithèse courte (« Smart in business, clueless in dating »).

### 4. Équilibrer vers et loin de
Vérifier qu'une campagne ne repose pas que sur la peur. Ouverture d'Abraham pour un texte long : « Je sais ce que vous ressentez. Je sais ce dont vous voulez vous rapprocher, ou vous éloigner. »

### 5. Passer au critique
Soumettre les hooks à `critique-hook` et au persona simulé (`simulateur-audience`).

### 6. Réutiliser la grille
Hormozi la réutilise pour les **fiches de poste** et les **questions d'entretien** ; Priestley pour les **questions de qualification** d'un formulaire (une « amour », une « peur »).

## Exemple appliqué (illustratif : Sillage, avatar « fondateur de startup avant un lancement »)
| Élément | Contenu (à confirmer par des verbatims) | Hook candidat |
|---|---|---|
| Peur | Lancer devant un silence total | « Le pire lancement n'est pas celui qui rate. C'est celui que personne ne remarque. » |
| Frustration | Expliquer son produit 20 fois par jour | « Si vous expliquez encore votre produit à chaque rendez-vous, il vous manque 10 secondes de vidéo. » |
| Désir | Être compris tout de suite | « Votre produit, compris avant la fin de la première phrase. » |
| Aspiration | Être vu comme une vraie entreprise | « Le jour où votre startup a l'air de ce qu'elle va devenir. » |
| Ce qui apaise | Voir avant de payer | Storyboard sous 48 h avant tout engagement |

## Erreurs fréquentes
- Une accroche « pour tout le monde ».
- Ne travailler que les peurs (campagne anxiogène).
- Prendre la liste de l'IA pour la réalité du marché.
- Oublier « ce que personne d'autre ne traite » (on écrit les mêmes accroches que les concurrents).

## Garde-fous (honnêteté et conformité)
- **Peurs** : décrire une peur **réelle** de la cible, sans l'amplifier artificiellement ni créer d'urgence fausse ([verif:OU01] dans `passe-3-droit-offres.md`).
- **Attributs sensibles** (santé, situation financière, vie amoureuse) : une pub ne doit pas affirmer ou sous-entendre la condition personnelle du lecteur (voir `objection-vers-angle.md`, étape 5) ; contrôle `garde-conformite`.
- **Verbatims** : cités fidèlement ; une reformulation de l'IA n'est jamais présentée comme une citation.

## Agents qui doivent l'utiliser
`redacteur-hooks` (propriétaire), `ecouteur-audience` (remplit la grille avec des verbatims), `architecte-persona`, `ideateur`, `redacteur-ads`, `critique-hook`, `simulateur-audience`, `strategiste-offre` (questions de qualification), `garde-conformite`.

## Voir aussi
`analyse-de-reputation-et-minage-d-avis.md` · `prompt-decouverte-personas.md` · `objection-vers-angle.md` · `echelle-de-specificite.md` · `de-la-caracteristique-au-resultat.md` · `scorecard-de-diagnostic.md`
