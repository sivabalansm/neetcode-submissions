class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * (m + 1) for _ in range(n + 1)]
        grid[n - 1][m - 1] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i][j + 1] + grid[i + 1][j]
        return grid[0][0]
