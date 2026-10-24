class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key = lambda s : len(s))
        compared = 0

        while compared != len(strs):
            for w in strs:
                if not w.startswith(smallest):
                    smallest = smallest[:-1]
                    compared = 0
                    break
                compared += 1
            
        return smallest



