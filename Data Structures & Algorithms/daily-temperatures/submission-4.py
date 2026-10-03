class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):

            while st and st[-1][0] < t:
                ot, j = st.pop()
                res[j] = i - j
            
            st.append((t, i))
        return res
