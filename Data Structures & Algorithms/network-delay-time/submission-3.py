class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        mh = [(0, k)]
        visit = set()
        time = 0

        while mh:
            w1, n1 = heapq.heappop(mh)
            if n1 in visit:
                continue
            visit.add(n1)
            
            time = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(mh, (w1 + w2, n2))
        return time if n == len(visit) else -1