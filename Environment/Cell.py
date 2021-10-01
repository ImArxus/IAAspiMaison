from __future__ import annotations

# Classe permettant la représentation d'une cellule de la grille (représentation d'une pièce du manoir)
class Cell:

    # Constructeur
    def __init__(self, dust: int, jewel: int, posX: int, posY: int) -> None:
        self.dust = dust # Représentation de si la pièce contient de la saleté (0: oui, 1: non)
        self.jewel = jewel # Représentation de si la pièce contient des bijoux (0: oui, 1: non)
        self.posX = posX # Représentation de la position horizontale de la cellule sur la grille
        self.posY = posY # Représentation de la position verticale de la cellule sur la grille

    # Getters et setters
    def get_dust(self) -> int:
        return self.dust

    def get_jewel(self) -> int:
        return self.jewel

    def get_posX(self) -> int:
        return self.posX

    def get_posY(self) -> int:
        return self.posY

    def set_posX(self, posX: int) -> None:
        self.posX = posX

    def set_posY(self, posY: int) -> None:
        self.posY = posY

    def set_dust(self, dust: int) -> None:
        self.dust = dust

    def set_jewel(self, jewel: int) -> None:
        self.jewel = jewel
    
    # Fonction permettant d'afficher la position de la cellule sous la forme positionXposition Y (exp:'00')
    def get_pos(self) -> str:
        return str(self.posX)+""+str(self.posY)
    
     # Fonction d'affichage de la cellule sous la forme [valeur de la poussière/valeur des bijoux] in (positionX,position Y)
    def __str__(self) -> str:
        return "[" + str(self.dust) + "/" + str(self.jewel) + "] in (" + str(self.posX) + "/" + str(self.posY) + ")"
    
    # Fonction permettant de cloner une cellule et ainsi d'économiser du temps, utilisé pour l'algorithme de recherche informé
    def clone(self) -> Cell:
        return Cell(self.dust, self.jewel, self.posX, self.posY)
