class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+", "*", "-", "/"}
        st = []
        for t in tokens:
            if t in op:
                n2 = st.pop()
                n1 = st.pop()
                r = 0
                if t == "+":
                    r = n1 + n2
                elif t == "-":
                    r = n1 - n2
                elif t == "*":
                    r = n1 * n2
                else:
                    r = n1 / n2
                st.append(r)
            else:
                st.append(int(t))
        return int(st[0])