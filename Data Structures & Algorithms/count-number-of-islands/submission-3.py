class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        R = len(grid)
        C = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res
            