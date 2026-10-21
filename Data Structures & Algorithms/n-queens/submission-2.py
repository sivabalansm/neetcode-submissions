class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag = set()
        neg_diag = set()

        res = []
        curr = [["."] * n for i in range(n)]

        def bt(r):
            if r == n:
                res.append(["".join(c) for c in curr])
                return
            for c in range(n):
                if c not in col and r + c not in diag and r - c not in neg_diag:
                    col.add(c)
                    diag.add(r + c)
                    neg_diag.add(r - c)
                    curr[r][c] = "Q"

                    bt(r + 1)

                    curr[r][c] = "."
                    col.remove(c)
                    diag.remove(r + c)
                    neg_diag.remove(r - c)
        bt(0)
        return res
                