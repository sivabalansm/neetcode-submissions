class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        op = {'(' : ')', '[' : ']', '{' : '}'}
        for i in range(len(s)):
            if s[i] in op:
                st.append(s[i])
                continue
            
            if st and s[i] == op[st.pop()]:
                continue
            return False
        
        return not st and True


        