import json,os
W='data/_work/'
old=json.load(open('data/personnages.json')); sk=json.load(open(W+'skeleton.json'))
OLD={c['id']:c for c in old['characters']}
G={}
for g in 'ABCD':
  f=W+g+'.json'
  if os.path.exists(f):
    for k,v in json.load(open(f)).items(): G.setdefault(k,{}).update(v)
SUM={
'bereshit':("ה׳ בּוֹרֵא אֶת הָעוֹלָם בְּשִׁשָּׁה יָמִים וְשׁוֹבֵת בַּשְּׁבִיעִי. אָדָם וְחַוָּה בְּגַן עֵדֶן, קַיִן וְהֶבֶל, וְהַדּוֹרוֹת עַד נֹחַ.","Dieu crée le monde en six jours et se repose le septième. Adam et ‘Hava au jardin d’Éden, Kaïn et Hével, puis les générations jusqu’à Noa’h."),
'noach':("נֹחַ בּוֹנֶה תֵּבָה וְנִצָּל מִן הַמַּבּוּל עִם מִשְׁפַּחְתּוֹ וְהַחַיּוֹת. אַחַר כָּךְ: הַקֶּשֶׁת, מִגְדַּל בָּבֶל וּמִשְׁפַּחַת תֶּרַח.","Noa’h construit l’arche et échappe au déluge avec sa famille et les animaux. Puis l’arc-en-ciel, la tour de Babel et la famille de Téra’h."),
'lech-lecha':("אַבְרָם יוֹצֵא לְאֶרֶץ כְּנַעַן, נִפְרָד מִלּוֹט, וּמְקַבֵּל בְּרִית מֵה׳. נוֹלַד יִשְׁמָעֵאל, וְהַשֵּׁמוֹת מִשְׁתַּנִּים לְאַבְרָהָם וּלְשָׂרָה.","Avram part pour Canaan, se sépare de Lot et reçoit l’alliance de Dieu. Yishmaël naît, et les noms deviennent Avraham et Sarah."),
'vayera':("אַבְרָהָם מְקַבֵּל אוֹרְחִים, מִתְפַּלֵּל עַל סְדוֹם, וְיִצְחָק נוֹלָד. הַפָּרָשָׁה נִגְמֶרֶת בַּעֲקֵדַת יִצְחָק.","Avraham accueille des invités, prie pour Sodome, et Yitzhak naît. La paracha se termine par la ligature d’Yitzhak."),
'chaye-sarah':None,
'toldot':("רִבְקָה יוֹלֶדֶת תְּאוֹמִים: עֵשָׂו וְיַעֲקֹב. יַעֲקֹב קוֹנֶה אֶת הַבְּכוֹרָה וּמְקַבֵּל אֶת בִּרְכַּת יִצְחָק.","Rivka donne naissance à des jumeaux, Essav et Yaakov. Yaakov achète le droit d’aînesse et reçoit la bénédiction d’Yitzhak."),
'vayetze':("יַעֲקֹב חוֹלֵם עַל סֻלָּם, עוֹבֵד אֵצֶל לָבָן וְנוֹשֵׂא אֶת לֵאָה וְאֶת רָחֵל. נוֹלָדִים לוֹ אַחַד עָשָׂר בָּנִים וּבַת.","Yaakov rêve d’une échelle, travaille chez Lavan et épouse Léa et Ra’hel. Il a onze fils et une fille."),
'vayishlach':("יַעֲקֹב נֶאֱבָק עִם מַלְאָךְ וּמְקַבֵּל אֶת הַשֵּׁם יִשְׂרָאֵל, וְנִפְגָּשׁ עִם עֵשָׂו. בִּנְיָמִין נוֹלָד וְרָחֵל נִפְטֶרֶת.","Yaakov lutte avec un ange, reçoit le nom d’Israël et retrouve Essav. Binyamin naît et Ra’hel meurt."),
'vayeshev':("יוֹסֵף חוֹלֵם חֲלוֹמוֹת, וְהָאַחִים מוֹכְרִים אוֹתוֹ. בְּמִצְרַיִם הוּא מַגִּיעַ לְבֵית פּוֹטִיפַר וְאַחַר כָּךְ לַכֶּלֶא.","Yossef fait des rêves et ses frères le vendent. En Égypte, il arrive chez Potifar puis en prison."),
'miketz':("יוֹסֵף פּוֹתֵר אֶת חֲלוֹמוֹת פַּרְעֹה וְנַעֲשֶׂה מִשְׁנֶה לַמֶּלֶךְ. הָאַחִים יוֹרְדִים לִקְנוֹת אֹכֶל וְלֹא מַכִּירִים אוֹתוֹ.","Yossef explique les rêves de Pharaon et devient vice-roi. Ses frères viennent acheter de la nourriture sans le reconnaître."),
'vayigash':("יְהוּדָה מְדַבֵּר בְּאֹמֶץ עַל בִּנְיָמִין, וְיוֹסֵף מִתְגַּלֶּה לְאֶחָיו. יַעֲקֹב וְכָל מִשְׁפַּחְתּוֹ יוֹרְדִים לְמִצְרַיִם.","Yehouda parle avec courage pour Binyamin, et Yossef se fait reconnaître. Yaakov et toute sa famille descendent en Égypte."),
'vayechi':("יַעֲקֹב מְבָרֵךְ אֶת אֶפְרַיִם וּמְנַשֶּׁה וְאֶת שְׁנֵים עָשָׂר בָּנָיו, וְנִפְטָר. יוֹסֵף מְבַקֵּשׁ שֶׁיַּעֲלוּ אֶת עַצְמוֹתָיו לָאָרֶץ.","Yaakov bénit Efraïm et Ménaché puis ses douze fils, et meurt. Yossef demande qu’on remonte ses ossements en Israël.")}
OP={p['id']:p for p in old['parachiot']}
parachiot=[]
for p in sk['parachiot']:
  if p['id'] in OP: q=OP[p['id']]
  else:
    q={"id":p['id'],"order":p['order'],"book":{"he":"בְּרֵאשִׁית","fr":"Bereshit"},"he":p['he'],"fr":p['fr'],"ref":{"he":p['refHe'],"fr":p['refFr'],"sefaria":p['sefaria']},"episodes":p['episodes'],"summary":{"he":SUM[p['id']][0],"fr":SUM[p['id']][1]}}
  parachiot.append(q)
