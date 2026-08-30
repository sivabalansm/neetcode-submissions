class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+", "*", "-", "/"}
        st = []
        for t in tokens:
            if t in op:
                n2 = int(st.pop())
                n1 = int(st.pop())
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
                st.append(t)
        return st[0]