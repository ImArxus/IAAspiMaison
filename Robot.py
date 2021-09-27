class Robot:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def __str__(self):
        return 'Le robot est situé à l emplacement :  {self.posX} , {self.posY}'.format(self=self)

    def moveLeft(self):
        if self.posX >0:
            self.posX=self.posX-1
    
    def moveRight(self):
        if self.posX <4:
            self.posX=self.posX+1
    
    def moveUp(self):
        if self.posY >0:
            self.posY=self.posY-1

    def moveDown(self):
        if self.posY <4:
            self.posY=self.posY+1