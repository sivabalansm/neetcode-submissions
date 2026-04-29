class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st = []
        res = []

        def bt(on, cn):
            if on == cn == n:
                res.append("".join(st))
                return
            if on < n:
                st.append("(")
                bt(on + 1, cn)
                st.pop()
            
            if cn < on:
                st.append(")")
                bt(on, cn + 1)
                st.pop()
        bt(0, 0)
        return res
