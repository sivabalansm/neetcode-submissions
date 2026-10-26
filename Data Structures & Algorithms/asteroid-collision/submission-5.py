class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for ast in asteroids:
            st.append(ast)
            while len(st) >= 2 and ((st[-1] < 0 and st[-2] > 0) or (st[-2] > 0 and st[-2] < 0)):
                ast = st.pop()
                prev = st.pop()
                if abs(prev) > abs(ast):
                    st.append(prev)
                elif abs(prev) < abs(ast):
                    st.append(ast)
        return st
        