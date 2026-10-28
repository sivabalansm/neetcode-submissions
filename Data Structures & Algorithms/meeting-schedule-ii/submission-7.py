"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        tm = defaultdict(int)
        L, R = float("inf"), 0
        for i in range(len(intervals)):
            s = intervals[i].start
            e = intervals[i].end
            tm[s] += 1
            tm[e] -= 1
            L = min(L, s)
            R = max(R, e)
        rooms = 0
        res = 0
        print(tm)
        for i in range(L, R + 1):
            if tm[i] != 0:
                rooms += tm[i]
                res = max(res, rooms)
        return res