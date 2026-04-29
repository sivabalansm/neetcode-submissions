class Solution:
    def count_str(self, s):
        count_s = {}
        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        return count_s
    def checkInclusion(self, s1: str, s2: str) -> bool:
      # populate frequency
      count_s1 = self.count_str(s1)
      count_win = {}
 
      l = 0
      for r in range(len(s2)):
        count_win[s2[r]] = count_win.get(s2[r], 0) + 1
        while r - l + 1 > len(s1):
            count_win[s2[l]] -= 1
            if count_win[s2[l]] == 0:
                del count_win[s2[l]]
            l += 1
            

        if count_win == count_s1:
            return True
      return False

        






        

