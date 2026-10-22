"""
axyy
a x y y
0 23 24 24

2 y, a, x
y a y x
abcdffff
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        res = []
        mh = [[cnt, c] for c, cnt in freq.items()]
        heapq.heapify_max(mh)
        prev = None
        while mh:
            cnt, c = heapq.heappop(mh)
            
            res.append(c)
            cnt -= 1

            if prev:
                heapq.heappush_max(mh, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, c]
        
        return "".join(res) if len(res) == len(s) else ""