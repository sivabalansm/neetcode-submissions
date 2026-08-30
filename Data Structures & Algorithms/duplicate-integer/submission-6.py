class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sn = set()

        for n in nums:
            if n in sn:
                return False
            sn.add(n)
        return True