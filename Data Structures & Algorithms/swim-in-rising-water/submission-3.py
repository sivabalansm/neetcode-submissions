class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        res = grid[0][0]
        mh = [(grid[0][0], 0, 0)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while mh:
            #print(mh)
            wl, r, c = heapq.heappop(mh)
            grid[r][c] = -1

            res = max(res, wl)
            if r == R - 1 and c == C - 1:
                return res
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] == -1:
                    continue
                heapq.heappush(mh, (grid[nr][nc], nr, nc))
                grid[nr][nc] = -1
        return -1




        