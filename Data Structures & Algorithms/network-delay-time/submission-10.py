class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))
        
        mh = [(0, k)]
        sn = set()
        res = 0
        while mh:
            time, n = heapq.heappop(mh)

            if n in sn:
                continue
            
            res = time
            sn.add(n)

            for v, t in adj[n]:
                heapq.heappush(mh, (time + t, v))
        return res if len(sn) == n else -1
