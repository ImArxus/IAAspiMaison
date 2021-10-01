import Cell
import Grid
from random import *
import threading
import time


threadLock = threading.Lock()
class Thread_Robot(threading.Thread):
    def __init__(self, threadID, name, counter, agent, dessin):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.agent = agent
        self.dessin = dessin


    def run(self):
        print( "Starting" + self.name)
        # Get lock to synchronize threads
        #threadLock.acquire()


        # Free lock to release next thread
        #threadLock.release()

