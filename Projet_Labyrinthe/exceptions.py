# exceptions.py

class MouvementInvalideError(Exception):
    """
    Exception personnalisée levée quand le joueur tente de traverser un mur
    ou de sortir des limites du labyrinthe.
    """
    def __init__(self, message="Mouvement invalide : vous avez percuté un mur."):
        super().__init__(message)