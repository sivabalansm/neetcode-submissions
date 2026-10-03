class Solution:
    def isValid(self, s: str) -> bool:
        compl = {")" : "(", "]" : "[", "}" : "{"}
        st = []

        for c in s:
            if c in compl:
                if st and st[-1] == compl[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        
        return not st