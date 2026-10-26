"""
5 7 5 4
"""

class FreqStack:
    def __init__(self):
        self.freq = {}
        self.maxFreq = 0
        self.st = {}

    def push(self, val: int) -> None:
        valf = 1 + self.freq.get(val, 0)
        self.freq[val] = valf
        if valf > self.maxFreq:
            self.maxFreq = valf
            self.st[valf] = []
        self.st[valf].append(val)
        
    def pop(self) -> int:
        val = self.st[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.st[self.maxFreq]:
            self.maxFreq -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()