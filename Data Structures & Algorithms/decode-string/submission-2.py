class Solution:
    def decodeString(self, s: str) -> str:
        num = []
        st = []
        """
        3 
        a x b zcccc
        """
        nc = []
        for c in s:
            if c.isdigit():
                nc.append(c)
            elif c == '[':
                num.append(int("".join(nc)))
                nc.clear()
            elif c == ']':
                n = num.pop()
                enc = st.pop()
                if st:
                    st[-1] += n * enc
                else:
                    st.append(n * enc)
            else:
                st.append(c)
            #print(st)
            #print(num)
        return "".join(st)