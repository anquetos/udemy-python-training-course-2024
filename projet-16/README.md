# Projet 16 : un tableau de bord avec Django

## Présentation 

Réalisation d'un tableau de bord avec le cours de devises.

Il sera possible modifier la période d'affichage des cours (mois, semaines, etc.).

Le site sera entièrement *responsive*.

## Etapes de création

1. Créer l'API pour récupérer le cours des devises.
2. Créer l'application Django pour afficher les informations de l'API.

## API

> Le site exchangeratesapi.io a malheureusement mis en place des mesures pour empêcher l'utilisation gratuite de leur API.
> 
> Pour pallier ce problème et vous permettre de réaliser ce projet, j'ai créé une API fictive sur Docstring qui fonctionne exactement comme celle que je vais vous présenter dans les prochaines parties.

À la place de :

    api.exchangeratesapi.io/latest

Utilisez :

    https://www.docstring.fr/api/rates/latest/


À la place de :

    api.exchangeratesapi.io/history?start_at=2020-01-01&end_at=2020-01-04

Utilisez :

    https://www.docstring.fr/api/rates/history/?start_at=2020-01-01&end_at=2020-01-04


Pour récupérer certaines devises uniquement dans un laps de temps défini :

À la place de :

    api.exchangerate.io/history?start_at=2020-10-01&end_at=2020-10-03&symbols=USD,CAD

Utilisez :

    https://www.docstring.fr/api/rates/history/?start_at=2020-01-01&end_at=2020-01-04&symbols=USD,CAD
