class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        def bt(i, arr, acc):
            if i >= len(candidates):
                if acc == target:
                    res.add(tuple(arr.copy()))
                return
            if acc > target:
                return


            bt(i + 1, arr, acc)
            arr.append(candidates[i])
            bt(i + 1, arr, acc + candidates[i])
            arr.pop()
        bt(0, [], 0)
        return list(list(e) for e in res)