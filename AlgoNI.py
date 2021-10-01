from Agent.Robot import Robot
from Environment.Cell import Cell
from Position import Position
from Environment.Grid import Grid
import random

class AlgoNI:

    def __init__(self, grid: Grid, robot:Robot) -> None:
        self.grid = grid
        self.robot = robot

    #Insertion de poussière de manière aléatoire (test pour meziane)
    def insertDustTest(self)-> None:
        rdm1:int = random.randint(0,self.grid.get_cols()-1)
        rdm2:int = random.randint(0,self.grid.get_rows()-1)
        dustcell: Cell = self.grid.get_cell(rdm1,rdm2)
        dustcell.set_dust(1)

    #Fonction d'analyse de la grille
    def analyseGrid(self,pos:Position,nodeStudied,nodeToVisit,posToVisit)-> Cell:
        nodeStudied.append(pos.get_pos())
        del nodeToVisit[0]
        del posToVisit[0]

        if (self.grid.get_cell(pos.get_posX(),pos.get_posY()).get_dust() == 1)|(self.grid.get_cell(pos.get_posX(),pos.get_posY()).get_jewel() == 1):
            return self.grid.get_cell(pos.get_posX(),pos.get_posY())
        else:
            newPos = Position(pos.get_posX(), pos.get_posY()-1)
            if (pos.get_posY()>0)&(~nodeStudied.__contains__(newPos.get_pos()))&(~nodeToVisit.__contains__(newPos.get_pos())):
                nodeToVisit.append(newPos.get_pos())
                posToVisit.append(newPos)

            newPos = Position(pos.get_posX(), pos.get_posY()+1)
            if  (pos.get_posY()<self.grid.get_rows()-1) &(~nodeStudied.__contains__(newPos.get_pos()))&(~nodeToVisit.__contains__(newPos.get_pos())):
                nodeToVisit.append(newPos.get_pos())
                posToVisit.append(newPos)

            newPos = Position(pos.get_posX()-1, pos.get_posY())
            if  (pos.get_posX()>0) &(~nodeStudied.__contains__(newPos.get_pos()))&(~nodeToVisit.__contains__(newPos.get_pos())):
                nodeToVisit.append(newPos.get_pos())
                posToVisit.append(newPos)

            newPos = Position(pos.get_posX()+1, pos.get_posY())
            if  (pos.get_posX()<self.grid.get_cols()-1) &(~nodeStudied.__contains__(newPos.get_pos()))&(~nodeToVisit.__contains__(newPos.get_pos())):
                nodeToVisit.append(newPos.get_pos())
                posToVisit.append(newPos)

            return None 