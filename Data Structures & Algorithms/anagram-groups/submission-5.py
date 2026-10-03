from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag = defaultdict(list)

        for s in strs:
            ana = [0] * 26
            for c in s:
                ana[ord(c) - ord('a')] += 1
            
            ag[tuple(ana)].append(s)
        
        return list(ag.values())
