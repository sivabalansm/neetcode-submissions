class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        subend = {}
        for i, c in enumerate(s):
            subend[c] = i

        res = []
        end = -1
        count = 0
        for i, c in enumerate(s):
            end = max(end, subend[c])
            count += 1
            if i == end:
                res.append(count)
                count = 0
        return res

