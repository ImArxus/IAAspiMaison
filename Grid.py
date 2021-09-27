from Cell import Cell


class Grid:

    def __init__(self, rows, cols) -> None:
        self.grid = [[Cell(0, 0, i, j) for i in range(cols)]
                     for j in range(rows)]

    def __str__(self) -> str:
        result = ""
        for r in self.grid:
            for c in r:
                result += c.__str__()
            result += "\n"
        return result
