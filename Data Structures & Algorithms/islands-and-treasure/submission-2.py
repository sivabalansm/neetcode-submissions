class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        R = len(grid)
        C = len(grid[0])


        visit = set()
        def dfs(r, c, prev):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == -1 or (r, c) in visit:
                return

            if grid[r][c] >= prev + 1:
                grid[r][c] = prev + 1
            else:
                return
            
            visit.add((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc, prev + 1)
            visit.remove((r, c))
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    dfs(r, c, -1)
            
            