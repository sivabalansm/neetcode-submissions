class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        c = {'(' : ')', '{' : '}', '[': ']'}

        for p in s:
            if p in c:
                st.append(p)
            elif st and c[st.pop()] != p:
                return False

        return not st