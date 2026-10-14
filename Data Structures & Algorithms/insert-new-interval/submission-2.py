class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            s, e = intervals[i]
            ns, ne = newInterval

            if ne < s:
                res.append(newInterval)
                return res + intervals[i:]
            elif ns > e:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(ns, s),
                    max(ne, e)
                ]
        res.append(newInterval)
        return res