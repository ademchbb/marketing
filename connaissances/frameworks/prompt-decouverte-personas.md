# Découverte de personas par IA à partir des avis — **version de l'agence** (le prompt de Denney n'est pas disponible)

> Famille : recherche client · Niveau : livrable 5 de la SOP de stratégie créative
> **Avertissement** : Dara Denney utilise un prompt maison **non transcrit** (montré à l'écran seulement). Le prompt ci-dessous est **notre propre version**, écrite à partir des entrées, de la sortie et des critères qu'elle décrit. Ce n'est **pas** son prompt et il n'a **aucun résultat mesuré** : à évaluer dans `experiences/` avant d'en faire un standard.

## Origine
- **Dara Denney** [fiche:yRgPbqywUJ8], framework E [09:14]-[09:47] [18:40] :
  - entrées : CSV des avis + analyse de réputation + PDF interne (contenu non précisé) + prompt maison ;
  - sortie : un deck de personas, revu **en équipe** ;
  - but : trouver des personas **nouveaux** (« net new audiences ») ;
  - classement par **intensité émotionnelle** du langage et **fréquence** d'apparition ;
  - confrontation au compte publicitaire (persona gap, voir `audit-des-lacunes-du-compte-pub.md`).
- Signal complémentaire : les clients « hors cible » satisfaits (« pas pour moi, et pourtant ») signalent un nouveau persona [19:44].
- Fiabilité : méthode décrite 3/5 ; **le prompt ci-dessous n'a pas de fiabilité établie** (création de l'agence).

## Problème résolu
Les personas sont souvent inventés ou copiés du brief marketing de la marque. Ici on les **fait émerger des mots des clients**, on les classe par opportunité, et on repère ceux que la marque n'a jamais ciblés.

## Étapes

### 1. Rassembler les entrées
- Export des avis (CSV) + feuille de minage + analyse de réputation + analyse IA des avis (voir `analyse-de-reputation-et-minage-d-avis.md`).
- Optionnel : brief de marque (`marques/<slug>/01-brief/`).
- Question : les verbatims ont-ils tous leur source ? Les données personnelles des auteurs d'avis sont-elles retirées (pas de noms complets dans les fichiers de travail) ?

### 2. Lancer le prompt (version agence)
```
Rôle : tu es analyste en recherche client. Tu travailles UNIQUEMENT à partir des documents fournis.
Documents : [avis.csv], [analyse-reputation.md], [analyse-ia-avis.md], [brief-marque.md facultatif].

Tâche :
1. Regroupe les auteurs d'avis en 4 à 8 personas distincts selon : la situation qui les a amenés
   au produit, le problème principal, le résultat recherché, les objections exprimées, le déclencheur
   d'achat.
2. Pour chaque persona, donne :
   - un nom descriptif (situation + besoin, pas un prénom fictif) ;
   - 3 à 5 verbatims EXACTS copiés des avis, avec leur numéro de ligne ;
   - la fréquence : nombre d'avis qui lui correspondent (et le pourcentage du total) ;
   - l'intensité émotionnelle du langage, de 1 à 5, justifiée par les verbatims ;
   - les objections et les déclencheurs d'achat propres à ce persona ;
   - 2 à 3 angles « piliers » possibles (grandes douleurs ou désirs, pas des concepts de pub).
3. Signale séparément les clients « hors cible » satisfaits (« je pensais que ce n'était pas pour moi,
   et pourtant… ») : ce sont des candidats à un nouveau persona.
4. Classe les personas par opportunité = fréquence × intensité, et indique pour chacun s'il apparaît
   dans le brief de marque (oui / non / partiellement).

Contraintes :
- N'invente aucun verbatim, aucun chiffre, aucun attribut démographique absent des avis. Si une
  information manque, écris « non indiqué ».
- Ne déduis aucune donnée de santé, d'origine, de religion ou d'orientation à partir d'indices.
- Sépare clairement ce qui est observé (verbatims) de ce qui est interprété.
```

### 3. Revoir en équipe (ou par `architecte-persona` + `controleur-qualite-marketing`)
- Vérifier chaque verbatim dans le fichier source (l'IA peut reformuler).
- Fusionner les personas trop proches, rejeter ceux qui reposent sur 1 ou 2 avis.
- Questions :
  - Ce persona est-il **ciblable** (plateforme, intérêt, contexte) ou seulement descriptible ?
  - Le classement fréquence × intensité est-il cohérent avec ce qu'on a lu ?

### 4. Confronter au compte publicitaire et à la stratégie
Remplir la grille du persona gap (voir `audit-des-lacunes-du-compte-pub.md`) : personas absents, personas sur-représentés face à une plus grosse opportunité.

### 5. Consigner et évaluer le prompt
Noter dans `experiences/` la version du prompt, la marque, et ce que l'équipe a dû corriger. Améliorer le prompt d'une version à l'autre.

## Exemple appliqué (illustratif, hypothétique)
Marque de porridge prêt à boire : le prompt sort 5 personas ; « actifs pressés le matin » (fréquence 38 %, intensité 2) et « rassasiement jusqu'au déjeuner » (fréquence 21 %, intensité 4). Le second est absent du brief et de toutes les créas actives → candidat prioritaire (même logique que l'observation de Denney sur Oats Overnight, qui reste une **proposition d'audit**).

## Erreurs fréquentes
- Utiliser le deck IA sans relecture humaine.
- Laisser l'IA inventer des attributs démographiques ou de santé.
- Classer par fréquence seule (on rate les personas à forte émotion).
- Présenter ce prompt comme « le prompt de Dara Denney ».
- Cibler explicitement un attribut de santé dans une pub (règles Meta sur les attributs personnels : voir `garde-conformite`).

## Agents qui doivent l'utiliser
`architecte-persona` (propriétaire), `ecouteur-audience` (entrées), `strategiste-ads`, `strategiste-positionnement`, `controleur-qualite-marketing` (relecture du deck), `concepteur-experiences` et `analyste-resultats` (évaluer le prompt), `garde-conformite`.

## Voir aussi
`analyse-de-reputation-et-minage-d-avis.md` · `audit-des-lacunes-du-compte-pub.md` · `sop-strategie-creative.md` · `cinq-composantes-du-positionnement.md` (en B2B, le best-fit se définit par des critères de compte)
