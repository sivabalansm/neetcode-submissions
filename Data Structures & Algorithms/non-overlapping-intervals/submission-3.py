class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        print(intervals)
        prev = intervals[0]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            ps, pe = prev
            if s < pe:
                prev = min(intervals[i], prev, key = lambda x : x[1])
                res += 1
        return res