class MyQueue:

    def __init__(self):
        self.push_st = []
        self.pop_st = []

    def push(self, x: int) -> None:
        self.push_st.append(x)

    def pop(self) -> int:
        if not self.pop_st:
            while self.push_st:
                self.pop_st.append(self.push_st.pop())
        return self.pop_st.pop()

    def peek(self) -> int:
        if not self.pop_st:
            while self.push_st:
                self.pop_st.append(self.push_st.pop())
        return self.pop_st[-1]

    def empty(self) -> bool:
        return len(self.pop_st) == len(self.push_st) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()