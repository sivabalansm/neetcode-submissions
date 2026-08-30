class Solution:
    def decodeString(self, s: str) -> str:
        str_st = []
        num_st = []
        cur = ""
        k = 0

        for c in s:
            if c.isnumeric():
                k = k * 10 + int(c)
            elif c == "[":
                num_st.append(k)
                str_st.append(cur)
                cur = ""
                k = 0
            elif c == "]":
                temp = cur
                cur = str_st.pop()
                count = num_st.pop()
                cur += temp * count
            else:
                cur += c
        return cur