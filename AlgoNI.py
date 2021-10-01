from Agent.Robot import Robot
from Environment.Cell import Cell
from Position import Position
from Environment.Grid import Grid
import random

# Classe permettant de modéliser l'algorithme de recherche non informée BFS (Breadth-First Search)
class AlgoNI:
    
    # Constructeur
    def __init__(self, grid: Grid, robot:Robot, nodeStudied:list[str],nodeToVisit:list[str],cellToVisit:list[Position]) -> None:
        self.grid = grid # Représente la grille sur laquelle agit l'algorithme
        self.robot = robot # Représente le robot sur lequel agit l'algorithme
        self.nodeStudied=nodeStudied # Représente la liste des noeuds déjà étudiés sous la forme de liste de str contenant les positions des cellules visitées (exp: '02')
        self.nodeToVisit=nodeToVisit # Représente la liste des noeuds à étudier sous la forme de liste de str contenant les positions des cellules à visiter (exp: '02')
        self.cellToVisit=cellToVisit # Représente la liste des cellules déjà étudiés sous la forme de liste de Cell
    
    # Getters and setters
    def get_nodeStudied(self) -> list[str]:
        return self.nodeStudied

    def set_nodeStudied(self, nodeStudied:list[str]) -> None:
        self.nodeStudied = nodeStudied
    
    def get_nodeToVisit(self) -> list[str]:
        return self.nodeToVisit

    def set_nodeToVisit(self, nodeToVisit:list[str]) -> None:
        self.nodeToVisit = nodeToVisit

    def get_cellToVisit(self) -> list[Position]:
        return self.cellToVisit

    def set_cellToVisit(self, cellToVisit:list[Position]) -> None:
        self.cellToVisit = cellToVisit

    # Insertion de poussière de manière aléatoire (test pour algoritme non informée)
    def insertDustTest(self)-> None:
        rdm1:int = random.randint(0,self.grid.get_cols()-1)
        rdm2:int = random.randint(0,self.grid.get_rows()-1)
        dustcell: Cell = self.grid.get_cell(rdm1,rdm2)
        dustcell.set_dust(1)

    # Fonction d'analyse de la grille, prend en paramètre la position de la cellule à étudier
    # Retourne soit une cellule sur laquelle l'agent devra agir soit une cellule vide, ceci reflétant que la cellule actuelle n'a pas besoin d'action
    def analyseGrid(self,pos:Position)-> Cell:
        self.nodeStudied.append(pos.get_pos())
        del self.nodeToVisit[0] # Supression de la cellule qui est en train d'être testée de celles à visiter, afin d'éviter des  appels de méthodes inutiles plus tard
        del self.cellToVisit[0]
        
        # Test afin de savoir si la cellule actuelle contient de la saleté ou un bijou, si oui la retourner
        if (self.grid.get_cell(pos.get_posX(),pos.get_posY()).get_dust() == 1)|(self.grid.get_cell(pos.get_posX(),pos.get_posY()).get_jewel() == 1):
            return self.grid.get_cell(pos.get_posX(),pos.get_posY())
        # Récursivité afin de trouver une nouvelle cellule à tester
        else:
            # Test de la cellule située en haut
            newPos = Position(pos.get_posX(), pos.get_posY()-1)
            # Vérification de l'existence de la cellule et qu'elle n'a pas déja prévue d'être étudiée ou été étudiée
            if (pos.get_posY()>0)&(~self.nodeStudied.__contains__(newPos.get_pos()))&(~self.nodeToVisit.__contains__(newPos.get_pos())):
                self.nodeToVisit.append(newPos.get_pos()) # Ajout de la cellule dans la liste des cellules à visiter, mise en place de récursivité poiur trouver la cellule sur laquelle agir la plus proche
                self.cellToVisit.append(newPos)
            
            # Logique similaire pour la cellule en bas
            newPos = Position(pos.get_posX(), pos.get_posY()+1)
            if  (pos.get_posY()<self.grid.get_rows()-1) &(~self.nodeStudied.__contains__(newPos.get_pos()))&(~self.nodeToVisit.__contains__(newPos.get_pos())):
                self.nodeToVisit.append(newPos.get_pos())
                self.cellToVisit.append(newPos)
            
            # Logique similaire pour la cellule à gauche
            newPos = Position(pos.get_posX()-1, pos.get_posY())
            if  (pos.get_posX()>0) &(~self.nodeStudied.__contains__(newPos.get_pos()))&(~self.nodeToVisit.__contains__(newPos.get_pos())):
                self.nodeToVisit.append(newPos.get_pos())
                self.cellToVisit.append(newPos)
            
             # Logique similaire pour la cellule à droite
            newPos = Position(pos.get_posX()+1, pos.get_posY())
            if  (pos.get_posX()<self.grid.get_cols()-1) &(~self.nodeStudied.__contains__(newPos.get_pos()))&(~self.nodeToVisit.__contains__(newPos.get_pos())):
                self.nodeToVisit.append(newPos.get_pos())
                self.cellToVisit.append(newPos)
            
            # Retour d'une cellule vide afin de continuer le traitement
            return None
