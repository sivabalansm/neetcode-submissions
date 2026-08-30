class FreqStack:

    def __init__(self):
        self.freq = {}
        self.sts= {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        """
        self.freq[val] = 1 + self.freq.get(val, 0)
        self.st.append(val)
        if not self.maxFreqSt:
            self.maxFreqSt.append(val)
            return
        lastMaxFreq = self.maxFreqSt[-1]
        if self.freq[lastMaxFreq] > self.freq[val]:
            self.maxFreqSt.append(lastMaxFreq)
        elif self.freq[lastMaxFreq] < self.freq[val]:
            self.maxFreqSt.append(val)
        else:
            for i in range(len(self.st) - 2, -1, -1):
                if self.st[i] == lastMaxFreq:
                    self.maxFreqSt.append(lastMaxFreq)
                    break
                elif self.st[i] == val:
                    self.maxFreqSt.append(val)
                    break
        """
        valFreq = 1 + self.freq.get(val, 0)
        self.freq[val] = valFreq
        if valFreq > self.maxFreq:
            self.maxFreq = valFreq
            self.sts[valFreq] = []
        self.sts[valFreq].append(val)
  
    def pop(self) -> int:
        res = self.sts[self.maxFreq].pop()
        self.freq[res] -= 1
        if not self.sts[self.maxFreq]:
            self.maxFreq -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()