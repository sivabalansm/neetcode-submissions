class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            fq = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                fq[i] += 1
            
            res[tuple(fq)] = res.get(tuple(fq), [])
            res[tuple(fq)].append(s)
        
        return list(res.values())
