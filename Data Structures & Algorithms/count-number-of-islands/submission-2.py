class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rl = len(grid)
        cl = len(grid[0])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rl or c >= cl or grid[r][c] ==  "0":
                return

            grid[r][c] = "0"
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        res = 0
        for r in range(rl):
            for c in range(cl):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res