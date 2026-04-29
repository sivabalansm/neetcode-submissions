class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        atl = set()
        pac = set()


        def dfs(r, c, visit, prevHeight):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r, c))

            for dr, dc in dirs:
                dfs(r + dr, c + dc, visit, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS - 1, atl, 0)
        
        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS - 1, c, atl, 0)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

