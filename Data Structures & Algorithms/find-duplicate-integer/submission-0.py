class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sn = set()
        for n in nums:
            if n in sn:
                return n
            sn.add(n)
            