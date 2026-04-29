class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        c = {'(' : ')', '{' : '}', '[': ']'}

        for p in s:
            print(p)
            print(st)
            if p in c:
                st.append(p)
                continue
            elif st and c[st.pop()] == p:
                continue
            return False

        return not st