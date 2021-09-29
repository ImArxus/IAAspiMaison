from __future__ import annotations


class Cell:

    def __init__(self, dust: int, jewel: int, posX: int, posY: int) -> None:
        self.dust = dust
        self.jewel = jewel
        self.posX = posX
        self.posY = posY

    def __str__(self) -> str:
        return "[" + str(self.dust) + "/" + str(self.jewel) + "] in (" + str(self.get_posX()) + "/" + str(self.get_posY()) + ")"

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

    def clone(self) -> Cell:
        return Cell(self.get_dust(), self.get_jewel(), self.get_posX(), self.get_posY())

    # ----- Fonction qui indique la distance d'une cellule dont on lui fournit les coordonnées jusqu'à elle même -----#
    def distance(self, cell_posX: int, cell_posY: int) -> int:
        distX = self.get_posX() - cell_posX
        distY = self.get_posY() - cell_posY
        distTot = abs(distX) + abs(distY)
        return distTot  # --- Distance en nombre de déplacement total---##
