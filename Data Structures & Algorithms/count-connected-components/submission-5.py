class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        visit = set()
        res = 0
        adj = { i : [] for i in range(n) }
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        for n in adj:
            if n not in visit:
                dfs(n)
                res += 1
        return res
        # TC: V + E SC : V + E