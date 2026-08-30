class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            lx, ly = res[-1]
            nx, ny = intervals[i]
            if ly < nx:
                res.append(intervals[i])
            else:
                newInterval = [min(lx, nx), max(ly, ny)]
                res.pop()
                res.append(newInterval)
        return res