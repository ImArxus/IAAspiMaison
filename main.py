import sys
from tkinter import *
import threading
import Thread_Environnement
import Thread_Robot
from Environment.Cell import *
from Environment.Grid import *
from random import *


def main():
    manoir = Grid(5, 5)
    update_time = 0

    threads = []

    c = 40  # Longueur d'un cote d'une piece
    n = 5  # Nombre de piece par ligne et pas colonne
    cases = []
    agent = []

    ##----- Creation de la fenetre -----##
    fen = Tk()
    fen.title('IAAspiMaison')

    ##----- Creation des boutons -----##
    bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
    bouton_quitter.grid(row=1, column=1, sticky=W + E, padx=3, pady=3)

    ##----- Creation des canevas -----##
    dessin = Canvas(fen, width=n * c + 2, height=n * c + 2)
    dessin.grid(row=0, column=0, columnspan=2, padx=3, pady=3)

    ##----- Creation des figures -----##
    for ligne in range(n):  # Les cases de chaque ligne seront stockees dans "pieces"
        pieces = []
        for colonne in range(n):  # Conception des pieces d'une ligne
            id = ligne * 5 + colonne
            pieces.append(
                dessin.create_rectangle(colonne * c, ligne * c, (colonne + 1) * c, (ligne + 1) * c, tags=f'{id}'))
        cases.append(pieces)  # Ajout de la ligne a la liste principale

    agent.append(dessin.create_rectangle(colonne * c + 12, ligne * c + 12, (colonne + 1) * c - 12, (ligne + 1) * c - 12,
                            tags='agent', fill='green'))

    ## Creation de threads
    thread_Manoir = Thread_Environnement(1, 'environnement', manoir, dessin, cases, n)
    thread_Robot = Thread_Robot(2, "agent", 2, agent, dessin)

    ## Lancement des threads
    thread_Manoir.start()
    thread_Robot.start()

    ## Ajout des threads dans la liste
    threads.append(thread_Manoir)
    threads.append(thread_Robot)

    # Wait for all threads to complete
    ##for t in threads:
    ##t.join()
    ##print( "Exiting Main Thread")

    fen.mainloop()


if __name__ == '__main__':
    main()
