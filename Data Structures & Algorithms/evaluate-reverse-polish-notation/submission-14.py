class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == "+":
                n2, n1 = st.pop(), st.pop()
                st.append(n1 + n2)
            elif t == "*":
                n2, n1 = st.pop(), st.pop()
                st.append(n1 * n2)
            elif t == "/":
                n2, n1 = st.pop(), st.pop()
                st.append(n1 / n2)
            elif t == "-":
                n2, n1 = st.pop(), st.pop()
                st.append(n1 - n2)
            else:
                st.append(int(t))
        return st[-1]