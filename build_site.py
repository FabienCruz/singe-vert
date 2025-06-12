"""
fichier: build_site.py
Description: code pour construire le site web

Les fichiers sources sont issus d'un vault Obsidian.
Une partie du formatage des fichiers est fait par convention au niveau Obsidian:
- titre de fichier: AAMMJJ-slug
- propriétés du Front-Matter = placeholders des templates
"""
import yaml
import markdown
import datetime
import locale
import shutil
import re
from pathlib import Path

settings = {
    'input': './Sources',
    'output': './docs',
    'templates': './Templates',
    'static': "./Static"
}

# Configuration de la locale française
try:
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')  # Linux/Mac
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'fr_FR')  # Windows
    except locale.Error:
        print("Locale française non disponible, utilisation de l'anglais par défaut")

"""
Utilitaires pour le traitement des templates
"""

def render_template(template_name, variables):
    """
    Charge un template et remplace les variables
    
    Args:
        template_name (str): nom du fichier template
        variables (dict): dictionnaire des variables à remplacer
    
    Returns:
        str: contenu du template avec variables remplacées
    """
    template_path = Path(settings['templates']) / template_name
    
    if not template_path.exists():
        raise FileNotFoundError(f"Template non trouvé : {template_path}")
    
    template_content = template_path.read_text(encoding="utf-8")
    
    result = template_content
    for key, value in variables.items():
        if value is not None:
            # Gestion spéciale des dates
            if hasattr(value, 'strftime'):
                value = value.strftime('%B %Y')
            result = result.replace(f"{{{{ {key} }}}}", str(value))
    
    return result

"""
Utilitaires pour le traitement du contenu markdown
"""

def make_excerpt(text, words=30):
    """Crée un extrait de texte en supprimant les footnotes"""
    text_cleaned = erase_footnote(text)
    words_list = text_cleaned.split()
    excerpt = ' '.join(words_list[:words])+"..."
    return excerpt

def erase_footnote(text):
    """Supprime les références de footnotes du texte"""
    cleaned = re.sub(r'\[\^?[^\]]+\]', '', text)
    return cleaned

def get_h1_text(md_content):
    """
    Sépare le titre h1 et le reste d'un markdown.
    Cherche la première ligne qui commence par "# "
    """
    match = re.search(r'^# (.+)\n+', md_content, flags=re.MULTILINE)
    if not match:
        return (None, md_content.strip())

    title_h1 = match.group(1).strip()
    # Convertir le titre en HTML pour gérer le formatage markdown
    title_html = md_to_html(title_h1)
    # Supprimer les balises <p> ajoutées par markdown
    title_html = re.sub(r'^<p>|</p>$', '', title_html.strip())

    content_after_h1 = md_content[match.end():].strip()

    return (title_html, content_after_h1)

def md_to_html(md_content):
    """Convertit du markdown en HTML"""
    html = markdown.markdown(md_content, extensions=["footnotes", "tables", "toc", "smarty"])
    return html
"""
Préparation du dossier /docs (convention Github Pages)
"""

def clean_output_directory():
    """Supprime et recrée le dossier de sortie pour un build propre"""
    
    output_path = Path(settings['output'])
    
    if output_path.exists():
        shutil.rmtree(output_path)
        print(f"Dossier {output_path} supprimé")
    
    output_path.mkdir(parents=True, exist_ok=True)
    print(f"Dossier {output_path} créé")

def copy_static_files():
    """Copie les fichiers statiques vers docs/"""
    import shutil
    static_path = Path(settings['static'])
    output_path = Path(settings['output'])
    
    for file in static_path.glob('*'):
        if file.is_file():
            shutil.copy2(file, output_path)

"""
Traitement des fichiers sources
"""

def get_content(file_content):
    """
    Décompose le contenu des fichiers markdown en métadonnées et article HTML.
    
    Returns:
        dict: {'metadata': dict, 'article': str}
    """
    content = {}
    
    if file_content.startswith('---'):
        parts = file_content.split('---', 2)
        if len(parts) >= 3:
            _, yaml_part, md_part = parts
            try:
                content['metadata'] = yaml.safe_load(yaml_part) or {}
            except yaml.YAMLError as e:
                print(f"Erreur YAML : {e}")
                content['metadata'] = {}
            
            title, text = get_h1_text(md_part)
            content['metadata']['titre'] = title
            content['metadata']['extrait'] = make_excerpt(text)
            content['article'] = md_to_html(md_part)
        else:
            content['metadata'] = {}
            content['article'] = md_to_html(file_content)
    else:
        content['metadata'] = {}
        content['article'] = md_to_html(file_content)
    
    return content

