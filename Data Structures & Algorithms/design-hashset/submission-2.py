class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyHashSet:
    def __init__(self):
        self.nodes = [ListNode(0) for _ in range(10000)]

    def add(self, key: int) -> None:
        cur = self.nodes[key % len(self.nodes)]
        while cur.next:
            if cur.next.data == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.nodes[key % len(self.nodes)]
        while cur.next:
            if cur.next.data == key:
                cur.next = cur.next.next

    def contains(self, key: int) -> bool:
        cur = self.nodes[key % len(self.nodes)]
        while cur.next:
            if cur.next.data == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)