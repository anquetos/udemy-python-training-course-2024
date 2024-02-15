# Projet 7 : le trieur de fichiers

Le but de ce projet est de créer un script qui permette de trier automatiquement des fichiers dans des sous-dossiers en fonction de leur type (extension).

Dans les sources de ce projet, vous trouverez un dossier `data` qui contient des fichiers de différents types (images, vidéos, documents...).

Vous pouvez partir de ce dossier ou utiliser n'importe quel dossier de votre disque dur (le dossier de téléchargements est généralement un bon endroit pour faire le ménage...).

Le but de ce script est de trier les fichiers selon leur type (et donc leur extension) dans des sous-dossiers.

Par exemple, vous devez regrouper tous les fichiers avec l'extension `.mp3` ou `.wav` dans un sous-dossier `Musique`.

Tous les fichiers textes quant à eux devront se retrouver dans un dossier `Documents`.

Voici l'association des extensions et des dossiers que vous devez utiliser :
```python
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
```
Pour ce projet je vous conseille d'utiliser la bibliothèque `pathlib` que l'on a vu dans la partie précédente.

Vous verrez que c'est bien plus facile de faire ce script avec `pathlib` qu'avec le module `os` ou le module `glob`.

Quelques éléments pour vous aider si vous êtes bloqués :
* Pour associer les extensions aux dossiers, pensez à utiliser un dictionnaire.
* Pensez à créer le dossier cible avant de déplacer le fichier (rappelez-vous également du paramètre `exist_ok` de la fonction `mkdir`).
* Pour déplacer un fichier, vous pouvez utiliser sur un objet de type Path (provenant de `pathlib`), la méthode `rename`.
