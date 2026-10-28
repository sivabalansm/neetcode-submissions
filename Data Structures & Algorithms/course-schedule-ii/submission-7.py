class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            pre = q.popleft()
            res.append(pre)
            for crs in adj[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
        return res