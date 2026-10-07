class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def bt(curr, pos):
            nonlocal res
            if pos == len(nums):
                res.append(curr.copy())
                return

            n = nums[pos]
            curr.append(n)
            bt(curr, pos + 1)
            curr.pop()

            while pos + 1 < len(nums) and nums[pos] == nums[pos + 1]:
                pos += 1
            bt(curr, pos + 1)

        bt([], 0)
        return res