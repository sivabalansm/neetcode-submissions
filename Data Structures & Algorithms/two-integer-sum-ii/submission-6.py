class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        s = numbers[l] + numbers[r]
        while l < r:
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [l + 1, r + 1]
            s = numbers[l] + numbers[r]
        return []