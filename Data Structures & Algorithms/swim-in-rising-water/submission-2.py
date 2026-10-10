class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        mh = [(grid[0][0], 0, 0)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        R = len(grid)
        C = len(grid[0])
        sn = set()
        res = 0
        while mh:
            w, r, c = heapq.heappop(mh)
            res = max(res, w)
            sn.add((r, c))

            if r == R - 1 and c == C - 1:
                return res
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= R or nc >= C or (nr, nc) in sn:
                    continue
                
                heapq.heappush(mh, (grid[nr][nc], nr, nc))
        return res



