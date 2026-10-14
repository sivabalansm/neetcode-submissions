"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        prev = intervals[0]
        for i in range(1, len(intervals)):
            s = intervals[i].start
            e = intervals[i].end
            ps, pe = prev.start, prev.end

            if s < pe:
                return False
            prev = intervals[i]
        return True
            