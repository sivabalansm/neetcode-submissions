class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, prevValue):
            if r < 0 or c < 0 or r == len(matrix) or c == len(matrix[0]) or matrix[r][c] <= prevValue:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = 1
            for dr, dc in dirs:
                res = max(res, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dfs(r, c, -1)
        
        return max(dp.values())