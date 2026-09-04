"""
class Node:
    def __init__(self, value : int = 0):
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev

            nxt = self.head.next
            node.next = nxt
            node.prev = self.head
            nxt.prev = node
            self.head.next = node

            return node.value
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev

            nxt = self.head.next
            node.next = nxt
            node.prev = self.head
            nxt.prev = node
            self.head.next = node
            return
        
        if len(self.cache) > self.capacity:
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        


        
