class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        ps, pe = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s < pe:
                if e < pe:
                    ps, pe = s, e
                res += 1
        return res
