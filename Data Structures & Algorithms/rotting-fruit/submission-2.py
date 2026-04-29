from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        fresh = 0 
        time = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        if not fresh:
            return 0

        while q:
            for _ in range(len(q)):
                rr, rc = q.popleft()

                for dr, dc in dirs:
                    nr, nc = rr + dr, rc + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
            time += 1
        
        return time - 1 if fresh == 0 else -1