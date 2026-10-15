from math import log2, ceil
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        bits = ceil(log2(1000))
        for i in range(n + 1):
            c = 0
            for _ in range(bits):
                c += i & 1
                i = i >> 1
            res.append(c)
        return res