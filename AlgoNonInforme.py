from Robot import Robot
from Node import Node
from Grid import Grid
from Cell import Cell
import random

# Création du robot et de la grille
rbt = Robot(0, 0)
grid = Grid(5, 5)

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
print(tree)

#Fonction d'analyse d'une pièce
def analyseCell(grid,posX,posY):
    if grid.get_cell(posX,posY).get_dust() == 1:
        print("Dust in cell ")
        print(posX, posY)
    elif grid.get_cell(posX,posY).get_jewel() == 1:
        print("Jewel in cell ")
        print(posX, posY)
    else:
        print("Nothing in cell ")
        print(posX, posY)

# Analyse de l'état de la pièce actuelle
analyseCell(grid,currentX,currentY)

# Sinon récursivité :
# Chercher les pièces juxtaposées jamais explorées et en créer des noeuds à ajouter à l'arbre et au stockage
if  currentY>0:
    newPos = currentX, currentY-1
    tree.insert(newPos,'up')
    print(tree)
    analyseCell(grid,currentX, currentY-1)
if  currentY<4:
    newPos = currentX, currentY+1
    tree.insert(newPos,'down')
    print(tree)
    analyseCell(grid,currentX, currentY+1)
if  currentX>0:
    newPos = currentX-1, currentY
    tree.insert(newPos,'left')
    print(tree)
    analyseCell(grid,currentX-1, currentY)
if  currentY<4:
    newPos = currentX+1, currentY
    tree.insert(newPos,'right')
    print(tree)
    analyseCell(grid,currentX+1, currentY)

# Répéter jusqu'à trouver une pièce sale puis retourner l'arbre créé
# En utilisant l'arbre déplacer le robot puis aspirer ou ramasser
# Répéter