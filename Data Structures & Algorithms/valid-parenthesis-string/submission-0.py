class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        (**))
        (*))(*)))
        """

        l = []
        st = []

        for c in s:
            if c == "(":
                l.append(c)
            elif c == "*":
                st.append(c)
            else:
                if l:
                    l.pop()
                elif st:
                    st.pop()
                else:
                    return False
        return len(l) == 0 or len(st) >= len(l)