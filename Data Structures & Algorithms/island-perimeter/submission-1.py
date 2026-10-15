class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visit = set()
        def dfs(r, c):
            if (r, c) in visit:
                return 0
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return 1

            visit.add((r, c))
            res = 0
            for dr, dc in dirs:
                res += dfs(r + dr, c + dc)
            return res
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return dfs(r, c)
            