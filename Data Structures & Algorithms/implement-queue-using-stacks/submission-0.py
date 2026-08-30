class MyQueue:

    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        self.stC = []
        for i in range(len(self.st)):
            self.stC.append(self.st.pop())
        res = self.stC.pop()
        for i in range(len(self.stC)):
            self.st.append(self.stC.pop())
        return res

    def peek(self) -> int:
        return self.st[0]

    def empty(self) -> bool:
        return len(self.st) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()