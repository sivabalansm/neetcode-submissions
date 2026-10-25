class Solution:
    def merge(self, arr, L, M, R):
        # [2, 1]
        #. l,m r
        print(arr[L:R+1])
        left = arr[L:M+1] # [2]
        j = 0
        right = arr[M+1:R+1] # [1]
        k = 0
        i = L

        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1
        
        while j < len(left):
            arr[i] = left[j]
            i += 1
            j += 1

        while k < len(right):
            arr[i] = right[k]
            i += 1
            k += 1




    def mergeSort(self, arr, l, r):
        if l >= r:
            return
        m = (l + r) // 2
        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m + 1, r)
        self.merge(arr, l, m, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums