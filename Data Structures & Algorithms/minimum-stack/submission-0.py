class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []

    def push(self, val: int) -> None:
        if self.prefix:
            self.prefix.append(min(val, self.prefix[-1]))
        else:
            self.prefix.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.prefix.pop() 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
        
