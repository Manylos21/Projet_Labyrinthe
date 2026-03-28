import numpy as np
import random

class GenerateurLabyrinthe:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = np.ones((hauteur, largeur), dtype=int)

    def generer_backtracking(self):
        """1er Algorithme : Backtracking (Longs couloirs)."""
        self.grille.fill(1) # Remplir de murs

        def creuser(y, x):
            directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
            random.shuffle(directions)
            
            for dy, dx in directions:
                nouvelle_y = y + dy
                nouvelle_x = x + dx
                
                if 1 <= nouvelle_y < self.hauteur-1 and 1 <= nouvelle_x < self.largeur-1:
                    if self.grille[nouvelle_y, nouvelle_x] == 1:
                        self.grille[y + dy//2, x + dx//2] = 0
                        self.grille[nouvelle_y, nouvelle_x] = 0
                        creuser(nouvelle_y, nouvelle_x)

        self.grille[1, 1] = 0
        creuser(1, 1)
        self.rendre_imparfait(10) # On ajoute des boucles
        self.placer_depart_arrivee()
        self.placer_pieges(10) # On place 10 pièges intelligents
        return self.grille

    def generer_prim(self):
        """2ème Algorithme : Prim (Beaucoup de culs-de-sac)."""
        self.grille.fill(1) # Remplir de murs
        
        # On commence en haut à gauche
        y_depart, x_depart = 1, 1
        self.grille[y_depart, x_depart] = 0
        
        # Liste pour stocker les murs qu'on peut potentiellement casser
        murs = []
        
        # Fonction locale pour ajouter les murs adjacents à la liste
        def ajouter_murs(y, x):
            directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 1 <= ny < self.hauteur-1 and 1 <= nx < self.largeur-1:
                    if self.grille[ny, nx] == 1:
                        murs.append((y, x, ny, nx)) # (Origine Y, Origine X, Cible Y, Cible X)

        ajouter_murs(y_depart, x_depart)
        
        while murs:
            # On choisit un mur au hasard dans la liste
            index_mur = random.randint(0, len(murs) - 1)
            y_orig, x_orig, y_cible, x_cible = murs.pop(index_mur)
            
            # Si la case derrière le mur n'a pas encore été visitée (c'est un 1)
            if self.grille[y_cible, x_cible] == 1:
                # On casse le mur entre les deux
                self.grille[(y_orig + y_cible)//2, (x_orig + x_cible)//2] = 0
                # On creuse la case cible
                self.grille[y_cible, x_cible] = 0
                
                # On ajoute les nouveaux murs adjacents à notre liste
                ajouter_murs(y_cible, x_cible)

        self.rendre_imparfait(10) # Optionnel sur Prim, mais rend le jeu plus sympa
        self.placer_depart_arrivee()
        return self.grille

    def rendre_imparfait(self, nombre_de_trous=10):
        """Casse des murs au hasard pour créer des chemins multiples."""
        trous_faits = 0
        while trous_faits < nombre_de_trous:
            y = random.randint(1, self.hauteur - 2)
            x = random.randint(1, self.largeur - 2)
            if self.grille[y, x] == 1:
                self.grille[y, x] = 0
                trous_faits += 1

    def placer_depart_arrivee(self):
        """Place l'entrée (2) et la sortie (3)."""
        self.grille[1, 1] = 2 
        self.grille[self.hauteur-2, self.largeur-2] = 3
    def trouver_chemin_principal(self):
        """
        Simule la résolution du labyrinthe pour trouver le chemin gagnant.
        Retourne une liste contenant les coordonnées du bon chemin.
        """
        visites = set()
        chemin_gagnant = []
        
        # On cherche depuis le départ (1,1) jusqu'à l'arrivée
        y_arrivee, x_arrivee = self.hauteur - 2, self.largeur - 2

        def explorer(y, x):
            # Si on a trouvé la sortie
            if y == y_arrivee and x == x_arrivee:
                chemin_gagnant.append((y, x))
                return True
                
            # Si on tape un mur, ou qu'on est déjà passé par là
            if self.grille[y, x] == 1 or (y, x) in visites:
                return False

            # On marque la case comme visitée et on l'ajoute au chemin potentiel
            visites.add((y, x))
            chemin_gagnant.append((y, x))

            # On essaie les 4 directions (Haut, Bas, Gauche, Droite) avec un pas de 1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dy, dx in directions:
                if explorer(y + dy, x + dx):
                    return True # Le bon chemin a été trouvé !

            # Si aucune direction ne mène à la sortie, ce n'est pas le bon chemin
            chemin_gagnant.pop()
            return False

        explorer(1, 1)
        return chemin_gagnant

    def placer_pieges(self, nombre_pieges=5):
        """Place des pièges uniquement sur les mauvais chemins."""
        # 1. On calcule le chemin intouchable
        chemin_interdit = self.trouver_chemin_principal()
        
        pieges_places = 0
        tentatives = 0 # Sécurité pour éviter une boucle infinie s'il n'y a plus de place
        
        while pieges_places < nombre_pieges and tentatives < 1000:
            y = random.randint(1, self.hauteur - 2)
            x = random.randint(1, self.largeur - 2)
            tentatives += 1
            
            # On place un piège si : 
            # - c'est un chemin vide (0)
            # - ce n'est PAS sur le chemin gagnant
            # - ce n'est pas sur le départ (2) ni l'arrivée (3)
            if self.grille[y, x] == 0 and (y, x) not in chemin_interdit:
                self.grille[y, x] = 5
                pieges_places += 1
