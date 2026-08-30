class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == "+":
                n1 = st.pop()
                n2 = st.pop()
                st.append(n1 + n2)
            elif t == "*":
                n1 = st.pop()
                n2 = st.pop()
                st.append(n1 * n2)
            elif t == "-":
                n1 = st.pop()
                n2 = st.pop()
                st.append(n2 - n1)
            elif t == "/":
                n1 = st.pop()
                n2 = st.pop()
                st.append(n2 // n1)
            else:
                st.append(int(t))
        return st[-1]