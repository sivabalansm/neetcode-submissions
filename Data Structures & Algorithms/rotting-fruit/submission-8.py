class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        q = deque([])

        fresh = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        time = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
            if q:
                time += 1
        return time if fresh == 0 else -1
