class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        i = 0
        while i < len(s):
            num = table[s[i]]
            if i + 1 < len(s):
                next_num = table[s[i + 1]]
                if next_num > num:
                    num = next_num - num
                    i += 1
            total += num
            i += 1
        return total
