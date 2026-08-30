class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small = min(strs, key=len)
        end = len(small)
        for word in strs:
            while word[:end] != small[:end]:
                end -= 1
        
        return small[:end]