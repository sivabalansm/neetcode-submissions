class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def bt(curr, acc, pos):
            nonlocal res 
            if acc == target:
                res.append(curr.copy())
                return
            if pos >= len(candidates) or acc > target:
                return
            
            n = candidates[pos]
            curr.append(n)
            bt(curr, acc + n, pos + 1)
            curr.pop()
            while pos + 1 < len(candidates) and candidates[pos] == candidates[pos + 1]:
                pos += 1
            bt(curr, acc, pos + 1)

        bt([], 0, 0)
        return res

