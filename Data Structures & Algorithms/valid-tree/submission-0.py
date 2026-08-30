class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
        print(adj)
        visit = set()

        def dfs(n):
            if n in visit:
                return False
                
            print(n)
            visit.add(n)
            for ad in adj[n]:
                if not dfs(ad):
                    return False
            return True
        
        return dfs(edges[0][0])
            
