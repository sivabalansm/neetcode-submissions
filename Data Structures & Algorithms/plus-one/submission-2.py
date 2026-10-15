class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ld = len(digits)
        c = 1
        for i in range(ld - 1, -1, -1):
            s = digits[i] + c
            c = s // 10
            s = s % 10
            digits[i] = s
        if c == 1:
            digits.insert(0, 1)
        return digits
