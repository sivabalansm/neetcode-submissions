class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        freq = defaultdict(int)
        available = [i for i in range(n)]
        used = []
        for s, e in meetings:
            if available:
                room = heapq.heappop(available)
                heapq.heappush(used, (e, room))
                continue
            
            if used:
                ended, room = heapq.heappop(used)
                freq[room] += 1
                if s < ended:
                    e = ended + (e - s)
                heapq.heappush(used, (e, room))
        return max(freq, key = lambda k : (freq[k], -k))


            

            
