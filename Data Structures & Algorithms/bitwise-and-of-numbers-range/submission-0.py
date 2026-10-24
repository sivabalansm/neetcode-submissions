class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = left
        for i in range(left, right + 1):
            res &= i
        return res
