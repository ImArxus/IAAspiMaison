from Node import Node
from Cell import Cell
from Grid import Grid


class Robot:
    def __init__(self, posX: int, posY: int, grid: Grid) -> None:
        self.posX = posX
        self.posY = posY
        self.action_expected = list[str]
        self.expected_grid = grid
        self.performance = 0

    def get_posX(self) -> int:
        return self.posX

    def get_posY(self) -> int:
        return self.posY

    def get_expected_grid(self) -> Grid:
        return self.expected_grid

    def get_action_expected(self):
        return self.action_expected

    def set_posX(self, X: int) -> None:
        self.posX = X

    def set_posY(self, Y: int) -> None:
        self.posY = Y

    def set_cell_in_expected_grid(self, cell_posX: int, cell_posY: int, cell: Cell) -> None:
        self.expected_grid.set_cell(cell_posX, cell_posY, cell)

    def set_action_expected(self, action_expected: list[str]) -> None:
        self.action_expected = action_expected

    def __str__(self) -> str:
        return "Robot is in :  {self.posX} , {self.posY}".format(self=self)

    def move_left(self) -> None:
        if self.posX > 0:
            self.posX = self.posX-1
            print("Robot has moved left")

    def move_right(self) -> None:
        if self.posX < self.expected_grid.get_cols():
            self.posX = self.posX+1
            print("Robot has moved right")

    def move_up(self) -> None:
        if self.posY > 0:
            self.posY = self.posY-1
            print("Robot has moved up")

    def move_down(self) -> None:
        if self.posY < self.expected_grid.get_rows():
            self.posY = self.posY+1
            print("Robot has moved down")

    def a_star(self, grid: Grid) -> Node:
        node_start = Node(grid.get_cell(self.posX, self.posY))
        node_start.affect_heuristique(self)
        node_list: list[Node] = []
        node_list.append(node_start)
        while self.goal_reached(node_list[0]) == False:
            node_tmp: Node = node_list[0]
            node_list.remove(node_list[0])
            new_nodes = node_tmp.expand(self.expected_grid, self)
            for node in new_nodes:
                node_list.append(node)
            node_list.sort()
        return node_list[0]

    def perfomance_after_action(self, node: Node, action: str) -> int:
        performance = 0
        if action == "clean":
            performance -= 1
            if self.expected_grid.get_cell(node.get_actual_cell().get_posX(), node.get_actual_cell().get_posY()).get_jewel() > 0:
                performance -= 50
            if self.expected_grid.get_cell(node.get_actual_cell().get_posX(), node.get_actual_cell().get_posY()).get_dust() > 0:
                performance += 25
        elif action == "pick up":
            performance += 9  # +10 -1
        elif action == "left" or "right" or "up" or "down":
            performance -= 1
        return performance

    def goal_reached(self, node: Node) -> bool:
        energy_cost: int = 0
        action = node.get_action()
        while action != "":
            action = node.get_action()
            energy_cost += self.perfomance_after_action(node, action)
            node = node.get_parent()
        estimated_total = energy_cost + self.performance
        if estimated_total > self.performance:
            return True
        return False

    def goal(self) -> Cell:
        cells_with_dust: list[Cell] = []
        for i in range(self.expected_grid.get_rows()):
            for j in range(self.expected_grid.get_cols()):
                if self.expected_grid.get_cell(j, i).get_dust() > 0:
                    cells_with_dust.append(
                        self.expected_grid.get_cell(j, i))
        goal = Cell(0, 0, self.posX, self.posY)
        if len(cells_with_dust) > 0:
            goal = cells_with_dust[0]
            for cell in cells_with_dust:
                robot_position = self.expected_grid.get_cell(
                    self.posX, self.posY)
                if robot_position.distance(cell.get_posX(), cell.get_posY()) < robot_position.distance(goal.get_posX(), goal.get_posY()):
                    goal = cell
        return goal
    
    def move_Robot(self,cellArrival:Cell) -> None:
        while self.get_posX()<cellArrival.get_posX():
            self.move_right()
        while self.get_posX()>cellArrival.get_posX():
            self.move_left()
        while self.get_posY()<cellArrival.get_posY():
            self.move_down()
        while self.get_posY()>cellArrival.get_posY():
            self.move_up()