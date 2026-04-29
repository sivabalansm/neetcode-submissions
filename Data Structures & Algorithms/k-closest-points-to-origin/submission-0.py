import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        def dist(x, y):
            return ((x**2) + (y**2)) ** 0.5
        minHeap = []

        for p in points:
            heapq.heappush(minHeap, (dist(*p), p))
        
        while len(res) < k:
            res.append(heapq.heappop(minHeap)[1])
        return res