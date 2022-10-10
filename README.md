
<h1 align="center">
  <br>
  Don't Look Up !
  <br>
</h1>

<h2 align="center">Application minimaliste pour afficher les astéroïds passant près de notre la Terre entre 2 dates</h2>
<h4 align="center">Application développée entièrement grâce au framework Django : (https://www.djangoproject.com)</h4>

## Téléchargement et installation

```bash

# Assurez-vous d'avoir Python3 et pip installés sur votre machine

# Clonez ce repository
$ git clone https://github.com/Adrien-GOGOIS/dont_look_up_projet.git
$ cd dont_look_up_project

# Installation

# Pour créer un virtual env et l'activer
$ python3 -m venv ./venv
$ source ./venv/bin/activate

# Dépendances
$ pip install django
$ pip install django-dotenv
$ pip install requests

# Générez votre clef API en vous inscrivant sur les services de la Nasa (voir lien plus bas)
# Puis, à la racine du projet, créez un fichier 'config.env' et ajoutez cette ligne de code avec votre clef comme ceci :
$ NASA_API_KEY = "insérez votre clef ici"

# L'application peut fonctionner de façon très limitée avec la clef API : DEMO_KEY
$ NASA_API_KEY = "DEMO_KEY"

# Lancez l'application
$ python manage.py runserver

# Ouvrez votre navigateur favoris et tapez dans la barre d'adresse : http://127.0.0.1:8000/

# Enjoy !

```

## Mode d'emploi

L'application interroge une API de la Nasa fournissant des données sur les objets célestes croisant l'orbite de la Terre.
<br>
--> [Lien vers l'API](https://api.nasa.gov/index.html#main-content)
<br>
Une fois lancée, l'application est visible sur votre navigateur à l'adresse http://127.0.0.1:8000/. 
<br>
La page d'accueil de l'application vous permet d'entrer 2 dates. Après un temps de chargement plus ou moins long selon votre connexion........
les astéroïds qui passeront au-dessus de votre tête entre les dates selectionnées s'afficheront sous forme de cartes.
<br>
Il est possible de voir les détails d'un astéroïds en cliquant sur "En savoir plus...". 
une nouvelle page s'ouvrira alors pour consulter les 5 derniers passages de cette astéroïd au-dessus de la Terre.

> GitHub [@Adrien-GOGOIS](https://github.com/Adrien-GOGOIS)


