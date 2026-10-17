class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for fro, to, price in flights:
            adj[fro].append((to, price))
        mh = []
        for to, price in adj[src]:
            heapq.heappush(mh, (price, to))
        
        k += 1
        while mh:
            price, to = heapq.heappop(mh)

            k -= 1
            if to == dst:
                return price

            if k == 0:
                continue
            
            for new_to, new_price in adj[to]:
                heapq.heappush(mh, (price + new_price, new_to))

            
        return -1


