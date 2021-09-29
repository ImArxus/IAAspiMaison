class Node:

    def __init__(self, data):
        self.data = data
        self.childUp = None
        self.childDown = None
        self.childLeft = None
        self.childRight = None

    def __str__(self):
        return '( {self.data} , up : {self.childUp}, down : {self.childDown}, left : {self.childLeft}, right : {self.childRight})'.format(self=self)

    def insert(self, node, position):
        if position == 'up':
            self.childUp = node
        elif position == 'down':
            self.childDown = node
        elif position == 'left':
            self.childLeft = node
        else:
            self.childRight = node