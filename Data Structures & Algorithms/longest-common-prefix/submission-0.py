class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key=len)
        start = 0
        end = len(smallest)
        for word in strs:
            while smallest[:end] != word[:end]:
                end -= 1
        
        return smallest[:end]