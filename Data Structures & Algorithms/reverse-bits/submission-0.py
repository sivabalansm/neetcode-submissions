class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        """
        0101
        0001
        res = 0001 << 1
        res = 0010
        """
        for i in range(31):
            if n & 1:
                res += 1
            n = n >> 1
            res = res << 1
        return res