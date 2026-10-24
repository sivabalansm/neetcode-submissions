class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashMap:

    def __init__(self):
        self.set = [Node((-1, -1)) for _ in range(1000)]
    
    def hash(self, key : int):
        return key % len(self.set)

    def put(self, key: int, value: int) -> None:
        curr = self.set[self.hash(key)]
        while curr.next:
            if curr.next.val[0] == key:
                curr.next.val = (key, value)
                return
            curr = curr.next
        curr.next = Node((key, value))

    def get(self, key: int) -> int:
        curr = self.set[self.hash(key)]
        while curr.next:
            if curr.next.val[0] == key:
                return curr.next.val[1]
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.set[self.hash(key)]
        while curr.next:
            if curr.next.val[0] == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)