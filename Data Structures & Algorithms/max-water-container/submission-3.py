class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        def area(l, r):
            return min(heights[l], heights[r]) * (r - l)
        
        maxA = 0
        while l < r:
            maxA = max(maxA, area(l, r))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxA
