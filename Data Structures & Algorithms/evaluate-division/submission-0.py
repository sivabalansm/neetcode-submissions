class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, eq in enumerate(equations):
            v = values[i]
            A, B = eq
            adj[A].append((B, v))
            adj[B].append((A, 1/v))
        
        def bfs(src, targ):
            if src not in adj or targ not in adj:
                return -1
            
            q = deque([(src, 1)])
            visit = set()
            while q:
                n, w = q.popleft()
                visit.add(n)
                if n == targ:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append((nei, w * weight))

            return -1
        
        return [bfs(a, b) for a, b in queries]