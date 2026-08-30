from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.tm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.tm[key]:
            return ""
        
        res, vals = "", self.tm[key]

        l = 0
        r = len(vals) - 1

        while l <= r:
            m = (l + r) // 2
            if vals[m][0] <= timestamp:
                l = m + 1
                res = vals[m][1]
            else:
                r = m - 1
        return res

        
