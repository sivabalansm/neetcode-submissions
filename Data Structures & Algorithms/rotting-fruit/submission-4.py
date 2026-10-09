class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        R = len(grid)
        C = len(grid[0])

        q = deque()
        fresh = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        time = 0
        while q and fresh > 0:
            qlen = len(q)
            for i in range(qlen):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= R or nc >= C or grid[nr][nc] == 2 or grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
            time += 1
        return time if fresh == 0 else -1