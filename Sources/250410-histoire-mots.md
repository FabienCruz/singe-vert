---
description: Compte-rendu du livre Histoire de mots
thème: Lexicométrie
date: 2025-04-10
---
#  _Histoires de mots_, usages de la lexicométrie en histoire


L'ouvrage collectif[^1] dirigé par Léo Dumont, Octave Julien et Stéphane Lamassé propose une immersion dans l’atelier de l’historien à l’ère numérique. Issu du travail d’une nouvelle génération d’universitaires, il s’intéresse à l’usage de la lexicométrie en histoire.

Le recueil présente des limites : des techniques peu variées et anciennes malgré l’essor actuel des _data sciences_; une ouverture limitée au-delà du cadre universitaire français; et un langage parfois abscons, mêlant vocabulaire informatique et jargon des sciences sociales. Ni manuel ni manifeste, il pourrait passer pour une simple collection de contributions.

Pourtant, il se révèle précieux grâce à ses retours d'expérience et ses réflexions méthodologiques. Ainsi pose-t-il des questions fondamentales: 
- À quelles conditions la lexicométrie enrichit-elle la pratique historienne ? 
- Comment la numérisation transforme-t-elle le rapport aux sources ? 
- Quelle place les méthodes quantitatives ont-elles dans l’historiographie actuelle française ?

Nous verrons d'abord comment les historiens fabriquent leurs sources numériques, et avec quelles contraintes. Ensuite, quelles analyses permet la lexicométrie, mais aussi quelles en sont les limites. Enfin, nous situerons ces méthodes quantitatives dans l'historiographie française contemporaine, entre héritage ancien et renouveau numérique hésitant.



La lexicométrie et le contexte numérique nécessitent des conditions précises pour être efficaces. Il convient de bien les vérifier avant de se lancer dans ce type de travaux.

Tous les contributeurs s'accordent sur un point : **la volumétrie** est un critère déterminant dans le choix d'une approche lexicométrique. Dans _1789: les mots d'un mythe_, Pascal Marchand et Pierre Ratinaud illustrent cette dimension avec le dépouillement des discours de l'Assemblée nationale entre 1789 et 1794: 82 volumes d'environ 800 pages chacun. Face à une telle masse documentaire, l'approche quantitative offre des possibilités d'exploration difficilement accessibles à une lecture traditionnelle.

