# jeu.py

from exceptions import MouvementInvalideError
from utils_fichiers import loguer_erreur
import numpy as np

class JeuLabyrinthe:
    def __init__(self, grille):
        self.grille = grille
        self.hauteur, self.largeur = grille.shape
        # Trouver la position de départ (valeur 2 dans NumPy)
        pos_y, pos_x = np.where(self.grille == 2)
        self.pos_joueur = [pos_y[0], pos_x[0]]

    def afficher(self):
        print("\n" * 50) # Nettoie grossièrement la console
        # 1: Mur, 0: Chemin, 2: Départ, 3: Arrivée, 4: Joueur
        symboles = {1: "██", 0: "  ", 2: "Dé", 3: "Fi", 4: "P "}
        
        for y in range(self.hauteur):
            ligne_affichage = ""
            for x in range(self.largeur):
                if [y, x] == self.pos_joueur:
                    ligne_affichage += symboles[4] # Affiche le joueur
                else:
                    ligne_affichage += symboles[self.grille[y, x]]
            print(ligne_affichage)

    def deplacer(self, direction):
        """Tente de déplacer le joueur et gère les erreurs de collision."""
        dy, dx = 0, 0
        if direction == 'z': dy = -1   # Haut
        elif direction == 's': dy = 1  # Bas
        elif direction == 'q': dx = -1 # Gauche
        elif direction == 'd': dx = 1  # Droite
        else:
            return False

        nouvelle_y = self.pos_joueur[0] + dy
        nouvelle_x = self.pos_joueur[1] + dx

        try:
            # Vérifier si on tape un mur (1)
            if self.grille[nouvelle_y, nouvelle_x] == 1:
                raise MouvementInvalideError("Aïe ! Vous avez percuté un mur.")

            # Si pas d'erreur, on applique le mouvement
            self.pos_joueur = [nouvelle_y, nouvelle_x]

            # Vérifier si on a gagné (3)
            if self.grille[nouvelle_y, nouvelle_x] == 3:
                return "Gagné"

        except MouvementInvalideError as e:
            # On affiche l'erreur et on la sauvegarde dans le fichier log [cite: 22, 24]
            print(f"\n[!] Attention : {e}")
            loguer_erreur(e)
            input("Appuyez sur Entrée pour continuer...") # Pause pour lire l'erreur

        return "Continue"