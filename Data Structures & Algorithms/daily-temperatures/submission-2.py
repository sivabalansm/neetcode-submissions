class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []

        for i, t in enumerate(temperatures):
            t = temperatures[i]
            while st and t > st[-1][0]:
                prevTemp, prevIdx = st.pop()
                res[prevIdx] = i - prevIdx
            st.append((t, i))
        return res
