import Cell
import Grid
from random import *
import threading
import time

threadLock = threading.Lock()
class Thread_Environnement(threading.Thread):
    def __init__(self, threadID, name, environnement):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.environnement = environnement

    def run(self):
      print( "Starting" + self.name)
      # Get lock to synchronize threads
      #threadLock.acquire()
      for col in range(self.environnement.get_cols()):
        for line in range(self.environnement.get_rows()):
            piece = self.environnement.get_cell(col,line) 
            n = randint(1,10)
            if n>=5 and n<=7 :
                piece.set_dust(1)
            if n>=8 and n<=9 :
                piece.set_jewel(1)
            if  n==10 :
                piece.set_dust(1)
                piece.set_jewel(1)
      # Free lock to release next thread

      print(self.environnement)
      #threadLock.release()
      threading.Timer(3000,self.run()).start()



