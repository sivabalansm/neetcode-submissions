class Solution:
    def decodeString(self, s: str) -> str:
        str_st = []
        count_st = []
        cur = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                str_st.append(cur)
                count_st.append(k)
                cur = ""
                k = 0
            elif c == "]":
                temp = cur
                cur = str_st.pop()
                count = count_st.pop()
                cur += temp * count
            else:
                cur += c
        return cur