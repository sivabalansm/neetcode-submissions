class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crs = { i:[] for i in range(numCourses) }
        for cr, pre in prerequisites:
            crs[cr].append(pre)
        
        res = []
        visit = set()
        cycle = set()
        def dfs(cr):
            if cr in cycle:
                return False

            if cr in visit:
                return True

            cycle.add(cr)
            for pre in crs[cr]:
                if not dfs(pre):
                    return False
            cycle.remove(cr)
            visit.add(cr)
            res.append(cr)
            return True
        
        for cr in range(numCourses):
            if not dfs(cr):
                return []
        return res
