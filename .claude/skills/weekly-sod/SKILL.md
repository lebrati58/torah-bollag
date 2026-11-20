---
name: weekly-sod
description: Préparer chaque semaine un dossier adulte de paracha sur Zohar, Kabbale, Midrash, commentaires, guématria et éventuellement ELS, avec des citations exactes, contrôle des calculs, et ajout au site Torah Bollag.
---

# Weekly Sod — תורה וסוד לפרשת השבוע

## Objectif
Ajouter **un dossier d'étude adulte** approfondi pour une paracha dans le dépôt `lebrati58/torah-bollag`, sans modifier les BD enfants. Langue principale : hébreu soigné ; traduction française fidèle. Aucun contenu nouveau n'est attribué à Yossef Bollag sans témoignage original confirmant l'attribution.

## Entrées
- Nom de la paracha, plage de versets et date du Shabbat (déterminer si nécessaire avec calendrier juif vérifié).
- Thème(s) : Zohar, Ari, Ramhal, Ramban, Baal HaTourim, Maharal, Or HaHaïm, Sefat Emet, gematria, temoura, notarikon, milouï, ELS.
- Source vidéo/document si fournie, avec transcription exacte et repères temporels.

## Étapes obligatoires
1. Lire `docs/ligne-editoriale.md` et `data/sod/catalogue.json`. Ne jamais remplacer ou réinterpréter sans le dire les propos d'une vidéo ou d'un document.
2. Identifier **3 à 5 références primaires distinctes** par paracha (verset, commentaire et section exacte, pas seulement un titre générique). Consulter le texte primaire ou une traduction identifiée. Les « feuilles de sources » secondaires ne remplacent pas une vérification primaire.
3. Pour chaque idée, préciser son statut :
   - **SOURCE** : auteur, œuvre, chapitre/folio/segment exact et lien stable ;
   - **PARAPHRASE** : synthèse moderne fidèle, pas une citation ;
   - **CALCUL** : égalité recomptée lettre par lettre et méthode annoncée ;
   - **HYPOTHÈSE** : interprétation moderne explicitement présentée comme telle ;
   - **NON VÉRIFIÉ** : ne pas publier comme découverte confirmée.
4. Pour chaque guématria, noter exactement la graphie hébraïque (défective ou pleine), normaliser nikoud/téamim **sans changer les consonnes**, expliciter la valeur des lettres finales, le type de guématria et tout `kollel`. Ne pas introduire de `kollel` pour « sauver » un calcul sans le signaler. Comparer les sommes avec un calcul indépendant.
5. Pour chaque code ELS, noter au préalable la version de la Torah, la section, les lettres comptées, la direction, les graphies et le pas ; garder TOUS les résultats et essais. Une séquence trouvée n'implique ni intention ni signification statistique. Prévoir contrôles aléatoires et correction des comparaisons multiples avant toute affirmation probabiliste.
6. Produire le dossier au format JSON validé : `data/sod/<parasha-id>.json`, sur le modèle de `data/sod/vayetze.json`. L'ordre des `studies` doit suivre une progression de difficulté. Chaque étude dispose d'un lien source, d'une paraphrase HE/FR et d'une question analytique.
7. Ajouter l'entrée dans `data/sod/catalogue.json` (id, nom HE/FR, `ref`, fichier, `shabbat`). Ne pas écraser les dossiers précédents.
8. Vérifier `sod.html` en HE/FR : RTL, navigation, liens de sources, guématria, ELS si pertinent. Respecter la séparation absolue avec `index.html` enfants, sauf ajout de liens de navigation.
9. Contrôler la cohérence historique et philologique avant publication ; produire une courte liste des réserves et incertitudes. Si une source primaire n'est pas accessible, laisser la fiche en brouillon et ne pas présenter l'attribution comme vérifiée.
10. Committer sur branche `feature/sod-<parasha>-<year>`, ouvrir PR, vérifier les tests et fusionner seulement si l'intégration est valide et autorisée.

## Format d'une étude
```json
{
  "id": "identifiant-stable",
  "kind": "zohar|gematria|midrash|hasidout|commentary",
  "label": {"he": "כותרת", "fr": "Titre"},
  "source": "Référence bibliographique précise",
  "url": "https://www.sefaria.org/...",
  "verse": "Genesis.28.12",
  "he": "Résumé exigeant en hébreu, sans fausse citation.",
  "fr": "Résumé fidèle en français.",
  "question": {"he": "שאלת עיון?", "fr": "Question d'étude ?"}
}
```

Pour une étude numérique, joindre éventuellement `figures: [{"word":"סלם","sum":130}]` après re-calcul.

## Contrôles automatiques de base
- JSON valides, noms d'ID uniques, aucune URL vide, textes HE/FR complets.
- Sommes des `figures` recalculées à partir des consonnes.
- Pas d'affirmation « le Zohar dit » sans référence directe et passage lisible.
- Aucune attribution à une vidéo, à un enseignant ou à Bollag sans preuve explicite.

## Angle intellectuel
Le but n'est pas de collectionner des coïncidences. Les dossiers doivent explorer de vraies tensions de lecture : pshat versus sod, différentes écoles de Kabbale, contexte historique des commentateurs, raisons philologiques des choix d'orthographe, et distinction entre un symbole théologique et un test scientifique. Pour chaque section, proposer au moins une question qui appelle un raisonnement ou une comparaison de sources.

## Exécution suggérée
« Exécute le skill `weekly-sod` pour la paracha [X]. Réutilise la structure `sod.html`, vérifie les références du Zohar et des commentaires, puis soumets la mise à jour sur GitHub. »
