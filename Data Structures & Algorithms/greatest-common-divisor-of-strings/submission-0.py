class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        n = math.gcd(l1, l2)
        p = -1
        for i in range(n):
            if str1[i] == str2[i]:
                p += 1
        if p == -1:
            return ""

        while p >= 0:
            sub = str1[:p + 1]
            ls = len(sub)
            if sub * (l1 // ls) == str1 and sub * (l2 // ls) == str2:
                return sub
            p -= 1
        return ""
