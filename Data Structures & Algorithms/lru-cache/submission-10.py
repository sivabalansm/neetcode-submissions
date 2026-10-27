class DListNode:
    def __init__(self, val = 0):
        self.key = -1
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = DListNode()
        self.right = DListNode()
        self.right.prev = self.left
        self.left.next = self.right
    
    def insert(self, node):
        prevNode = self.right.prev
        self.right.prev = None
        prevNode.next = None

        self.right.prev = node
        prevNode.next = node
        node.prev = prevNode
        node.next = self.right
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # detach
            leftNode = node.prev
            rightNode = node.next

            leftNode.next = rightNode
            rightNode.prev = leftNode

            self.insert(node)

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.get(key)
            node = self.cache[key]
            node.val = value
            return
        
        print(len(self.cache), self.capacity)
        if len(self.cache) == self.capacity:
            en = self.left.next
            prev = en.prev
            next = en.next
            prev.next = next
            next.prev = prev

            del self.cache[en.key]
            en.next = None
            en.prev = None
        
        node = DListNode(value)
        node.key = key
        self.cache[key] = node
        self.insert(node)


        
