class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [100000000] * n
        visit = [False] * n

        edges, res = 0, 0
        node = 0

        while edges < n - 1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if visit[i]:
                    continue
                curDist = (abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i
            
            edges += 1
            node = nextNode
            res += dist[nextNode]
        return res