
class MouvementInvalideError(Exception):
  
    def __init__(self, message="Mouvement invalide : vous avez percuté un mur."):
        super().__init__(message)

class PiegeError(Exception):
 
    pass
