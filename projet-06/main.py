# Projet 6 : la liste de course avec sauvegarde

import sys
from pathlib import Path
import json

CURRENT_DIR = Path(__file__).parent.absolute()
LISTE_FILE_PATH = CURRENT_DIR / 'liste.json'

# Initialise les variables
if LISTE_FILE_PATH.is_file():
    with open(LISTE_FILE_PATH, 'r') as f:
        liste = json.load(f)
else:
    liste = []

MENU = ['1', '2', '3', '4', '5']

# Affiche le menu
print('-- Liste de courses --')

while True:
    choix = input(
        '\nSaisissez un nombre entre 1 et 5 en fonction de l\'action que vous souhaitez réaliser.\n'
        '1. Ajouter un élément à la liste de courses\n'
        '2. Retirer un élément de la liste de courses\n'
        '3. Afficher les éléments de la liste de courses\n'
        '4. Vider la liste de courses\n'
        '5. Quitter le programme\n'
    )

    if choix not in MENU:
        print('Votre choix n\'est pas valide')
        continue

    if choix == '1':
        add_item = input('Quel élément voulez-vous ajouter ?')
        liste.append(add_item)
        print(f'{add_item} a été ajouté.')

    elif choix == '2':
        del_item = input('Quel élément voulez-vous supprimer ?')
        if del_item in liste:
            liste.remove(del_item)
            print(f'{del_item} a été supprimé.')
        else:
            print(f'{del_item} n\'existe pas')

    elif choix == '3':
        if liste:
            print('Eléments dans la liste :')
            for i, item in enumerate(liste, 1):
                print(f'{i} - {item}')
        else:
            print('La liste est vide')

    elif choix == '4':
        liste.clear()
        print('La liste a été vidée')

    elif choix == '5':
        with open(LISTE_FILE_PATH, 'w') as f:
            json.dump(liste, f)
        sys.exit()