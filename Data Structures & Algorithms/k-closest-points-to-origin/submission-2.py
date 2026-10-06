class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return ((x ** 2) + (y ** 2)) ** 0.5
        
        mah = []
        for x, y in points:
            d = -1 * dist(x, y)
            heapq.heappush(mah, (d, x, y))
            if len(mah) > k:
                heapq.heappop(mah)
        return [[x, y] for d, x, y in mah]