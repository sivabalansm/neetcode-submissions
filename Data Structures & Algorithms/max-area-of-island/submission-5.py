class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        R = len(grid)
        C = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            res = 1
            for dr, dc in dirs:
                res += dfs(r + dr, c + dc)
            return res

        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res