def get_md_files(path):
    """Récupère tous les fichiers markdown du dossier"""
    return list(path.glob('*.md'))

def make_data(files):
    """
    Traite tous les fichiers et crée le dictionnaire de données principal
    
    Args:
        files (list): liste des fichiers Path
    
    Returns:
        dict: dictionnaire avec slug comme clé
    """
    data = {}
    for file in files:
        try:
            file_content = file.read_text(encoding="utf-8")
            page = get_content(file_content)
            page['metadata']['slug'] = file.stem
            data[file.stem] = page
        except Exception as e:
            print(f"Erreur lors du traitement de {file.name} : {e}")
            continue
    
    return data

"""
Génération des pages HTML
"""

def build_article_cards(data):
    """
    Génère toutes les cartes d'articles pour l'index
    
    Args:
        data (dict): dictionnaire des données d'articles
    
    Returns:
        str: HTML de toutes les cartes concaténées
    """
    all_cards = []
    
    for article_id, article_data in data.items():
        try:
            card_html = render_template("article-card.html", article_data['metadata'])
            all_cards.append(card_html)
        except Exception as e:
            print(f"Erreur lors de la génération de la carte {article_id} : {e}")
            continue
    
    return '\n'.join(all_cards)

def build_index(cards_html):
    """
    Génère la page d'index articles avec toutes les cartes
    
    Args:
        cards_html (str): HTML de toutes les cartes
    
    Returns:
        str: HTML complet de l'index
    """
    try:
        # Métadonnées pour l'index (à adapter selon vos besoins)
        index_variables = {
            'cards': cards_html,
            'meta-name': 'description',
            'meta-content': 'Blog personnel - Les histoires d\'un singe vert'
        }
        
        index_html = render_template("index.html", index_variables)
        
        # Écriture du fichier
        output_path = Path(settings['output']) / "index.html"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(index_html, encoding="utf-8")
        
        return index_html
        
    except Exception as e:
        print(f"Erreur lors de la génération de l'index : {e}")
        return None

def build_articles(data):
    """
    Génère toutes les pages d'articles individuelles
    
    Args:
        data (dict): dictionnaire des données d'articles
    """
    output_dir = Path(settings['output'])
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for article_id, article_data in data.items():
        try:
            # Préparation des variables pour le template
            article_variables = {
                'titre': article_data['metadata'].get('titre', 'Sans titre'),
                'texte': article_data['article'],
                'meta_html': ''  # À développer selon vos besoins
            }
            
            article_html = render_template("article.html", article_variables)
            
            # Écriture du fichier
            output_path = output_dir / f"{article_id}.html"
            output_path.write_text(article_html, encoding="utf-8")
            
        except Exception as e:
            print(f"Erreur lors de la génération de l'article {article_id} : {e}")
            continue

"""
Fonction principale de construction du site
"""

def build_site():
    """
    Fonction principale qui orchestre la construction complète du site
    
    Returns:
        dict: dictionnaire des données pour debugging
    """
    try:
        # 1. Nettoyage complet du dossier docs
        clean_output_directory()
    
        # 2. Copie des fichiers statiques
        copy_static_files()
        
        # 3. Récupération des fichiers markdown sources
        input_path = Path(settings['input'])
        if not input_path.exists():
            raise FileNotFoundError(f"Dossier source introuvable : {input_path}")
        
        files = get_md_files(input_path)
        if not files:
            print("Aucun fichier markdown trouvé")
            return {}
        
        print(f"Traitement de {len(files)} fichiers...")
        
        # 4. Création du dictionnaire de données principal
        data = make_data(files)
        
        # 5. Génération des cartes et de l'index
        cards_html = build_article_cards(data)
        build_index(cards_html)
        
        # 6. Génération des articles individuels
        build_articles(data)
        
        print(f"Site généré avec succès : {len(data)} articles")
        return data
        
    except Exception as e:
        print(f"Erreur lors de la construction du site : {e}")
        return {}

if __name__ == '__main__':
    build_site()