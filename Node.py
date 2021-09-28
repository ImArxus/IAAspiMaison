from Cell import Cell


class Node:

    def __init__(self, actualCell, parent, action, depth, cost, heuristique):
        self.actualCell = actualCell
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost
        self.heuristique = heuristique

    def __init__(self, data):
        self.data = data
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.depth = 0
        self.parent = None

    def __str__(self):
        return '( {self.data} , up : {self.up}, down : {self.down}, left : {self.left}, right : {self.right})'.format(self=self)

    def insert(self, data, position):
        if position == 'up':
            self.up = Node(data)
            self.up.parent = self
        elif position == 'down':
            self.down = Node(data)
            self.down.parent = self
        elif position == 'left':
            self.left = Node(data)
            self.left.parent = self
        else:
            self.right = Node(data)
            self.right.parent = self

    def expand(self, grid, robot):
        successors = []
        actions = []
        for action in actions:
            s = Node(self.position_after_action(action, grid), self, action,
                     self.depth+1, self.parent.get_cost()+self.cost_action(action), 0)
            self.affect_heuristique(robot)
            successors.append(s)
        return successors

    def position_after_action(self, action, grid):
        cell_cloned = self.actualCell.clone()
        if action == "up" and cell_cloned.get_posY() > 0:
            cell_cloned = grid.get_cell(self.actualCell.get_posX(), self.actualCell.get_posY()+1).clones()
            
        return cell_cloned
