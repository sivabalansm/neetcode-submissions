class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for fro, to, price in flights:
            adj[fro].append((to, price))
        
        q = deque([(src, 0, 0)])
        dist = [float('inf')] * n

        while q:
            d, p, s = q.popleft()

            if s > k:
                continue

            for nei, np in adj[d]:
                if p + np < dist[nei]:
                    dist[nei] = p + np
                    q.append((nei, p + np, s + 1))
        return dist[dst] if dist[dst] != float("inf") else -1

        