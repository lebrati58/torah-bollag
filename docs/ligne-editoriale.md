# Torah Bollag — bandes dessinées pour enfants

## Objectif
Adapter les enseignements de Bollag en bandes dessinées faciles à lire et à comprendre, en commençant par חיי שרה — ‘Hayé Sarah.

## Format
- Hébreu simple avec nikoud ; lecture de droite à gauche.
- Bulles courtes, vocabulaire accessible, une idée principale par case.
- Planches de six cases par défaut, à adapter au texte reçu.
- Personnages et style visuel cohérents entre les épisodes.

## Fidélité aux sources
- Lire le texte original avant toute adaptation.
- Conserver la référence du message source et sa date dans les métadonnées privées de l’épisode.
- Distinguer le récit biblique, le commentaire cité et les dialogues pédagogiques ajoutés.
- Ne pas inventer d’enseignement attribué à Bollag ni de référence.
- Vérifier le nikoud, les noms, l’ordre des cases et la lisibilité avant de finaliser.

## Classement prévu
Chaque épisode est classé par paracha puis par date : `parachiot/chaye-sarah/AAAA-MM-JJ/`.
Il comprend le texte adapté, le découpage des cases, les références et la planche illustrée.

## Suivi quotidien
Le dépôt sert à conserver les épisodes. Ce fichier ne configure à lui seul aucune automatisation de lecture Gmail ou de publication GitHub.

## Auteur et personnages — règle obligatoire
Yossef Bollag est l’auteur des enseignements, jamais un personnage du comics.
- Ne jamais le dessiner, le représenter ou introduire son avatar dans les cases.
- Ne jamais le faire intervenir comme narrateur représenté, guide ou interlocuteur des personnages.
- Ne pas mettre son nom dans les bulles ou le récit des cases.
- L’attribution à l’auteur est réservée aux crédits hors des cases ou à la présentation du site.
- Appliquer cette règle à chaque demande de génération d’images et vérifier son respect avant publication.

## Encyclopédie (encyclopedie.html) — règles pour chaque mise à jour
- Sefer Bereshit est complet dans `data/personnages.json` : 84 personnages, une fiche par personnage, un arbre généalogique par paracha (`trees[].parasha`). La source des fiches est `data/_work/` (A à D) et `data/_work/merge.py`.
- Chaque semaine (le jeudi) : mettre `week` sur la paracha du Shabbat suivant, ajouter ses épisodes, et relier les vidéos des personnages (`video`). Pour Chemot et les livres suivants, ajouter les personnages livre par livre, avec le même format et la même vérification.
- Portraits : la bibliothèque officielle est `assets/portraits.js` (et les PNG de `assets/portraits/`). Chaque personnage a UN portrait, le même dans les épisodes, les fiches, les arbres et les vidéos. Un nouveau personnage reçoit un portrait créé une seule fois dans ce style ; on ne modifie jamais un portrait existant et on ne crée jamais de second visage.
- Dates : années depuis la création en chiffres dans le JSON (`am`), affichées en lettres hébraïques ; années avant l'ère commune affichées avec un signe moins (−1813).
- Vérification : chaque fait porte un verset ; « torah » seulement si c'est explicite ; Rachi / Midrash / Targoum avec la source ; adaptation artistique signalée. Faire relire par un vérificateur indépendant avant de publier.
