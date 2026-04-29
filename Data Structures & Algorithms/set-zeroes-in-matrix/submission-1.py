class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        zR = [False] * ROWS
        zC = [False] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zR[r] = True
                    zC[c] = True
        
        for r in range(ROWS):
            for c in range(COLS):
                if zR[r] or zC[c]:
                    matrix[r][c] = 0
        





                
        
        