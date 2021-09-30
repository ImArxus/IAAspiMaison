from Environment.Cell import Cell


class Effectors:

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

    def clean(self, cellToClean: Cell) -> None:
        cellToClean.set_dust(0)

    def grab(self, cellToGrab: Cell) -> None:
        cellToGrab.set_jewel(0)

    # Effectue les actions contenues dans l attribut du robot
    def action_robot(self, cellArrival: Cell) -> None:
        while len(self.robot.get_actions_expected()) > 0:
            action: str = self.robot.get_actions_expected()[0]
            self.robot.get_actions_expected().remove(action)
            if(action == 'right'):
                self.move_right()
            elif(action == 'left'):
                self.move_left()
            elif(action == 'down'):
                self.move_down()
            elif(action == 'up'):
                self.move_up
            elif(action == 'grab'):
                self.grab(cellArrival)
            else:
                self.clean(cellArrival)
