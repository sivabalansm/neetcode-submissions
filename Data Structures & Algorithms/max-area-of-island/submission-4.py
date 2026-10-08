class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        res = 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            total = 1
            for dr, dc in dirs:
                total += dfs(r + dr, c + dc)
            return total

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res
        
