class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(n, part):
            if n in visit:
                return False
            
            visit.add(n)
            for nn in adj[n]:
                if nn == part:
                    continue
                if not dfs(nn, n):
                    return False
            
            return True
        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                res += 1
        return res