chars=[]
for s in sk['characters']:
  i=s['id']; c=OLD.get(i,{}).copy(); g=G.get(i,{})
  c['id']=i
  for k in ['he','fr','status','parachiot']: c[k]=s[k]
  if OLD.get(i,{}).get('status')=='full': c['status']='full'
  c['portrait']=i
  # relations: skeleton authoritative, keep existing refs where same id
  for rel in ['parents','spouses','siblings']:
    ex={x['id']:x for x in OLD.get(i,{}).get(rel,[])}
    sx=s.get(rel,[]); c[rel]=[ex.get(x['id'],x) for x in sx]+[x for k,x in ex.items() if k not in {y['id'] for y in sx}]
    if not c[rel]: c.pop(rel,None)
  lf=dict(s['life']); 
  if 'life' in OLD.get(i,{}) and OLD[i]['life'].get('note'): lf['note']=OLD[i]['life']['note']
  c['life']={k:v for k,v in lf.items() if v is not None} or {}
  if 'bio' in g: c['bio']=g['bio']
  for k in ['lessons','quiz','historical']:
    if k in g: c[k]=g[k]
  if 'events' in g: c['events']=g['events']
  if 'addEvents' in g: c['events']=c.get('events',[])+g['addEvents']
  if 'addLessons' in g: c['lessons']=c.get('lessons',[])+g['addLessons']
  for n in g.get('notes',[]):
    key=n.pop('key','nameNote')
    if key in c and c[key] is not OLD.get(i,{}).get(key):
      for L in ('he','fr'): c[key][L]=c[key][L]+' '+n[L]
    else: c[key]=n
  if 'otherChildren' in OLD.get(i,{}): c['otherChildren']=OLD[i]['otherChildren']
  c.setdefault('events',[]); c.setdefault('bio',{"he":"","fr":""})
  if c['status']=='full' and (len(c.get('quiz',[]))<5 or not c.get('lessons')): c['status']='link'
  c.pop('woman',None)
  chars.append(c)
