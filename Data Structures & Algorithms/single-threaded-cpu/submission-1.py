class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key = lambda x : (x[0]))
        mh = []
        res = []

        time = tasks[0][0]
        i = 0
        while mh or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(mh, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not mh:
                time = tasks[i][0]
            else:
                proc, idx = heapq.heappop(mh)
                time += proc
                res.append(idx)
        return res

        
