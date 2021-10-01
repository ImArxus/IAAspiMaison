from Agent.Robot import Robot
from Environment.Grid import Grid
from Environment.Cell import Cell
import random


# Création du robot et de la grille
grid: Grid = Grid(2, 2)
robot: Robot = Robot(0, 0, grid)


# Insertion de poussière de manière aléatoire (test pour meziane)
def insertDustTest() -> None:
    rdm1: int = random.randint(0, robot.get_expected_grid().get_cols()-1)
    rdm2: int = random.randint(0, robot.get_expected_grid().get_rows()-1)
    dustcell: Cell = robot.get_expected_grid().get_cell(rdm1, rdm2)
    dustcell.set_dust(1)


# Execution
for i in range(1, 2):
    # Initiation du code
    finished: bool = False
    listemp: list[Cell] = robot.get_cellToVisit()
    listemp.append(grid.get_cell(robot.get_posX(), robot.get_posY()))
    robot.set_cellToVisit(listemp)
    # insertDustTest()
    # insertDustTest()
    # insertDustTest()
    print(grid)
    print(robot)
    # Appel de la fonction
    cellObtained: Cell = None
    while ~finished & len(robot.get_cellToVisit()) > 0:
        listtemp: list[Cell] = robot.get_cellToVisit()
        cellObtained = robot.get_sensors().analyse_grid(listemp[0])
        if cellObtained != None:
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
    for node in robot.get_nodeStudied():
        print(node)
    print("")
    print("Noeuds à étudier : ")
    for node in robot.get_cellToVisit():
        print(node)
    # Déplacement du robot
    if(cellObtained != None):
        print("")
        print("Déplacement robot : ")
        print(robot)
        robot.get_sensors().calcul_destination_to_cell(cellObtained)
        print(robot.get_actions_expected())
        robot.get_effectors().action_robot()
        print(robot)
