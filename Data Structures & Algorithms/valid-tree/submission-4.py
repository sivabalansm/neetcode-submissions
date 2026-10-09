class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(n, par):
            if n in visit:
                return False
            if adj[n] == []:
                return True
            
            visit.add(n)
            for nei in adj[n]:
                if nei == par:
                    continue
                if not dfs(nei, n):
                    return False
            adj[n] = []
            visit.remove(n)
            return True

        for n in adj:
            if not dfs(n, -1):
                return False
        return True