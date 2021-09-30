from Agent.Robot import Robot
from Environment.Grid import Grid
from Environment.Cell import Cell
import random


class AlgoNI:

    def __init__(self, grid: Grid, robot: Robot) -> None:
        self.grid = grid
        self.robot = robot

    # Insertion de poussière de manière aléatoire (test pour meziane)
    def insertDustTest(self) -> None:
        rdm1: int = random.randint(0, self.grid.get_cols()-1)
        rdm2: int = random.randint(0, self.grid.get_rows()-1)
        dustcell: Cell = self.grid.get_cell(rdm1, rdm2)
        dustcell.set_dust(1)

    # Fonction d'analyse de la grille
    def analyseGrid(self, cell:Cell, nodeStudied, nodeToVisit, posToVisit) -> Cell:
        nodeStudied.append(cell.get_pos())
        del nodeToVisit[0]
        del posToVisit[0]

        if (self.grid.get_cell(cell.get_posX(), cell.get_posY()).get_dust() == 1) | (self.grid.get_cell(cell.get_posX(), cell.get_posY()).get_jewel() == 1):
            return self.grid.get_cell(cell.get_posX(), cell.get_posY())
        else:
            cellR = self.grid.get_cell(cell.get_posX(),cell.get_posY()-1)
            if (cell.get_posY() > 0) & (~nodeStudied.__contains__(cellR.get_pos())) & (~nodeToVisit.__contains__(cellR.get_pos())):
                nodeToVisit.append(cellR.get_pos())
                posToVisit.append(cellR)

            cellR = self.grid.get_cell(cell.get_posX(),cell.get_posY()+1)
            if (cell.get_posY() < self.grid.get_rows()-1) & (~nodeStudied.__contains__(cellR.get_pos())) & (~nodeToVisit.__contains__(cellR.get_pos())):
                nodeToVisit.append(cellR.get_pos())
                posToVisit.append(cellR)

            cellR = self.grid.get_cell(cell.get_posX()-1,cell.get_posY())
            if (cell.get_posX() > 0) & (~nodeStudied.__contains__(cellR.get_pos())) & (~nodeToVisit.__contains__(cellR.get_pos())):
                nodeToVisit.append(cellR.get_pos())
                posToVisit.append(cellR)

            cellR = self.grid.get_cell(cell.get_posX()+1,cell.get_posY())
            if (cell.get_posX() < self.grid.get_cols()-1) & (~nodeStudied.__contains__(cellR.get_pos())) & (~nodeToVisit.__contains__(cellR.get_pos())):
                nodeToVisit.append(cellR.get_pos())
                posToVisit.append(cellR)

            return None
