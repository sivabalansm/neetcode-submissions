class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        
        mh = [(0, k)]
        visit = set()
        res = 0
        while mh:
            w, no = heapq.heappop(mh)
            visit.add(no)
            res = w

            for v, t in adj[no]:
                if v not in visit:
                    heapq.heappush(mh, (w + t, v))
        return res if n == len(visit) else -1

