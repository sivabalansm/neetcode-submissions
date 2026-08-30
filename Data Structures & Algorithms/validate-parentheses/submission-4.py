class Solution:
    def isValid(self, s: str) -> bool:
        op = { '(' : ')', '[' : ']', '{' : '}' }
        st = []

        for p in st:
            if p in op:
                st.append(p)
                continue
            
            if st and p != op[st.pop()]:
                return False
        return not st