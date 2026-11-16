# CLAUDE.md — Torah Bollag · התורה בסרטים

Site de **bandes dessinées de Torah pour enfants**, tirées des enseignements de Yossef Bollag : 54 parachiot, en hébreu simple avec nikoud, lu de droite à gauche. Titre et bannière du site : « התורה בסרטים ». Il y a aussi une encyclopédie des personnages (frise, fiches, arbres généalogiques).

**Règles éditoriales obligatoires : [`docs/ligne-editoriale.md`](docs/ligne-editoriale.md).** Lis-les avant toute production de contenu.

## Stack
Site **statique**, sans build, hébergé sur GitHub Pages (`.nojekyll`). Pas de tests automatisés.
- `index.html` (accueil), `genesis.html`, `encyclopedie.html` (פרשת השבוע · ציר הזמן · דמויות בתורה, hébreu RTL par défaut, bouton Français).
- `data/personnages.json` est la **seule source** de la frise, des fiches et des arbres. Ses données sources sont dans `data/_work/` (A à D + `merge.py`, règles dans `SPEC.md`).
- `assets/portraits.js` et `assets/portraits/*.png` forment la bibliothèque officielle des portraits.
- `parachiot/<livre>/<nn-paracha>/<AAAA-MM-JJ>/` contient un épisode : `texte-he.md`, `BD.md` (découpage des cases), `README.md`. `episodes/<paracha>/` contient les épisodes quotidiens.

## Vérifier
```bash
python3 -m http.server 8000     # puis http://localhost:8000/encyclopedie.html
python3 -c "import json;json.load(open('data/personnages.json'))"   # le JSON doit rester valide
```
Pour les vérifications visuelles (RTL, nikoud, portraits, mobile), utilise le skill **playwright** du dépôt.

## Rythme
**Une paracha par semaine, mise à jour chaque jeudi.** Ce jour-là, mets `week` sur la paracha du Shabbat suivant, ajoute ses épisodes, relie les vidéos des personnages (champ `video`) et mets à jour le sommaire du `README.md`. L'encyclopédie de Bereshit est déjà complète. Pour Chemot et les livres suivants, les personnages s'ajoutent livre par livre, avec le même format.

## Règles absolues
- **Yossef Bollag est l'auteur, jamais un personnage.** Ne le dessine jamais, ne le fais jamais parler, ne mets jamais son nom dans une case. Son nom n'apparaît que dans les crédits.
- **Un personnage = un seul portrait**, le même partout (épisodes, fiches, arbres, vidéos). Ne modifie jamais un portrait existant. Un nouveau personnage reçoit un portrait créé une seule fois, dans le même style. Un personnage sans portrait garde une silhouette : on n'invente pas de visage.
- **Fidélité aux sources** : chaque fait porte son verset. Marque « torah » seulement si c'est explicite dans le texte. Rachi, Midrash et Targoum sont cités avec leur source. Une adaptation artistique est signalée comme telle. N'invente jamais un enseignement attribué à Bollag.
- Vérifie le nikoud, les noms et l'ordre des cases avant de publier. Fais relire par un vérificateur indépendant (un autre agent) avant toute publication.
- Dates : années depuis la création dans le JSON (`am`), affichées en lettres hébraïques. Les années avant l'ère commune s'affichent avec un signe moins (−1813).
- Travaille sur une branche avec une PR. « **yallah** » veut dire : fusionne dans `main`, puis vérifie la publication.
- Ne dis jamais qu'une chose est vérifiée si elle ne l'a pas été.
