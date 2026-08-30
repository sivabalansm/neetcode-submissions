class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(r, c, visit):

            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return True

            if (r, c) in visit or board[r][c] == "X":
                return False
            
            visit.add((r, c))

            boolSum = []
            for dr, dc in dirs:
                boolSum.append(dfs(r + dr, c + dc, visit))
            if not any(boolSum):
                board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    print("Found", r, c)
                    dfs(r, c, set())