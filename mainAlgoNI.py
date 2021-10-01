from Agent.Robot import Robot
from Environment.Grid import Grid
from Environment.Cell import Cell
from AlgoNI import AlgoNI

# Création du robot et de la grille
grid: Grid = Grid(5, 5)
rbt: Robot = Robot(0, 1, grid)

# Execution
for i in range(1, 2):
    # Initiation du code
    algoni: AlgoNI = AlgoNI(grid, rbt, [], [], [])
    finished: bool = False
    listemp: list[Cell] = algoni.get_nodeToVisit()
    listemp.append(grid.get_cell(rbt.get_posX(), rbt.get_posY()))
    algoni.set_nodeToVisit(listemp)
    listemp: list[Cell] = algoni.get_cellToVisit()
    listemp.append(grid.get_cell(rbt.get_posX(), rbt.get_posY()))
    algoni.set_cellToVisit(listemp)
    algoni.insertDustTest()
    algoni.insertDustTest()
    algoni.insertDustTest()
    print(grid)
    print(rbt)
    # Appel de la fonction
    cellObtained: Cell = None
    while ~finished & len(algoni.get_cellToVisit()) > 0:
        listtemp: list[Cell] = algoni.get_cellToVisit()
        cellObtained = algoni.analyseGrid(listemp[0])
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
    for node in algoni.get_nodeStudied():
        print(node)
    print("")
    print("Noeuds à étudier : ")
    for node in algoni.get_nodeToVisit():
        print(node)
    # Déplacement du robot
    if(cellObtained != None):
        print("")
        print("Déplacement robot : ")
        print(rbt)
        rbt.calcul_Dest_To_Case(cellObtained)
        print(rbt.get_actions_expected())
        rbt.get_effectors().action_robot()
        print(rbt)
