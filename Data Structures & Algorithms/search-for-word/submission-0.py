class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        wlen = len(word)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.res = False

        def dfs(r, c, subs):
            if len(subs) == wlen and "".join(subs) == word:
                self.res = True

            if self.res or r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == "#" or len(subs) == wlen:
                return
            
            subs.append(board[r][c])
            board[r][c] = "#"
            for d in dirs:
                dr, dc = d
                dfs(r + dr, c + dc, subs)
            board[r][c] = subs.pop()
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, [])

        return self.res

                