from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.d[key]
        if not vals:
            return ""
        
        l = 0
        r = len(vals) - 1
        res = "" 
        while l <=  r:
            m = (l + r) // 2
            mt = vals[m][0]
            if mt <= timestamp:
                res = vals[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
