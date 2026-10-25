class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1


        while p3 >= 0:
            n1 = nums1[p1] if p1 >= 0 else float("-inf")
            n2 = nums2[p2] if p2 >= 0 else float("-inf")


            if n1 < n2:
                nums1[p3] = n2
                p2 -= 1
            else:
                nums1[p3] = n1
                p1 -= 1
            p3 -= 1