# Projet 2 : la calculatrice avec gestion des erreurs

# Initialise les variables
premier_nombre = ''
deuxieme_nombre = ''

while not (premier_nombre.isdigit() and deuxieme_nombre.isdigit()):

    
    # Récupère la les nombres saisies
    premier_nombre = input('Entrez un premier nombre :')
    deuxieme_nombre = input('Entrez un deuxième nombre :')

    # Affiche le message d'erreur
    if not (premier_nombre.isdigit() and deuxieme_nombre.isdigit()):
        print('Veuillez entrer deux nombres valides.')

# Calcule la somme et affiche le résultat
somme = int(premier_nombre) + int(deuxieme_nombre)
print(f'Le résultat de l\'addition du nombre {premier_nombre} avec le nombre {deuxieme_nombre} est égal à {somme}.')