Deuxième condition, les textes doivent être au **format numérique**, avec deux possibilités. Soit ce sont des documents papier qui sont numérisés, "océrisés" dans le jargon (de l'acronyme anglais OCR, _Optical Character Recognition_); soit des documents nativement numériques, par exemple des sites web ou des messages échangés sur réseaux sociaux. Le travail de numérisation est généralement effectué par des institutions disposant des moyens nécessaires. 

**Les données nativement numériques sont très volatiles**: souvent modifiées et vite supprimées. La traçabilité des sources et la reproductibilité de la recherche sont alors de véritables défis. 

Troisième condition, les textes numérisés ne sont pas exploitables en l'état. **Des traitements** sont encore nécessaires, notamment leur mise au format TEI (Text Encoding Initiative), pour qu'ils puissent être analysés par les logiciels de lexicométrie. L'article _Du nettoyage des données à la critique des sources_ de Max Beligné, Sabine Loudcher et Isabelle Lefort détaille ce processus et ses implications.

Enfin l'utilisation de textes numérisés et la lexicométrie requièrent une diversité de **compétences** à réunir : informatique, statistiques, linguistique, archivistique, histoire. 
**La charge de travail préparatoire est importante** au final et interroge la pertinence même de l’usage de la lexicométrie dans certaines recherches. 

Ce coût doit être mis au regard des bénéfices attendus.



La lexicométrie classe automatiquement certains groupes de mots dans un corpus et les positionne au fil du temps. Elle facilite ainsi l'identification de ruptures ou de continuités dans les discours.

**L'automatisation du processus n'efface pas le chercheur, bien au contraire.**

La **notion de "co-occurrence"** est centrale pour en comprendre le fonctionnement. Il s'agit d'identifier des grappes de mots utilisés ensemble. 

Par exemple, Hugo Bonin, dans _Histoire des idées politiques et « tournant numérique »_, montre que le mot _democracy_ évolue selon ses contextes de co-occurrents. 
En **1790**, au Royaume-Uni, avec la Révolution française en toile de fond, il est généralement connoté négativement: il est associé à des termes comme "sanglant" ou "tyrannique", dans des réflexions sur le régime idéal.
En **1832**, lors de débats sur l'élargissement du vote dans le cadre du _Reform Act_, il glisse peu à peu pour désigner les classes populaires, utilisé en contraste de _aristocratic_. Son usage négatif devient alors le seul fait des conservateurs.

"L'inflation documentaire et archivistique" est devenue exponentielle avec internet. Ce contexte de "données massives" rend l'automatisation nécessaire.  

 Dans  _Si loin, si proche : histoire, mémoire et lecture distante à l’ère des données massives_, Frédéric Clavert étudie les messages échangés en 2018 sur Twitter concernant les commémorations de la Grande Guerre. 

Comme la plupart des autres contributeurs, il fait référence au concept de "lecture distante" du professeur de littérature Franco Moretti qui parle aussi de **"géographie littéraire"**. L'analyse quantitative dresse des "cartes" qui révèlent des structures souvent invisibles à l’œil nu, comme la géographie le faisait pour Ferdinand Braudel.

La contribution de Magali Guaresi, _Logométrie et deep learning_, illustre cette idée et se distingue par l’utilisation de l’apprentissage supervisé. Elle entraîne un modèle de machine learning à repérer l’orientation politique de discours à partir des professions de foi législatives remontant jusqu'à 1958. 

Bien qu'il dépasse 80 % de précision lorsqu'il est mis face aux discours des élections de 2017, il classe à droite un discours de Mathilde Panot soutenant la candidature de Jean-Luc Mélenchon. 

Cette anomalie met en évidence un usage croissant d’un schéma langagier typique de la droite ("je+pronom+verbe" par exemple “je vous demande”) par la gauche. Ce glissement témoigne d’une **uniformisation du discours politique**, marquée par la mise en avant du leader, tous bords confondus.



Ces classifications automatiques peuvent donc être d'une grande aide pour les chercheurs qui font face à des corpus importants. Mais les contributeurs en soulignent aussi les limites.

La principale : **les acteurs disparaissent**, par l'écrasement des textes en un corpus unique. **Leurs intentions, les jeux d'influence, les alliances et les oppositions ne ressortent pas.** Alors qu'à l'Assemblée nationale en septembre 1792, les parlementaires débattaient de "Louis XVI" et de ses" crimes", les outils n'identifient ni partisans ni opposants. Ne comprenant pas les intentions, un texte ironique peut aussi se retrouver compté dans le mauvais ensemble. 

**L'oeil et le tour de main du chercheur sont donc essentiels.** 

Ainsi peut-il **noter des silences**. Dans _Les anciens combattants et la rhétorique de la Révolution nationale_, Anne-Sophie Anglaret analyse des journaux de propagande vichyste et note l'absence quasi totale de mention à l'Allemagne et à l'Occupation.

Autre apport du regard humain: **identifier les anomalies et les irrégularités**, relever des écarts face à des attendus.  En étudiant le magazine nazi Signal (1940-1945), Claire Aslangul, Anatole Lucet et Adrien Barbaresi s’attendent à y retrouver les traits de la “Langue du Troisième Reich” décrite par Viktor Klemperer. Leur absence les amènent alors à poser des hypothèses pour une lecture plus approfondie.



Aucune contribution n'oppose méthode quantitative à méthode qualitative. La plupart appellent à **des allers-retours entre lecture distante et lecture rapprochée**. En sociologie ou en géographie, on parle naturellement de confronter les chiffres au "terrain". Mais, comme si elle n'allait pas de soi, les historiens rappellent sans cesse dans ce livre la nécessaire complémentarité des approches.

Pourquoi  cette insistance ? Il faut sans doute y voir **l'héritage traumatisant de l'histoire quantitative** des années 1960 - 1970. Cette histoire a été critiquée jusqu'à la caricature: elle était envoutée par le scientisme des chiffres et des graphiques, mue par l'effet magique de rendre visible des structures invisibles. Emportée par la volonté de domination des sciences sociales, à une époque où les historiens étaient aussi des personnalités médiatiques, la chute fût plus lourde. Bien que la lexicométrie ne porte pas ces excès de l'histoire quantitative qui s'intéressait davantage à l'économie et à la démographie, elle a été emportée par le flot de la critique des chiffres et des études de données massives.

Cette méfiance contribue peut-être à expliquer un autre aspect : si l’intérêt pour l’informatique en histoire est ancien, les méthodes majoritairement utilisées dans l'ouvrage datent souvent des années 1980.

Frédéric Clavert cite un article datant de 1959 où François Furet et Adeline Daumard montraient déjà un intérêt pour l'usage de l'informatique dans le domaine historique. 
Or, **la plupart des articles de ce livre de 2023 utilisent la méthode Reinert qui a plus de quarante ans**. Seule parmi la douzaine de contributions, Magali Guaresi s'essaie à des techniques plus récentes de _Machine learning_. Les techniques semblent se développer ailleurs: en linguistique, littérature, informatique, voire en marketing. 



Au final, ce recueil montre moins l'amorce d'un tournant numérique en histoire que l’hésitation encore palpable de la discipline. La méfiance issue de l'héritage de l’histoire quantitative apparaît encore dans les discours. Reste à savoir combien de temps les historiens continueront d'observer ces outils à distance avant de les investir réellement.

[^1]: Dumont, Léo, Octave Julien, et Stéphane Lamassé, éd. _Histoires de mots_. Paris: Éditions de la Sorbonne, 2023. (version en ligne - open book: https://doi.org/10.4000/12wwq.)