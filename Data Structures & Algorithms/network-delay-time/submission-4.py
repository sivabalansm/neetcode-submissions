class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        
        mh = [(0, k)]
        visit = set()
        while mh:
            w, no = heapq.heappop(mh)
            visit.add(no)
            if len(visit) == n:
                return w
            for v, t in adj[no]:
                heapq.heappush(mh, (w + t, v))
        return -1

