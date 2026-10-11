class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        R = len(matrix)
        C = len(matrix[0])
        memo = {}
        def dfs(r, c, prev):
            if r >= R or r < 0 or c >= C or c < 0 or matrix[r][c] <= prev:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            res = 0
            for dr, dc in dirs:
                res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            memo[(r, c)] = res
            return res
        res = 0
        for r in range(R):
            for c in range(C):
                res = max(res, dfs(r, c, -1))
        return res