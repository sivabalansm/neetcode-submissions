class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        #print(pair)
        st = []
        for p, s in pair:
            time = (target - p) / s
            st.append(time)
            while len(st) >= 2 and st[-2] >= st[-1]:
                st.pop()
        return len(st)