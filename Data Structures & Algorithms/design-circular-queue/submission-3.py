class Node():
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = Node()
        self.right = self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        n = Node(value)
        if self.isEmpty():
            self.left.next = n
            self.right = n
        else:
            self.right.next = n
            self.right = n
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        
        self.left.next = self.left.next.next
        if self.left.next is None:
            self.right = self.left
        self.space += 1
        return True

    def Front(self) -> int:
        return self.left.next.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.right.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.left == self.right

    def isFull(self) -> bool:
        return self.space == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()