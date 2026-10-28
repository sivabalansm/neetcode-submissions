class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v):
        # print("parent of", v)
        while self.parents[v] != v:
            v = self.parents[v]
        # print(v)
        return v

    def union(self, u, v):
        pv, pu = self.find(v), self.find(u)
        # print("pu, pv", pu, pv)
        if pu == pv:
            return False

        if self.rank[pv] > self.rank[pu]:
            self.rank[pv] += self.rank[pu]
            self.parents[pu] = pv
        else:
            self.rank[pu] += self.rank[pv]
            self.parents[pv] = pu
        # print(self.parents)
        return True
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        res = []
        N = len(points)
        for i in range(N):
            xi, yi = points[i]
            for j in range(i + 1, N):
                xj, yj = points[j]
                d = dist(xi, yi, xj, yj)
                res.append((d, i, j))
        res.sort()
        dsu = DSU(N)

        total = 0
        for p in res:
            d, i, j = p
            if dsu.union(i, j):
                total += d
        return total
        


