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
                res[i] += res[i - 1] + 1
            elif pr > cr:
                res[i - 1] = res[i] + 1
        print(res)
        return sum(res) - 1
