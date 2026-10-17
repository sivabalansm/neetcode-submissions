class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R = len(heights)
        C = len(heights[0])

        res = 0
        mh = [(0, 0, 0)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()
        while mh:
            dh, r, c = heapq.heappop(mh)
            visit.add((r, c))
            res = max(res, dh)
            if r == R - 1 and c == C - 1:
                return res

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr >= R or nr < 0 or nc < 0 or nc >= C or (nr, nc) in visit:
                    continue
                ph = heights[r][c]
                h = heights[nr][nc]
                ndh = abs(h - ph)
                heapq.heappush(mh, (ndh, nr, nc))
        


