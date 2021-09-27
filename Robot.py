from Node import Node


class Robot:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def get_positionX(self):
        return self.posX

    def get_positionY(self):
        return self.posY

    def set_positionX(self, X):
        self.posX = X

    def set_positionY(self, Y):
        self.posY = Y

    def __str__(self):
        return 'Le robot est situé à l emplacement :  {self.posX} , {self.posY}'.format(self=self)

    def move_left(self):
        if self.posX > 0:
            self.posX = self.posX-1

    def move_right(self):
        if self.posX < 4:
            self.posX = self.posX+1

    def move_up(self):
        if self.posY > 0:
            self.posY = self.posY-1

    def move_down(self):
        if self.posY < 4:
            self.posY = self.posY+1

    def a_star(self, grid) -> Node:
        node_start = Node(grid.getCell(
            self.get_positionX(), self.get_positionY()))
        node_start.affect_heuristique(self)
        node_list = []
        node_list.append(node_start)
        while self.goal_reached(node_list[0]) == False:
            node_tmp = node_list[0]
            node_list.remove(node_list[0])
            new_nodes = node_tmp.expand(self.get_belief(), self)
            for node in new_nodes:
                node_list.append(node)
            node_list.sort()
        return node_list[0]