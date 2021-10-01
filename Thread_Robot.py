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
    def __init__(self, threadID, name, grid, agent, dessin, c, effector, fenetre):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.agent = agent
        self.dessin = dessin
        self.grid = grid
        self.c = c
        self.effector = effector
        self.fenetre = fenetre

    def run(self):
        print( "Starting" + self.name)
        # Get lock to synchronize threads
        #threadLock.acquire()
        while 1:
            self.action()
            time.sleep(1)

        # Free lock to release next thread
        #threadLock.release()

    def action(self):
        for i in range(1, 2):
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
            algoni.insertDustTest()
            algoni.insertDustTest()
            algoni.insertDustTest()
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
            print("")
            print("Noeuds étudiés : ")
            print(algoni.get_nodeStudied())
            print("")
            print("Noeuds à étudier : ")
            print(algoni.get_nodeToVisit())
            # Déplacement du robot
            if (cellObtained != None):
                print("")
                print("Déplacement robot : ")
                print(self.agent)
                self.agent.calcul_Dest_To_Case(cellObtained)
                print(self.agent.get_actions_expected())
                self.effector.action_robot(cellObtained)

                self.dessin.delete('agent') #delete previous picture of robot
                self.dessin.create_rectangle(self.agent.posY * self.c + 12, self.agent.posX * self.c + 12,
                                             (self.agent.posY + 1) * self.c - 12,
                                             (self.agent.posX + 1) * self.c - 12,
                                             tags='agent', fill='green')         #display robot at his new pos
                #self.fenetre.update()

                print(self.agent)

