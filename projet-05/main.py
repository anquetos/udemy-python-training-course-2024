# Projet 5 : le nombre mystère

import random

# Initialise les variables
us_life = 50
opponent_life = 50
n_potions = 3
choices = ['1', '2']
turn = 1

# Affiche le début du jeu
print(f'~ Le jeu de rôle - essayez de battre votre adversaire ! ~')

# Boucle tant que nous ou notre adversaire a des points de vie
while us_life or opponent_life > 0:

    # Affiche les informations les points de vie et potion(s)
    print(
        f'\nTour {turn}\n'
        f'''{'-' * 57}\n'''
        f'Points de vie :\t\tVous [{us_life}] | Adversaire [{opponent_life}]\n'
        f'Potion(s) restante(s) : {n_potions}\n'
        f'''{'-' * 57}\n'''
        )
    
    choice = input(f'Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?')

    if (choice in choices) and (n_potions > 0):
        
        if choice == '1':
            attack_points = random.randint(5, 10)
            opponent_life -= attack_points
            print(f'\n[+] Vous infligez {attack_points} points de dégats à votre adversaire.')
            turn += 1

        elif choice == '2':
                life_points = random.randint(15, 50)
                us_life += life_points
                print(f'\n[+] Vous récupérez {life_points} points de vie.')
                turn += 1
                n_potions -= 1

        if opponent_life <= 0:
            print(f'[*] Bravo, vous avez battu votre adversaire !')
            break
        elif opponent_life > 0:
            attack_points = random.randint(5, 15)
            us_life -= attack_points
            print(f'[-] Votre adversaire vous inflige {attack_points} points de dégats.')
        
    elif (choice in choices) and (n_potions == 0):

        if choice == '1':
            attack_points = random.randint(5, 10)
            opponent_life -= attack_points
            print(f'\n[+] Vous infligez {attack_points} points de dégats à votre adversaire.')
            turn += 1

            if opponent_life <= 0:
                print(f'[*] Bravo, vous avez battu votre adversaire !')
                break
            elif opponent_life > 0:
                attack_points = random.randint(5, 15)
                us_life -= attack_points
                print(f'[-] Votre adversaire vous inflige {attack_points} points de dégats.')
        
        elif choice == '2':
            print(f'\n[!] Votre choix n\'est pas valide, veuillez recommencer.')

    elif choice not in choices:
        print(f'\n[!] Votre choix n\'est pas valide, veuillez recommencer.')

    if us_life <= 0:
        print(f'[x] Dommage, votre adversaire vous a battu !')
        break

print(f'[!] Fin du jeu\n')