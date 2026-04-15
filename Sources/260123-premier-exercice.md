---
description: Article de blog, humanités numériques, premier exercice de comptage de mots
thème: Humanités numériques
date: 2026-01-26
---

# Premier exercice de comptage des mots

Comment analyser des textes avec l'informatique ?
La question est vaste. Le risque est de verser dans la paralysie ou dans une agitation improductive. 

Il est essentiel de se lancer concrètement. Je me suis concocté un exercice très simple : compter les mots dans un mini-corpus.

Ce dernier est constitué de trois fichiers contenant des textes issus de contextes historiques différents. 

**L'hypothèse est que les mots les plus fréquents de chaque fichier révèlent leur contexte historique**. 

Cet exercice est réalisé en trois étapes.
## Etape 1 : constituer un _corpus_

Je choisis des **documents d'époques très différentes**, donnés pour les travaux dirigés de trois cours d'histoire de licence:

1. L'âge des révolutions (1760 - 1820)
2. Église et société (1000 - 1300)
3. Afrique de l'Ouest et Maghreb (1850 - 1950)

Chacun a un vocabulaire particulier, par exemple:

- "roi" ou "assemblée" dans L'âge des révolutions
- "moine" ou "monastère" dans Église et société
- "indigène" ou "Européens" dans Afrique de l'Ouest et Maghreb

C'est ce que l'on veut mettre en évidence. 

Il y a aussi certains "pièges": par exemple, le mot "Dieu" peut se retrouver dans les trois fichiers.

> **Notes sur la préparation des fichiers**
> 
> Aucun des auteurs originaux n'a évidemment utilisé de logiciel de traitement de texte. Les textes analysés ne sont pas des données brutes mais issus de transcriptions successives. Chacune avec ces intentions: traductions, annotations pédagogiques ou mise en format informatique, etc

## Etape 2 : compter les mots

Mon algorithme de dénombrement en [pseudo-code](https://fr.wikipedia.org/wiki/Pseudo-code):

1. Récupérer les contenus des différents fichiers
2. Pour chaque fichier, récupérer les mots
	1. Enlever la ponctuation (.,;!?, etc)
	2. Prendre toute chaîne de caractères comprise entre deux espaces
		1. Pour chaque apparition d'un mot dans le fichier,
			1. ajouter 1 à son occurence
3. Afficher les 50 premiers résultats de chaque fichier

Le pseudo-code, ici simplifié, est un support de réflexion personnelle et de conversation avec une Intelligence Artificielle, jouant le rôle de tutrice.

>**Remarque sur le vibe coding**
>
>Il est possible de laisser une Intelligence Artificielle (IA) coder entièrement le script. Faire du [vibe coding](https://en.wikipedia.org/wiki/Vibe_coding#)
>
>Une IA produira un script fonctionnel souvent optimisé. Les développeurs parlent de [code refactorisé](https://fr.wiktionary.org/wiki/refactorisation#:~:text=Nom%20commun,-Singulier&text=(Programmation)%20Action%20de%20refactoriser%20%3A,son%20d%C3%A9bogage%20et%20son%20extension.) ou de code "élégant".
>
>La différence est celle de regarder un athlète faire du sport et faire du sport soi-même. 
>
> Cependant, comme pour la rédaction de texte ou la génération d'images, les IA font des erreurs.

## Etape 3 : analyser le résultat

#### Les mots-vides

Le mot le plus fréquent dans les trois fichiers est le mot **"de"**. 

Dans le Top 5, on trouve "le", "et", "à", "des".

La documentation parle de '_mots vides_' ou de [stopword](https://voyant-tools.org/docs/tutorial-stopwords.html) en anglais. Ils ont une grande utilité grammaticale mais pas sémantique.
#### Un mot ?

Récupérer les 'mots' suppose de définir ce qu'est un mot et de faire des choix.

J'ai suivi une idée simple: "un mot est ce qui est entre deux espaces."

J'ai aussi choisi d'enlever la ponctuation (.,;!? ...).  

Les conséquences :

- un nom propre comme "Le marquis de La Fayette" est découpé en "Le", "marquis", "de", "La" et "Fayette".
- enlever les tirets découpe et perd "États-Unis".

La graphie française comprend aussi des accents, des apostrophes et la cédille. Il est possible de les enlever et de mettre tout le texte en minuscule. En effet, "Roi" et "roi" sont deux mots différents pour ce script (il est dit "sensible à la casse").
#### Implications de méthode

Chacune de ces opérations de _normalisation_ du texte (enlever la ponctuation, les majuscules, les accents, etc) élimine des mots. L'analogie la plus commune est celle du _data mining_: creuser et tamiser la terre pour trouver un trésor. 

Et comme le disait Marcel Mauss, on ne "va pas à la chasse, on va à la chasse au lapin". Il faut donc avoir les outils adaptés à la situation. La pelle et le tamis.

Plusieurs listes seraient nécessaires pour "normaliser" les textes:

- une liste de la ponctuation que l'on va supprimer
- une liste des mots-vides
- une liste d'exceptions: des mots composés à conserver

Pour créer ces listes, il est nécessaire de travailler de manière itérative. On prend les textes, on fait tourner le script, on ajuste, et ainsi de suite. Ici ce travail n'a pas encore été mené à son terme. 

Reste que ce petit exercice met le doigt sur des questions de méthodes. Exactement ce que je cherchais.