from Agent.Effectors import Effectors
from Agent.Robot import Robot
from Environment.Grid import Grid
from Environment.Cell import Cell
from Position import Position
from AlgoNI import AlgoNI

# Création du robot et de la grille
grid:Grid = Grid(5,5)
rbt:Robot = Robot(0,1,grid)
eff:Effectors=Effectors(rbt)

#Execution
