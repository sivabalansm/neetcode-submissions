class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        res = 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(curr, r, c):
            nonlocal res
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return
            curr += 1
            res = max(res, curr)
            grid[r][c] = 0

            for dr, dc in dirs:
                dfs(curr, r + dr, c + dc)
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    dfs(0, r, c)
        return res
        
