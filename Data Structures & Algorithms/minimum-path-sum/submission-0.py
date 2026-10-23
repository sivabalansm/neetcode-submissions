class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    continue

                bottom = float("inf")
                right = float("inf")

                if r + 1 < n:
                    bottom = grid[r + 1][c]

                if c + 1 < m:
                    right = grid[r][c + 1]
                
                grid[r][c] += min(bottom, right)
        return grid[0][0]
                

                    