from Cell import Cell
from Grid import Grid
from Robot import Robot
from Node import Node


class Node:

    def __init__(self, actualCell: Cell, parent: Node, action: str, depth: int, cost: int, heuristique: int) -> None:
        self.actualCell = actualCell
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost
        self.heuristique = heuristique

    def __str__(self) -> str:
        return "Actual cell : " + self.actualCell.__str__()

    def expand(self, grid: Grid, robot: Robot) -> list:
        successors = []
        actions = self.possible_actions(grid)
        for action in actions:
            s = Node(self.position_after_action(action, grid), self, action,
                     self.depth+1, self.parent.get_cost()+self.cost_action(action), 0)
            self.affect_heuristique(robot)
            successors.append(s)
        return successors

    def position_after_action(self, action: str, grid: Grid) -> Cell:
        cell_cloned = self.actualCell.clone()
        if action == "grab":
            cell_cloned.set_jewel(0)
        elif action == "clean":
            cell_cloned.set_dust(0)
        elif action == "up" and cell_cloned.get_posY() > 0:
            cell_cloned = grid.get_cell(
                self.actualCell.get_posX(), self.actualCell.get_posY()-1).clone()
        elif action == "down" and cell_cloned.get_posY() < grid.get_rows():
            cell_cloned = grid.get_cell(
                self.actualCell.get_posX(), self.actualCell.get_posY()+1).clone()
        elif action == "left" and cell_cloned.get_posX() > 0:
            cell_cloned = grid.get_cell(
                self.actualCell.get_posX()-1, self.actualCell.get_posY()).clone()
        elif action == "down" and cell_cloned.get_posX() < grid.get_cols():
            cell_cloned = grid.get_cell(
                self.actualCell.get_posX()+1, self.actualCell.get_posY()).clone()
        return cell_cloned

    def possible_actions(self, grid: Grid) -> list[str]:
        actions = []
        if self.actualCell.get_dust() > 0:
            actions.append("clean")
        if self.actualCell.get_jewel() > 0:
            actions.append("grab")
        if self.actualCell.get_posX() < grid.get_cols():
            actions.append("right")
        if self.actualCell.get_posX() > 0:
            actions.append("left")
        if self.actualCell.get_posY() < grid.get_rows():
            actions.append("down")
        if self.actualCell.get_posY() > 0:
            actions.append("up")
        return actions
