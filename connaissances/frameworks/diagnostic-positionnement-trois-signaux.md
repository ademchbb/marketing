# Diagnostic du positionnement : les 3 signaux du premier appel, l'alignement interne et le test de l'acheteur qualifié

> Famille : positionnement · Niveau : diagnostic (avant de repositionner, et après pour valider) · Durée : 1 à 2 semaines d'écoute

## Origine
- **April Dunford** [fiche:hdjlCLb9Hl8] :
  - aucune métrique ne révèle un positionnement faible, il abîme tout le pipeline [00:09]-[00:11] ;
  - diagnostic en 3 signaux dans un premier appel de vente (framework C [00:10]-[00:11]) ;
  - le désalignement interne, cause « the majority of the time » [00:13]-[00:17] ;
  - le seul vrai test : un prospect qualifié s'enthousiasme-t-il et veut-il acheter ? [00:17] [00:19]-[00:21].
- Périmètre : B2B avec appels de vente. Transposition B2C (premiers DM, commentaires, questions d'avant-vente) = **déduction**.
- Fiabilité : 4/5 pour la méthode ; test entièrement **qualitatif**, donc invérifiable par construction.

## Problème résolu
Un positionnement faible ne se voit dans aucun tableau de bord : les gens ne réagissent pas en haut du pipeline, tout ralentit au milieu (« the light doesn't come on until they've had three calls »), et on signe sur un malentendu qui finit en churn. On ne voit le problème qu'en écoutant, et en comparant ses métriques à ses propres métriques passées.

## Étapes

### 1. Écouter les **premiers** appels (ou premiers échanges)
- Assister à 5 à 10 premiers appels de vente, ou relire les premiers échanges prospect (en B2C, déduction : premiers DM, premiers commentaires, questions avant achat). Dunford commençait chaque poste de VP marketing par « hang out with sales ».
- Question : qu'entend-on dans les 10 premières minutes, avant que le commercial n'ait « rattrapé » le discours ?

### 2. Relever les 3 signaux
| Signal | Ce que dit le prospect | Gravité |
|---|---|---|
| **Confusion** | « Could you just back up at the beginning and do that thing from the beginning? » | le plus fréquent |
| **Mauvaise catégorisation** | « I get it, you're just like Salesforce. » | **le pire** : il croit savoir, et se trompe |
| **Valeur non perçue** | « I totally get what you do. I just don't get why anyone would pay for that… I can do that in a spreadsheet. » | « terrible » |

- Questions :
  - Quel signal revient le plus ? Il indique quelle composante reprendre : confusion → catégorie et récit ; mauvaise catégorisation → catégorie ; valeur non perçue → valeur différenciée et best-fit (voir `cinq-composantes-du-positionnement.md`). (Correspondance déduite, pas formulée par Dunford.)
  - Le « spreadsheet » cité est-il dans notre colonne statu quo ?

### 3. Vérifier l'alignement interne
- Demander **séparément** au fondateur, aux ventes, au marketing et au produit : que vendons-nous, à qui, en quoi sommes-nous différents ?
- Comparer les versions : elles sont souvent « not a lot different, but a little bit different ».
- Identifier le scénario :
  - **le fondateur sait** (« put me in front of a customer, I crush it ») mais n'arrive pas à transmettre ;
  - **l'équipe sait**, et le fondateur est resté sur l'ancien marché (« we're positioned for what the market used to be »).
- Question : qui détient quel morceau de la réalité ? (Tous doivent être dans l'atelier.)

### 4. Tester un positionnement (nouveau ou existant) auprès d'acheteurs qualifiés
- Raconter le récit (voir `recit-de-vente-et-pitch-carte-du-marche.md`) à un **prospect qualifié** et observer : s'enthousiasme-t-il ? veut-il acheter ?
- Ne pas juger en lisant la page d'accueil soi-même, sauf si l'on est l'acheteur. « It's okay if your grandmother doesn't understand what it is. »
- Un excellent positionnement « feels obvious » **pour la cible** : « of course that's it » / « of course we need one of those ».
- Questions :
  - Le testeur est-il vraiment dans le best-fit ?
  - Note-t-on l'enthousiasme et l'envie d'acheter, pas la politesse ?

### 5. Consigner et décider
- Consigner les répliques mot pour mot, le signal, le profil du prospect. Pour l'agence (déduction) : `simulateur-audience` simule l'**acheteur qualifié** (jamais « le grand public ») et les réactions réelles sont versées dans `experiences/`.
- Décider : repositionner (atelier complet) ou seulement réaligner l'équipe sur un positionnement correct.

## Exemple appliqué (illustratif : Sillage)
- Écoute de 6 premiers échanges avec des fondateurs (DM LinkedIn, appels découverte).
- Répliques relevées (hypothétiques) : « Donc vous faites des pubs animées ? » (mauvaise catégorisation : « vidéo de lancement » perçu comme « pub ») ; « On peut faire ça sur Canva, non ? » (valeur non perçue, statu quo = outil de templates).
- Alignement : le fondateur parle de « moment de lancement », le site parle de « motion design premium ». Écart à traiter en atelier.
- Test : le récit révisé est raconté à 5 fondateurs SaaS en pré-lancement ; on note qui demande un devis.

## Erreurs fréquentes
- Chercher le problème dans les métriques au lieu de l'écouter.
- Écouter des appels tardifs, où le commercial a déjà compensé.
- Tester sur l'équipe, la famille ou « les grands-mères » (contre-exemple : le concours « pitch the grandmas » de Startupfest).
- Repositionner sans avoir vérifié l'alignement interne (souvent, la bonne version existe déjà chez quelqu'un).
- Présenter le résultat d'un test qualitatif comme une mesure.

## Agents qui doivent l'utiliser
`strategiste-positionnement` (propriétaire), `analyste-marque` (comparer site, réseaux et discours du fondateur), `ecouteur-audience` et `gestionnaire-communaute` (répliques des premiers DM et commentaires), `simulateur-audience` (jouer l'acheteur qualifié), `critique-hook` (même règle : juger comme la cible, pas comme le grand public), `concepteur-experiences`.

## Voir aussi
`cinq-composantes-du-positionnement.md` · `recit-de-vente-et-pitch-carte-du-marche.md` · `delivery-et-destinataire-unique.md`
