from Agent.Robot import Robot
from Environment.Cell import Cell
from Environment.Grid import Grid
import random


class AlgoNI:

    def __init__(self, grid: Grid, robot: Robot, nodeStudied: list[Cell], nodeToVisit: list[Cell], cellToVisit: list[Cell]) -> None:
        self.grid = grid
        self.robot = robot
        self.nodeStudied = nodeStudied  # Liste des noeuds déjà étudiés
        self.nodeToVisit = nodeToVisit  # Liste des noeuds encore à étudier
        self.cellToVisit = cellToVisit  # Liste des positions à explorer

    # Getters and setters
    def get_nodeStudied(self) -> list[Cell]:
        return self.nodeStudied

    def set_nodeStudied(self, nodeStudied: list[Cell]) -> None:
        self.nodeStudied = nodeStudied

    def get_nodeToVisit(self) -> list[Cell]:
        return self.nodeToVisit

    def set_nodeToVisit(self, nodeToVisit: list[Cell]) -> None:
        self.nodeToVisit = nodeToVisit

    def get_cellToVisit(self) -> list[Cell]:
        return self.cellToVisit

    def set_cellToVisit(self, cellToVisit: list[Cell]) -> None:
        self.cellToVisit = cellToVisit

    # Insertion de poussière de manière aléatoire (test pour meziane)
    def insertDustTest(self) -> None:
        rdm1: int = random.randint(0, self.grid.get_cols()-1)
        rdm2: int = random.randint(0, self.grid.get_rows()-1)
        dustcell: Cell = self.grid.get_cell(rdm1, rdm2)
        dustcell.set_dust(1)

    # Fonction d'analyse de la grille
    def analyseGrid(self, cell: Cell) -> Cell:
        self.nodeStudied.append(self.grid.get_cell(
            cell.get_posX(), cell.get_posY()))
        del self.nodeToVisit[0]
        del self.cellToVisit[0]

        if (self.grid.get_cell(cell.get_posX(), cell.get_posY()).get_dust() == 1) | (self.grid.get_cell(cell.get_posX(), cell.get_posY()).get_jewel() == 1):
            return self.grid.get_cell(cell.get_posX(), cell.get_posY())
        else:
            if (cell.get_posY()-1 > 0):
                newCell = self.grid.get_cell(
                    cell.get_posX(), cell.get_posY()-1)
                if (~self.nodeStudied.__contains__(newCell)) & (~self.nodeToVisit.__contains__(newCell)):
                    self.nodeToVisit.append(newCell)
                    self.cellToVisit.append(newCell)

            if (cell.get_posY() < self.grid.get_rows()-1):
                newCell = self.grid.get_cell(
                    cell.get_posX(), cell.get_posY()+1)
                if (~self.nodeStudied.__contains__(newCell)) & (~self.nodeToVisit.__contains__(newCell)):
                    self.nodeToVisit.append(newCell)
                    self.cellToVisit.append(newCell)

            if (cell.get_posX() > 0):
                newCell = self.grid.get_cell(
                    cell.get_posX()-1, cell.get_posY())
                if (~self.nodeStudied.__contains__(newCell)) & (~self.nodeToVisit.__contains__(newCell)):
                    self.nodeToVisit.append(newCell)
                    self.cellToVisit.append(newCell)

            if (cell.get_posX() < self.grid.get_cols()-1):
                newCell = self.grid.get_cell(
                    cell.get_posX()+1, cell.get_posY())
                if (~self.nodeStudied.__contains__(newCell)) & (~self.nodeToVisit.__contains__(newCell)):
                    self.nodeToVisit.append(newCell)
                    self.cellToVisit.append(newCell)

            return None
