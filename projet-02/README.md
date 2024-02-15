# Projet 2 : la calculatrice avec gestion des erreurs

Dans ce projet, vous devez réaliser une calculatrice en ligne de commande qui vous permettra d'additionner deux nombres ensemble.

## Déroulé du script

Le script doit demander à l'utilisateur de saisir deux nombres :
```python
>>> Entrez un premier nombre : 5
>>> Entrez un deuxième nombre : 10
```

Le script doit ensuite afficher la phrase suivante :
```python
"Le résultat de l'addition de 5 avec 10 est égal à 15"
```

Vous devrez donc utiliser une fonction de Python qui permet de récupérer la saisie de l'utilisateur (deux fois), pour ensuite additionner ces variables et afficher le résultat.

Vous devez vous assurer que le programme ne retournera pas d'erreur si l'utilisateur rentre autre chose que deux nombres.

Il va donc falloir gérer ces cas de figure. Si l'utilisateur rentre une lettre, un symbole ou quoi que ce soit d'autre qu'un nombre, vous devrez lui demander de nouveau de saisir deux valeurs valides :
```python
>>> Entrez un premier nombre : a
>>> Entrez un deuxième nombre : sgoind
Veuillez entrer deux nombres valides
>>> Entrez un premier nombre
```