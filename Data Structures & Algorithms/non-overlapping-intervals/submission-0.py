class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()

        pe = intervals[0][1]
        for i in range(1, len(intervals)):
            cs, ce = intervals[i]

            if not pe <= cs:
                pe = min(pe, ce)
                res += 1
        return res