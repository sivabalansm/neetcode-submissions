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
            if n1 & n2 or n1 & carry or n2 & carry:
                carry = 1
            else:
                carry = 0
            
            if s:
                res = res | offset
            offset = offset << 1
        return res