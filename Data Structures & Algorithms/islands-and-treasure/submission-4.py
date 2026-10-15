class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        R = len(grid)
        C = len(grid[0])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] != INF:
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
        
