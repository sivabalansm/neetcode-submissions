class MedianFinder:

    def __init__(self):
        self.mah = [] # left
        self.mh = [] # right

    def addNum(self, num: int) -> None:
        if not self.mh and not self.mah:
            heapq.heappush(self.mh, num)
            return
        
        #ma = self.mah[0]
        mi = self.mh[0]
        
        if num > mi:
            heapq.heappush(self.mh, num)
        else:
            heapq.heappush_max(self.mah, num)
        
        if abs(len(self.mah) - len(self.mh)) > 1:
            if len(self.mah) > len(self.mh):
                heapq.heappush(self.mh, heapq.heappop_max(self.mah))
            else:
                heapq.heappush_max(self.mah, heapq.heappop(self.mh))
        
    def findMedian(self) -> float:
        if len(self.mah) == len(self.mh):
            return (self.mah[0] + self.mh[0]) / 2
        else:
            return self.mah[0] if len(self.mah) > len(self.mh) else self.mh[0]
        
        
        