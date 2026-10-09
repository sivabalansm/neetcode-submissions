class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        c -> prepreq
        0 -> 1, ...
        1 -> 0
        """
        adj = {i : [] for i in range(numCourses)}
        for c, p in prerequisites:
            adj[c].append(p)
        
        visit = set()
        def dfs(c):
            if c in visit:
                return False
            
            if adj[c] == []:
                return True

            visit.add(c)
            for pre in adj[c]:
                if not dfs(pre):
                    return False
            visit.remove(c)
            adj[c] = []
            return True
        

        for c in adj:
            if not dfs(c):
                return False
        return True
        
