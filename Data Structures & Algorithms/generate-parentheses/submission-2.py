class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bt(curr, op, cl):
            nonlocal res
            if op == cl == n:
                res.append(curr)
                return
            if op > n or cl > n:
                return
            print(curr)
            if op < n:
                bt(curr + "(", op + 1, cl)
            if op > cl:
                bt(curr + ")", op, cl + 1)
        bt("", 0, 0)
        return res
            

