import sys
from tkinter import *
import AlgoNonInforme
import Cell
import Grid
import Node
import Robot


 



def main():
   c = 40     
   n = 5
   cases = [] 

   ##----- Creation de la fenetre -----##
   fen = Tk()
   fen.title('IAAspiMaison')



   ##----- Creation des boutons -----##
   bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
   bouton_quitter.grid(row = 1, column = 1, sticky=W+E, padx=3, pady=3)

   ##----- Creation des canevas -----##
   dessin = Canvas(fen, width= n*c+2, height = n*c+2)
   dessin.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3)

   ##----- Creation des figures -----##
   for ligne in range(n):          # Les cases de chaque ligne seront stockees dans "pieces"
        pieces=[]
        for colonne in range(n):    # Conception des pieces d'une ligne
            pieces.append(dessin.create_rectangle(colonne*c, ligne*c, (colonne+1)*c, (ligne+1)*c))
        cases.append(pieces)       # Ajout de la ligne a la liste principale

    ##----- Modification des figures creees -----##
   for ligne in range(n):
        for colonne in range(n):
            if (ligne+colonne)%2 == 0:      # Parite
                dessin.itemconfigure(cases[ligne][colonne], outline='black',fill='black' )
            else:
                dessin.itemconfigure(cases[ligne][colonne], outline='white')

   fen.mainloop() 














if __name__ == '__main__':
    main()