class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))
        prices[src] = 0
        q = deque([(0, src, 0)])
        while q:
            cst, src, stops = q.popleft()
            if stops > k:
                continue

            for nei, w in adj[src]:
                if cst + w < prices[nei]:
                    q.append((cst + w, nei, stops + 1))
                    prices[nei] = cst + w

        return prices[dst] if prices[dst] != float("inf") else -1