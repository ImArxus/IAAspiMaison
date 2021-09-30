from Cell import Cell


class Grid:

    def __init__(self, cols: int, rows: int) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(0, 0, i, j) for i in range(cols)]
                     for j in range(rows)]

    def __str__(self) -> str:
        result = ""
        for r in self.grid:
            for c in r:
                result += "|" + c.__str__() + "|"
            result += "\n"
        return result

    def get_cell(self, posX: int, posY: int) -> Cell:
        return self.grid[posY][posX]

    def get_rows(self) -> int:
        return self.rows

    def get_cols(self) -> int:
        return self.cols

    def set_cell(self, posX: int, posY: int, cell: Cell) -> None:
        self.grid[posY][posX] = cell

    def list_special_cells(self) -> list:
        index = 0
        listIndexSpecialCells = []
        for cell in self.grid:
            if cell.get_dust() == 1 or cell.get_jewel() == 1:
                listIndexSpecialCells.append(index)
                index += 1
        return listIndexSpecialCells

    def list_each_path_size(self,posX: int, posY: int) -> dict:
        index = 0
        list = {}
        for cell in self.grid:
            list[index] = cell.distance(posX,posY)
            index += 1
        return list


