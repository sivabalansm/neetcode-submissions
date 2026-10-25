class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        res = 0

        while l < r:
            h1, h2 = heights[l], heights[r]
            a = min(h1, h2) * (r - l)
            res = max(res, a)
            if h1 > h2:
                r -= 1
            else:
                l += 1
        return res