# sort events by am/ref
def rk(e):
  import re
  m=re.match(r'(\w+)\.(\d+)\.(\d+)',e['ref'] or '');b={'Genesis':0,'Exodus':1,'Numbers':3,'Deuteronomy':4}
  return (b.get(m.group(1),9),int(m.group(2)),int(m.group(3))) if m else (9,0,0)
for c in chars:
  seen=set(); ev=[]
  for e in c['events']:
    if e['ref'] in seen: continue
    seen.add(e['ref']); ev.append(e)
  c['events']=sorted(ev,key=rk)
T=[
('bereshit',"מֵאָדָם עַד נֹחַ: עֲשָׂרָה דּוֹרוֹת","D’Adam à Noa’h : dix générations",[[["adam","hava"]],[["kayin"],["hevel"],["shet"]],[["enosh"]],[["kenan"]],[["mahalalel"]],[["yered"]],[["hanokh"]],[["metushelah"]],[["lemekh"]],[["noah"]]],("שֵׁת נוֹלַד ״תַּחַת הֶבֶל״ (ד׳:כ״ה). מִשֵּׁת וְעַד נֹחַ יֵשׁ עֲשָׂרָה דּוֹרוֹת מֵאָדָם (ה׳).","Chet naît « à la place d’Hével » (4,25). D’Adam à Noa’h, il y a dix générations (chapitre 5).")),
('noach',"נֹחַ וּבָנָיו, וּמִשְׁפַּחַת תֶּרַח","Noa’h, ses fils et la famille de Téra’h",[[["noah"]],[["shem"],["ham"],["yefet"]],[["kenaan"],["nimrod"]],[["terah"]],[["avraham","sarah"],["nahor","milka"],["haran"]],[["lot"]]],("בֵּין שֵׁם לְתֶרַח יֵשׁ שִׁבְעָה דּוֹרוֹת (י״א:י׳–כ״ו). נִמְרֹד הוּא נֶכֶד שֶׁל חָם (י׳:ו׳–ח׳).","Entre Chem et Téra’h il y a sept générations (11,10-26). Nimrod est un petit-fils de ‘Ham (10,6-8).")),
('lech-lecha',"מִשְׁפַּחַת אַבְרָם","La famille d’Avram",[[["terah"]],[["hagar","avraham","sarah"],["haran"]],[["yishmael"],["lot"]]],("לוֹט הוּא בֶּן אָחִיו שֶׁל אַבְרָם (י״ב:ה׳).","Lot est le neveu d’Avram (12,5).")),
('vayera',"אַבְרָהָם, לוֹט וּמִשְׁפַּחַת נָחוֹר","Avraham, Lot et la famille de Na’hor",[[["terah"]],[["hagar","avraham","sarah"],["nahor","milka"],["lot","eshet-lot"]],[["yishmael"],["yitzhak"],["betuel"]],[["rivka"]]],("בְּסוֹף הַפָּרָשָׁה נוֹלֶדֶת רִבְקָה (כ״ב:כ״ג).","À la fin de la paracha, Rivka naît (22,23).")),
('toldot',"יִצְחָק, רִבְקָה וְהַתְּאוֹמִים","Yitzhak, Rivka et les jumeaux",[[["avraham","sarah"],["betuel"]],[["yishmael"],["yitzhak","rivka"],["lavan"]],[["esav"],["yaakov"]]],("עֵשָׂו וְיַעֲקֹב הֵם תְּאוֹמִים (כ״ה:כ״ד).","Essav et Yaakov sont jumeaux (25,24).")),
('vayetze',"יַעֲקֹב, נָשָׁיו וִילָדָיו","Yaakov, ses épouses et ses enfants",[[["yitzhak","rivka"],["lavan"]],[["zilpa","lea","yaakov","rahel","bilha"]],[["reuven"],["shimon"],["levi"],["yehuda"],["issakhar"],["zevulun"],["dina"],["dan"],["naftali"],["gad"],["asher"],["yossef"]]],("בִּנְיָמִין יִוָּלֵד בְּפָרָשַׁת וַיִּשְׁלַח (ל״ה:י״ח).","Binyamin naîtra dans Vayichla’h (35,18).")),
('vayishlach',"יַעֲקֹב וְעֵשָׂו, וּבְנֵיהֶם","Yaakov, Essav et leurs enfants",[[["yitzhak","rivka"],["hamor"]],[["esav"],["lea","yaakov","rahel"],["shekhem"]],[["elifaz"],["dina"],["yossef"],["binyamin"]],[["amalek"]]],("עֲמָלֵק הוּא נֶכֶד שֶׁל עֵשָׂו (ל״ו:י״ב).","Amalek est un petit-fils d’Essav (36,12).")),
('vayeshev',"יוֹסֵף וְאֶחָיו, וּמִשְׁפַּחַת יְהוּדָה","Yossef, ses frères et la famille de Yehouda",[[["yaakov"]],[["reuven"],["yehuda"],["yossef"]],[["er","tamar"],["onan"],["shela"]],[["peretz"],["zerah"]]],("מִפֶּרֶץ תֵּצֵא מִשְׁפַּחַת דָּוִד הַמֶּלֶךְ (רוּת ד׳:י״ח–כ״ב).","De Pérets descendra le roi David (Ruth 4,18-22).")),
('miketz',"יוֹסֵף בְּמִצְרַיִם","Yossef en Égypte",[[["yaakov"]],[["shimon"],["yehuda"],["yossef","osnat"],["binyamin"]],[["menashe"],["efraim"]]],("מְנַשֶּׁה וְאֶפְרַיִם נוֹלְדוּ בְּמִצְרַיִם (מ״א:נ׳–נ״ב).","Ménaché et Efraïm sont nés en Égypte (41,50-52).")),
('vayigash',"יוֹרְדִים לְמִצְרַיִם: מִלֵּוִי עַד מֹשֶׁה וְאַהֲרֹן","La descente en Égypte : de Lévi à Moché et Aharon",[[["yaakov"]],[["levi"],["yehuda"],["asher"],["yossef"]],[["gershon"],["kehat"],["merari"],["peretz"],["zerah"],["serah"],["menashe"],["efraim"]],[["amram","yokheved"]],[["aharon"],["moshe"],["miriam"]]],("עַמְרָם, יוֹכֶבֶד, אַהֲרֹן, מֹשֶׁה וּמִרְיָם מוֹפִיעִים בְּסֵפֶר שְׁמוֹת (שמות ו׳:ט״ז–כ׳; במדבר כ״ו:נ״ט).","Amram, Yokhéved, Aharon, Moché et Myriam apparaissent dans Chemot (Ex 6,16-20 ; Nb 26,59).")),
('vayechi',"בִּרְכוֹת יַעֲקֹב","Les bénédictions de Yaakov",[[["yaakov"]],[["reuven"],["shimon"],["levi"],["yehuda"],["issakhar"],["zevulun"],["dan"],["naftali"],["gad"],["asher"],["yossef"],["binyamin"]],[["menashe"],["efraim"]]],("יַעֲקֹב מְבָרֵךְ אֶת אֶפְרַיִם לִפְנֵי מְנַשֶּׁה (מ״ח:כ׳).","Yaakov bénit Efraïm avant Ménaché (48,20).")),
]
trees=[{"id":"tree-"+p,"parasha":p,"he":he,"fr":fr,"rows":rows,"note":{"he":n[0],"fr":n[1]}} for p,he,fr,rows,n in T]+[t for t in old['trees']]
ids={c['id'] for c in chars}
for t in trees:
  for r in t['rows']:
    for g in r:
      for x in g: assert x in ids,x
for c in chars:
  for rel in ['parents','spouses','siblings']:
    for x in c.get(rel,[]): assert x['id'] in ids,(c['id'],x)
old['parachiot']=parachiot; old['characters']=chars; old['trees']=trees; old['week']='chaye-sarah'
json.dump(old,open('data/personnages.json','w'),ensure_ascii=False,indent=1)
print(len(chars),'full',sum(c['status']=='full' for c in chars),'quiz',sum(len(c.get('quiz',[])) for c in chars))
