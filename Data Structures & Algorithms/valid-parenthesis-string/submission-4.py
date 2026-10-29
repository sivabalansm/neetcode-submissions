"""
((**)

leftMin = 0 - 1 = -1 -> 0
leftMax = 4 - 1 = 3 -> 3

(((*)
leftMin = 1
leftMax = 4
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax = 0
        leftMin = 0
        for p in s:
            if p == "(":
                leftMin += 1
                leftMax += 1
            elif p == ")":
                leftMin -= 1
                leftMax -= 1
            elif p == "*":
                leftMin -= 1
                leftMax += 1
            
            if leftMin < 0:
                leftMin = 0
            
            if leftMax < 0:
                return False
        
        return leftMin == 0 
