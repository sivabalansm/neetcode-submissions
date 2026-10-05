class Node:
    def __init__(self):
        self.value = 0
        self.key = 0
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self._attach_front(self.tail)

    def _remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        node.prev = None
        node.next = None
    
    def _attach_front(self, node):
        prev = self.head.prev 
        self.head.prev = node

        node.next = self.head
        node.prev = prev

        if prev:
            prev.next = node
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._attach_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.get(key)
            return
            
        if len(self.cache) == self.capacity:
            evict_node = self.tail.next
            self._remove(evict_node)
            del self.cache[evict_node.key]
        
        node = Node()
        node.key = key
        node.value = value
        self._attach_front(node)

        self.cache[key] = node

