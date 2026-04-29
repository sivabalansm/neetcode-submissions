class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.res = 0
        self.count = 0
        rl = len(grid)
        cl = len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rl or c >= cl or grid[r][c] == 0:
                return

            self.count += 1
            grid[r][c] = 0
            self.res = max(self.res, self.count)

            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        
        for r in range(rl):
            for c in range(cl):
                if grid[r][c] == 1:
                    self.count = 0
                    dfs(r, c)
        return self.res