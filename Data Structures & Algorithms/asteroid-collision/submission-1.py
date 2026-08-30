class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for a in asteroids:
            if st and st[-1] > 0 and a < 0:
                co = st.pop()
                if abs(co) > abs(a):
                    st.append(co)
                elif abs(co) < abs(a):
                    st.append(a)
            else:
                st.append(a)
        return st