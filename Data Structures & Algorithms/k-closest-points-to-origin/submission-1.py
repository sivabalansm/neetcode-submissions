class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return ((x ** 2) + (y ** 2)) ** 0.5
        
        mh = []
        for p in points:
            x, y = p
            d = dist(x, y)
            heapq.heappush(mh, (d, x, y))
        
        return [[mh[i][1], mh[i][2]] for i in range(k)]

