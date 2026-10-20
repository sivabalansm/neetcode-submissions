"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ls = defaultdict(int)

        for interval in intervals:
            s = interval.start
            e = interval.end
            ls[s] += 1
            ls[e] -= 1
        
        res = 0
        count = 0
        for i in sorted(ls.keys()):
            count += ls[i]
            res = max(res, count)
        
        return res