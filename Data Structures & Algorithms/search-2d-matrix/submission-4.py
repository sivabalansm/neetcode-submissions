class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])

        l = 0
        r = R * C - 1

        while l <= r:
            m = (l + r) // 2
            ro = m // C
            co = m % C
            val = matrix[ro][co]
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return True
        return False
