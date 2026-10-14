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

        for i in intervals:
            ls[i.start] += 1
            ls[i.end] -= 1
        
        res = 0
        count = 0
        for se in range(max(ls.keys()) + 1):
            if ls[se] != 0:
                count += ls[se]
                res = max(res, count)
        return res