class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crs = { i:[] for i in range(numCourses) }
        for cr, pr in prerequisites:
            crs[cr].append(pr)
        
        res = []
        visit, cycle = set(), set()

        def dfs(cr):
            if cr in cycle:
                return False
            if cr in visit:
                return True
            
            cycle.add(cr)
            for pr in crs[cr]:
                if not dfs(pr):
                    return False

            cycle.remove(cr)
            visit.add(cr)
            res.append(cr)
            return True
        for cr in range(numCourses):
            if not dfs(cr):
                return []
        return res


        