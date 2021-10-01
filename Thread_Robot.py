from Environment.Cell import *
from Environment.Grid import *
from random import *
import threading
import time
from Agent.Robot import Robot
from AlgoNI import AlgoNI
from Position import Position

threadLock = threading.Lock()


class Thread_Robot(threading.Thread):
    def __init__(self, threadID, name, grid, agent: Robot, dessin, c, fenetre):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.agent = agent
        self.dessin = dessin
        self.grid = grid
        self.c = c
        self.fenetre = fenetre

    def run(self):
        print("Starting" + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        while 1:
            self.action()
            time.sleep(1)

        # Free lock to release next thread
        # threadLock.release()

    def action(self, informed: bool) -> None:
        if informed:
            self.agent.get_sensors().generate_actions()
            self.agent.get_effectors().action_robot(self.agent.get_sensors().goal(),
                                                    self.fenetre, self.dessin, self.agent, self.c)
        else:
            # Initiation du code
            algoni = AlgoNI(self.grid, self.agent, [], [], [])
            currentPos = Position(self.agent.posX, self.agent.posY)
            finished: bool = False
            listemp: list[str] = algoni.get_nodeToVisit()
            listemp.append(currentPos.get_pos())
            algoni.set_nodeToVisit(listemp)
            listemp: list[Position] = algoni.get_cellToVisit()
            listemp.append(currentPos)
            algoni.set_cellToVisit(listemp)
            print(self.grid)
            print(self.agent)
            # Appel de la fonction
            cellObtained: Cell = None
            while ~finished & len(algoni.get_cellToVisit()) > 0:
                listtemp: list[Position] = algoni.get_cellToVisit()
                cellObtained = algoni.analyseGrid(listemp[0])
                if (cellObtained != None):
                    finished = True
                    print("Position de la case trouvée: ")
                    print(cellObtained.get_posX(), cellObtained.get_posY())
                    if (cellObtained.get_dust() == 1):
                        print("Contient de la saleté")
                    else:
                        print("Contient des bijoux")
                    break
            print("\nNoeuds étudiés : ")
            print(algoni.get_nodeStudied())
            print("\nNoeuds à étudier : ")
            print(algoni.get_nodeToVisit())
            # Déplacement du robot
            if (cellObtained != None):
                print("")
                print("Déplacement robot : ")
                print(self.agent)
                self.agent.get_sensors().calcul_destination_to_cell(cellObtained)
                print(self.agent.get_actions_expected())
                self.agent.get_effectors().action_robot(
                    cellObtained, self.fenetre, self.dessin, self.agent, self.c)

                print(self.agent)
