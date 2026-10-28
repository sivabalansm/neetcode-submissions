class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))
        
        mh = [(0, k)]
        sn = set()
        res = 0
        while mh:
            time, no = heapq.heappop(mh)

            if no in sn:
                continue
            
            res = time
            sn.add(no)

            for v, t in adj[no]:
                heapq.heappush(mh, (time + t, v))
        print(n)
        return res if len(sn) == n else -1
