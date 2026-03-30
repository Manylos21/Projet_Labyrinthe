# main.py

from generateurs import GenerateurLabyrinthe
import time
from jeu import JeuLabyrinthe
from utils_fichiers import sauvegarder_labyrinthe

def demander_difficulte():
  
    while True:
        print("\n" + "="*40)
        print("    BIENVENUE DANS LE LABYRINTHE ")
        print("="*40)
        print("1. Niveau Facile (Algorithme de Prim)")
        print("2. Niveau Difficile (Algorithme de Backtracking)")
        print("3. Quitter")
        print("-" * 40)
        
        try:
            choix = int(input("Choisissez votre difficulté (tapez 1, 2 ou 3) : "))
            
            # Si l'utilisateur tape un autre chiffre que 1 ou 2 ou 3
            if choix not in [1, 2, 3]:
                raise ValueError("VEUILLEZ TAPER UNIQUEMENT 1, 2 OU 3.")
            
            return choix
            
        except ValueError :
            # Si l'utilisateur tape une lettre ou un mauvais chiffre, on gère l'erreur
            print(  "\n[!] Saisie incorrecte : VEUILLEZ TAPER UNIQUEMENT 1, 2 OU 3.\n")

def main():
    choix_difficulte = demander_difficulte()

    if choix_difficulte == 3:
        print("\nFermeture du jeu, A bientôt !")
        return
    
    print("\nGénération du labyrinthe en cours...")
    gen = GenerateurLabyrinthe(21, 21) 
    
    # 2. On génère selon le choix
    if choix_difficulte == 1:
        grille = gen.generer_prim()
        temps_limite = 120
    else:
        grille = gen.generer_backtracking()
        temps_limite = 60

    # Sauvegarde la matrice dans un fichier txt (TP Fichiers)
    sauvegarder_labyrinthe(grille)
    
    jeu = JeuLabyrinthe(grille)
    etat = "Continue"

    # --- DÉBUT DU CHRONOMÈTRE ---
    debut_partie = time.time() # On enregistre l'heure exacte du début

    try:
        while etat != "Gagné":
            # On calcule combien de temps s'est écoulé
            temps_ecoule = time.time() - debut_partie
            temps_restant = int(temps_limite - temps_ecoule)
            
            # Application directe de l'Exercice 2 du TP 1 !
            if temps_restant <= 0:
                raise TimeoutError("Le temps imparti est écoulé !")
                
            jeu.afficher()
            print(f"⏳ Temps restant : {temps_restant} secondes ⏳")
            choix = input("Déplacement (z=haut, s=bas, q=gauche, d=droite, quit=quitter) : ").lower()
            
            if choix == 'quit':
                print("Partie abandonnée. À bientôt !")
                break
                
            etat = jeu.deplacer(choix)
        

        if etat == "Gagné":
            jeu.afficher()
            print("\nFÉLICITATIONS ! Tu as réussi a trouvé la sortie (La chance du débutant)")

    except TimeoutError as e:
        # Si le temps est écoulé (Game Over)
        print("\n" * 2)
        print(f"💀 GAME OVER : {e} 💀")
        print("Le labyrinthe s'est refermé a jamais sur vous (l'important c'est de participé -RIP💀-)")

if __name__ == "__main__":
    main()
