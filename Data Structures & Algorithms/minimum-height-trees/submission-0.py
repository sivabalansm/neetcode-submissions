class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        mht = float("inf")
        res = []

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        def dfs(node, visit):
            if node in visit:
                return 0
            visit.add(node)
            res = 0
            for nei in adj[node]:
                res = max(res, 1 + dfs(nei, visit))
            
            return res
        
        
        for i in range(n):
            mht_new = dfs(i, set())
            if mht_new < mht:
                res.clear()
                mht = mht_new
                res.append(i)
            elif mht_new == mht:
                res.append(i)
        return res

