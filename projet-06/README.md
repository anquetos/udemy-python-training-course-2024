# Projet 6 : la liste de courses avec sauvegarde

Dans ce projet, tu vas devoir modifier le script de départ afin d'ajouter la lecture et la sauvegarde de la liste de courses sur le disque.

## Déroulé du script

Pour rappel, le programme permet de réaliser les 5 actions suivantes :
1. ***Ajouter*** un élément à la liste de courses
1. ***Retirer*** un élément de la liste de courses
1. ***Afficher*** les éléments de la liste de courses
1. ***Vider*** la liste de courses
1. ***Quitter*** le programme

Tu dois rajouter des lignes de code au fichier de départ afin de vérifier si un fichier liste.json existe dans le même dossier que le script python.  
Si c'est le cas, tu dois lire le contenu de ce fichier et le stocker dans la variable `LISTE` afin qu'on puisse modifier la liste existante.  
Sinon, on part avec une liste vide.  
Finalement, quand l'utilisateur choisit de quitter le programme avec l'option numéro 5, tu dois sauvegarder la liste sur le disque dans le fichier liste.json (et l'écraser s'il existe déjà).  
Vous pouvez bien entendu également partir d'un fichier Python vide et refaire tout le script depuis le début, à vous de voir.  

Pour récupérer le chemin du dossier courant, vous pouvez utiliser cette ligne de code :
```python
CUR_DIR = os.path.dirname(__file__)
```
La variable `__file__` est définie automatiquement par Python et correspond au chemin complet du script Python exécuté. `os.path.dirname` permet de récupérer le dossier parent de ce chemin.