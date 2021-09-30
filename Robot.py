from Node import Node
from Cell import Cell
from Grid import Grid


class Robot:
    def __init__(self, posX: int, posY: int, grid: Grid) -> None:
        self.posX = posX
        self.posY = posY
        self.actions_expected: list[str] = []
        self.expected_grid = grid
        self.performance = 0

    def get_posX(self) -> int:
        return self.posX

    def get_posY(self) -> int:
        return self.posY

    def get_expected_grid(self) -> Grid:
        return self.expected_grid

    def get_actions_expected(self):
        return self.actions_expected

    def set_posX(self, X: int) -> None:
        self.posX = X

    def set_posY(self, Y: int) -> None:
        self.posY = Y

    def set_cell_in_expected_grid(self, cell_posX: int, cell_posY: int, cell: Cell) -> None:
        self.expected_grid.set_cell(cell_posX, cell_posY, cell)

    def set_actions_expected(self, actions_expected: list[str]) -> None:
        self.actions_expected = actions_expected

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

    def generate_actions(self, informed_search: bool) -> None:
        nodes: Node
        if informed_search:
            nodes = self.a_star(self.expected_grid)
        else:
            print("Uninfomred search")  # TODO
        generated_actions: list[str] = []
        action = "start"
        actions = self.reverse_nodes(nodes)
        actions.reverse()
        del actions[0]
        action = "start"
        while action != "":
            if len(actions) > 0:
                action = actions[0]
                generated_actions.append(action)
                del actions[0]
            else:
                action = ""
        self.actions_expected = generated_actions

    def reverse_nodes(self, nodes: Node) -> list[str]:
        actions: list[str] = []
        while(nodes.get_parent() != None):
            actions.append(nodes.get_action())
            nodes = nodes.get_parent()
        return actions

    def a_star(self, grid: Grid) -> Node:
        node = Node(grid.get_cell(self.posX, self.posY), Node(
            None, None, None, -1, 0, 0), "", 0, 0, 0)  # Noeud de départ du robot
        # node.affect_heuristique(self)
        nodes_list: list[Node] = []
        nodes_list.append(node)
        while self.goal_reached(nodes_list[0]) == False:
            node = nodes_list[0]
            nodes_list.remove(nodes_list[0])
            new_nodes = node.expand(self.expected_grid, self)
            for node in new_nodes:
                nodes_list.append(node)
            node_goal = Node(self.goal(), Node(
                None, None, None, -1, 0, 0), "", 0, 0, 0)
            nodes_list.sort(key=lambda x: x.get_energy_cost() + x.distance(
                node_goal.get_actual_cell().get_posX(), node_goal.get_actual_cell().get_posY()))
        return nodes_list[0]

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
        performance_after_action: int = 0
        action = node.get_action()
        while action != "":
            action = node.get_action()
            performance_after_action += self.perfomance_after_action(
                node, action)
            node = node.get_parent()
        estimated_total = performance_after_action + self.performance
        if estimated_total > self.performance:
            return True
        return False

    # Fonction retournant la cellule la plus proche contenant de la poussière
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
                robot_cell = self.expected_grid.get_cell(
                    self.posX, self.posY)
                robot_node = Node(robot_cell, Node(
                    None, None, None, -1, 0, 0), "", 0, 0, 0)
                if robot_node.distance(cell.get_posX(), cell.get_posY()) < robot_node.distance(goal.get_posX(), goal.get_posY()):
                    goal = cell
        return goal

    def move_Robot(self, cellArrival: Cell) -> None:
        while self.get_posX() < cellArrival.get_posX():
            self.move_right()
        while self.get_posX() > cellArrival.get_posX():
            self.move_left()
        while self.get_posY() < cellArrival.get_posY():
            self.move_down()
        while self.get_posY() > cellArrival.get_posY():
            self.move_up()
