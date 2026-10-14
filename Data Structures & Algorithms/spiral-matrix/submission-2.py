class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        rt = len(matrix[0])
        ct = len(matrix)
        r, c = 0, 0
        while rt > 0 and ct > 0:
            # move right
            for i in range(rt):
                res.append(matrix[r][c])
                c += 1
            c -= 1
            ct -= 1
            r += 1
            if ct <= 0:
                break

            # move down
            for i in range(ct):
                res.append(matrix[r][c])
                r += 1
            r -= 1
            rt -= 1
            c -= 1

            if rt <= 0:
                break
            # move left
            for i in range(rt):
                res.append(matrix[r][c])
                c -= 1
            c += 1
            ct -= 1
            r -= 1

            if ct <= 0:
                break
            # move up
            for i in range(ct):
                res.append(matrix[r][c])
                r -= 1
            r += 1
            rt -= 1
            c += 1
            if rt <= 0:
                break
        return res
            