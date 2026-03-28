# generateurs.py

import numpy as np
import random

class GenerateurLabyrinthe:
    def __init__(self, largeur, hauteur):
        # Utilisation de NumPy pour initialiser la grille remplie de murs (1) [cite: 185]
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = np.ones((hauteur, largeur), dtype=int)

    def generer_backtracking(self):
        """Génération avec l'algorithme de Backtracking (Recherche en profondeur)."""
        self.grille.fill(1) # Remplir de murs
        
        def creuser_passage(cx, cy):
            directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
            random.shuffle(directions)
            
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                # Si la case de destination est dans les limites et est un mur
                if 1 <= ny < self.hauteur-1 and 1 <= nx < self.largeur-1 and self.grille[ny, nx] == 1:
                    self.grille[cy + dy//2, cx + dx//2] = 0 # Casse le mur entre les deux
                    self.grille[ny, nx] = 0                 # Creuse la nouvelle cellule
                    creuser_passage(nx, ny)

        # Point de départ du creusage
        self.grille[1, 1] = 0
        creuser_passage(1, 1)
        
        # Placement de l'entrée (2) et de la sortie (3)
        self.grille[1, 1] = 2 
        self.grille[self.hauteur-2, self.largeur-2] = 3 
        return self.grille
        
    def generer_prim(self):
        """Structure pour l'algorithme de Prim."""
        # À développer si tu as le temps, sinon le Backtracking suffit amplement !
        pass