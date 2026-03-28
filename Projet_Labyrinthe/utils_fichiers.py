# utils_fichiers.py

import datetime
import os

def loguer_erreur(exception):
    """Enregistre les erreurs avec horodatage dans journal.log."""
    os.makedirs("data", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("data/journal.log", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] ERREUR ({type(exception).__name__}) : {str(exception)}\n")

def sauvegarder_labyrinthe(grille, nom_fichier="data/dernier_labyrinthe.txt"):
    """Sauvegarde la grille NumPy dans un fichier texte."""
    os.makedirs("data", exist_ok=True)
    with open(nom_fichier, "w", encoding="utf-8") as f:
        for ligne in grille:
            # Convertit chaque ligne du tableau en chaîne de caractères
            f.write("".join(str(cell) for cell in ligne) + "\n")