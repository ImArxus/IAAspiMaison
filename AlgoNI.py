from Agent.Robot import Robot
from Environment.Grid import Grid
from Environment.Cell import Cell
import random

# Classe permettant la représentation de l'algorithme de recherche non informé 
class AlgoNI:

    # Constructeur de l'algorithme non informé
    def __init__(self, grid: Grid, robot: Robot) -> None:
        self.grid = grid # Grille sur laquelle l'algorithme va agir
        self.robot = robot # Robot à déplacer et à faire agir

    # Fonction de test permettant l'insertion de poussière de manière aléatoire (à suppr plus tard)
    def insertDustTest(self) -> None:
        rdm1: int = random.randint(0, self.grid.get_cols()-1)
        rdm2: int = random.randint(0, self.grid.get_rows()-1)
        dustcell: Cell = self.grid.get_cell(rdm1, rdm2)
        dustcell.set_dust(1)

    # Fonction d'analyse de la grille retournant la cellule à atteindre
    def analyseGrid(self, cell:Cell, nodeStudied, nodeToVisit, posToVisit) -> Cell:
        nodeStudied.append(cell.get_pos()) # Ajout de la cellule dans celles déjà visitées
        del nodeToVisit[0] # Suppression de la cellule que nous testons actuellement de celles à tester
        del posToVisit[0]

        if (self.grid.get_cell(cell.get_posX(), cell.get_posY()).get_dust() == 1) | (self.grid.get_cell(cell.get_posX(), cell.get_posY()).get_jewel() == 1):
            # Si la cellule contient de la saleté ou des bijoux la retourner
            return self.grid.get_cell(cell.get_posX(), cell.get_posY())
        else: # Sinon analyse des cellules voisines
            cellR = self.grid.get_cell(cell.get_posX(),cell.get_posY()-1) # Détermination de si la cellule en haut existe et n'a pas été déjà visitée
            if (cell.get_posY() > 0) & (~nodeStudied.__contains__(cellR.get_pos())) & (~nodeToVisit.__contains__(cellR.get_pos())):
                nodeToVisit.append(cellR.get_pos()) # L'ajouter à la liste des cellules à visiter pour obtenir l'ordre BFS
                posToVisit.append(cellR)

            cellR = self.grid.get_cell(cell.get_posX(),cell.get_posY()+1) # Même idée pour la cellule en bas
            if (cell.get_posY() < self.grid.get_rows()-1) & (~nodeStudied.__contains__(cellR.get_pos())) & (~nodeToVisit.__contains__(cellR.get_pos())):
                nodeToVisit.append(cellR.get_pos())
                posToVisit.append(cellR)

            cellR = self.grid.get_cell(cell.get_posX()-1,cell.get_posY()) # Même idée pour la cellule à gauche
            if (cell.get_posX() > 0) & (~nodeStudied.__contains__(cellR.get_pos())) & (~nodeToVisit.__contains__(cellR.get_pos())):
                nodeToVisit.append(cellR.get_pos())
                posToVisit.append(cellR)

            cellR = self.grid.get_cell(cell.get_posX()+1,cell.get_posY()) # Même idée pour la cellule à droite
            if (cell.get_posX() < self.grid.get_cols()-1) & (~nodeStudied.__contains__(cellR.get_pos())) & (~nodeToVisit.__contains__(cellR.get_pos())):
                nodeToVisit.append(cellR.get_pos())
                posToVisit.append(cellR)

            return None # Retourner une cellule vide si la cellule actuelle n'était pas celle cherchée, de cette manière on peut analyser les autres cellules de la file
