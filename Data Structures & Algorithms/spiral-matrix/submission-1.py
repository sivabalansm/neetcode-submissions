class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        def dfs(rows, cols, r, c, dr, dc):
            if rows == 0 or cols == 0:
                return

            for i in range(cols):
                r += dr
                c += dc
                res.append(matrix[r][c])
            
            dfs(cols, rows - 1, r, c, dc, -dr)
        
        dfs(m, n, 0, -1, 0, 1)
        return res
