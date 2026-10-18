class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        adj = defaultdict(list)
        for fro, to, price in flights:
            adj[fro].append((to, price))
        q = deque([(0, src, 0)])
        prices[src] = 0 
        while q:
            price, to, stops = q.popleft()

            if k < stops:
                continue
            
            for new_to, new_price in adj[to]:
                if new_price + price < prices[new_to]:
                    q.append((price + new_price, new_to, stops + 1))
                    prices[new_to] = price + new_price 
            
        return prices[dst] if prices[dst] != float("inf") else -1


