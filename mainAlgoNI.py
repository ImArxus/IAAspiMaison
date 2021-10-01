from Agent.Robot import Robot
from AlgoNI import AlgoNI
from Environment.Grid import Grid
from Environment.Cell import Cell
from Position import Position
from AlgoNI import AlgoNI

# Création du robot et de la grille
grid: Grid = Grid(5, 5)
rbt: Robot = Robot(0, 1, grid)

# Execution, boucle permettant de tester notre solution un nombre fini de fois
for i in range(1, 2):
    # Initiation du code
    algoni: AlgoNI = AlgoNI(grid, rbt, [], [], []) # Création d'un algorithme BFS de recherche non informée
    currentPos = Position(rbt.posX, rbt.posY) # Position de départ du robot
    finished: bool = False # Bool permettant de représenter si l'agent a trouvé ou non la cellule sur laquelle à agir
    listemp: list[str] = algoni.get_nodeToVisit() # Ajout de la position actuelle dans la liste des noeuds à visiter
    listemp.append(currentPos.get_pos())
    algoni.set_nodeToVisit(listemp)
    listemp: list[Position] = algoni.get_cellToVisit()
    listemp.append(currentPos)
    algoni.set_cellToVisit(listemp)
    algoni.insertDustTest() # Appel d'une fonction de test permettant la génération de poussière
    algoni.insertDustTest()
    algoni.insertDustTest()
    print(grid) # Affichage textuelle de notre situation actuelle
    print(rbt)
    cellObtained: Cell = None # Cellule sur laquelle agir
    while ~finished & len(algoni.get_cellToVisit()) > 0: # Boucle permettant les recherches jusqu'à ce que nous trouvons la solution
        listtemp: list[Position] = algoni.get_cellToVisit()
        cellObtained = algoni.analyseGrid(listemp[0]) # Tester l'algorithme de recherche sur le prochain noeud
        if(cellObtained != None): # Si une cellule sur laquelle effectuer des actions a été trouvée
            finished = True # Stopper la boucle
            print("Position de la case trouvée: ") # Affichage de la solution
            print(cellObtained.get_posX(), cellObtained.get_posY())
            if(cellObtained.get_dust() == 1):
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
    if(cellObtained != None): # Déplacement de l'agent si une cellule a été trouvée
        print("")
        print("Déplacement robot : ")
        print(rbt)
        rbt.get_sensors().calcul_destination_to_cell(cellObtained) # Calcul des actions à effectuer
        print(rbt.get_actions_expected())
        rbt.get_effectors().action_robot() # Agissement du robot
print(rbt)
