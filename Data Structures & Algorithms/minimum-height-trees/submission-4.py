class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        q = deque()
        indegree = [0] * n
        for no in adj:
            nei = adj[no]
            indegree[no] = len(nei)
            if len(nei) == 1:
                q.append(no)
        print(q)
        print(adj)
        while q:
            if n <= 2:
                return list(q)
                
            for _ in range(len(q)):
                l = q.popleft()
                n -= 1
                indegree[l] -= 1
                for nei in adj[l]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)

        


