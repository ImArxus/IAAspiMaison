class Node:

    def __init__(self, data):
        self.data = data
        self.childUp = None
        self.childDown = None
        self.childLeft = None
        self.childRight = None
        self.parent = None
        self.parentDirection = None

    def __str__(self):
        return '( {self.data} , up : {self.childUp}, down : {self.childDown}, left : {self.childLeft}, right : {self.childRight})'.format(self=self)

    def insert(self, node, position):
        node.parent = self
        if position == 'up':
            self.childUp = node
            self.parentDirection = 'up'
        elif position == 'down':
            self.childDown = node
            self.parentDirection = 'down'
        elif position == 'left':
            self.childLeft = node
            self.parentDirection = 'left'
        else:
            self.childRight = node
            self.parentDirection = 'right'
