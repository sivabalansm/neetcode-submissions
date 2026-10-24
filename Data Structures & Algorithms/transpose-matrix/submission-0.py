class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R = len(matrix)
        C = len(matrix[0])
        res = []
        for c in range(C):
            new_row = []
            for r in range(R):
                new_row.append(matrix[r][c])
            res.append(new_row)
        return res