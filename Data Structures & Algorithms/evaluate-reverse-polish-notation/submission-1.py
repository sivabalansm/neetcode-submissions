class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ops = {'+', '-', '*', '/'}
        for t in tokens:
            if t in ops:
                n1 = st.pop()
                n2 = st.pop()
                r = 0
                if t == '+':
                    r = n1 + n2
                elif t == '-':
                    r = n2 - n1
                elif t == '/':
                    r = n2 // n1
                else:
                    r = n2 * n1
                st.append(r)
            else:
                st.append(int(t))
        return st[0]

        