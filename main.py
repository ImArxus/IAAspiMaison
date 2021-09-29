from Robot import Robot
from Node import Node
from Grid import Grid
from Cell import Cell

# Obtenir la position de l'aspirateur
rbt = Robot(2, 0)
grid = Grid(5, 4)
cell = Cell(0, 0, 2, 4)
grid.get_cell(cell.get_posX(), cell.get_posY()).set_dust(1)
node = Node(cell, None, None, 0, 0, 0)
print(rbt)
print(grid)
rbt.move_left()
rbt.move_up()
print(rbt)
# Créer un arbre de recherches et un stockage
print(node)
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
