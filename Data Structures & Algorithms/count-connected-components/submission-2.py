class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [ [] for _ in range(n) ]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(n):
            if n in visit:
                return
            visit.add(n)
            for nn in adj[n]:
                dfs(nn)

        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res