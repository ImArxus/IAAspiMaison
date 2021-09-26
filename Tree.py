class Node:

    def __init__(self, data):
        self.data = data
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def insert(self, data, position):
        if position is 'up':
            self.up = Node(data)
            self.up.parent = self
        elif position is 'down':
            self.down = Node(data)
            self.down.parent = self
        elif position is 'left':
            self.left = Node(data)
            self.left.parent = self
        else:
            self.right = Node(data)
            self.right.parent = self  