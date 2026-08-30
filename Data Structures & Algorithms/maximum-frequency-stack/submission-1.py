from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.maxCnt = 0
        self.sts = {}

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        cnt = self.cnt[val]
        if cnt > self.maxCnt:
            self.maxCnt = cnt
            self.sts[cnt] = []
        self.sts[cnt].append(val)

    def pop(self) -> int:
        res = self.sts[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.sts[self.maxCnt]:
            self.maxCnt -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()