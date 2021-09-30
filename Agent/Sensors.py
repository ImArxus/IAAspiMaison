from Environment.Node import Node
from Environment.Grid import Grid
from Environment.Cell import Cell


class Sensors:

    def __init__(self, robot) -> None:
        self.robot = robot

    # Initialise les actions a effectuer par le robot en fonction de l algorithme choisi (informe ou non informe)
    def generate_actions(self, informed_search: bool) -> None:
        nodes: Node
        generated_actions: list[str] = []
        action = "start"
        if informed_search:
            # Recupere le noeud avec ses parents du chemin le plus court pour aspirer la poussiere
            nodes = self.a_star(self.robot.get_expected_grid())
            # Inverse l ordre des actions puisque a_star renvoie d abord le noeud le plus bas
            actions = self.actions_in_nodes(nodes)
            actions.reverse()
            # Supprime le premier noeud, qui possède une action vide ("")
            del actions[0]
        else:
            print("Uninfomred search")  # TODO
        # Ajoute chaque action contenue dans les noeuds à une liste
        while action != "":
            if len(actions) > 0:
                action = actions[0]
                generated_actions.append(action)
                del actions[0]
            else:
                action = ""
        # Donne la liste d'actions résultante en attribut des capteurs du robot
        self.robot.set_actions_expected(generated_actions)

    # Donne toutes les actions contenues dans le noeud et ses parents
    def actions_in_nodes(self, nodes: Node) -> list[str]:
        actions: list[str] = []
        while(nodes.get_parent() != None):
            actions.append(nodes.get_action())
            nodes = nodes.get_parent()
        return actions

    # Algorithme de recherche vu en cours
    def a_star(self, grid: Grid) -> Node:
        node = Node(grid.get_cell(self.robot.get_posX(), self.robot.get_posY()), Node(
            None, None, None, -1, 0, 0), "", 0, 0, -1)  # Noeud de départ du robot
        # Liste des noeuds visites
        nodes_list: list[Node] = []
        nodes_list.append(node)
        # Tant que le robot n a pas atteint son objectif on continu
        while self.goal_reached(nodes_list[0]) == False:
            node = nodes_list[0]
            nodes_list.remove(nodes_list[0])
            # Cherche la liste de noeuds non visites voisins a celui actuel
            new_nodes = node.expand(self.robot.get_expected_grid(), self.robot)
            nodes_list.extend(new_nodes)
            # Trie les noeuds en fonction de leur cout en energie et de la distance par rapport a la cellule cible
            nodes_list.sort(
                key=lambda x: x.get_energy_cost() + x.get_heuristique())
        return nodes_list[0]

    # Calcul de la performance du robot apres avoir effectue l action donnee en parametre 
    # Chaque action coute 1 de perfomance
    def perfomance_after_action(self, node: Node, action: str) -> int:
        performance = 0
        if action == "clean":
            performance -= 1
            if self.robot.get_expected_grid().get_cell(node.get_actual_cell().get_posX(), node.get_actual_cell().get_posY()).get_jewel() > 0:
                performance -= 50 # Si on aspire un bijou => malus
            if self.robot.get_expected_grid().get_cell(node.get_actual_cell().get_posX(), node.get_actual_cell().get_posY()).get_dust() > 0:
                performance += 25 # Si on aspire la poussiere => bonus
        elif action == "pick up":
            performance += 9  # +10 -1 => pour avoir recupere un bijou au lieu de l aspirer
        elif action == "left" or "right" or "up" or "down":
            performance -= 1
        return performance

    # Fonction indiquant si la cellule avec la poussiere a ete atteinte de maniere optimale (performance)
    def goal_reached(self, node: Node) -> bool:
        performance_after_action: int = 0
        action = "start"
        # Parcours chaque noeud pour calculer la performance de leur action
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
        # Recupere toutes les cellules contenant de la poussiere
        for i in range(self.robot.get_expected_grid().get_rows()):
            for j in range(self.robot.get_expected_grid().get_cols()):
                if self.robot.get_expected_grid().get_cell(j, i).get_dust() > 0:
                    cells_with_dust.append(
                        self.robot.get_expected_grid().get_cell(j, i))
        goal = Cell(0, 0, 0, 0) # Cellule de base
        # Cherche la cellule la plus proche parmi celles contenant de la poussiere
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

    # Calcul de la distance par rapport a la cellule d arrivee pour l algo non informe
    # Retourne la liste des actions a effectuer pour atteindre la cellule d arrivee
    def calcul_dest_to_cell(self, cellArrival: Cell) -> None:
        listToReturn: list[str] = []
        posX: int = self.robot.get_posX()
        posY: int = self.robot.get_posY()
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
