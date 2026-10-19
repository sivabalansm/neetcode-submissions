class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        start = 0
        while start != len(s) - 1:
            newStart = -1
            for i in range(start + minJump, start + maxJump + 1):
                if i < len(s) and s[i] != "1":
                    #print(i, s[i])
                    newStart = i
            #print("newStart", newStart)
            if newStart == -1:
                return False
            start = newStart
        return True if s[len(s) - 1] != "1" else False