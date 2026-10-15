class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R = len(heights)
        C = len(heights[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pac = set()
        atl = set()
        def dfs(r, c, oc, prev):
            if r < 0 or r >= R or c < 0 or c >= C or heights[r][c] < prev or (r, c) in oc:
                return
            
            oc.add((r, c))

            for dr, dc in dirs:
                dfs(r + dr, c + dc, oc, heights[r][c])
        
        for c in range(C):
            dfs(0, c, pac, 0)
            dfs(R - 1, c, atl, 0)
        
        for r in range(R):
            dfs(r, 0, pac, 0)
            dfs(r, C - 1, atl, 0)
        
        res = []
        for r in range(R):
            for c in range(C):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
