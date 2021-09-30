from Environment.Node import Node
from Environment.Grid import Grid
from Environment.Cell import Cell

class Sensors:

    def __init__(self, robot) -> None:
        self.robot = robot

    def generate_actions(self, informed_search: bool) -> None:
        nodes: Node
        if informed_search:
            nodes = self.a_star(self.robot.get_expected_grid())
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
        self.robot.set_actions_expected(generated_actions)

    def reverse_nodes(self, nodes: Node) -> list[str]:
        actions: list[str] = []
        while(nodes.get_parent() != None):
            actions.append(nodes.get_action())
            nodes = nodes.get_parent()
        return actions

    def a_star(self, grid: Grid) -> Node:
        node = Node(grid.get_cell(self.robot.get_posX(), self.robot.get_posY()), Node(
            None, None, None, -1, 0, 0), "", 0, 0, 0)  # Noeud de départ du robot
        # node.affect_heuristique(self)
        nodes_list: list[Node] = []
        nodes_list.append(node)
        while self.goal_reached(nodes_list[0]) == False:
            node = nodes_list[0]
            nodes_list.remove(nodes_list[0])
            new_nodes = node.expand(self.robot.get_expected_grid(), self)
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
            if self.robot.get_expected_grid().get_cell(node.get_actual_cell().get_posX(), node.get_actual_cell().get_posY()).get_jewel() > 0:
                performance -= 50
            if self.robot.get_expected_grid().get_cell(node.get_actual_cell().get_posX(), node.get_actual_cell().get_posY()).get_dust() > 0:
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
        estimated_total = performance_after_action + self.robot.get_performance()
        if estimated_total > self.robot.get_performance():
            return True
        return False

    # Fonction retournant la cellule la plus proche contenant de la poussière
    def goal(self) -> Cell:
        cells_with_dust: list[Cell] = []
        for i in range(self.robot.get_expected_grid().get_rows()):
            for j in range(self.robot.get_expected_grid().get_cols()):
                if self.robot.get_expected_grid().get_cell(j, i).get_dust() > 0:
                    cells_with_dust.append(
                        self.robot.get_expected_grid().get_cell(j, i))
        goal = Cell(0, 0, self.robot.get_posX(), self.robot.get_posY())
        if len(cells_with_dust) > 0:
            goal = cells_with_dust[0]
            for cell in cells_with_dust:
                robot_cell = self.robot.get_expected_grid().get_cell(
                    self.robot.get_posX(), self.robot.get_posY())
                robot_node = Node(robot_cell, Node(
                    None, None, None, -1, 0, 0), "", 0, 0, 0)
                if robot_node.distance(cell.get_posX(), cell.get_posY()) < robot_node.distance(goal.get_posX(), goal.get_posY()):
                    goal = cell
        return goal
