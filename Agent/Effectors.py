from Environment.Cell import Cell
import time


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
            self.robot.set_posY(self.robot.get_posY()-1)
            print("Robot has moved up")

    def move_down(self) -> None:
        if self.robot.get_posY() < self.robot.get_expected_grid().get_rows():
            self.robot.set_posY(self.robot.get_posY()+1)
            print("Robot has moved down")

    def clean(self, cellToClean: Cell) -> None:
        cellToClean.set_dust(0)
        print("Robot has cleaned")

    def grab(self, cellToGrab: Cell) -> None:
        cellToGrab.set_jewel(0)
        print("Robot has grabed")

    # Effectue les actions contenues dans l attribut du robot
    def action_robot(self, fenetre, dessin, c) -> None:
        while len(self.robot.get_actions_expected()) > 0:
            robot_cell: Cell = self.robot.get_expected_grid().get_cell(
                self.robot.get_posX(), self.robot.get_posY())
            action: str = self.robot.get_actions_expected()[0]
            self.robot.get_actions_expected().remove(action)
            if action == 'right':
                self.move_right()
            elif action == 'left':
                self.move_left()
            elif action == 'down':
                self.move_down()
            elif action == 'up':
                self.move_up()
            elif action == 'grab' or robot_cell.get_jewel() > 0:
                self.grab(robot_cell)
            elif action == 'clean' or robot_cell.get_dust() > 0:
                self.clean(robot_cell)

            self.robot.set_performance(self.robot.get_performance()+self.robot.get_sensors().perfomance_after_action(robot_cell, action))
            print("Performance : " + str(self.robot.get_performance()))

            dessin.delete('agent')  # delete previous picture of robot
            dessin.create_rectangle(self.robot.get_posY() * c + 12, self.robot.get_posX() * c + 12,
                                    (self.robot.get_posY() + 1) * c - 12,
                                    (self.robot.get_posX() + 1) * c - 12,
                                    tags='agent', fill='green')  # display robot at his new pos
            fenetre.update()
            time.sleep(1)
