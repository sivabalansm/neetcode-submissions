class MedianFinder:

    def __init__(self):
        self.left = [] # smaller nums so max heap
        self.right = [] # bigger nums so min heap

    def addNum(self, num: int) -> None:
        if not self.left and not self.right:
            heapq.heappush_max(self.left, num)
            return
        
        lnum = self.left[0]

        if num < lnum:
            heapq.heappush_max(self.left, num)
        else:
            heapq.heappush(self.right, num)
        
        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
                heapq.heappush(self.right, heapq.heappop_max(self.left))
            else:
                heapq.heappush_max(self.left, heapq.heappop(self.right))
        
    def findMedian(self) -> float:

        if len(self.left) == len(self.right):
            return (self.left[0] + self.right[0]) / 2
        else:
            if len(self.left) > len(self.right):
                return self.left[0]
            else:
                return self.right[0]
        
        