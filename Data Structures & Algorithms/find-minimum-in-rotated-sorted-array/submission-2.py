
class Solution:
    def binary_search(self, arr, target):
        b = 0
        e = len(arr) - 1

        while b <= e:
            mid = (b + e) // 2
            if arr[mid] == target:
                return True
            if arr[mid] < target:
                b = mid + 1
            else:
                e = mid - 1
        return False




    def findMin(self, nums: List[int]) -> int:

        start, end = 0, len(nums) - 1
        smol = nums[start]
        
        
        while start <= end:
            if nums[start] < nums[end]:
                smol = min(smol, nums[start])
                break

            mid = (start + end) // 2
            smol = min(smol, nums[mid])

            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        return smol
