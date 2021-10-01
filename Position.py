# Classe permettant de simuler la position d'une cellule
class Position:
    
    # Constructeur
    def __init__(self, posX, posY):
        self.posX = posX # Représentation de la position horizontale
        self.posY = posY # Représentation de la position verticale

    # Getters and setters
    def get_posX(self) -> int:
        return self.posX

    def get_posY(self) -> int:
        return self.posY

    def get_pos(self) -> str:
        return str(self.posX)+""+str(self.posY)

    def set_posX(self, X):
        self.posX = X

    def set_posY(self, Y):
        self.posY = Y
    
    # Fonction d'affichage de la position sous la forme (positionX, positionY) (exp: '00')
    def __str__(self) -> str:
        return "({self.posX}, {self.posY})".format(self=self)
