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
        intervals.sort(key = lambda interval : interval.start)
        # print(intervals)
        ps, pe = intervals[0].start, intervals[0].end

        # print(ps, pe)
        for i in range(1, len(intervals)):
            s, e = intervals[i].start, intervals[i].end

            if pe <= s:
                ps, pe = s, e
            else:
                return False
        return True
        
