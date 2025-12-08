# Singe Vert

Générateur de site statique pour le blog "Les histoires d'un singe vert".

## 🚀 Site en ligne

Le site est déployé automatiquement sur GitHub Pages : **https://fabiencruz.github.io/singe-vert/**

## 📁 Structure du projet

```
.
├── Sources/              # Articles markdown sources (vault Obsidian)
├── Templates/            # Templates HTML
│   ├── article.html      # Template pour articles individuels
│   ├── article-card.html # Template pour cartes d'articles
│   └── index.html        # Template page d'accueil
├── Static/               # Fichiers statiques (CSS, images)
├── docs/                 # Site généré (GitHub Pages)
├── build_site.py         # Script principal de génération
├── build.sh              # Script de déploiement
├── Makefile              # Commandes d'automatisation
└── requirements.txt      # Dépendances Python
```

## 🛠️ Installation

### Prérequis
- Python 3.x
- Git configuré

### Configuration initiale

1. **Cloner le repository :**
```bash
git clone https://github.com/fabiencruz/singe-vert.git
cd singe-vert
```

2. **Installer les dépendances :**
```bash
make install
```

3. **Configuration de l'alias global (optionnel) :**
Ajouter dans `~/.zshrc` :
```bash
alias sv-build="cd /chemin/vers/singe-vert && ./build.sh"
```

Puis recharger :
```bash
source ~/.zshrc
```

## 🔧 Utilisation

### Commandes Make disponibles

```bash
make install    # Créer l'environnement virtuel et installer les dépendances
make build      # Générer le site uniquement
make site       # Générer + déployer sur GitHub Pages
make clean      # Nettoyer le dossier docs/
```

### Workflow recommandé

1. **Ajouter/modifier un article** dans le dossier `Sources/`
2. **Déployer** avec une seule commande :
```bash
# Depuis le dossier du projet
make site

# Ou depuis n'importe où (si alias configuré)
sv-build
```

Le site sera automatiquement mis à jour sur GitHub Pages.

## 📝 Format des articles

Les articles sont des fichiers markdown avec front-matter YAML :

```markdown
---
thème: "Histoire"
date: "2025-05-24"
---

# Mon titre d'article

Contenu de l'article en markdown...
```

### Conventions de nommage

Les fichiers doivent suivre le format : `AAMMJJ-slug.md`
- `AA` : année (25 pour 2025)
- `MM` : mois (01-12)
- `JJ` : jour (01-31)
- `slug` : identifiant de l'article

Exemple : `250524-mythe-national.md`

## 🎨 Personnalisation

### Templates
Les templates utilisent la syntaxe `{{ variable }}` pour l'interpolation :
- `{{ titre }}` : titre de l'article
- `{{ texte }}` : contenu HTML généré
- `{{ thème }}` : catégorie de l'article
- `{{ date }}` : date de publication
- `{{ extrait }}` : extrait automatique (30 premiers mots)

### Styles
Le fichier `Static/singevert.css` contient tous les styles du site.

## 🔄 Processus de génération

1. **Lecture** des fichiers markdown dans `Sources/`
2. **Extraction** du front-matter YAML et conversion markdown → HTML
3. **Génération** des pages individuelles avec `Templates/article.html`
4. **Création** de la page d'accueil avec les cartes d'articles
5. **Copie** des fichiers statiques vers `docs/`

## 🚀 Déploiement

Le déploiement sur GitHub Pages est automatique :
- Le dossier `docs/` est configuré comme source pour GitHub Pages
- Chaque `git push` met à jour le site en ligne
- La commande `make site` fait tout automatiquement

## 📦 Dépendances

- **PyYAML** : traitement du front-matter
- **Markdown** : conversion markdown → HTML avec extensions (footnotes, tables, TOC)

## 🤝 Contribution

1. Fork le projet
2. Créer une branche pour votre feature
3. Commit vos modifications
4. Push vers la branche
5. Ouvrir une Pull Request

## 📄 Licence

Projet personnel - © 2025 Fabien Cruz