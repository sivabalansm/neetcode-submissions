class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * (numCourses)
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        if not q:
            return False
        
        while q:
            n = q.popleft()
            for nei in adj[n]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return not any(indegree)
