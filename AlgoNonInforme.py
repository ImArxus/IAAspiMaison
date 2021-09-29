from Robot import Robot
from Tree import Node
from Grid import Grid
from Cell import Cell
import random

# Création du robot et de la grille
rbt = Robot(0, 1)
grid = Grid(2, 2)

#Insertion de poussière de manière aléatoire
rdm1:int = random.randint(0,grid.get_cols()-1)
rdm2:int = random.randint(0,grid.get_rows()-1)
dustcell: Cell = grid.get_cell(rdm1,rdm2)
dustcell.set_dust(1)
print(grid)
print(rbt)

#Création d'un arbre de recherches et d'un stockage
currentX = rbt.posX
currentY = rbt.posY
currentPos = currentX, currentY
tree = Node(currentPos)

#Fonction d'analyse d'une pièce
def analyseCell(gr,X,Y)-> Cell:
    cell:Cell=None
    if gr.get_cell(X,Y).get_dust() == 1:
        cell=gr.get_cell(X,Y)
    elif gr.get_cell(X,Y).get_jewel() == 1:
        cell=gr.get_cell(X,Y)
    return cell

#Fonction d'analyse des cellules juxtaposées
def recursiveAnalyse(X,Y,boolean)->Cell:
    cellToReturn:Cell=None
    if Y>0:
        newPos = X, Y-1
        newNode : Node =  Node(newPos)
        tree.insert(newNode,'up')
        testR=analyseCell(grid,X, Y-1)
        if(testR!=None):
            cellToReturn=testR
            boolean=False
    if  (Y<grid.get_rows()-1) & (boolean):
        newPos = X, Y+1
        newNode : Node =  Node(newPos)
        tree.insert(newNode,'down')
        testR=analyseCell(grid,X, Y+1)
        if(testR!=None):
            cellToReturn=testR
            boolean=False
    if  (X>0) & (boolean):
        newPos = X-1, Y
        newNode : Node =  Node(newPos)
        tree.insert(newNode,'left')
        testR= analyseCell(grid,X-1, Y)
        if(testR!=None):
            cellToReturn=testR
            boolean=False
    if  (X<grid.get_cols()-1) & (boolean):
        newPos = X+1, Y
        newNode : Node =  Node(newPos)
        tree.insert(newNode,'right')
        testR=analyseCell(grid,X+1, Y)
        if(testR!=None):
            cellToReturn=testR
    return cellToReturn

# Analyse de l'état de la pièce actuelle
test=analyseCell(grid,currentX,currentY)
if(test!=None):
    print("position de la case trouvée: ")
    print(test.get_posX(), test.get_posY())
    if(test.get_dust()==1):
        print("Contient de la saleté")
    else:
        print("Contient des bijoux")
else:
    test2=recursiveAnalyse(currentX,currentY,True)
    if(test2!=None):
        print("position de la case trouvée: ")
        print(test2.get_posX(), test2.get_posY())
        if(test2.get_dust()==1):
            print("Contient de la saleté")
        else:
            print("Contient des bijoux")
    print("")
print("Arbre de recherche : ")
print(tree)

# Sinon récursivité :
# Chercher les pièces juxtaposées jamais explorées et en créer des noeuds à ajouter à l'arbre et au stockage


# Répéter jusqu'à trouver une pièce sale puis retourner l'arbre créé
# En utilisant l'arbre déplacer le robot puis aspirer ou ramasser
# Répéter