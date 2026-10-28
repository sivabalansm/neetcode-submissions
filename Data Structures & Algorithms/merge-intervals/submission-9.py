class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        tm = defaultdict(int)

        L, R = 0, 0
        for s, e in intervals:
            tm[s] += 1
            tm[e] -= 1
            L = min(s, L)
            R = max(e, R)
        res = []
        have = 0
        interval = []
        for i in sorted(tm):
            interval.append(i)
            have += tm[i]
        
            if have == 0:
                res.append([interval[0], interval[-1]])
                interval = []

        return res

            


        