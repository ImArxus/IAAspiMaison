from Robot import Robot
from Node import Node
from Grid import Grid
from Cell import Cell

grid = Grid(5, 4)
cell1 = Cell(1, 0, 0, 2)
cell2 = Cell(0, 0, 4, 0)
cell3 = Cell(1, 0, 4, 3)
grid.set_cell(cell1.get_posX(), cell1.get_posY(), cell1)
grid.set_cell(cell2.get_posX(), cell2.get_posY(), cell2)
grid.set_cell(cell3.get_posX(), cell3.get_posY(), cell3)
#grid.get_cell(cell1.get_posX(), cell1.get_posY()).set_dust(0)
grid.get_cell(cell2.get_posX(), cell2.get_posY()).set_jewel(1)
node = Node(cell1, None, None, 0, 0, 0)
robot = Robot(4, 0, grid)
print(robot)
print(grid)
robot.move_left()
robot.move_up()
robot.move_down()
print(robot)
print("Dust : " + str(robot.goal()))
"""node.insert(1, 'up')
node.insert(0, 'left')
node.insert(2, 'down')
print(node)
node.insert(0, 'up')
print(node)"""
# Analyser l'état de la pièce actuelle
# S'il y a de la poussière > aspirer
# S'il y a un bijou > le ramasser
# Sinon récursivité :
# Chercher les pièces juxtaposées jamais explorées et en créer des noeuds à ajouter à l'arbre et au stockage
# Répéter jusqu'à trouver une pièce sale puis retourner l'arbre créé
# En utilisant l'arbre déplacer le robot puis aspirer ou ramasser
# Répéter
