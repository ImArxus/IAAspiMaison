from Agent.Robot import Robot
from Environment.Cell import Cell
from Position import Position
from Environment.Grid import Grid
import random

class AlgoNI:

    def __init__(self, grid: Grid, robot:Robot, nodeStudied:list[str],nodeToVisit:list[str],cellToVisit:list[Position]) -> None:
        self.grid = grid
        self.robot = robot
        self.nodeStudied=nodeStudied # Liste des noeuds déjà étudiés
        self.nodeToVisit=nodeToVisit # Liste des noeuds encore à étudier
        self.cellToVisit=cellToVisit # Liste des positions à explorer
    
    # Getters and setters
    def get_nodeStudied(self) -> list[str]:
        return self.nodeStudied

    def set_nodeStudied(self, nodeStudied:list[str]) -> None:
        self.nodeStudied = nodeStudied
    
    def get_nodeToVisit(self) -> list[str]:
        return self.nodeToVisit

    def set_nodeToVisit(self, nodeToVisit:list[str]) -> None:
        self.nodeToVisit = nodeToVisit

    def get_cellToVisit(self) -> list[Position]:
        return self.cellToVisit

    def set_cellToVisit(self, cellToVisit:list[Position]) -> None:
        self.cellToVisit = cellToVisit

    #Insertion de poussière de manière aléatoire (test pour meziane)
    def insertDustTest(self)-> None:
        rdm1:int = random.randint(0,self.grid.get_cols()-1)
        rdm2:int = random.randint(0,self.grid.get_rows()-1)
        dustcell: Cell = self.grid.get_cell(rdm1,rdm2)
        dustcell.set_dust(1)

    #Fonction d'analyse de la grille
    def analyseGrid(self,pos:Position)-> Cell:
        self.nodeStudied.append(pos.get_pos())
        del self.nodeToVisit[0]
        del self.cellToVisit[0]

        if (self.grid.get_cell(pos.get_posX(),pos.get_posY()).get_dust() == 1)|(self.grid.get_cell(pos.get_posX(),pos.get_posY()).get_jewel() == 1):
            return self.grid.get_cell(pos.get_posX(),pos.get_posY())
        else:
            newPos = Position(pos.get_posX(), pos.get_posY()-1)
            if (pos.get_posY()>0)&(~self.nodeStudied.__contains__(newPos.get_pos()))&(~self.nodeToVisit.__contains__(newPos.get_pos())):
                self.nodeToVisit.append(newPos.get_pos())
                self.cellToVisit.append(newPos)

            newPos = Position(pos.get_posX(), pos.get_posY()+1)
            if  (pos.get_posY()<self.grid.get_rows()-1) &(~self.nodeStudied.__contains__(newPos.get_pos()))&(~self.nodeToVisit.__contains__(newPos.get_pos())):
                self.nodeToVisit.append(newPos.get_pos())
                self.cellToVisit.append(newPos)

            newPos = Position(pos.get_posX()-1, pos.get_posY())
            if  (pos.get_posX()>0) &(~self.nodeStudied.__contains__(newPos.get_pos()))&(~self.nodeToVisit.__contains__(newPos.get_pos())):
                self.nodeToVisit.append(newPos.get_pos())
                self.cellToVisit.append(newPos)

            newPos = Position(pos.get_posX()+1, pos.get_posY())
            if  (pos.get_posX()<self.grid.get_cols()-1) &(~self.nodeStudied.__contains__(newPos.get_pos()))&(~self.nodeToVisit.__contains__(newPos.get_pos())):
                self.nodeToVisit.append(newPos.get_pos())
                self.cellToVisit.append(newPos)

            return None 