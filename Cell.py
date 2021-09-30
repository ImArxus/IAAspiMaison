from __future__ import annotations


class Cell:

    def __init__(self, dust: int, jewel: int, posX: int, posY: int) -> None:
        self.dust = dust
        self.jewel = jewel
        self.posX = posX
        self.posY = posY

    def __str__(self) -> str:
        return "[" + str(self.dust) + "/" + str(self.jewel) + "] in (" + str(self.posX) + "/" + str(self.posY) + ")"

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
        return Cell(self.dust, self.jewel, self.posX, self.posY)
