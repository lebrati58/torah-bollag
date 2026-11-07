# Spécification des fiches (encyclopédie Bereshit pour enfants 6-10 ans)

Lis d'abord : `data/personnages.json` (fiches DÉJÀ écrites pour ‘Hayé Sarah : c'est le modèle exact de ton et de format) et `data/_work/skeleton.json` (liste des personnages, relations familiales, dates : ils sont FIXÉS, ne les change pas, ne les répète pas).

Tu écris UN fichier JSON `data/_work/<GROUPE>.json` : un objet dont les clés sont les id des personnages de ton groupe.

Pour un personnage "full" :
```
"id": {
  "bio": {"he": "...", "fr": "..."},           // 4-5 phrases, racontées comme une histoire, hébreu AVEC NIKOUD COMPLET
  "events": [ {"am": 1656 ou null, "datesrc": "torah"|"midrash", "ref": "Genesis.7.11", "parasha": "noach", "he": "...", "fr": "..."} ],  // 3-6 moments, dans l'ordre
  "lessons": [ {"src": "torah"|"midrash"|"adaptation", "ref": "Genesis.x.y", "source": {"he":"רש״י בראשית ז׳:א׳","fr":"Rachi sur Gn 7,1"} (seulement si midrash), "he": "...", "fr": "..."} ],  // 2-3
  "quiz": [ {"q":{"he","fr"}, "options":[{"he","fr"},{"he","fr"},{"he","fr"}], "answer": 0|1|2, "ref": "Genesis.x.y", "src":"midrash" (seulement si la réponse vient de Rachi)} ],  // EXACTEMENT 5, bonne réponse à des positions variées
  "notes": [ {"key":"nameNote"|"identityNote"|"parentsNote", "src":"torah"|"midrash", "source":{...}?, "ref":"..."?, "he":"...", "fr":"..."} ],  // optionnel : nom non donné par le texte, identification par Rachi, parents non nommés…
  "historical": {"he": "...", "fr": "..."}       // "Non datable." / "לֹא נִתָּן לְתַאֲרֵךְ." sauf rare proposition savante, marquée débattue
}
```
Pour un personnage "link" : seulement `"bio"` (1-2 phrases) et, si utile, `"events"` (1-2) et `"notes"`.

Pour un personnage déjà présent dans `data/personnages.json` (groupe B surtout) : écris `"addEvents"` et, si utile, `"addLessons"` (1 maximum) pour les AUTRES parachiot que ‘Hayé Sarah, et `"bio"` seulement si la bio actuelle doit couvrir toute sa vie (réécris-la alors entièrement, 5-6 phrases). Ne touche pas au quiz existant.

## Règles absolues
- Ne jamais inventer : chaque fait porte un verset exact (format Sefaria `Genesis.24.10` ou `Genesis.24.10-12`). Vérifie les versets sur Sefaria (WebFetch https://www.sefaria.org/api/texts/Genesis.7.11?context=0 et Rachi https://www.sefaria.org/api/texts/Rashi_on_Genesis.7.1 ) dès que tu as le moindre doute.
- `src:"torah"` = explicite dans le verset. Ce qui vient de Rachi/Midrash = `src:"midrash"` avec la source exacte. Choix d'illustration = `adaptation`.
- Dates `am` (années depuis la création, chronologie Seder Olam) seulement si elles se déduisent des âges du texte (ex. déluge 1656, Noa’h 600 ans) ; datesrc "torah" si calcul direct depuis les versets, "midrash" si Seder Olam/Rachi. Sinon null.
- Jamais de représentation de Dieu ; parler de « ה׳ » / « Dieu » sans le décrire.
- Sujets délicats (Kaïn et Hével, Sodome, Dina, Tamar, la femme de Potifar, Èr et Onan) : version très douce, non détaillée, adaptée à des enfants de 6-10 ans, sans rien de sexuel ni de violent en détail.
- Hébreu simple avec nikoud complet et correct (attention aux בומ״ף : וּ, aux accords nombre/genre). Français simple.
- Yossef Bollag n'apparaît jamais.
- Termine par un message court : liste des id écrits + points incertains.
