class Node:
    def __init__(self, key, value, prev, next):
        self.k = key
        self.val = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(None,None,None,None)
        self.tail = Node(None,None,None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodeMap = {}


    def get(self, key: int) -> int:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.remove(node.prev,node,node.next)
            self.add(self.tail.prev,node,self.tail)
            return node.val
        else:
            return -1


        

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.remove(node.prev,node,node.next)
            self.add(self.tail.prev,node,self.tail)
            node.val = value
        else:
            if self.cap > 0:
                node = Node(key,value,None,None)
                self.add(self.tail.prev,node,self.tail)
                self.nodeMap[key] = node
                self.cap -= 1
            else:
                del self.nodeMap[self.head.next.k]
                self.remove(self.head,self.head.next,self.head.next.next)
                node = Node(key,value,None,None)
                self.add(self.tail.prev,node,self.tail)
                self.nodeMap[key] = node

                
            
    
    def add(self,left,node,right):
        left.next = node
        node.prev = left
        right.prev = node
        node.next = right

    def remove(self,left,node,right):
        left.next = right
        right.prev = left
        node.prev = None
        node.next = None

        
