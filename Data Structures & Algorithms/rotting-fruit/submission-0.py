class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rl = len(grid)
        cl = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        time, fresh = 0, 0

        for r in range(rl):
            for c in range(cl):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            l = len(q)
            for i in range(l):
                r, c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= rl or nc >= cl or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc)) 
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1