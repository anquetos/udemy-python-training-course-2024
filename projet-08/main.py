# Projet 8 : le créateur de dossiers

from pathlib import Path

p = Path(__file__).parent.absolute()
chemin = p / "dossier_test"

d = {
    "Films": [
        "Le seigneur des anneaux",
        "Harry Potter",
        "Moon",
        "Forrest Gump"
    ],
    "Employes": [
            "Paul",
            "Pierre",
            "Marie"
    ],
    "Exercices": [
        "les_variables",
        "les_fichiers",
        "les_boucles"
    ]
}

for key, value in d.items():
    for item in value:
        dossier_a_creer = chemin / key / item
        dossier_a_creer.mkdir(parents=True, exist_ok=True)