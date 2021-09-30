from Agent.Effectors import Effectors
from Agent.Robot import Robot
from Environment.Grid import Grid
from Environment.Cell import Cell
from AlgoNI import AlgoNI

# Classe d'implémentation de l'algorithme non informé (à supprimer plus tard)

grid:Grid = Grid(5,5) # Création de la grille
rbt:Robot = Robot(0,1,grid) # Création du robot
eff:Effectors=Effectors(rbt) # Création des effecteurs du robot
algoni:AlgoNI=AlgoNI(grid,rbt) # Création de l'algorithme non informé

for i in range(1,2): # Boucle for permettant le test de plusieurs itérations de recherche (à modifier plus tard)
    nodeToVisit = [] # Liste des noeuds que nous devrons visiter
    cellToVisit = [] # Liste des cellules à visiter
    nodeStudied = [] # Liste des noeuds déja étudiés
    currentPos = grid.get_cell(rbt.posX,rbt.posY) # Cellule initiale
    finished:bool=False # Booléen permettant de déterminer la fin du parcours de l'algorythme
    nodeToVisit.append(currentPos.get_pos()) # Ajout de la cellule actuelle dans celles à visiter
    cellToVisit.append(currentPos)
    algoni.insertDustTest() # Insertion de poussière dans le code
    print(grid) # Affichage de la grille et du robot
    print(rbt)
    cellObtained:Cell=None # Cellule de résultat
    while ~finished & len(cellToVisit)>0: # Boucle while permettant de faire tourner l'algorithme jusqu'à ce qu'il trouve une cellule
        cellObtained=algoni.analyseGrid(cellToVisit[0],nodeStudied,nodeToVisit,cellToVisit) # Appel de la fonction reccursive
        if(cellObtained!=None): # Si une cellule a été trouvée
            finished=True # Alors il faut terminer la boucle
            print("Position de la case trouvée: ")
            print(cellObtained.get_posX(), cellObtained.get_posY()) # L'afficher
            if(cellObtained.get_dust()==1): # Détecter l'action à réaliser
                print("Contient de la saleté")
            else:
                print("Contient des bijoux")
            print("")
            print("Déplacement robot : ")
            print(rbt)
            rbt.calcul_Dest_To_Case(cellObtained)# Déplacement du robot
            print(rbt.get_actions_expected())
            eff.action_robot(cellObtained)
            print(rbt)
            break
    print("")
    print("Noeuds étudiés : ") # Affichage des noeuds étudiés
    print(nodeStudied)