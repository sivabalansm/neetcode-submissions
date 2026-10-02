class Solution:
    def isValid(self, s: str) -> bool:
        corr = {")" : "(", "}" : "{", "]" : "["}

        st = []

        for p in s:
            if p not in corr:
                st.append(p)
            else:
                if not st or corr[p] != st.pop():
                    return False
        
        return not st


