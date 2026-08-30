class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(m):
            for j in range(n):
                n1 = int(num1[i])
                n2 = int(num2[j])
                res[i + j] += n1 * n2
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10
        print(res)
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        print(beg)
        print(res, res[beg:])
        res = map(str, res[beg:])
        return "".join(res)



