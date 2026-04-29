class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [ [] for _ in range(len(edges ) + 1) ]
        def dfs(n, par):
            if n in visit:
                return False
            visit.add(n)
            for nn in adj[n]:
                if nn == par:
                    continue
                if not dfs(nn, n):
                    return False
            return True
            
            
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = set()
            if not dfs(u, -1):
                return [u, v]
        return []