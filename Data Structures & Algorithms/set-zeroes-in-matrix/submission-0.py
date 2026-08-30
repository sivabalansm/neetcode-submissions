class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def setZeroRow(row):
            for j in range(COLS):
                matrix[row][j] = 0

        def setZeroCol(col):
            for  i in range(ROWS):
                matrix[i][col] = 0
        
        zeroedCol = set()

        i = 0
        while i < ROWS:
            j = 0
            while j < COLS:
                if j not in zeroedCol and matrix[i][j] == 0:
                     setZeroRow(i)
                     setZeroCol(j)
                     zeroedCol.add(j)
                     break
                j += 1
            
            i += 1
                
        
        