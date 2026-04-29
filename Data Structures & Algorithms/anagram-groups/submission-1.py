from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            fq = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                fq[i] += 1
            
            res[tuple(fq)].append(s)
        
        return list(res.values())
