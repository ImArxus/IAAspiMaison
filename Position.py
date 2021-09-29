class Position:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

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

    def __str__(self) -> str:
        return "({self.posX}, {self.posY})".format(self=self)