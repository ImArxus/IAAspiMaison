from Environment.Cell import Cell


# Classe permettant la représentation du manoir sous la forme d'une grille
class Grid:
    
    # Constructeur
    def __init__(self, cols: int, rows: int) -> None:
        self.rows = rows # Représentation du nombre de lignes de la grille
        self.cols = cols # Représentation du nombre de colonnes de la grille
        # Création de la grille
        self.grid = [[Cell(0, 0, i, j) for i in range(cols)]
                     for j in range(rows)]
    
    # Getters et setters
    def get_rows(self) -> int:
        return self.rows

    def get_cols(self) -> int:
        return self.cols
    
    # Fonction d'affichage de la grille sous la forme de tableau
    def __str__(self) -> str:
        result = ""
        for r in self.grid:
            for c in r:
                result += "|" + c.__str__() + "|"
            result += "\n"
        return result

    # Fonction permettant de retourner une cellule de la grille en utilisant ses positions horizontales et verticales
    def get_cell(self, posX: int, posY: int) -> Cell:
        return self.grid[posY][posX]

    # Fonction permettant de définir la valeur d'une cellule d'une grille
    def set_cell(self, posX: int, posY: int, cell: Cell) -> None:
        self.grid[posY][posX] = cell
