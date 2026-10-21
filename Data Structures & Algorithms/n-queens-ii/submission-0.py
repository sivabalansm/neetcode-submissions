class Solution:
    def totalNQueens(self, n: int) -> int:
        diag = set()
        neg_diag = set()
        col = set()

        res = 0

        def bt(r):
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                if c not in col and r + c not in diag and r - c not in neg_diag:
                    col.add(c)
                    diag.add(r + c)
                    neg_diag.add(r - c)

                    bt(r + 1)

                    col.remove(c)
                    diag.remove(r + c)
                    neg_diag.remove(r - c)
        bt(0)
        return res