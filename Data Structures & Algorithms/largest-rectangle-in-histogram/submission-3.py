class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        st = []

        for i, h in enumerate(heights):
            curr_i = i
            while st and st[-1][1] > h:
                pi, ph = st.pop()
                res = max(res, (i - pi) * ph)
                curr_i = pi
            st.append((curr_i, h))
        print(res)
        for i, h in st:
            res = max(res, h * (len(heights) - i))
        return res

