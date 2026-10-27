
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = nums[slow]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[slow]]
        return slow
        slow = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return nums[slow]