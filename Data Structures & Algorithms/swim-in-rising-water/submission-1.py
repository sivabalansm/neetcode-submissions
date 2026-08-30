import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        minH = [[grid[0][0], 0, 0]]
        visit = set()
        while minH:
            t, r, c = heapq.heappop(minH)

            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in dirs:
                nR, nC = r + dr, c + dc
                if nR < 0 or nC < 0 or nR >= N or nC >= N or (nR, nC) in visit:
                    continue
                visit.add((nR, nC))
                heapq.heappush(minH, [max(t, grid[nR][nC]), nR, nC])
        return -1
