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