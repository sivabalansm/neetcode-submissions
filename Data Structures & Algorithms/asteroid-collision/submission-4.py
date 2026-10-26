class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for ast in asteroids:
            if st and ((ast < 0 and st[-1] > 0) or (ast > 0 and st[-1] < 0)):
                prev = st.pop()
                if abs(prev) > abs(ast):
                    st.append(prev)
                elif abs(prev) < abs(ast):
                    st.append(ast)
            else:
                st.append(ast)
        return st
        