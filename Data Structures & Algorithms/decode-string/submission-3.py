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
                st.append('[')
            elif c == ']':

                n = num.pop()
                enc = ""
                while st[-1] != '[':
                    enc = st.pop() + enc
                st.pop() # pop out '['

                st.append(n * enc)
            else:
                st.append(c)
            #print(st)
            #print(num)
        return "".join(st)