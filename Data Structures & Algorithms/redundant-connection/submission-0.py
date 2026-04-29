class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [ [] for _ in range(n+1) ]

        def dfs(node, par):
            if visit[node]:
                return True
            
            visit[node] = True

            for nn in adj[node]:
                if nn == par:
                    continue
                if dfs(nn, node):
                    return True
            return False
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

            visit = [False] * (n + 1)
            if dfs(u, -1):
                return [u, v]
        return []
        
