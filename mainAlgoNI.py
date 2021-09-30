from Agent.Effectors import Effectors
from Agent.Robot import Robot
from Environment.Grid import Grid
from Environment.Cell import Cell
from Position import Position
from AlgoNI import AlgoNI

# Création du robot et de la grille
grid: Grid = Grid(5, 5)
rbt: Robot = Robot(0, 1, grid)
algoni: AlgoNI = AlgoNI(grid, rbt)

# Execution
for i in range(1, 2):
    # Initiation du code
    nodeToVisit = []
    posToVisit = []
    nodeStudied = []
    currentPos = Position(rbt.posX, rbt.posY)
    finished: bool = False
    nodeToVisit.append(currentPos.get_pos())
    posToVisit.append(currentPos)
    algoni.insertDustTest()
    algoni.insertDustTest()
    algoni.insertDustTest()
    print(grid)
    print(rbt)
    # Appel de la fonction
    cellObtained: Cell = None
    while ~finished & len(posToVisit) > 0:
        cellObtained = algoni.analyseGrid(
            posToVisit[0], nodeStudied, nodeToVisit, posToVisit)
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
    if(cellObtained != None):
        print()
        print("Déplacement robot : ")
        print(rbt)
        rbt.get_sensors().calcul_dest_to_cell(cellObtained)
        print(rbt.get_actions_expected())
        rbt.get_effectors().action_robot(cellObtained)
        print(rbt)
