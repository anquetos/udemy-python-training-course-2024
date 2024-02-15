# Projet 4 : le nombre mystère

import random

nombre_aleatoire = random.randint(0, 100)
i = 1
n_essais = 5
essais_restants = n_essais

print(f'### Le jeu du nombre mystère ###\n'
      f'--------------------------------')

while i < (n_essais+1):

    print(f'Il te reste {essais_restants} essai(s)')

    nombre = input(f'Devine le nombre : ')

    if nombre.isdigit() != True:
        print('Veuillez entrer un  nombre valide.')
    elif nombre_aleatoire < int(nombre):
        print(f'Le nombre mystère est plus petit que {nombre}')
        i += 1
        essais_restants -= 1
    elif nombre_aleatoire > int(nombre):
        print(f'Le nombre mystère est plus grand que {nombre}')
        i += 1
        essais_restants -= 1
    elif nombre_aleatoire == int(nombre):
        print(f'Bravo ! Le nombre mystère était bien {nombre_aleatoire} !\n'
              f' Tu as trouvé le nombre en {i} essai(s)')
        break

if essais_restants == 0:
    print(f'Dommage ! Le nombre mystère était {nombre_aleatoire}\n'
          f'Fin du jeu.') 
        