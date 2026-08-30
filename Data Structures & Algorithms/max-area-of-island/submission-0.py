class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res = 0
        rl = len(grid)
        cl = len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, spot, count):
            if r < 0 or c < 0 or r >= rl or c >= cl or grid[r][c] != spot:
                return
            
            grid[r][c] = -1
            self.res = max(self.res, count)

            for dr, dc in dirs:
                dfs(r + dr, c + dc, spot, count + 1)
        
        for r in range(rl):
            for c in range(cl):
                if grid[r][c] > -1:
                    dfs(r, c, grid[r][c], 1)
        return self.res