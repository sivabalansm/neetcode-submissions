class Solution:
    def isValid(self, s: str) -> bool:
        op = { '(' : ')', '[' : ']', '{' : '}' }
        st = []

        for p in s:
            if p in op:
                st.append(p)
                continue
            
            if st or p == op[st.pop()]:
                continue
            return False
        return not st