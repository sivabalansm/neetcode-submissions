class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        for i, num in enumerate(temperatures):
            if not st or num < st[-1][1]:
                st.append((i, num))
            else:
                while st and num > st[-1][1]:
                    smi, sm = st.pop()
                    res[smi] = i - smi 
                st.append((i, num))
        return res