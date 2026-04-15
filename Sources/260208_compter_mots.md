---
description: Article de blog, humanités numériques, comptage de mots sur de petits corpus
thème: Humanités numériques
date: 2026-02-09
---
# Compter les mots : une première exploration

[Le premier exercice de comptage](./230126-premier-exercice.html) de mots avait révélé l'évidence : les mots les plus fréquents sont des mots grammaticaux. "De", "le", "que" et consorts prédominent. Pas surprenant. Cela a ouvert l'analogie avec la fouille: creuser, tamiser pour trouver un éventuel trésor ou revenir bredouille. 

L'étape suivante : enlever ces mots-vides pour faire émerger le vocabulaire significatif. Mais cette opération de "nettoyage", simple à première vue, soulève aussi des questions de méthode.

> **rappel du dispositif**: 
> trois corpus de textes sont constitués à partir de documents étudiés en cours de licence sur:
> 
> - L’âge des révolutions (1760 - 1820)
> - Église et société (1000 - 1300)
> - Afrique de l’Ouest et Maghreb (1850 - 1950)
> 
> Les corpus sont relativement petits : un peu moins de 3000 signes (entre 1 et 2 pages A4 en police 12) et le corpus sur l'Afrique de l'ouest et le Maghreb fait moins de 1500 signes.
> Chaque corpus contient des extraits de textes de différents auteurs.
> Ces textes ont été choisis par les professeurs pour leur intérêt historique. 

**Quelle liste de mots-vides utiliser ?**

Il existe des listes standards de mots-vides, accessibles en ligne. Elles enlèvent les pronoms et les verbes auxiliaires être et avoir, considérés comme purement grammaticaux.

J'ai choisi de constituer ma propre liste, en retirant seulement les articles ("le", "la", "les", "un", "des") et quelques prépositions courantes ("de", "à", "dans", "pour"). Je garde les pronoms et les auxiliaires. Un choix qui s'avère révélateur.

**Le "je" du Moyen-Âge**

En conservant les pronoms, une surprise m'attend: le corpus du Moyen-Âge est le seul où "je" est utilisé. C'est même un des mots les plus utilisé. Il n'apparaît pas dans les deux autres corpus.
Est-ce le signe d'une place de l'individu qu'on ne soupçonne pas ?
Sans investigation supplémentaire, impossible de savoir. Mais la piste est ouverte. Et elle n'aurait pas émergé avec une liste standard de mots-vides.

**Le futur de la Révolution**

Le futur de être à la troisième personne du pluriel : "seront" est dans le Top 15 des mots les plus fréquent du corpus sur les révolutions. Pas de futur dans les autres corpus. Signe d'un rapport différent au temps ? Les travaux de François Hartog qui sont étudiés en licence, rendent sensibles sur ce point.

Il s'agit plutôt certainement de biais de corpus: un texte particulier peut avoir une incidence forte. L'auxiliaire "avoir" n'est pas employé au futur.

Je me suis posé la question de l'importance des majuscules en voyant à "Sa Majesté" dans le corpus des révolutions. Dans un texte, on a "Monsieur de Mirabeau" mais "M.Necker", un noble en entier, un roturier en abrégé. Effet de la transcription ?

Quoiqu'il en soit : pronoms, le temps des verbes voire les majuscules peuvent être des éléments significatifs.

**Des thématiques qui émergent**

Une fois quelques mots-vides retirés, des articles ("le", "la", "les", "de", "du", "des", ...) et des mots de liaisons ("de", "avec", "pour", ...) un vocabulaire spécifique à chaque corpus apparait :

*Révolutions* : roi, Majesté, Majestés, royale, France, armées, Paris, habitants. Le champ lexical du pouvoir monarchique et de la citoyenneté.

*Afrique* : Dieu, esclaves, impôts, enseignement, gouvernement, Africains, Européens, Blancs. Le vocabulaire de la domination coloniale surgit, avec cette opposition marquée entre populations.

*Chrétienté* : Dieu, Seigneur, esprit, livre. Un vocabulaire plus intemporel, plus difficile à situer précisément dans le temps.

Pourrait-on, à partir de ces seules thématiques, remonter au sujet et à l'époque des corpus ? J'en doute. Mais on commence à percevoir des différences de registre, de préoccupations.

**Que retenir de ce petit exercice ?**

Suivre uniquement une démarche ne produit pas d'analyse. Le comptage des mots et de leurs fréquence est un premier travail descriptif. Il ouvre des pistes qui demandent vérification.

La démarche est moins celle d'une randonnée avec son plan et son objectif qu'un labyrinthe où l'on avance à tatons: une piste, une impasse, on revient sur ses pas, on teste une autre direction. Il n'y a pas vraiment de sortie, mais chaque exploration permet de tracer un morceau de la carte. Et parfois, de mieux comprendre les questions qu'on se pose.

