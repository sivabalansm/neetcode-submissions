class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(Nums)

        def drob(l, r):
            one = nums[l]
            two = max(nums[l], nums[l + 1])

            for i in range(l + 2, r):
                tmp = two
                two = max(two, nums[i] + one)
                one = tmp
            return two
        print(drob(0, len(nums)))
        return max(drob(0, len(nums) - 1), drob(1, len(nums)))
