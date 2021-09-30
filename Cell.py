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

    def heuristique(self, listCells): #--- On obtient l'element de la liste le plus proche de la case où on est ---#
        bestCaseToGo = 25
        lowestNbMovement = 11
        i = 0
        for cell in listCells:
            val = self.distance(cell.getPosX, cell.getPosY)
            if val < lowestMovement:
                bestCaseToGo = i
            i += 1
        return bestCaseToGo
