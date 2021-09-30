from Agent.Robot import Robot
from Environment.Grid import Grid
from Environment.Cell import Cell
from Position import Position
import random

# Insertion de poussière de manière aléatoire


def insertDust(gr: Grid) -> None:
    rdm1: int = random.randint(0, grid.get_cols()-1)
    rdm2: int = random.randint(0, grid.get_rows()-1)
    dustcell: Cell = grid.get_cell(rdm1, rdm2)
    dustcell.set_dust(1)


# Création du robot et de la grille
grid = Grid(5, 5)
rbt = Robot(0, 1, grid)

# Fonction d'analyse de la grille
def analyseGrid(gr: Grid, pos: Position) -> Cell:
    nodeStudied.append(pos.get_pos())
    del nodeToVisit[0]
    del posToVisit[0]

    if (gr.get_cell(pos.get_posX(), pos.get_posY()).get_dust() == 1) | (gr.get_cell(pos.get_posX(), pos.get_posY()).get_jewel() == 1):
        return gr.get_cell(pos.get_posX(), pos.get_posY())
    else:
        newPos = Position(pos.get_posX(), pos.get_posY()-1)
        if (pos.get_posY() > 0) & (~nodeStudied.__contains__(newPos.get_pos())) & (~nodeToVisit.__contains__(newPos.get_pos())):
            nodeToVisit.append(newPos.get_pos())
            posToVisit.append(newPos)

        newPos = Position(pos.get_posX(), pos.get_posY()+1)
        if (pos.get_posY() < grid.get_rows()-1) & (~nodeStudied.__contains__(newPos.get_pos())) & (~nodeToVisit.__contains__(newPos.get_pos())):
            nodeToVisit.append(newPos.get_pos())
            posToVisit.append(newPos)

        newPos = Position(pos.get_posX()-1, pos.get_posY())
        if (pos.get_posX() > 0) & (~nodeStudied.__contains__(newPos.get_pos())) & (~nodeToVisit.__contains__(newPos.get_pos())):
            nodeToVisit.append(newPos.get_pos())
            posToVisit.append(newPos)

        newPos = Position(pos.get_posX()+1, pos.get_posY())
        if (pos.get_posX() < grid.get_cols()-1) & (~nodeStudied.__contains__(newPos.get_pos())) & (~nodeToVisit.__contains__(newPos.get_pos())):
            nodeToVisit.append(newPos.get_pos())
            posToVisit.append(newPos)

        return None


# Création d'une boucle
for i in range(1, 2):
    # Initiation du code
    nodeToVisit = []
    posToVisit = []
    nodeStudied = []
    currentPos = Position(rbt.posX, rbt.posY)
    finished: bool = False
    nodeToVisit.append(currentPos.get_pos())
    posToVisit.append(currentPos)
    insertDust(grid)
    print(grid)
    print(rbt)
    # Appel de la fonction
    cellObtained: Cell = None
    while ~finished:
        cellObtained = analyseGrid(grid, posToVisit[0])
        if(cellObtained != None):
            finished = True
            print("Position de la case trouvée: ")
            print(cellObtained.get_posX(), cellObtained.get_posY())
            if(cellObtained.get_dust() == 1):
                print("Contient de la saleté")
            else:
                print("Contient des bijoux")
            break
    print("")
    print("Noeuds étudiés : ")
    print(nodeStudied)
    # Déplacement du robot
    print("")
    print("Déplacement robot : ")
    print(rbt)

rbt.calcul_Dest_To_Case(cellObtained)
print(rbt.get_actions_expected())
rbt.get_effectors().action_robot(cellObtained)
print(rbt)