Car il faut aussi se méfier de soi-même. On trouve d'abord ce que l'on cherche : le futur dans Révolutions, parce qu'on est sensibilisé aux travaux sur la temporalité. On remarque ce qui surprend, sort des habitudes : le "je" médiéval. Mais que rate-t-on ? Qu'est-ce qui nous paraît si évident qu'on ne le voit plus ?

Cette démarche d'observation, de questionnement, de vérification n'est pas propre à l'histoire. Elle emprunte aux sciences, à la littérature, à la linguistique, parfois aux neurosciences (quand on s'interroge sur nos propres biais). C'est peut-être là un apport des humanités numériques : forcer le dialogue avec d'autres disciplines, d'autres manières de construire le savoir.

## Annexes

#### Top 50 des mots les plus fréquents par corpus

|           | **Révolutions** |                | **Afrique**  |                | **Chrétienté** |                |
| --------- | --------------- | -------------- | ------------ | -------------- | -------------- | -------------- |
| **Ordre** | **Mot**         | **Occurences** | **Mot**      | **Occurences** | **Mot**        | **Occurences** |
| 1         | il              | 23             | Nous         | 21             | il             | 59             |
| 2         | ils             | 23             | avons        | 17             | est            | 36             |
| 3         | leur            | 22             | est          | 13             | nous           | 28             |
| 4         | leurs           | 20             | nous         | 13             | avec           | 27             |
| 5         | ce              | 15             | il           | 11             | ce             | 24             |
| 6         | pour            | 15             | ne           | 11             | pour           | 23             |
| 7         | roi             | 15             | Notre        | 11             | ne             | 19             |
| 8         | est             | 13             | plus         | 9              | comme          | 19             |
| 9         | n               | 11             | leur         | 9              | j              | 17             |
| 10        | tous            | 11             | Dieu         | 8              | lui            | 17             |
| 11        | avec            | 10             | pour         | 8              | me             | 16             |
| 12        | deux            | 10             | avec         | 7              | pas            | 16             |
| 13        | était           | 10             | notre        | 7              | tout           | 15             |
| 14        | sans            | 10             | vous         | 7              | je             | 14             |
| 15        | seront          | 10             | monde        | 6              | m              | 13             |
| 16        | a               | 9              | eux          | 5              | notre          | 13             |
| 17        | son             | 9              | comme        | 5              | n              | 13             |
| 18        | M               | 9              | ce           | 5              | on             | 13             |
| 19        | sur             | 9              | pays         | 5              | avait          | 13             |
| 20        | ont             | 8              | être         | 5              | si             | 11             |
| 21        | France          | 8              | esclaves     | 5              | mon            | 11             |
| 22        | La              | 7              | ils          | 5              | a              | 11             |
| 23        | sous            | 7              | impôt        | 5              | plus           | 11             |
| 24        | plus            | 7              | enseignement | 4              | où             | 9              |
| 25        | jusqu           | 7              | où           | 4              | était          | 9              |
| 26        | personnes       | 7              | sur          | 4              | sa             | 9              |
| 27        | habitants       | 7              | gouvernement | 4              | sur            | 8              |
| 28        | Sa              | 7              | –            | 4              | étais          | 8              |
| 29        | Majesté         | 7              | province     | 4              | ainsi          | 8              |
| 30        | pas             | 6              | Nos          | 4              | Dieu           | 8              |
| 31        | encore          | 6              | pas          | 4              | ni             | 7              |
| 32        | Le              | 6              | cette        | 4              | leur           | 7              |
| 33        | lui             | 6              | ensemble     | 4              | cette          | 7              |
| 34        | contre          | 6              | tous         | 4              | même           | 7              |
| 35        | Blancs          | 6              | a            | 4              | Seigneur       | 7              |
| 36        | troupes         | 6              | autre        | 4              | travail        | 7              |
| 37        | Leurs           | 6              | faire        | 3              | son            | 7              |
| 38        | Majestés        | 6              | Africains    | 3              | esprit         | 7              |
| 39        | royale          | 6              | Européens    | 3              | écrit          | 7              |
| 40        | également       | 5              | leurs        | 3              | ils            | 7              |
| 41        | armées          | 5              | ont          | 3              | tous           | 7              |
| 42        | eux             | 5              | sujets       | 3              | âge            | 7              |
| 43        | où              | 5              | rabī‘        | 3              | bien           | 6              |
| 44        | Paris           | 5              | al-awwal     | 3              | Le             | 6              |
| 45        | immédiatement   | 5              | seraient     | 3              | moi            | 6              |
| 46        | ai              | 5              | 1258         | 3              | toute          | 6              |
| 47        | fait            | 5              | cela         | 3              | aussi          | 6              |
| 48        | été             | 5              | même         | 3              | livre          | 6              |
| 49        | ne              | 5              | système      | 3              | elle           | 6              |
| 50        | quelques        | 5              | personnel    | 3              | nos            | 6              |

#### Liste des mots-vides

"de", "des", "d", "du", "le", "la", "les", "l", "à", "au", "et", "ou", "en", "qui", "que", "qu", "dans", "par", "un", "une", "aux", "se", "s", "y"