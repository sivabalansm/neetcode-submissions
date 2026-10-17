class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float("inf")] * n
        visit = [False] * n
        res = 0
        node = 0
        edges = 0
        nextNode = -1
        while edges < n - 1:
            visit[node] = True
            x, y = points[node]
            for i in range(n):
                if visit[i]:
                    continue
                px, py = points[i]
                curDist = abs(x - px) + abs(y - py)
                dist[i] = min(dist[i], curDist)
                #print(node, dist[i])
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            edges += 1
            res += dist[nextNode]
            node = nextNode
        return res
