# main.py

from generateurs import GenerateurLabyrinthe
from jeu import JeuLabyrinthe
from utils_fichiers import sauvegarder_labyrinthe

def main():
    print("Génération du labyrinthe en cours...")
    # Dimensions impaires obligatoires pour l'algorithme
    gen = GenerateurLabyrinthe(21, 21) 
    grille = gen.generer_backtracking()

    # Sauvegarde la matrice dans un fichier txt (TP Fichiers)
    sauvegarder_labyrinthe(grille)
    
    jeu = JeuLabyrinthe(grille)
    etat = "Continue"
    
    while etat != "Gagné":
        jeu.afficher()
        choix = input("Déplacement (z=haut, s=bas, q=gauche, d=droite, quit=quitter) : ").lower()
        
        if choix == 'quit':
            print("Partie abandonnée.")
            break
            
        etat = jeu.deplacer(choix)

    if etat == "Gagné":
        jeu.afficher()
        print("\n🏆 FÉLICITATIONS ! Vous avez trouvé la sortie ! 🏆")

if __name__ == "__main__":
    main()