class Solution:
    def isValid(self, s: str) -> bool:
        op = { '(' : ')', '{' : '}', '[' : ']'}
        st = []

        for c in s:
            if c in op:
                st.append(c)
                continue
            
            if st and c == op[st.pop()]:
                continue
            return False
        return not st and True

        