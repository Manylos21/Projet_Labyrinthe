# main.py

from generateurs import GenerateurLabyrinthe
from jeu import JeuLabyrinthe
from utils_fichiers import sauvegarder_labyrinthe

def demander_difficulte():
    """
    Demande la difficulté à l'utilisateur.
    Utilise un bloc try-except pour gérer les erreurs de saisie (ValueError).
    """
    while True:
        print("\n" + "="*40)
        print("    BIENVENUE DANS LE LABYRINTHE ")
        print("="*40)
        print("1. Niveau Facile (Algorithme de Prim)")
        print("2. Niveau Difficile (Algorithme de Backtracking)")
        print("3. Quitter")
        print("-" * 40)
        
        try:
            # On demande un entier 
            choix = int(input("Choisissez votre difficulté (tapez 1, 2 ou 3) : "))
            
            # Si l'utilisateur tape un autre chiffre que 1 ou 2 ou 3
            if choix not in [1, 2, 3]:
                raise ValueError("VEUILLEZ TAPER UNIQUEMENT 1, 2 OU 3.")
            
            return choix
            
        except ValueError :
            # Si l'utilisateur tape une lettre ou un mauvais chiffre, on gère l'erreur
            print(f"\n[!] Saisie incorrecte : VEUILLEZ TAPER UNIQUEMENT 1, 2 OU 3.\n")

def main():
    choix_difficulte = demander_difficulte()

    if choix_difficulte == 3:
        print("\nFermeture du jeu, À bientôt !")
        return
    
    print("\nGénération du labyrinthe en cours...")
    gen = GenerateurLabyrinthe(21, 21) 
    
    # 2. On génère selon le choix
    if choix_difficulte == 1:
        grille = gen.generer_prim()
    else:
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
        print("\nFÉLICITATIONS ! Tu as réussi a trouvé la sortie")

if __name__ == "__main__":
    main()
