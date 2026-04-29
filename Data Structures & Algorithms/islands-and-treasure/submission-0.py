class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rl = len(grid)
        cl = len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


        def dfs(r, c, dist):
            if r < 0 or c < 0 or r >= rl or c >= cl or grid[r][c] == -1 or grid[r][c] < dist:
                return
            
            grid[r][c] = min(grid[r][c], dist)
            for dr, dc in dirs:

                dfs(r + dr, c + dc, dist + 1)
        
        for r in range(rl):
            for c in range(cl):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
            

