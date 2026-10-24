class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        for i in range(left, right + 1):
            if res == 0:
                return res
            res &= i
        return res
