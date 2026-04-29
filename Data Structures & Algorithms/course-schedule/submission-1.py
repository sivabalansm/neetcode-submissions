class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crs = { i:[] for i in range(numCourses) }
        for cr, pre in prerequisites:
            crs[cr].append(pre)

        visit = set()
        def dfs(cr):
            if not crs[cr]:
                return True

            if cr in visit:
                return False
            
            visit.add(cr)
            for pre in crs[cr]:
                if not dfs(pre):
                    return False
            
            visit.remove(cr)
            return True
        
        for cr in crs:
            if not dfs(cr):
                return False
        return True