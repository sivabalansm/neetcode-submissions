class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        q = deque()
        indegree = [0] * n
        for n in adj:
            nei = adj[n]
            indegree[n] = len(nei)
            if len(nei) == 1:
                q.append(n)
        print(q)
        print(adj)
        while q:
            if len(q) <= 2:
                return list(q)
                
            for _ in range(len(q)):
                n = q.popleft()
                indegree[n] -= 1
                for nei in adj[n]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)

        


