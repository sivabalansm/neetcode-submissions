"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x : x.start)
        prevEnd = intervals[0].end
        for inte in intervals[1:]:
            start = inte.start
            end = inte.end
            if not prevEnd <= start:
                return False
            prevEnd = end
        return True