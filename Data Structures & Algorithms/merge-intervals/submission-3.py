class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            cs, ce = curr
            s, e = intervals[i]
            if ce < s:
                res.append([cs, ce])
                curr = [s, e]
            elif s <= ce:
                curr = [min(cs, s), max(ce, e)]
        res.append(curr)
        return res
            
                
