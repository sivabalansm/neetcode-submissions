class Solution:
    def isValid(self, s: str) -> bool:
        cor = { ")" : "(", "]" : "[", "}" : "{" }
        st = []

        for s in st:
            if s not in cor:
                st.append(s)
            else:
                if st and st.pop() == cor[s]:
                    continue
                return False
        return True
