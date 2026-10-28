class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, price in flights:
            adj[s].append((d, price))
        
        mh = [(0, src, -1)]
        visit = set()
        while mh:
            p, n, s = heapq.heappop(mh)

            #print(p, n, s)
            #print(p, n, s)
            #print(mh)
            if n == dst:
                return p

            if s + 1 > k:
                continue
            
            visit.add(n)
            
            for d, np in adj[n]:
                if d not in visit:
                    heapq.heappush(mh, (np + p, d, s + 1))
        return -1

