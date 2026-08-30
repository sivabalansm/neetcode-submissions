from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

            if len(freq) <= 2:
                continue
            
            new_freq = defaultdict(int)
            for key, value in freq.items():
                if value > 1:
                    new_freq[key] = value - 1
            
            freq = new_freq
        
        res = []
        for key in freq:
            if nums.count(key) > len(nums) // 3:
                res.append(key)
        return res
                


