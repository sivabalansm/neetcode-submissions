class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)

        l = max(weights)
        r = total
        res = r

        while l <= r:
            m = (l + r) // 2
            print("rate", m)
            dc = 1
            curr = 0
            for w in weights:
                if curr + w > m:
                    curr = 0
                    dc += 1
                curr += w
            print("days", dc)
            if dc <= days:
                r = m - 1
                res = m
            else: # dc > days
                l = m + 1
        return res