class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        c = list(zip(position, speed))
        c.sort()
        c.reverse()
        
        res = 0
        st = []
        for p, s in c:
            e = (target - p) / s
            st.append(e)
            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()
        return len(st)

        