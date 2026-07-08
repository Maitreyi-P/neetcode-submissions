class Node:
    def __init__(self, k, val, prev, next):
        self.k = k
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.head = Node(None, None, None, None)
        self.tail = Node(None, None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.remove(node.prev, node, node.next)
            self.add(self.tail.prev, node, self.tail)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            self.remove(node.prev, node, node.next)
            self.add(self.tail.prev, node, self.tail)
        else:
            if self.cap > 0:
                self.hmap[key] = Node(key,value, None, None)
                self.add(self.tail.prev,self.hmap[key],self.tail)
                self.cap -= 1
            else:
                lru_node = self.head.next
                del self.hmap[lru_node.k]
                self.remove(self.head, lru_node, lru_node.next)
                self.hmap[key] = Node(key,value, None, None)
                self.add(self.tail.prev,self.hmap[key],self.tail)

        
    def add(self,left,node,right):
        left.next = node
        node.prev = left
        right.prev = node
        node.next = right

    def remove(self,left, node, right):
        left.next = right
        right.prev = left
        node.prev = node.next = None