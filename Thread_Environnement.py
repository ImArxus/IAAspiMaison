from random import *
import threading
import time

threadLock = threading.Lock()

class Thread_Environnement(threading.Thread):
    def __init__(self, threadID, name, environnement, dessin, cases, n):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.environnement = environnement
        self.dessin = dessin
        self.cases = cases
        self.n = n
    def run(self):
        while (1):
            # Get lock to synchronize threads
            #threadLock.acquire()
            col = randint(0,4)
            line = randint(0,4)
            piece = self.environnement.get_cell(col, line)
            rand_n = randint(0, 10)
            if rand_n >= 4 and rand_n <= 6:
                piece.set_dust(1)
            if rand_n >= 7 and rand_n <= 9:
                piece.set_jewel(1)
            if rand_n == 10:
                piece.set_dust(1)
                piece.set_jewel(1)

            ##----- Modification des figures creees -----##
            for colonne in range(self.n):
                for ligne in range(self.n):
                    if ((self.environnement.get_cell(colonne, ligne).get_dust()) == 1 and (
                            self.environnement.get_cell(colonne, ligne).get_jewel()) == 1):  # dirt + jewel
                        self.dessin.itemconfigure(self.cases[colonne][ligne], outline='black', fill='yellow')
                    elif ((self.environnement.get_cell(colonne, ligne).get_dust()) == 1 and (
                            self.environnement.get_cell(colonne, ligne).get_jewel()) == 0):  # dirt only
                        self.dessin.itemconfigure(self.cases[colonne][ligne], outline='black', fill='red')
                    elif ((self.environnement.get_cell(colonne, ligne).get_dust()) == 0 and (
                            self.environnement.get_cell(colonne, ligne).get_jewel()) == 1):  # jewel only
                        self.dessin.itemconfigure(self.cases[colonne][ligne], outline='black', fill='blue')
                    else:  # rien
                        self.dessin.itemconfigure(self.cases[colonne][ligne], outline='black', fill='white')
            # Free lock to release next thread

            time.sleep(2)
            #threadLock.release()
