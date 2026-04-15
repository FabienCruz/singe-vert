---
description: Article de blog, humanités numériques, lemmatisation
thème: Humanités numériques
date: 2026-03-23
---
# Le "roi" et les "rois", faut-il les distinguer ?

L'ordinateur ne sait pas lire. Pour lui, "roi" et "rois" sont deux choses complètement différentes.

Dans nos comptages de mots, notamment lorsque les volumes à traiter augmentent, regrouper les variations (les linguistes parlent de _flexions_) d'un même mot [^1] peut être nécessaire pour améliorer la lisibilité des résultats.

Les rédacteurs de dictionnaires (les lexicographes) regroupent les différentes formes d'un mot sous une seule racine, par exemple l'infinitif pour les verbes: "être" pour "est", "était", "été", "sera", etc. La forme du mot qui regroupe ses variantes s'appelle un _lemme_ et l'exercice de regroupement, la _lemmatisation_.

Nous utilisons comme corpus historique [les archives parlementaires de l'Assemblée nationale du 22 septembre au 26 octobre 1792- La Convention Nationale](https://sul-philologic.stanford.edu/philologic/archparl/navigate/52/3/) Il s'agit d'une version mise en ligne par l'Université de Stanford, numérisée à partir d'une source imprimée de la fin du XIXe siècle [^2]. Le corpus contient les débats qui entourent l'abolition de la royauté et la proclamation de la République. Il est assez volumineux, environ 700 pages.

Le corpus contient 611 877 mots.
si on enlève les mots vides ("de", "du", "le", la", etc), il reste 285 036 mots.
Le Top 5 des mots les plus fréquents:
- convention : 3642 occurrences
- nationale : 2492
- demande : 1559
- citoyens : 1493
- comité : 1387

Ce vocabulaire est cohérent avec des discours d'une assemblée à l'époque révolutionnaire, ce que l'on voit avec l'importance des mots "citoyens" et "nationale".

> **Rappel du contexte de 1792**
> 
> - 20 avril : la France déclare la guerre à l'Autriche
> - 1e août : le manifeste de Brunswick, lettre de menace aux Parisiens s'ils portent atteinte au roi.
> - 10 août : prise des Tuileries. Louis XVI et sa famille sont enfermés au Temple. Annonce de l'élection d'une convention au suffrage universel masculin.
> - 20 septembre : ouverture de la Convention nationale et bataille de Valmy

Après plusieurs défaites françaises, les troupes prussiennes et autrichiennes sont entrées sur le territoire français par le nord-est et avancent vers Paris.

Depuis septembre 1791, la France est une monarchie constitutionnelle. Aussi la Convention nationale commence-t-elle par l'abolition de la royauté et la proclamation de la république.

> **Extrait du corpus**
> 
> Grégoire.
>
>Certes, personne de nous ne proposera jamais de conserver en France la race funeste des rois; nous savons trop bien que toutes les dynasties n’ont jamais été que des races dévorantes qui ne vivaient que du sang des peuples; mais il faut pleinement rassurer les amis de la liberté; il faut détruire ce mot de roi, qui est encore un talisman dont la force magique serait propre à stupéfier bien des hommes. Je demande donc que, par une loi solennelle, vous consacriez l'abolition de la royauté.
>
>Le Président.
>
>Je mets aux voix la proposition de M. l’abbé Grégoire :
>« La Convention nationale décrète que la royauté est abolie en France. »
>(L’Assemblée décrète cette proposition à l’unanimité.)
>(Des acclamations de joie, des cris de : Vive la nation ! répétés par tous les spectateurs se prolongent pendant plusieurs instants.)

Dans ce contexte, nous regardons les mots qui entourent le lemme "roi" soit "roi" et "rois". 

Pour comprendre l'effet de la lemmatisation, nous testons deux approches:

1. avec une lemmatisation automatique d'un mot grâce à l'outil [SpaCy](https://spacy.io/) La lemmatisation s'effectue sur le mot recherché, le "mot-pivot", donc "roi" et "rois" sont recherchés indistinctement, et aussi sur le résultats : "applaudissement" regroupe le singulier "applaudissement" et le pluriel "applaudissements", ou encore, "combattre" regroupe les conjugaisons "combattons", "combattez", "combattent", etc
2. de manière séquentielle, avec un même mot pris au singulier puis au pluriel. Le comptage est effectué avec "roi" puis avec "rois". Le résultat distingue le singulier "applaudissement" et le pluriel "applaudissements".

## Résultats avec la lemmatisation automatique

Le lemme "roi" apparait 439 fois.
##### Les rois et leurs entourages :

Il est question de plusieurs rois différents : 
- (de) Prusse (69 apparitions),
- (de) Sardaigne (17)
 et aussi :
- empereur (6)
- prince (5)

dont les entourages sont visibles:
- conseiller (10)
- ministre (9)
- famille (8)
- maison (7)
- reine (4)

et des symboles:
- trône (5)
- effigie (5)
##### Le contexte de la guerre :
- troupe (14)
- combattre (10)
- guerre (9)
- détruire (5)
- camp (5)
- lieutenant (5)
- Dumouriez (5)
- militaire (4)
- traité (4)
##### Les acteurs de la révolution
- commissaire (12)
- assemblée (5)
- citoyen (4)
- émigré (4)
##### Des concepts politiques
- nation (17)
- peuple (15)
- royauté (11)
- liberté (8)
- république (6)
##### Des expression de sentiments négatifs
- haine (7)
- lâche (5)
- tyran (4)
- despotisme (4)
- luxe (4)
##### Des actes juridiques
- jurer (6)
- décret (6)
- ordre (5)
- parjure (4)
- loi (4)
- traité (4)
- captivité (4)
- serment (3)

Les thématiques sont cohérentes avec le contexte. Ces résultats sont aussi décevants. Au mieux, ils confirment ce que l'on attendait. 

Mais, aucune surprise, aucun accident. Ils ouvrent peu de nouvelles questions. Ces limites s'expliquent en partie par les caractéristiques de l'outil.

En effet, le nettoyage de mots-vides par SpaCy pose problème : "Louis" est éliminé du résultat car considéré comme mot-vide mais pas les verbes "être" ou "faire", ou encore "-" et "«" qui sont conservés comme des mots. La configuration de l'outil est binaire: soit on prend la liste de mots-vides de SpaCy soit on ne la prend pas. Et c'est un peu une boîte noire.

De manière surprenante, il distingue "applaudissement" et "Applaudissements". Il faut dire que la numérisation de ce dernier est fautive: "{Applaudissements", la parenthèse est lue comme une accolade. Idem "Majesté" ou "majestés".

Enfin c'est un outil assez gourmand en mémoire. Il traite nos 700 pages en quelques minutes alors que mes scripts plus frustres le font en quelques secondes. 
## Résultats en séparant singulier et pluriel 

#### Roi au singulier
323 apparitions dans le texte

On retrouve toutes les thématiques identifiées avec la lemmatisation automatique de SpaCy mais avec **plus de précisions**.

Par exemple, dans l'entourage des rois "Comte" apparaît 9 fois (les frères du roi ont le titre de Comte).

Un thème se dessine davantage, le rapport au temps, avec les co-occurrences suivantes :
- 1792 (12 co-occurrences)
- septembre (11)
- moment (12)
- temps (10)
- jour (8)
#### Rois au pluriel

116 apparitions

**Les thèmes sont légèrement différents de ceux du mot au singulier.**

Les co-occurrences se concentrent sur **les grandes notions politiques**, avec une **attitude républicaine plus marquée**. 

Par exemple le Top 4 des co-occurences:
- liberté (19)
- royauté (14)
- peuple (14) 
- république (13)

**D'une manière générale, le champ thématique des mots n'est pas exactement le même entre le singulier et le pluriel.**

Par exemple, le mot "haine" est davantage associé aux "rois" au pluriel  (7 co-occurrences) et aux "tyrans" au pluriel (7 co-occurrences) qu'au "roi" au singulier (4 co-occurrences) et pas du tout à "tyran" au singulier. 

Autre exemple de différence entre singulier et pluriel, dans tout le corpus, "tyran" est utilisé 10 fois au singulier mais 123 fois au pluriel.

Est-ce à dire que les révolutionnaires haïssent LES rois et non LE roi, LES tyrans et non LE tyran ? 

**Ces différences ouvrent la curiosité.**

Au final, l'exercice de comptage des co-occurrences est intéressant lorsqu'il permet de débuter un regroupement thématique, d'identifier des différences et suscite des surprises.

La lemmatisation est utile pour rendre les résultats lisibles. Il est cependant préférable qu'elle soit contrôlée par l'analyste. Comme nous l'avons vu, les distinctions grammaticales (singulier / pluriel, passé / présent / futur) peuvent apporter un éclairage sur le corpus. C'est à l'historienne ou à l'historien d'en décider. SpaCy, dont les objectifs sont différents, lisse trop le texte. Mieux vaut parfois un outil plus frustre mais mieux maîtrisé.

[^1]: Le français est une langue à flexion: masculin, féminin, singulier, pluriel, passé, présent, futur, etc font varier la forme d'un mot. 

[^2]: Le texte a été transcrit de manière automatique. Il affiche un taux de fiabilité de 88%. Ce taux s'applique aux caractères pas au mot. "Hautc-Loire" contient 11 caractères avec 1 erreur le "c" à la place du "e", soit un taux de fiabilité de 91%.
