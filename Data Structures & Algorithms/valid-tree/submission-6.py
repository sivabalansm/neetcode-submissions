class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(n, prev):
            if n in visit:
                return False 
            visit.add(n)
            for nei in adj[n]:
                if nei == prev:
                    continue
                if not dfs(nei, n):
                    return False
            
            return True
        
        return dfs(0, -1)


