class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        freq = defaultdict(int)
        available = [i for i in range(n)]
        used = []
        for s, e in meetings:
            while used and used[0][0] < s:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                freq[room] += 1
                heapq.heappush(used, (e, room))
            else:
                ended, room = heapq.heappop(used)
                freq[room] += 1
                if s < ended:
                    e = ended + (e - s)
                heapq.heappush(used, (e, room))
        return max(freq, key = lambda k : (freq[k], -k))


            

            
