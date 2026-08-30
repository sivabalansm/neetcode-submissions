class Solution:
    def isValid(self, s: str) -> bool:
        cor = { ")" : "(", "]" : "[", "}" : "{"}
        st = []

        for p in s:
            if p not in cor:
                st.append(p)
            else:
                if not st or st.pop() != cor[p]:
                    return False
        return True
