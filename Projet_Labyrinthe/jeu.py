# jeu.py

import time
import numpy as np
from exceptions import MouvementInvalideError, PiegeError
from utils_fichiers import loguer_erreur

class JeuLabyrinthe:
    def __init__(self, grille):
        self.grille = grille
        self.hauteur, self.largeur = grille.shape
        # trouver la position de départ (2)
        pos_y, pos_x = np.where(self.grille == 2) #  il renvoie deux listes (lignes et colonnes)
        self.pos_joueur = [int(pos_y[0]), int(pos_x[0])] # On prend la première position trouvée et on transforme les valeurs numpy en int

    def afficher(self):
        print("\n" * 50) # nettoie la console
        # Le dictionnaire des symboles
        symboles = {1: "██", 0: "  ", 2: "Dé", 3: "Fi", 4: "P ", 5: "><"}
        
        for y in range(self.hauteur):
            ligne_affichage = ""
            for x in range(self.largeur):
                if [y, x] == self.pos_joueur:
                    ligne_affichage += symboles[4] # affiche le joueur (P)
                else:
                    ligne_affichage += symboles[self.grille[y, x]]
            print(ligne_affichage)

    def deplacer(self, direction):
        dy, dx = 0, 0
        if direction == 'z': dy = -1   
        elif direction == 's': dy = 1  
        elif direction == 'q': dx = -1 
        elif direction == 'd': dx = 1  
        else:
            return "Continue" 

        nouvelle_y = self.pos_joueur[0] + dy
        nouvelle_x = self.pos_joueur[1] + dx

        try:
            # Vérifier si on tape un mur (1)
            if self.grille[nouvelle_y, nouvelle_x] == 1:
                raise MouvementInvalideError()

            # Vérifier si on marche sur un piège (5)
            if self.grille[nouvelle_y, nouvelle_x] == 5:
                raise PiegeError()

            # Si tout va bien (pas de mur, pas de piège), on avance normalement
            self.pos_joueur = [nouvelle_y, nouvelle_x]

            # Vérifier si on a gagné (3)
            if self.grille[nouvelle_y, nouvelle_x] == 3:
                return "Gagné"

        except MouvementInvalideError as e:
            print(f"\n[!] Attention : {e}")
            loguer_erreur(e)
            input("Appuyez sur entrée pour continuer...")

        except PiegeError:
            print("\n")
            print(" BOOM ! Tu as marché sur un piège (floko) ")
            print("🔄 Retour à la case départ... 🔄")
            
            # Petite pause de 2 secondes de penalité sur le timer 
            time.sleep(2) 
            
            # Suppression du piege 
            self.grille[nouvelle_y, nouvelle_x] = 0

            # On recherche les coordonnées du Départ (le chiffre 2 dans la grille numpy)
            pos_y, pos_x = np.where(self.grille == 2)
            
            # On téléporte le joueur de force à ces coordonnées
            self.pos_joueur = [int(pos_y[0]), int(pos_x[0])]

        return "Continue"
