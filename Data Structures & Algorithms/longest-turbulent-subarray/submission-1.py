class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        res = 1
        lessThen = False
        curr = 1

        for k in range(len(arr) - 1):
            if curr == 1 and arr[k] != arr[k + 1]:
                print(arr[k], arr[k + 1])
                curr += 1
                lessThen = not (arr[k] < arr[k + 1])
            elif lessThen and arr[k] < arr[k + 1]:
                print(arr[k], arr[k + 1])
                curr += 1
                lessThen = False
            elif not lessThen and arr[k] > arr[k + 1]:
                print(arr[k], arr[k + 1])
                curr += 1
                lessThen = True
            elif arr[k] == arr[k + 1]:
                curr = 1
            res = max(res, curr)
        
        return res

