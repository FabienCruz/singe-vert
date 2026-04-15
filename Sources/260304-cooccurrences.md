---
description: Article de blog, humanités numériques, notion de co-occurrences
thème: Humanités numériques
date: 2026-03-04
---

# Comprendre un mot à partir de ceux qui l'entourent

Les intentions des auteurs qui écrivent "sa majesté le roi" et "à mort le roi !" sont évidemment différentes.
Comment appréhender ces variations avec un outil d'analyse automatique ? Les Humanités numériques utilisent la notion de _cooccurrences_: avec quels autres mots un mot est-il utilisé ? Dans nos exemples : "majesté" et "mort" sont des cooccurrences du _mot-pivot_ "roi". 

L'exercice consiste à prendre deux textes, réunis dans un _corpus_[^1], utilisant un même mot mais dans des contextes différents et de voir ce que les co-occurences révèlent.

Notre corpus est constitué [^2] d'une lettre de Thomas Jefferson, [ici la version complète en anglais](https://founders.archives.gov/documents/Jefferson/01-15-02-0277) qui rapporte les évènements de juillet 1789 en France où il était ambassadeur, un point de vue plutôt pro-révolutionnaire, et du [manifeste du duc de Brunswick](https://gallica.bnf.fr/ark:/12148/btv1b6948324w) attribué au chef des armées autrichiennes et prussiennes et qui menaçait en juillet 1792 les parisiens en cas de manifestations contre le roi et sa famille, un texte contre-révolutionnaire.

Deux modalités de co-occurrences ont été testées [^3]:

1. **Le "mot-clé en contexte"** (_Key Word In Context_ et l'acronyme _KWIC_). Il s'agit de repérer le mot pivot dans le texte puis d'extraire la phrase.
2. **Le comptage des cooccurences**. Le mot-pivot est isolé. Les mots qui l'entourent, dans une fenêtre de quelques mots, sont regroupés puis dénombrés.

Par exemple avec le manifeste de Brunswick, pour le mot-pivot "roi", 

La première modalité, le KWIC, produit ce type de résultat:

-  "légitime exercé contre la personne sacrée du [roi] et contre son auguste famille des attentats"

et la seconde, le comptage des co-occurences :

- roi : 14 apparitions dans le texte
- empereur  :  5 occurrences
- prusse  :  5
- majesté  :  5
- france  :  4

Bien que les morceaux de phrases extraites par la méthode du KWIC soient très lisibles, elle n'apporte pas plus qu'un simple surlignage. Avec notre extraction, on perd même l'information de sa place dans le texte: est-ce que le mot "roi" apparaît tout au long du texte, plutôt au début, à la fin ? Si on l'améliore, cette technique ouvre à une analyse visuelle du texte: surligner, colorer, zoomer, dé-zoomer. Sur des volumes importants, cette méthode sera certainement limitée.

**Le comptage des cooccurrences fait bien apparaître les thématiques et la tonalité des textes**, même sur des extraits aussi courts. Le texte de Thomas Jefferson entoure le roi de "cris", "populaires" et de "nation", c'est la prise de la Bastille et le port de la cocarde par le roi à l'Hôtel de Ville qui sont racontés, et celui du Duc de Brunswick parle autorité avec "majesté", "ordre", "légitime" mêlée de crainte avec la "violence", "contre", la "famille", "royale".

Cette technique du comptage de co-occurrence sera, au final, plus intéressante avec du volume. Il faut que le mot-pivot soit utilisé de nombreuses fois. Plus les mots ou expressions co-occurrents sont fréquents, plus le contexte devient apparent et significatif. Son avantage est aussi de pouvoir faire des comparaisons : selon l'auteur, selon le moment. Un mot apparaît avec un contexte pour l'un  et un différent pour l'autre.

La prochaine étape consistera à sophistiquer le dispositif en travaillant sur les flexions d'un mot (roi / rois / royal) et sa _lemmatisation_ pour le ramener à sa racine.

---

## Annexe : comptage des cooccurrences

Seules les cooccurrences avec plus de deux apparitions sont listées.

Cooccurrences dans le texte de Thomas Jefferson

pivot : roi
nb apparitions : 11
vive  :  6
troupes  :  4
cris  :  4
nation  :  4
jour  :  2
chapitre  :  2
changement  :  2
paris  :  2
seul  :  2
entendu  :  2
descendit  :  2
hôtel  :  2
ville  :  2
là  :  2
monsieur  :  2
bailly  :  2
présenta  :  2
prononça  :  2
jusqu  :  2
audience  :  2
venait  :  2
retour  :  2
populaires  :  2
raccompagné  :  2

Cooccurrences avec le Manifeste de Brunswick 

pivot : roi
nb apparitions : 14
empereur  :  5
prusse  :  5
majesté  :  5
majestés  :  4
france  :  4
fait  :  3
contre  :  3
famille  :  3
soumettre  :  3
moindre  :  3
armées  :  2
combinées  :  2
adressée  :  2
habitants  :  2
ll  :  2
mm  :  2
ordre  :  2
gouvernement  :  2
légitime  :  2
sûreté  :  2
liberté  :  2
mettre  :  2
sans  :  2
délai  :  2
reine  :  2
royale  :  2
bourgs  :  2
villages  :  2
insulté  :  2
violence  :  2


[^1]: La constitution de corpus est un enjeu en soi. Il n'est pas celui de notre exercice. Ce dernier se centre uniquement sur la notion de co-occurrence.
[^2]: J'utilise des versions numérisés des textes données en cours de licence sur la Révolution française. Les textes sont modifiés pour des raisons pédagogiques. Principalement la lettre de Jefferson est traduite en français et raccourcie.
[^3]: Un aspect trivial mais consommateur d'énergie : l'ordinateur ne comprend pas ce qu'il lit. Il ne fait que capturer un ensemble de trois lettres : r + o + i ,et cela aussi bien dans "[roi]" que dans "t[roi]s".
