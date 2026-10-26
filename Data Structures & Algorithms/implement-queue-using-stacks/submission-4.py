class MyQueue:

    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        tmp = []
        for _ in range(len(self.st) - 1):
            tmp.append(self.st.pop())
        front = self.st.pop()
        for _ in range(len(tmp)):
            self.st.append(tmp.pop())
        return front

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