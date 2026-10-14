"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])
        starting_column = False
        starting_row = False
        for r in matrix:
            print(r)
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    if (r, 0) == (0, 0):
                        starting_row = True
                        continue
                    if (0, c) == (0, 0):
                        starting_column = True
                        continue

                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                if c == 0 and starting_column:
                    matrix[r][c] = 0
                if r == 0 and starting_row:
                    matrix[r][c] = 0

                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
            
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0