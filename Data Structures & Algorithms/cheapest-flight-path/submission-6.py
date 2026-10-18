class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for fro, to, price in flights:
            adj[fro].append((to, price))
        mh = [(0, src, 0)]

        while mh:
            price, to, stops = heapq.heappop(mh)

            if to == dst:
                return price

            if k < stops:
                continue
            
            for new_to, new_price in adj[to]:
                heapq.heappush(mh, (price + new_price, new_to, stops + 1))

            
        return -1


