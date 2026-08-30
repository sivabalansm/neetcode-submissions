class Solution:
    def twoSum(self, A: List[int], target: int) -> List[int]:
        l = 0
        r = len(A) - 1

        while l < r:
            s = A[l] + A[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [l + 1, r + 1]
                