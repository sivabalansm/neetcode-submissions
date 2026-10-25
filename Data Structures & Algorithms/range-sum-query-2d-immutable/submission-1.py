class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        R = len(matrix)
        C = len(matrix[0])
        self.sumMat = [[0] * (C + 1) for _ in range(R + 1)]

        for r in range(R):
            prefix = 0
            for c in range(C):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        topLeft = self.sumMat[row1 - 1][col1 - 1]
        top = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        bottomRight = self.sumMat[row2][col2]
        return bottomRight - top - left + topLeft



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)