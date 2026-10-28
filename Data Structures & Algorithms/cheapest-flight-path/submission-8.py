class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, price in flights:
            adj[s].append((d, price))
        
        mh = [(0, src, -1)]

        while mh:
            p, n, s = heapq.heappop(mh)

            print(p, n, s)
            print(mh)
            if n == dst:
                return p

            if s + 1 > k:
                continue
            
            
            for d, np in adj[n]:
                heapq.heappush(mh, (np + p, d, s + 1))
        

