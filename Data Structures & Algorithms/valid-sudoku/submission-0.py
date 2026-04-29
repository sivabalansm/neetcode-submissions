class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rl = len(board)
        cl = len(board[0])
        cols = {i:set() for i in range(9)}
        rows = {i:set() for i in range(9)}
        squares = {i:set() for i in range(9)}
        for r in range(rl):
            for c in range(cl):
                n = board[r][c]
                if n == ".": continue
                if n in rows[r] or n in cols[c] or n in squares[ ((r // 3) * 3) + (c // 3) ]:
                    print(n)
                    return False
                rows[r].add(n)
                cols[c].add(n)
                squares[((r // 3) * 3) + (c // 3)].add(n)
        return True