class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        m = len(s)

        
        i, j = 0, 0

        maxSub = 0
        while j < m:
             if i != j:
                 if s[j] not in c:
                     c.add(s[j])
                     j += 1
                 else:
                     maxSub = max(len(c), maxSub)
                     c.remove(s[i])
                     i += 1
             else:
                 c.clear()
                 c.add(s[i])
                 j += 1
        return max(maxSub, len(c))