from Cell import Cell


class Grid:

    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(0, 0, i, j) for i in range(cols)]
                     for j in range(rows)]

    def __str__(self) -> str:
        result = ""
        for r in self.grid:
            for c in r:
                result += c.__str__()
            result += "\n"
        return result

    def get_cell(self, posX, posY):
        return self.grid[posX][posY]

    def get_rows(self):
        return self.rows
    
    def get_cols(self):
        return self.cols