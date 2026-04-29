class Solution:
    def isValid(self, s: str) -> bool:
        op = { '(' : ')', '[' : ']', '{' : '}' }
        st = []

        for p in s:
            if p in op:
                st.append(p)
                continue
            
            if not st or p != op[st.pop()]:
                return False
        return not st