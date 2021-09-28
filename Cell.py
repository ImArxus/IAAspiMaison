class Cell:

    def __init__(self, dust, jewel, posX, posY) -> None:
        self.dust = dust
        self.jewel = jewel
        self.posX = posX
        self.posY = posY

    def __str__(self) -> str:
        return "[" + str(self.dust) + "/" + str(self.jewel) + "]"

    def get_dust(self) -> int:
        return self.dust

    def get_jewel(self) -> int:
        return self.jewel

    def get_posX(self) -> int:
        return self.posX

    def get_posY(self) -> int:
        return self.posY

    def set_posX(self, posX) -> None:
        self.posX = posX

    def set_posY(self, posY) -> None:
        self.posY = posY

    def set_dust(self, dust) -> None:
        self.dust = dust

    def set_jewel(self, jewel) -> None:
        self.jewel = jewel

    def clone(self):
        return Cell(self.get_dust(), self.get_jewel(), self.get_posX(), self.get_posY())
