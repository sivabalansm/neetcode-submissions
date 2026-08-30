class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        """
        n = 0101
        1 = 0001
        res = 0001 << 1
        res = 0010
        n = 0010
        """
        for i in range(32):
            if n & 1:
                res += 1
            n = n >> 1
            res = res << 1
        return res >> 1