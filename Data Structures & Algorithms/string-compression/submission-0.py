class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        res = i = 0

        while i < n:
            chars[res] = chars[i]
            res += 1
            j = i + 1
            while j < n and chars[i] == chars[j]:
                j += 1

            if j - i > 1:
                for c in str(j - i):
                    chars[res] = c
                    res += 1
            i = j
        return res
            