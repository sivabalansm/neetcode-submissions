class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        interval = intervals[0]
        res = []
        for i in range(1, len(intervals)):

            s, e = intervals[i]
            ps, pe = interval
            if pe < s:
                res.append(interval)
                interval = [s, e]
            else:
                interval = [min(s, ps), max(e, pe)]
        
        res.append(interval)
        return res