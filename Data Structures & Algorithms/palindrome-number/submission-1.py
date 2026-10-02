class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        flipped = 0
        curr = x
        while curr > 0:
            flipped *= 10
            flipped += curr % 10
            curr //= 10
        print(flipped)
        while flipped > 0 and x > 0:
            if flipped % 10 != x % 10:
                return False
            
            flipped //= 10
            x //= 10
        return True