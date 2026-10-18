class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(condi):
            order = []
            indegree = [0] * (k + 1)
            adj = defaultdict(set)

            for u, v in condi:
                if v not in adj[u]:
                    adj[u].add(v)
                    indegree[v] += 1
            
            q = deque()
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    q.append(i)
            
            while q:
                n = q.popleft()
                order.append(n)
                for nei in adj[n]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            return order
        
        row_order = topo_sort(rowConditions)
        if len(row_order) != k:
            return []

        col_order = topo_sort(colConditions)
        if len(col_order) != k:
            return []

        colIdx = [0] * (k + 1)
        for i in range(k):
            colIdx[col_order[i]] = i
        
        res = [[0] * k for _ in range(k)]

        for r in range(k):
            num = row_order[r]
            c = colIdx[num]
            res[r][c] = num
        return res
