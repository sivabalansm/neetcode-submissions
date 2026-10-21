class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p):
            x, y = p
            return ((x ** 2) + (y ** 2)) ** 0.5
        
        mh = []

        for p in points:
            dist = distance(p)
            heapq.heappush(mh, (-dist, p))
            if len(mh) > k:
                heapq.heappop(mh)
        
        return [p for d, p in mh]
        
