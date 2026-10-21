class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        t = sum(nums)
        if t % k != 0:
            return False

        size = t // k
        subs = [0] * k
        nums.sort(reverse=True)
        print(nums)
        def bt(i):
            if i == len(nums):
                return True
            print(subs)
            for j in range(k):
                if subs[j] + nums[i] <= size:
                    subs[j] += nums[i]
                    if bt(i + 1):
                        return True
                    subs[j] -= nums[i]
                
                if subs[j] == 0:
                    break
            return False
        
        return bt(0)