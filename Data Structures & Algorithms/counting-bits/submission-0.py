class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0, 1, 1, 2, 1]
        if n > 4:
            for i in range(n):
                res.append(res[-5] + 1)

        return res[:n+1]