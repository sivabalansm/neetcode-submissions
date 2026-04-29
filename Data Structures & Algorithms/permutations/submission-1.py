class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def bt(perm, nums, pick):
            if len(perm) == len(nums):
                self.res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    bt(perm, nums, pick)
                    perm.pop()
                    pick[i] = False
        bt([], nums, [False] * len(nums))
        return self.res

