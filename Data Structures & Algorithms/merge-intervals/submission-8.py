class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        tm = defaultdict(int)

        L, R = 0, 0
        for s, e in intervals:
            tm[s] += 1
            tm[e] -= 1
            L = min(s, L)
            R = max(e, R)
            if s == e:
                tm[s] = float("inf")
        res = []
        have = 0
        interval = []
        print(tm)
        for i in range(L, R + 1):
            if tm[i] == float('inf'):
                res.append([i, i])
            elif tm[i] != 0:
                interval.append(i)
                have += tm[i]
            
                if have == 0:
                    res.append([interval[0], interval[-1]])
                    interval = []

        return res

            


        