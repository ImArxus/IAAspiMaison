from __future__ import annotations
from Environment.Cell import Cell
from Environment.Grid import Grid

# Classe représentant un noeud, que nous utiliserons pour nos algorithmes
class Node:
    
    # Constructeur
    def __init__(self, actual_cell: Cell, parent: Node, action: str, depth: int, energy_cost: int, heuristique: int) -> None:
        self.actual_cell = actual_cell # Représentation de la cellule que va modéliser le noeud
        self.parent = parent # Représentation du noeud parent
        self.action = action # Représentation de l'action à effectuer
        self.depth = depth # Représentation de la profondeur du noeud
        self.energy_cost = energy_cost # Représentation du coût en énergie pour atteindre ce noeud
        # Représentation de l'heuristique, à savoir la distance par rapport a la case cible
        self.heuristique = heuristique

    # Getters et setters
    def get_actual_cell(self) -> Cell:
        return self.actual_cell

    def get_parent(self) -> Node:
        return self.parent

    def get_action(self) -> str:
        return self.action

    def get_depth(self) -> int:
        return self.depth

    def get_energy_cost(self) -> int:
        return self.energy_cost

    def get_heuristique(self) -> int:
        return self.heuristique

    def set_actual_cell(self, actual_cell: Cell) -> None:
        self.actual_cell = actual_cell

    def set_parent(self, parent: Node) -> None:
        self.parent = parent

    def set_action(self, action: str) -> None:
        self.action = action

    def set_depth(self, depth: int) -> None:
        self.depth = depth

    def set_energy_cost(self, energy_cost: int) -> None:
        self.energy_cost = energy_cost

    def set_heuristique(self, heuristique: int) -> None:
        self.heuristique = heuristique

    # Fonction d'affichage du noeud, ceci en affichant la cellule contenue
    def __str__(self) -> str:
        return "Actual cell : " + self.actual_cell.__str__()

    # Fonction qui indique la distance d'un noeud, dont on lui fournit les coordonnées, jusqu à elle même
    def distance(self, node_posX: int, node_posY: int) -> int:
        distX = self.actual_cell.get_posX() - node_posX
        distY = self.actual_cell.get_posY() - node_posY
        distTot = abs(distX) + abs(distY)
        return distTot  # Distance en nombre de déplacements total

    # Donne la liste des noeuds voisins en fonction des actions possibles
    def expand(self, grid: Grid, robot) -> list:
        successors: list[Node] = []
        actions = self.possible_actions(grid)
        # Cellule la plus proche contenant de la poussière pour ajouter la distance par rapport à celle ci dans l heuristique
        goal = robot.get_sensors().goal()
        for action in actions:
            s = Node(self.position_after_action(action, grid), self,
                     action, self.depth+1, self.parent.get_energy_cost()+1, self.distance(goal.get_posX(), goal.get_posY()))  # Ajoute 1 de profondeur et 1 au coût énergétique global pour chaque action effectuée
            successors.append(s)
        return successors

    # Donne l'état de la cellule apres avoir effectué l'action donnée en paramètre
    def position_after_action(self, action: str, grid: Grid) -> Cell:
        cell_cloned = self.actual_cell.clone()
        if action == "grab":
            cell_cloned.set_jewel(0)
        elif action == "clean":
            cell_cloned.set_dust(0)
        elif action == "up" and cell_cloned.get_posY() > 0:
            cell_cloned = grid.get_cell(
                self.actual_cell.get_posX(), self.actual_cell.get_posY()-1).clone()
        elif action == "down" and cell_cloned.get_posY() < grid.get_rows()-1:
            cell_cloned = grid.get_cell(
                self.actual_cell.get_posX(), self.actual_cell.get_posY()+1).clone()
        elif action == "left" and cell_cloned.get_posX() > 0:
            cell_cloned = grid.get_cell(
                self.actual_cell.get_posX()-1, self.actual_cell.get_posY()).clone()
        elif action == "right" and cell_cloned.get_posX() < grid.get_cols()-1:
            cell_cloned = grid.get_cell(
                self.actual_cell.get_posX()+1, self.actual_cell.get_posY()).clone()
        return cell_cloned

    # Donne la liste des actions possibles par rapport à la cellule actuelle
    def possible_actions(self, grid: Grid) -> list[str]:
        actions = []
        if self.actual_cell.get_dust() > 0:
            actions.append("clean")
        if self.actual_cell.get_jewel() > 0:
            actions.append("grab")
        if self.actual_cell.get_posX() < grid.get_cols():
            actions.append("right")
        if self.actual_cell.get_posX() > 0:
            actions.append("left")
        if self.actual_cell.get_posY() < grid.get_rows():
            actions.append("down")
        if self.actual_cell.get_posY() > 0:
            actions.append("up")
        return actions
