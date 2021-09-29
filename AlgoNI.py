from Robot import Robot
from Grid import Grid
from Cell import Cell
from Position import Position
import random

# Création du robot et de la grille
grid = Grid(5,5)
rbt = Robot(0,1,grid)

#Insertion de poussière de manière aléatoire
rdm1:int = random.randint(0,grid.get_cols()-1)
rdm2:int = random.randint(0,grid.get_rows()-1)
dustcell: Cell = grid.get_cell(rdm1,rdm2)
dustcell.set_dust(1)
print(grid)
print(rbt)

#Initiation du code
nodeToVisit = []
posToVisit = []
nodeStudied = []
currentPos = Position(rbt.posX,rbt.posY)
finished:bool=False
nodeToVisit.append(currentPos.get_pos())
posToVisit.append(currentPos)

#Fonction d'analyse de la grille
def analyseGrid(gr:Grid,pos:Position)-> Cell:
    nodeStudied.append(pos.get_pos())
    del nodeToVisit[0]
    del posToVisit[0]

    if (gr.get_cell(pos.get_posX(),pos.get_posY()).get_dust() == 1)|(gr.get_cell(pos.get_posX(),pos.get_posY()).get_jewel() == 1):
        return gr.get_cell(pos.get_posX(),pos.get_posY())
    else:
        newPos = Position(pos.get_posX(), pos.get_posY()-1)
        if (pos.get_posY()>0)&(~nodeStudied.__contains__(newPos.get_pos()))&(~nodeToVisit.__contains__(newPos.get_pos())):
            nodeToVisit.append(newPos.get_pos())
            posToVisit.append(newPos)

        newPos = Position(pos.get_posX(), pos.get_posY()+1)
        if  (pos.get_posY()<grid.get_rows()-1) &(~nodeStudied.__contains__(newPos.get_pos()))&(~nodeToVisit.__contains__(newPos.get_pos())):
            nodeToVisit.append(newPos.get_pos())
            posToVisit.append(newPos)

        newPos = Position(pos.get_posX()-1, pos.get_posY())
        if  (pos.get_posX()>0) &(~nodeStudied.__contains__(newPos.get_pos()))&(~nodeToVisit.__contains__(newPos.get_pos())):
            nodeToVisit.append(newPos.get_pos())
            posToVisit.append(newPos)

        newPos = Position(pos.get_posX()+1, pos.get_posY())
        if  (pos.get_posX()<grid.get_cols()-1) &(~nodeStudied.__contains__(newPos.get_pos()))&(~nodeToVisit.__contains__(newPos.get_pos())):
            nodeToVisit.append(newPos.get_pos())
            posToVisit.append(newPos)
        
        return None

#Appel de la fonction
while ~finished:
    cellObtained:Cell=analyseGrid(grid,posToVisit[0])
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
print(nodeStudied)