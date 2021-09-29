from Node import Node
from Cell import Cell
from Grid import Grid


class Robot:
    def __init__(self, posX, posY, grid) -> None:
        self.posX = posX
        self.posY = posY
        self.intent = ""
        self.expected_grid = [[Cell(0, 0, i, j) for i in range(grid.get_cols())]
                              for j in range(grid.get_rows())]

    def get_posX(self) -> int:
        return self.posX

    def get_posY(self) -> int:
        return self.posY

    def get_expected_grid(self) -> Grid:
        return self.expected_grid

    def get_intent(self):
        return self.intent

    def set_posX(self, X: int) -> None:
        self.posX = X

    def set_posY(self, Y: int) -> None:
        self.posY = Y

    def set_expected_grid(self, cell_posX: int, cell_posY: int, cell: Cell) -> None:
        self.expected_grid.set_cell(cell_posX, cell_posY, cell)

    def __str__(self) -> str:
        return "Le robot est situé à l'emplacement :  {self.posX} , {self.posY}".format(self=self)

    def move_left(self) -> None:
        if self.posX > 0:
            self.posX = self.posX-1

    def move_right(self) -> None:
        if self.posX < 4:
            self.posX = self.posX+1

    def move_up(self) -> None:
        if self.posY > 0:
            self.posY = self.posY-1

    def move_down(self) -> None:
        if self.posY < 4:
            self.posY = self.posY+1

    def a_star(self, grid: Grid) -> Node:
        node_start = Node(grid.getCell(
            self.get_posX(), self.get_posY()))
        node_start.affect_heuristique(self)
        node_list = []
        node_list.append(node_start)
        while self.goal_reached(node_list[0]) == False:
            node_tmp = node_list[0]
            node_list.remove(node_list[0])
            new_nodes = node_tmp.expand(self.get_expected_grid(), self)
            for node in new_nodes:
                node_list.append(node)
            node_list.sort()
        return node_list[0]

    def goal(self) -> Cell:
        goal = Cell()
        return goal
