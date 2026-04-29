class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)

        visit = set()
        def dfs(n):
            if n in visit:
                return
            
            visit.add(n)
            for nn in adj[n]:
                if nn not in visit:
                    dfs(nn)
            
        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res

