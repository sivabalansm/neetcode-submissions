class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 0
        jumps = 1
        while nums[i] + i < len(nums) - 1:
            next_i = i + 1
            for j in range(1, nums[i] + 1):
                if next_i + nums[next_i] <= i + j + nums[i + j]:
                    next_i = i + j
            i = next_i
            jumps += 1
        return jumps
        
