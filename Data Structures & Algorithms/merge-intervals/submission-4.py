class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(start for start, end in intervals)

        ib = [0] * (max_val + 1)

        for s, e in intervals:
            ib[s] = max(e, ib[s])
        print(ib)
        have = -1
        cs = -1
        res = []
        for i in range(max_val + 1):
            if ib[i] != 0:
                if cs == -1:
                    cs = i
                have = max(have, ib[i])
            if have == i:
                res.append([cs, have])
                cs = -1
                have = -1
        if cs != -1 and have != -1:
            res.append([cs, have])
        return res