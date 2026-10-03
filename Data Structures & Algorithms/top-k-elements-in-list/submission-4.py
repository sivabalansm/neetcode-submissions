from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        buckets_by_freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq[num] += 1
        for num, cnt in freq.items():
            buckets_by_freq[cnt].append(num)
        
        res = []
        for i in range(len(buckets_by_freq) - 1, 0, -1):
            for num in buckets_by_freq[i]:
                res.append(num)
                if len(res) == k:
                    return res