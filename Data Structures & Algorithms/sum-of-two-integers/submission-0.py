class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        offset = 1
        carry = 0
        for i in range(32):
            n1 = a & offset
            n2 = b & offset
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