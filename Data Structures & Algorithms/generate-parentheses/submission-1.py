class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.subs = []

        def bt(o, c):
            if len(self.subs) == 2 * n:
                self.res.append("".join(self.subs))
                return

            if o < n:
                self.subs.append("(")
                bt(o + 1, c)
                self.subs.pop()
            
            if c < o:
                self.subs.append(")")
                bt(o, c + 1)
                self.subs.pop()
        bt(0, 0)
        return self.res
            

            
