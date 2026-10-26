class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for tok in tokens:
            if tok == "+":
                n2, n1 = st.pop(), st.pop()
                st.append(n1 + n2)
            elif tok == "-":
                n2, n1 = st.pop(), st.pop()
                st.append(n1 - n2)
            elif tok == "*":
                n2, n1 = st.pop(), st.pop()
                st.append(n1 * n2)
            elif tok == "/":
                n2, n1 = st.pop(), st.pop()
                st.append(int(n1 / n2))
            else:
                st.append(int(tok))
        return st[-1]