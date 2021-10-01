from Agent.Effectors import Effectors
from Agent.Robot import Robot
from Agent.Sensors import Sensors
from AlgoNI import AlgoNI
from Environment.Grid import Grid
from Environment.Cell import Cell
from Position import Position
# Création du robot et de la grille
grid:Grid = Grid(5,5)
rbt:Robot = Robot(0,1,grid)

#Execution
for i in range(1,2):
    #Initiation du code
    algoni:AlgoNI =AlgoNI(grid,rbt,[],[],[])
    currentPos = Position(rbt.posX,rbt.posY)
    finished:bool=False
    listemp:list[str]=algoni.get_nodeToVisit()
    listemp.append(currentPos.get_pos())
    algoni.set_nodeToVisit(listemp)
    listemp:list[Position]=algoni.get_cellToVisit()
    listemp.append(currentPos)
    algoni.set_cellToVisit(listemp)
    algoni.insertDustTest()
    algoni.insertDustTest()
    algoni.insertDustTest()
    print(grid)
    print(rbt)
    #Appel de la fonction
    cellObtained:Cell=None
    while ~finished & len(algoni.get_cellToVisit())>0:
        listtemp:list[Position]=algoni.get_cellToVisit()
        cellObtained=algoni.analyseGrid(listemp[0])
        if(cellObtained!=None):
            finished=True
            print("Position de la case trouvée: ")
            print(cellObtained.get_posX(), cellObtained.get_posY())
            if(cellObtained.get_dust()==1):
                print("Contient de la saleté")
            else:
                print("Contient des bijoux")
            break
    print("")
    print("Noeuds étudiés : ")
    print(algoni.get_nodeStudied())
    print("")
    print("Noeuds à étudier : ")
    print(algoni.get_nodeToVisit())
    #Déplacement du robot
    if(cellObtained!=None):
        print("")
        print("Déplacement robot : ")
        print(rbt)
        rbt.get_sensors().calcul_destination_to_cell(cellObtained)
        print(rbt.get_actions_expected())
        rbt.get_effectors().action_robot()
print(rbt)