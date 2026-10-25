class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        mval = max(freq.values())
        buck = [[] for _ in range(mval + 1)]

        for num in freq:
            buck[freq[num]].append(num)
        res = []
        for i in range(mval, -1, -1):
            bk = buck[i]
            for num in bk:
                if len(res) == k:
                    break
                res.append(num)
        return res