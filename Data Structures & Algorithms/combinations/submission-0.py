class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def bt(i, arr):
            nonlocal res

            if len(arr) == k:
                res.append(arr.copy())
                return
            
            if i > n:
                return
                
            arr.append(i)
            bt(i + 1, arr)
            arr.pop()
            bt(i + 1, arr)

        bt(1, [])
        return res
