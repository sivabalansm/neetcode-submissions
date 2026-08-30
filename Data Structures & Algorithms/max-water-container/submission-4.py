class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(l, r):
            return min(heights[l], heights[r]) * (r - l)
        
        l = 0
        r = len(heights) - 1
        maxA = 0
        while l < r:
            maxA = max(maxA, area(l, r))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxA