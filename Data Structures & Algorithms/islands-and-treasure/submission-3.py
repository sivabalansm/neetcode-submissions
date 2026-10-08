class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R = len(grid)
        C = len(grid[0])

        q = deque()
        visit = set()

        def addCell(r, c):
            if r < 0 or c < 0 or r >= R or c >= C or (r, c) in visit or grid[r][c] == -1:
                return
            visit.add((r, c))
            q.append([r, c])
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        dist = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in dirs:
                    addCell(r + dr, c + dc)
            dist += 1
