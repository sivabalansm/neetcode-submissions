class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = False
        def dfs(pos, r, c):
            nonlocal res
            if r >= R or r < 0 or c >= C or c < 0 or pos >= len(word) or board[r][c] != word[pos]:
                return
            
            if pos == len(word) - 1:
                res = True
            
            for dr, dc in dirs:
                dfs(pos + 1, r + dr, c + dc)

        for r in range(R):
            for c in range(C):
                if res:
                    return res
                dfs(0, r, c)
        return res
        