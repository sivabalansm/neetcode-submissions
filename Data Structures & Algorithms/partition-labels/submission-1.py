class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        subend = {}
        for i, c in enumerate(s):
            subend[c] = i
        
        end = 0
        count = 1
        res = []
        for i, c in enumerate(s):
            end = max(end, subend[c])

            if i == end:
                res.append(count)
                count = 0
            count += 1
        return res
