from Robot import Robot
from Tree import Node
from Grid import Grid
from Cell import Cell
from Position import Position
import random

# Création du robot et de la grille
rbt = Robot(0, 1)
grid = Grid(3,3)

#Insertion de poussière de manière aléatoire
rdm1:int = random.randint(0,grid.get_cols()-1)
rdm2:int = random.randint(0,grid.get_rows()-1)
dustcell: Cell = grid.get_cell(rdm1,rdm2)
dustcell.set_dust(1)
print(grid)
print(rbt)

#Fonction d'analyse d'une pièce
def analyseCell(gr,pos:Position)-> Cell:
    cell:Cell=None
    if gr.get_cell(pos.get_posX(),pos.get_posY()).get_dust() == 1:
        cell=gr.get_cell(pos.get_posX(),pos.get_posY())
    elif gr.get_cell(pos.get_posX(),pos.get_posY()).get_jewel() == 1:
        cell=gr.get_cell(pos.get_posX(),pos.get_posY())
    return cell

#Fonction d'analyse des cellules juxtaposées 
def recursiveAnalyse(pos:Position,boolean)->Cell:
    nodeLaps = []
    newPos = Position(pos.get_posX(), pos.get_posY()-1)
    if (pos.get_posY()>0)&~(nodeStudied.__contains__(newPos.get_pos())) & (~boolean):
        nodeStudied.append(newPos.get_pos())
        nodeLaps.append(newPos.get_pos())
        newNode : Node =  Node(newPos)
        tree.insert(newNode,'up')
        posR = Position(pos.get_posX(), pos.get_posY()-1)
        testR=analyseCell(grid,posR)
        if(testR!=None):
            boolean=True
            return testR
        else:
            return recursiveAnalyse(posR,boolean)

    newPos = Position(pos.get_posX(), pos.get_posY()+1)
    if  (pos.get_posY()<grid.get_rows()-1) & (~boolean)&~(nodeStudied.__contains__(newPos.get_pos())):
        nodeStudied.append(newPos.get_pos())
        nodeLaps.append(newPos.get_pos())
        newNode : Node =  Node(newPos)
        tree.insert(newNode,'down')
        posR = Position(pos.get_posX(), pos.get_posY()+1)
        testR=analyseCell(grid,posR)
        if(testR!=None):
            boolean=True
            return testR
        else:
            return recursiveAnalyse(posR,boolean)

    newPos = Position(pos.get_posX()-1, pos.get_posY())
    if  (pos.get_posX()>0) & (~boolean)&~(nodeStudied.__contains__(newPos.get_pos())):
        nodeStudied.append(newPos.get_pos())
        nodeLaps.append(newPos.get_pos())
        newNode : Node =  Node(newPos)
        tree.insert(newNode,'left')
        posR = Position(pos.get_posX()-1, pos.get_posX())
        testR=analyseCell(grid,posR)
        if(testR!=None):
            boolean=True
            return testR
        else:
            return recursiveAnalyse(posR,boolean)

    newPos = Position(pos.get_posX()+1, pos.get_posY())
    if  (pos.get_posX()<grid.get_cols()-1) & (~boolean)&~(nodeStudied.__contains__(newPos.get_pos())):
        nodeStudied.append(newPos.get_pos())
        nodeLaps.append(newPos.get_pos())
        newNode : Node =  Node(newPos)
        tree.insert(newNode,'right')
        posR = Position(pos.get_posX()+1, pos.get_posY())
        testR=analyseCell(grid,posR)
        if(testR!=None):
            boolean=True
            return testR
        else:
            return recursiveAnalyse(posR,boolean)
    return None
    """while ~boolean:
        element=nodeLaps[0]
        posRec = Position(int(element[0]),int(element[1]))
        cellRec:Cell=recursiveAnalyse(posRec,boolean)
        del nodeLaps[0]
        if cellRec!=None:
            boolean=True"""

#Création d'un arbre de recherches et d'un stockage + algo
currentPos = Position(rbt.posX,rbt.posY)
tree = Node(currentPos)
nodeStudied = []
found:bool = False

res=analyseCell(grid,currentPos)
nodeStudied.append(currentPos.get_pos())
if(res!=None):
    found=True
else:
    res=recursiveAnalyse(currentPos,found)
if(res!=None):
    print("Position de la case trouvée: ")
    print(res.get_posX(), res.get_posY())
    if(res.get_dust()==1):
        print("Contient de la saleté")
    else:
        print("Contient des bijoux")
print("")
print("Arbre de recherche : ")
print(tree)
print("")
print("Noeuds étudiés : ")
for element in nodeStudied:
            print(element)