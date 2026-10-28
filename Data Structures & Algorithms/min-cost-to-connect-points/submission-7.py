class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        N = len(points)
        adj = defaultdict(list)
        for i in range(N):
            p1 = points[i]
            for j in range(i + 1, N):
                p2 = points[j]
                d = dist(p1, p2)
                adj[i].append((d, j))
                adj[j].append((d, i))
        
        res = 0
        mh = [(0, 0)]
        sn = set()
        while mh:
            d, n = heapq.heappop(mh)
            if n in sn:
                continue

            sn.add(n)
            res += d

            for d, nei in adj[n]:
                heapq.heappush(mh, (d, nei))

        return res