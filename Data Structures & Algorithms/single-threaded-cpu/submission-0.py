class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort(key=lambda t: t[0])

        res = []
        mh = []
        time = tasks[0][0]
        i = 0

        while mh or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(mh, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not mh:
                time = tasks[i][0]
            else:
                proc, idx = heapq.heappop(mh)
                time += proc
                res.append(idx)
        
        return res
            