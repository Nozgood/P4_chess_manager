# Welcome to your chess tournament manager ! 

## Prerequisites

- To install and run this project, we start from the principle that you have `Python` and it package manager `pip` installed on your machine 
- If not, you can install this by following this link: [https://www.python.org/downloads/]

- You will need pipenv to install the virtual environment of this project, if pipenv is not installed on your machine, run this following command: `pip install pipenv`

## Installation

1. Clone this repository on your machine (using SSH or HTTP, as you want)
2. Open a terminal, and go to the project's root directory
3. Install the necessaries dependencies by running the following command: `pip install -r requirements.txt`

## Launching 

1. Open a terminal and go to the project's root directory
2. Launch the application by running the following command: `python3 main.py`
3. Enjoy ! :D

## Flask8

If you want to generate a flask8 report, please follow this commands:

1. In the root of the project, you've got 2 choices:
	- Using the MakeFile (and assuming you've got Make install on your machine), run this command: `Make flake8`
	- Or you can just run this command: `flake8 --max-line-length=119 --format=html --htmldir=flake8_rapport ./`

2. A report will be generate in html format, you can launch it in your favorite browser to check if there is no issue to fix

# Bienvenue sur votre gestionnaire de tournois d'échecs ! 

## Pré-requis

-   Pour installer et exécuter ce projet, nous partons du principe que vous avez `Python` et son gestionnaire de packages `pip` installés sur votre machine.
    
-   Si ce n'est pas le cas, vous pouvez l'installer en suivant ce lien : [[https://www.python.org/downloads/](https://www.python.org/downloads/)]
    

## Installation

1.  Clonez ce repository sur votre machine (en utilisant SSH ou HTTP, comme vous voulez).
2.  Ouvrez un terminal et allez dans le répertoire racine du projet.
3.  Installez les dépendances nécessaires en exécutant la commande suivante : `pip install -r requirements.txt`

## Lancement

1.  Ouvrez un terminal et allez dans le répertoire racine du projet.
2.  Lancez l'application en exécutant la commande suivante : `python3 main.py`
3.  Amusez-vous bien ! :D

## Flask8

Si vous voulez générer un rapport Flask8, veuillez suivre ces commandes :

1.  À la racine du projet, vous avez deux choix :
    
    -   En utilisant le fichier Makefile (et en supposant que Make est installé sur votre machine), exécutez cette commande : `Make flake8`
    -   Ou vous pouvez simplement exécuter cette commande : `flake8 --max-line-length=119 --format=html --htmldir=flake8_rapport ./`
2.  Un rapport sera généré en format html, vous pouvez l'ouvrir dans votre navigateur préféré pour vérifier s'il n'y a pas de problèmes à résoudre.
