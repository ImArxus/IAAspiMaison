import Cell
import Grid
from random import *
import threading
import time

threadLock = threading.Lock()


class Thread_Environnement(threading.Thread):
    def __init__(self, threadID, name, environnement, manoir, dessin, cases, n):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.environnement = environnement
        self.manoir = manoir
        self.dessin = dessin
        self.cases = cases
        self.n = n

    def run(self):
        while (1):
            print("Starting" + self.name)
            # Get lock to synchronize threads
            # threadLock.acquire()
            col = randint(0,4)
            line = randint(0,4)
            piece = self.environnement.get_cell(col, line)
            rand_n = randint(0, 10)
            if rand_n >= 3 and rand_n <= 5:
                piece.set_dust(1)
            if rand_n >= 6 and rand_n <= 9:
                piece.set_jewel(1)
            if rand_n == 10:
                piece.set_dust(1)
                piece.set_jewel(1)

                    ##----- Modification des figures creees -----##
            for colonne in range(self.n):
                for ligne in range(self.n):
                    if ((self.manoir.get_cell(colonne, ligne).get_dust()) == 1 and (
                            self.manoir.get_cell(colonne, ligne).get_jewel()) == 1):  # dirt + jewel
                        self.dessin.itemconfigure(self.cases[ligne][colonne], outline='black', fill='yellow')
                    elif ((self.manoir.get_cell(colonne, ligne).get_dust()) == 1 and (
                            self.manoir.get_cell(colonne, ligne).get_jewel()) == 0):  # dirt only
                        self.dessin.itemconfigure(self.cases[ligne][colonne], outline='black', fill='red')
                    elif ((self.manoir.get_cell(colonne, ligne).get_dust()) == 0 and (
                            self.manoir.get_cell(colonne, ligne).get_jewel()) == 1):  # jewel only
                        self.dessin.itemconfigure(self.cases[ligne][colonne], outline='black', fill='blue')
                    else:  # rien
                        self.dessin.itemconfigure(self.cases[ligne][colonne], outline='black', fill='white')
            # Free lock to release next thread

            print(self.environnement)
            # threadLock.release()
            time.sleep(3)
