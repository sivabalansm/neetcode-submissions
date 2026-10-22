class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        mh = [(cnt, c) for cnt, c in [(a, 'a'), (b, 'b'), (c, 'c')] if cnt > 0]
        res = []
        heapq.heapify_max(mh)
        print(mh)
        prev = None
        while mh:
            cnt, c = heapq.heappop_max(mh)
            if cnt >= 2:
                cnt -= 2
                res.append(c * 2)
            else:
                cnt -= 1
                res.append(c)
            
            if prev:
                heapq.heappush_max(mh, prev)
                prev = None
            
            if cnt != 0:
                prev = (cnt, c)
        return "".join(res) 

