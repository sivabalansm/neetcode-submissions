class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digits = digits[::-1]
        digits.insert(0, 0)
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            digits[i - 1] += digits[i] // 10
            digits[i] = digits[i] % 10
        return digits[1:] if digits[0] == 0 else digits