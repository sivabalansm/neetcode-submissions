class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        c = 0
        for i in range(32):
            da = a & 1
            db = b & 1
            #print(da, db)
            """
            100
            111
            """

            if da & 1 and db & 1 or da & 1 and c & 1 or db & 1 and c & 1:
                res |= (da ^ db ^ c) << i
                c = 1
            else:
                res |= (da ^ db ^ c) << i
                c = 0
            a = a >> 1
            b = b >> 1
        return res
