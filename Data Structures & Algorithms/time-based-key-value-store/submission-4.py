from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.tm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.tm[key]:
            return ""
        
        vals = self.tm[key]
        l = 0
        r = len(vals) - 1

        while l <= r:
            m = (l + r) // 2
            if timestamp < vals[m][0]:
                r = m - 1
            elif vals[m][0] < timestamp:
                l = m + 1
            else:
                return vals[m][1]
        return vals[m][1] if vals[m][0] <= timestamp else ""

        
