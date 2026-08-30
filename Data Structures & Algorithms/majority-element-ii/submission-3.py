
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

            if len(freq) <= 2:
                continue
            print(freq)
            new_freq = {}
            for key in freq:
                if freq[key] > 1:
                    new_freq[key] = freq[key] - 1
            print(new_freq)
            freq = new_freq
        
        res = []
        for key in freq:
            print(nums.count(key), len(nums) // 3)
            if nums.count(key) > len(nums) // 3:
                res.append(key)
        
        return res
