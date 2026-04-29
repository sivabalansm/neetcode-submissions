class DLinkedList:
    def __init__(self, val = 0, key = 0, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev



class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.data = {}
        self.head = DLinkedList(0)
        self.tail = DLinkedList(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        node.prev = None
        node.next = None

        prevNode.next = nextNode
        nextNode.prev = prevNode
        return node

    def appendNode(self, node):
        nextNode = self.head.next
        self.head.next = node
        node.prev = self.head

        node.next = nextNode
        nextNode.prev = node



    def get(self, key: int) -> int:
        if key in self.data:
            node = self.data[key]
            self.removeNode(node)
            self.appendNode(node)
            return self.data[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            node.val = value
            self.removeNode(node)
            self.appendNode(node)
            return

        newNode = DLinkedList(value, key)
        
        if len(self.data) == self.capacity:
            oldnode = self.removeNode(self.tail.prev)
            del self.data[oldnode.key]
            
        self.appendNode(newNode)
        self.data[key] = newNode



        
