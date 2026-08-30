class TimeMap:
    def __init__(self):
        self.time_map = dict()
    
    def _create_pair(self, value, timestamp):
        return (value, timestamp)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = [self._create_pair(value, timestamp)]
            return
        
        pairs = self.time_map[key]
        pairs.append(self._create_pair(value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # binary search
        if key not in self.time_map:
            return ""
        
        pairs = self.time_map[key]

        l = 0
        r = len(pairs) - 1
        cand = -1
        while l <= r:
            m = (l + r) // 2

            if pairs[m][1] == timestamp:
                return pairs[m][0]
            
            if pairs[m][1] < timestamp:
                l = m + 1
                cand = m
            else:
                r = m - 1
        return pairs[cand][0]
        

        
