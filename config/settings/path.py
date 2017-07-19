"""
    Ce module contient les chemins des dossiers du projet, créés dynamiquement.

    Tous les chemins sont absolus, sans liens, et en unicode.

    Il ajoute aussi les dossiers 'apps' et 'libs' au PYTHON PATH, ce qui
    va nous faciliter les imports.
"""


import sys
import os
import tempfile

# Cette partie est un peu compliquée et n'est pas forcément nécessaire
# à votre projet, mais elle rend le projet complètement portable car tous
# les chemins de tous les dossiers sont créés dynamiquement au lieu
# d'être écris en dur.

# Nous créons ces paramètres dynamiquement, ce qui nous donne les chemins
# absolus vers le dossier du projet et le dossier racine contenant tout
# notre travail ainsi que tout autre dossier dont nous pourrions avoir
# besoin.
SETTINGS_DIR = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(SETTINGS_DIR)
BASE_DIR = ROOT_DIR = os.path.dirname(PROJECT_DIR)
APPS_DIR = os.path.join(BASE_DIR, 'apps')
LIBS_DIR = os.path.join(BASE_DIR, 'libs')
TEMP_DIR = tempfile.gettempdir()


# Nous ajoutons les dossiers "apps" et "libs" au PYTHON PATH, de telle sorte
# que nous puissions importer chaque package sans avoir à les préfixer du nom
# du package parent. Ceci imite le comportement que nous aurions si ils
# étaient à la racine ou installés avec pip.
#
# Ex: nous pouvons importer "from app1_hello.views import hello" plutôt que
#     "from apps.app1_hello.views import hello" ou "import django" à la place
#     de "from libs import django"
#
# Quand vous avez un petit projet, vous pouvez éviter cela et mettre toutes
# les apps dans le dossier racine comme dans le tutorial Django officiel, mais
# dans un gros projet avec beaucoup d'apps, on les met généralement toutes
# dans un dossier "apps" comme nous venons de faire, donc c'est une bonne
# chose à connaitre.
sys.path.append(APPS_DIR)
sys.path.append(LIBS_DIR)
