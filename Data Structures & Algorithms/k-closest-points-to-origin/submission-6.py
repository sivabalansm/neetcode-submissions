class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mah = []

        def distance(p1):
            return ((p1[0] ** 2) + (p1[1]  ** 2)) ** 0.5
        
        for p in points:
            d = distance(p)
            heapq.heappush_max(mah, (d, p))
            if len(mah) > k:
                heapq.heappop_max(mah)
        
        return [p for _, p in mah]
        
