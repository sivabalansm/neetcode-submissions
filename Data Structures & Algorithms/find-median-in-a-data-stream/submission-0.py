import heapq
class MedianFinder:
    def __init__(self):
        self.smallHeap = []
        self.bigHeap = []

    def addNum(self, num: int) -> None:
        if self.bigHeap and num > self.bigHeap[0]:
            heapq.heappush(self.bigHeap, num)
        else:
            heapq.heappush(self.smallHeap, -num)
        
        if len(self.smallHeap) > len(self.bigHeap) + 1:
            val = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.bigHeap, val)
        if len(self.bigHeap) > len(self.smallHeap) + 1:
            val = -heapq.heappop(self.bigHeap)
            heapq.heappush(self.smallHeap, val)

    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.bigHeap):
            return (-self.smallHeap[0] + self.bigHeap[0]) / 2
        
        if len(self.smallHeap) > len(self.bigHeap):
            return -self.smallHeap[0]
        else:
            return self.bigHeap[0]

        
        