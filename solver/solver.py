from exceptions import *

class solver:
    def __init__(self):
        self._grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        #for i in range(9):
        #    self.getGrid(i)
        self._getGridFromFile("grid")

    def solve(self):
        if self._backtrack(0, 0):
            for row in self._grid:
                print(row)
            return True
        print("Error: unable to solve")

    def _getGridFromFile(self, file):
        with open(file, 'r') as fh:
            rowNumber = 0
            for row in fh.readlines():
                try:
                    row = row .strip('\n').split(',')
                    if len(row) != 9:
                        raise InvalidRowLength

                    row = [int(column) for column in row]
                except InvalidRowLength:
                    print("Error: Row must have 9 values")
                    return
                except ValueError:
                    print("Error: All values must be integers")
                    return
                for index, column in enumerate(row):
                    self._grid[rowNumber][index] = column
                    index += 1
                rowNumber += 1



    def getGrid(self, rowNumber):
        print(f"Enter row {rowNumber + 1} in form c1,c2,c3,...,c9, if empty use 0: ")
        try:
            row = input()
            row = row.split(',')
            if len(row) != 9:
                raise InvalidRowLength

            row = [int(column) for column in row]

        except InvalidRowLength:
            print("Error: Row must have 9 values")
            return
        except ValueError:
            print("Error: All values must be integers")
            return

        for index, column in enumerate(row):
            self._grid[rowNumber][index] = column
            index += 1

    def _isValid(self, row, column, value):
        validRow = value not in self._grid[row]
        validColumn = value not in [self._grid[r][column] for r in range(9)]
        validSquare = value not in [self._grid[r][c] for r in range(row//3*3, row//3*3+3) for c in range(column//3*3, column//3*3+3) if self._grid[r][c] != 0]
        return validRow and validColumn and validSquare
        

    def _backtrack(self, row, column):
        if row == 9:
            return True
        elif column == 9:
            return self._backtrack(row+1, 0)
        elif self._grid[row][column] != 0:
            return self._backtrack(row, column+1)
        else:
            for value in range(1, 10):
                if self._isValid(row, column, value):
                    self._grid[row][column] = value
                    if self._backtrack(row, column+1):
                        return True
                    self._grid[row][column] = 0
            return False
solve = solver()
solve.solve()
