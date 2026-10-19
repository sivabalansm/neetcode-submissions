class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        start = 0
        while start + maxJump < len(s) - 1:
            newStart = -1
            for i in range(start + minJump, start + maxJump + 1):
                #print(i)
                if i < len(s) and s[i] != "0":
                    newStart = i
            
            if newStart == -1:
                return False
            start = newStart
        return True