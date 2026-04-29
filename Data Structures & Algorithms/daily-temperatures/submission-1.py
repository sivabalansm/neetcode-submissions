class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        for i, t in enumerate(temperatures):
            t = temperatures[i]
            while st and t > st[-1][0]:
                stT, stI = st.pop()
                res[stI] = i - stI
            st.append((t, i))
        return res