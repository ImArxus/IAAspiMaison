class Cell:

    def __init__(self, dust, jewel, posX, posY) -> None:
        self.dust = dust
        self.jewel = jewel
        self.posX = posX
        self.posY = posY

    def __str__(self) -> str:
        return "[" + str(self.dust) + "/" + str(self.jewel) + "]"

    def get_dust(self):
        return self.dust

    def get_jewel(self):
        return self.jewel

    def get_posX(self):
        return self.posX

    def get_posY(self):
        return self.posY

    def set_posX(self, posX):
        self.posX = posX

    def set_posY(self, posY):
        self.posY = posY

    def set_dust(self, dust):
        self.dust = dust

    def set_jewel(self, jewel):
        self.jewel = jewel

    def clone(self) -> Cell:
        return Cell(self.get_dust(), self.get_jewel(), self.get_posX(), self.get_posY())

    def distance(self, cellPosX,
                 cellPosY):  ##----- Fonction qui indique la distance d'une cellule dont on lui fournit les coordonnées jusqu'a elle même -----#
        distX = self.posX - cellPosX
        distY = self.posY - cellPosY
        distTot = abs(distX) + abs(distY)
        return distTot  ##--- distance en nombre de déplacement total---##
