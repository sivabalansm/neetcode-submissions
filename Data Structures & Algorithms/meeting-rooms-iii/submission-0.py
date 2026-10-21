class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        used = []
        count = [0] * n

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room)
            
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1
        
        return count.index(max(count))

"""
        meetings.sort(key = lambda x : x[0])

        res = [0] * n
        mh = []
        count = 0
        for s, e in meetings:
            if len(mh) < n:
                heapq.heappush(mh, (e, s, count))
                res[count] += 1
                count += 1
                continue
            else:
                os, oe, oc = heapq.heappop(mh)
                if oe > s:
                    diff = oe - s
                    s += diff
                    e += diff
                heapq.heappush(mh, (e, s, oc))
                res[oc] += 1
        print(res)
        mres = n - 1
        for i in range(n - 1, -1, -1):
            if res[mres] < res[i]:
                mres = i
        return mres
"""