from Environment.Cell import Cell


class Effector:

    def __init__(self, robot) -> None:
        self.robot = robot

    def move_left(self) -> None:
        if self.robot.get_posX() > 0:
            self.robot.set_posX(self.robot.get_posX()-1)
            print("Robot has moved left")

    def move_right(self) -> None:
        if self.robot.get_posX() < self.robot.get_expected_grid().get_cols():
            self.robot.set_posX(self.robot.get_posX()+1)
            print("Robot has moved right")

    def move_up(self) -> None:
        if self.robot.get_posY() > 0:
            self.robot.set_posY(self.get_posY()-1)
            print("Robot has moved up")

    def move_down(self) -> None:
        if self.robot.get_posY() < self.robot.get_expected_grid().get_rows():
            self.robot.set_posY(self.robot.get_posY()+1)
            print("Robot has moved down")

    def move_Robot(self, cellArrival: Cell) -> None:
        while self.robot.get_posX() < cellArrival.get_posX():
            self.move_right()
        while self.robot.get_posX() > cellArrival.get_posX():
            self.move_left()
        while self.robot.get_posY() < cellArrival.get_posY():
            self.move_down()
        while self.robot.get_posY() > cellArrival.get_posY():
            self.move_up()
