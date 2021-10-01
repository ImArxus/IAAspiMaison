from Environment.Cell import Cell
from Environment.Grid import Grid
from Agent.Effectors import Effectors
from Agent.Sensors import Sensors

# Classe permettant la représentation d'un objet Robot


class Robot:

    # Constructeur du Robot
    def __init__(self, posX: int, posY: int, grid: Grid) -> None:
        self.posX = posX  # Position horizontale du robot
        self.posY = posY  # Position verticale du robot

        # ETAT MENTAL
        # Liste des actions que le robot devra effectuer pour atteindre son but
        self.actions_expected: list[str] = []
        self.expected_grid = grid  # Grille exploitée par le robot

        self.performance = 0  # Compteur de performances du robot
        self.effectors = Effectors(self)  # Effecteurs du robot
        self.sensors = Sensors(self)  # Capteurs du robot

        # Pour algo non informe
        self.nodeStudied: list[Cell] = []  # Liste des noeuds déjà étudiés
        self.cellToVisit: list[Cell] = []  # Liste des positions à explorer

    # Getters and setters
    def get_posX(self) -> int:
        return self.posX

    def get_posY(self) -> int:
        return self.posY

    def get_expected_grid(self) -> Grid:
        return self.expected_grid

    def get_actions_expected(self) -> list[str]:
        return self.actions_expected

    def get_performance(self) -> int:
        return self.performance

    def get_effectors(self) -> Effectors:
        return self.effectors

    def get_sensors(self) -> Sensors:
        return self.sensors

    def get_nodeStudied(self) -> list[Cell]:
        return self.nodeStudied

    def get_cellToVisit(self) -> list[Cell]:
        return self.cellToVisit

    def set_nodeStudied(self, nodeStudied: list[Cell]) -> None:
        self.nodeStudied = nodeStudied

    def set_cellToVisit(self, cellToVisit: list[Cell]) -> None:
        self.cellToVisit = cellToVisit

    def set_posX(self, X: int) -> None:
        self.posX = X

    def set_posY(self, Y: int) -> None:
        self.posY = Y

    def set_cell_in_expected_grid(self, cell_posX: int, cell_posY: int, cell: Cell) -> None:
        self.expected_grid.set_cell(cell_posX, cell_posY, cell)

    def set_actions_expected(self, actions_expected: list[str]) -> None:
        self.actions_expected = actions_expected

    def set_performance(self, performance: int) -> None:
        self.performance = performance

    # Fonction permettant d'afficher la position actuelle du robot sur la grille
    def __str__(self) -> str:
        return "Robot is in :  {self.posX} , {self.posY}".format(self=self)

    # Fonction permettant de lister les étapes que devra accomplir le robot afin d'atteindre son but
    def calcul_Dest_To_Case(self, cellArrival: Cell) -> None:
        listToReturn: list[str] = []
        posX: int = self.get_posX()
        posY: int = self.get_posY()
        while posX < cellArrival.get_posX():
            listToReturn.append('right')
            posX += 1
        while posX > cellArrival.get_posX():
            listToReturn.append('left')
            posX -= 1
        while posY < cellArrival.get_posY():
            listToReturn.append('down')
            posY += 1
        while posY > cellArrival.get_posY():
            listToReturn.append('up')
            posY -= 1
        if cellArrival.get_dust() == 1:
            listToReturn.append('clean')
        else:
            listToReturn.append('grab')
        self.actions_expected = listToReturn
