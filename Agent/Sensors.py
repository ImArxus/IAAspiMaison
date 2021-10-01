from Environment.Node import Node
from Environment.Grid import Grid
from Environment.Cell import Cell

# Classe permettant de représenter les capteurs de l'agent
class Sensors:

    # Constructeur
    def __init__(self, robot) -> None:
        self.robot = robot

    # Initialise les actions à effectuer par le robot en fonction de l'algorithme choisi (informé ou non informé)
    def generate_actions(self) -> None:
        nodes: Node
        generated_actions: list[str] = []
        action = "start"
        # Récupère le noeud avec ses parents du chemin le plus court pour aspirer la poussière
        nodes = self.a_star(self.robot.get_expected_grid())
        # Inverse l'ordre des actions puisque a_star renvoie d'abord le noeud le plus bas
        actions = self.actions_in_nodes(nodes)
        actions.reverse()
        # Supprime le premier noeud, qui possède une action vide ("")
        del actions[0]
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
        # Liste des noeuds visités
        nodes_list: list[Node] = []
        nodes_list.append(node)
        # Tant que le robot n'a pas atteint son objectif on continue
        while self.goal_reached(nodes_list[0]) == False:
            node = nodes_list[0]
            nodes_list.remove(nodes_list[0])
            # Cherche la liste de noeuds non visites voisins a celui actuel
            new_nodes = node.expand(self.robot.get_expected_grid(), self.robot)
            nodes_list.extend(new_nodes)
            # Trie les noeuds en fonction de leur coût en énergie et de la distance par rapport à la cellule cible
            nodes_list.sort(
                key=lambda x: x.get_energy_cost() + x.get_heuristique())
        return nodes_list[0]

    # Calcul de la performance du robot apres avoir effectué l'action donnée en paramètre
    # Chaque action coute 1 de perfomance
    def perfomance_after_action(self, cell: Cell, action: str) -> int:
        performance = 0
        if action == "clean":
            performance -= 1
            if self.robot.get_expected_grid().get_cell(cell.get_actual_cell().get_posX(), cell.get_actual_cell().get_posY()).get_jewel() > 0:
                performance -= 50  # Si on aspire un bijou => malus
            if self.robot.get_expected_grid().get_cell(cell.get_actual_cell().get_posX(), cell.get_actual_cell().get_posY()).get_dust() > 0:
                performance += 25  # Si on aspire la poussière => bonus
        elif action == "grab":
            performance += 9  # +10 -1 => pour avoir recupere un bijou au lieu de l aspirer
        elif action == "left" or "right" or "up" or "down":
            performance -= 1
        return performance

    # Fonction indiquant si la cellule avec la poussière a été atteinte de manière optimale (performance)
    def goal_reached(self, node: Node) -> bool:
        performance_after_action: int = 0
        action = "start"
        # Parcours chaque noeud pour calculer la performance de leur action
        while action != "":
            action = node.get_action()
            performance_after_action += self.perfomance_after_action(
                node.get_actual_cell(), action)
            node = node.get_parent()
        estimated_total = performance_after_action + self.robot.get_performance()
        if estimated_total > self.robot.get_performance():
            return True
        return False

    # Fonction retournant la cellule la plus proche contenant de la poussière
    def goal(self) -> Cell:
        cells_with_dust: list[Cell] = []
        # Récupère toutes les cellules contenant de la poussiere
        for i in range(self.robot.get_expected_grid().get_rows()):
            for j in range(self.robot.get_expected_grid().get_cols()):
                if self.robot.get_expected_grid().get_cell(j, i).get_dust() > 0:
                    cells_with_dust.append(
                        self.robot.get_expected_grid().get_cell(j, i))
        goal = Cell(0, 0, 0, 0)  # Cellule de base
        # Cherche la cellule la plus proche parmi celles contenant de la poussière
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

    def contains(self, list: list[Cell], cell: Cell) -> bool:
        for cell_containing in list:
            if (cell_containing.get_posX() == cell.get_posX()) & (cell_containing.get_posY() == cell.get_posY()):
                return True
        return False

    # Fonction d'analyse non informée de la grille
    def analyse_grid(self, cell: Cell) -> Cell:
        node_studied: list[Cell] = self.robot.get_nodeStudied() # Ajout de la cellule actuelle dans la liste de celles étudiées
        node_studied.append(self.robot.get_expected_grid().get_cell(
            cell.get_posX(), cell.get_posY()))
        self.robot.set_nodeStudied(node_studied)
        cell_toVisit: list[Cell] = self.robot.get_cellToVisit() # Suppression de la cellule actuelle des cellules à visiter afin d'éviter des traitements double
        del cell_toVisit[0] 
        self.robot.set_cellToVisit(cell_toVisit)
        
        # Si la cellule actuelle possède de la poussière ou des bijoux, la retourner afin que l'agent y effectue une action
        if (self.robot.get_expected_grid().get_cell(cell.get_posX(), cell.get_posY()).get_dust() == 1) | (self.robot.get_expected_grid().get_cell(cell.get_posX(), cell.get_posY()).get_jewel() == 1):
            return self.robot.get_expected_grid().get_cell(cell.get_posX(), cell.get_posY())
        else: # Récursivité
            node_studied = self.robot.get_nodeStudied()
            cell_toVisit = self.robot.get_cellToVisit()
            # Analyse de la cellule située en haut
            if (cell.get_posY()-1 > 0):
                newCell = self.robot.get_expected_grid().get_cell(
                    cell.get_posX(), cell.get_posY()-1)
                # Vérification qu'elle n'a pas déjà été traitée ou prévue de l'être
                if (~self.contains(node_studied, newCell)) & (~self.contains(cell_toVisit, newCell)):
                    cell_toVisit.append(newCell) # Ajout de la cellule dans celles à visiter
                    self.robot.set_cellToVisit(cell_toVisit)
            
            #Traitement similaire pour la cellule en bas
            if (cell.get_posY() < self.robot.get_expected_grid().get_rows()-1):
                newCell = self.robot.get_expected_grid().get_cell(
                    cell.get_posX(), cell.get_posY()+1)
                if (~self.contains(node_studied, newCell)) & (~self.contains(cell_toVisit, newCell)):
                    cell_toVisit.append(newCell)
                    self.robot.set_cellToVisit(cell_toVisit)
            
            #Traitement similaire pour la cellule à gauche
            if (cell.get_posX() > 0):
                newCell = self.robot.get_expected_grid().get_cell(
                    cell.get_posX()-1, cell.get_posY())
                if (~self.contains(node_studied, newCell)) & (~self.contains(cell_toVisit, newCell)):
                    cell_toVisit.append(newCell)
                    self.robot.set_cellToVisit(cell_toVisit)
            
            #Traitement similaire pour la cellule à droite
            if (cell.get_posX() < self.robot.get_expected_grid().get_cols()-1):
                newCell = self.robot.get_expected_grid().get_cell(
                    cell.get_posX()+1, cell.get_posY())
                if (~self.contains(node_studied, newCell)) & (~self.contains(cell_toVisit, newCell)):
                    cell_toVisit.append(newCell)
                    self.robot.set_cellToVisit(cell_toVisit)

            return None

    # Calcul de la distance par rapport à la cellule d'arrivée pour l'algo non informé
    # Retourne la liste des actions à effectuer pour atteindre la cellule d'arrivée
    def calcul_destination_to_cell(self, cellArrival: Cell) -> None:
        listToReturn: list[str] = []
        posX: int = self.robot.get_posX()
        print(posX)
        posY: int = self.robot.get_posY()
        print(posY)
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
        self.robot.set_actions_expected(listToReturn)
