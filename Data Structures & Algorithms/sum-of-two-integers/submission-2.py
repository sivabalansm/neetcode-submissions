class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        offset = 1
        carry = 0
        for i in range(32):
            n1 = 1 if a & offset  else 0
            n2 = 1 if b & offset else 0
            print(n1)
            print(n2)
            print(bin(res))


            s = n1 ^ n2 ^ carry
            carry = (n1 & n2) | (n1 & carry) | (n2 & carry)
        
            if s:
                res = res | offset
            offset = offset << 1
        return res