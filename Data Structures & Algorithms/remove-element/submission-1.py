class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        n = len(nums)

        while k < len(nums):
            if nums[k] != val:
                k += 1
            else:
                nums.pop(k)
        print(nums)
        return k