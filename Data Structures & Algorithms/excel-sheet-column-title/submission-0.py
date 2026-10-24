class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        curr = columnNumber
        while curr > 0:
            curr -= 1
            offset = curr % 26
            res.append(chr(ord('A') + offset))
            curr = curr // 26
        return ''.join(res[::-1])


