class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def bt(curr, pos):
            if pos >= len(nums):
                self.res.append(curr.copy())
                return

            curr.append(nums[pos])
            bt(curr, pos + 1)
            curr.pop()
            bt(curr, pos + 1)
        
        bt([], 0)
        return self.res
