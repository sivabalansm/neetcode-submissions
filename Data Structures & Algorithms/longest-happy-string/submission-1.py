class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        mh = [(cnt, c) for cnt, c in [(a, 'a'), (b, 'b'), (c, 'c')] if cnt > 0]
        res = []
        heapq.heapify_max(mh)
        print(mh)
        prev = None
        while mh:
            cnt, c = heapq.heappop_max(mh)
            if len(res) > 1 and res[-1] == res[-2] == c:
                if not mh:
                    break
                cnt2, c2 = heapq.heappop_max(mh)
                res.append(c2)
                cnt2 -= 1
                if cnt2 > 0:
                    heapq.heappush_max(mh, (cnt2, c2))
                heapq.heappush_max(mh, (cnt, c))
            else:
                res.append(c)
                cnt -= 1
                if cnt > 0:
                    heapq.heappush_max(mh, (cnt, c))
        return "".join(res) 

