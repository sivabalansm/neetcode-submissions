class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        pa = len(a) - 1
        pb = len(b) - 1
        c = 0
        while pa >= 0 or pb >= 0 or c:
            s = 0
            if pa >= 0:
                s += int(a[pa])
                pa -= 1
            
            if pb >= 0:
                s += int(b[pb])
                pb -= 1
            
            s += c

            if s == 1:
                res.append("1")
                c = 0
            elif s == 2:
                res.append("0")
                c = 1
            elif s == 3:
                res.append("1")
                c = 1
            elif s == 0:
                res.append("0")
                c = 0

            
        return "".join(res[::-1])
                

