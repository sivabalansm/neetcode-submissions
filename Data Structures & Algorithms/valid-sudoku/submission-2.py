class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = 9
        COLS = 9
        SQUARES = 9
        rowS = [set() for _ in range(ROWS)]
        colS = [set() for _ in range(COLS)]
        squareS = [set() for _ in range(SQUARES)]

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if val != ".":
                    squareIdx = ((r // 3) * 3) + (c // 3) 
                    if val in rowS[r] or val in colS[c] or val in squareS[squareIdx]:
                        return False
                    rowS[r].add(val)
                    colS[c].add(val)
                    squareS[squareIdx].add(val)
        return True
