class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        res = 0
        lessThen = -1
        curr = 0

        for k in range(len(arr) - 1):
            if arr[k] > arr[k + 1]:
                curr = curr + 1 if lessThen == 0 else 1
                lessThen = 1
            elif arr[k] < arr[k + 1]:
                curr = curr + 1 if lessThen == 1 else 1
                lessThen = 0
            else:
                curr = 0
                lessThen = -1
            res = max(res, curr)
        
        return res + 1

