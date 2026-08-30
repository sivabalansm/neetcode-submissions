class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = len(temperatures) * [0]
        st = []

        for i, t in enumerate(temperatures):
            while st and t > st[-1][0]:
                pTemp, pIdx = st.pop()
                res[pIdx] = i - pIdx
            st.append((t, i))
        return res
        