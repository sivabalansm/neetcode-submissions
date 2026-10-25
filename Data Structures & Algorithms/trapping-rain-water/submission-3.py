class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        lmax = height[l]
        rmax = height[r]
        res = 0

        while l < r:
            lh = height[l]
            rh = height[r]

            lmax = max(lmax, lh)
            rmax = max(rmax, rh)

            if lmax < rmax:
                res += lmax - lh
                l += 1
            else:
                res += rmax - rh
                r -= 1
        return res
