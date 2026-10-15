class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = {i : set() for i in range(numCourses)}
        indegree = [0] * numCourses
        for pre, crs in prerequisites:
            adj[pre].add(crs)
            indegree[crs] += 1
        
        def dfs(node):
            newVals = set()
            for nei in adj[node]:
                newVals.update(dfs(nei))
            adj[node].update(newVals)
            return adj[node]
        
        for n in adj:
            if indegree[n] == 0:
                dfs(n)
            
        print(adj)
        res = []
        for pre, crs in queries:
            res.append(crs in adj[pre])

        return res

