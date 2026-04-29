class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rl = len(grid)
        cl = len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rl or c >= cl or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            count = 1
            for dr, dc in dirs:
                count += dfs(r + dr, c + dc)
            return count
        
        for r in range(rl):
            for c in range(cl):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res