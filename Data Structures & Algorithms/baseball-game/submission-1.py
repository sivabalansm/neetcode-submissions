class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        st = []
        for op in operations:
            if op == "C":
                res -= st.pop()
            elif op == "+":
                s = st[-1] + st[-2]
                st.append(s)
                res += s
            elif op == "D":
                d = st[-1] * 2
                st.append(d)
                res += d
            else:
                st.append(int(op))
                res += int(op)
        return res