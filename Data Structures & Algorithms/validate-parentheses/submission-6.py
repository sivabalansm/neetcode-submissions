class Solution:
    def isValid(self, s: str) -> bool:
        op = { '(' : ')', '[' : ']', '{' : '}' }
        st = []
        if len(s) == 1:
            return False
    

        for p in s:
            if p in op:
                st.append(p)
                continue
            
            if st and p != op[st.pop()]:
                return False
        return not st