class Solution:
    def candy(self, ratings: List[int]) -> int:
        r = len(ratings)
        if r == 1:
            return 1
        res = [1] * r

        for i in range(1, r):
            pr = ratings[i - 1]
            cr = ratings[i]
            if pr < cr:
                res[i] = res[i - 1] + 1
        print(res)
        for i in range(r - 2, -1, -1):
            pr = ratings[i + 1]
            cr = ratings[i]
            if cr > pr:
                res[i] = max(res[i + 1] + 1, res[i])
        print(res)
        return sum(res)
