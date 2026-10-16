class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = { i : [] for i in range(1, len(edges) + 1) }
        indegree = [0] * (len(edges) + 1)
        print(adj)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque([i for i, indeg in enumerate(indegree) if i != 0 and indeg == 1])

        while q:
            n = q.popleft()
            indegree[n] -= 1
            for nei in adj[n]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        
        for u, v in reversed(edges):
            if indegree[u] > 0 and indegree[v] > 0:
                return [u, v]
        return []
