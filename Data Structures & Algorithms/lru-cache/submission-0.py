class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = 2
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def bind(self, before_node, after_node):
        before_node.next = after_node
        after_node.prev = before_node

    def insert(self, node):
        after_node = self.left.next
        self.bind(self.left, node)
        self.bind(node, after_node)
    
    def remove_node(self, node) -> Node:
        before_node = node.prev
        after_node = node.next
        self.bind(before_node, after_node)
        return node

    def remove_last(self) -> Node:
        return self.remove_node(self.right.prev) 
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            # have to move it as well to the front
            self.remove_node(node)
            self.insert(node)
            return
        
        if len(self.cache) + 1 > self.capacity:
            # eviction
            evicted_node = self.remove_last()
            # do deletion in cache
            del self.cache[evicted_node.key]

        new_node = Node(key, value)
        self.insert(new_node) 
        self.cache[key] = new_node



        
