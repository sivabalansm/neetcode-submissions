class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.dic[key]
        if not vals:
            return ""
        
        l = 0
        r = len(vals) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if vals[m][0] < timestamp:
                l = m + 1
                res = vals[m][1]
            elif vals[m][0] > timestamp:
                r = m - 1
            else:
                return vals[m][1]
        return res

        
