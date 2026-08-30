class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []

        for op in operations:
            if op == "+":
                st.append(str(int(st[-1]) + int(st[-2])))
            elif op == "C":
                st.pop()
            elif op == "D":
                st.append(str(int(st[-1]) * 2))
            else:
                st.append(op)
        
        return sum(map(int, st))
