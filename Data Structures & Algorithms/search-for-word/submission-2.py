class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS = len(board)
        COLS = len(board[0])
        self.res = False

        def dfs(i, r, c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or board[r][c] == "#" or i >= len(word) or self.res:
                return
            if i == len(word) - 1 and board[r][c] == word[-1]:
                self.res = True
                return

            if board[r][c] == word[i]:
                board[r][c] = "#"
                for dr, dc in dirs:
                    dfs(i + 1, r + dr, c + dc)
                board[r][c] = word[i]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(0, r, c)

        return self.res
