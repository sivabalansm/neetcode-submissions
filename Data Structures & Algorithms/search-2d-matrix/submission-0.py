class Solution:
    def bs(self, arr, target):
        l = 0
        r = len(arr) - 1

        print(arr)
        print(target)
        while l <= r:
            mid = (r + l) // 2
            print(arr[mid])

            if arr[mid] == target:
                return True

            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
  
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            print(matrix[mid])

            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                return self.bs(matrix[mid], target)
            
            if matrix[mid][-1] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        