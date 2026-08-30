class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kMax = max(piles)

        l = 1
        r = kMax
        print(r)
        res = kMax
        while l <= r:
            m = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / m)
            
            if time >= h:
                l = m + 1
            else:
                res = min(m, res)
                r = m - 1
        return res
            