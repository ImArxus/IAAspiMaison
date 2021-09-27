class Node:

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
            s = Node(self, self.position_after_action(action, grid), action,
                     self.depth+1, self.cost_action(action)+self.parent.get_cost(), 0)
            self.affect_heuristique(robot)
            successors.append(s)
        return successors
