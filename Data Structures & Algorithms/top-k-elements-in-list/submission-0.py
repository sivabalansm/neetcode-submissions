class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fq = {}
        for i in nums:
            fq[i] = fq.get(i, 0) + 1
        # 1 2 3 4 5 6 7
        # 6 6 6 6 6 6 6
        # counted 6, 7 times
        # so in 7th bucket, drop 6
        # added + 1 so we have that extra bucket 
        buck = [[] for i in range(len(nums) + 1)]

        for num, count in fq.items():
            buck[count].append(num)

        res = []
        for i in range(len(buck) - 1, -1, -1):
            for x in buck[i]:
                res.append(x)
                if len(res) == k:
                    return res
        return res