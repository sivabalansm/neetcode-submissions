class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        interval = newInterval

        for i in range(len(intervals)):
            s, e = intervals[i]

            if e < interval[0]:
                res.append([s, e])
            elif interval[1] < s:
                res.append(interval)
                return res + intervals[i:]
            else:
                interval = [
                    min(s, interval[0]),
                    max(e, interval[1])
                ]
        res.append(interval)
        return res

