class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sn = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                sn[nums[l]] -= 1
                if sn[nums[l]] <= 0:
                    del sn[nums[l]]
                l += 1
            if nums[r] in sn:
                return True
            sn[nums[r]] += 1
        return False
            
            
