class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while st and st[-1][0] < temp:
                small_temp, prev_i = st.pop()
                res[prev_i] = i - prev_i
            st.append((temp, i))
        return res
