import sys
from tkinter import *
#import AlgoNonInforme
import Cell
import Grid
from random import *
#import Node
#import Robot


 



def main():
    manoir = Grid.Grid(5,5)
    print(manoir)
    for col in range(manoir.get_cols()):
        for line in range(manoir.get_rows()):
            piece = manoir.get_cell(col,line) 
            n = randint(1,10)
            if n>=5 and n<=7 :
                piece.set_dust(1)
            if n>=8 and n<=9 :
                piece.set_jewel(1)
            if  n==10 :
                piece.set_dust(1)
                piece.set_jewel(1)
    print(manoir)



    c = 40     # Longueur d'un cote d'une piece
    n = 5      # Nombre de piece par ligne et pas colonne
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
            if ( (manoir.get_cell(ligne,colonne).get_dust()) == 1 and (manoir.get_cell(ligne,colonne).get_jewel()) == 1 ):     # dirt + jewel
                dessin.itemconfigure(cases[ligne][colonne], outline='black',fill='yellow' )
            elif ( (manoir.get_cell(ligne,colonne).get_dust()) == 1 and (manoir.get_cell(ligne,colonne).get_jewel()) == 0 ): # dirt only
                dessin.itemconfigure(cases[ligne][colonne], outline='black',fill='red')
            elif ( (manoir.get_cell(ligne,colonne).get_dust()) == 0 and (manoir.get_cell(ligne,colonne).get_jewel()) == 1 ):  # jewel only
                dessin.itemconfigure(cases[ligne][colonne], outline='black',fill='blue')
            else:                                                                                                              # rien
                dessin.itemconfigure(cases[ligne][colonne], outline='black',fill='white')
    fen.mainloop() 














if __name__ == '__main__':
    main()