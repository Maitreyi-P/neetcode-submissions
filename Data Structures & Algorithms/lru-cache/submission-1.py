class Node:
    def __init__(self,key,val,prev,next):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(None,None,None,None)
        self.tail = Node(None,None,None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodemap = {}


    def get(self, key: int) -> int:
        if key in self.nodemap:
            node = self.nodemap[key]
            self.remove(node.prev,node.next,node)
            self.insert(self.tail.prev,self.tail,node)
            return node.val
        else:
            return -1
   

    def put(self, key: int, value: int) -> None:
        if key in self.nodemap:
            node = self.nodemap[key]
            node.val = value
            self.remove(node.prev,node.next,node)
            self.insert(self.tail.prev,self.tail,node)
        else:
            if self.cap == 0:
                k = self.head.next.key
                del self.nodemap[k]
                self.remove(self.head,self.head.next.next,self.head.next)
            else:
                self.cap -=1
            self.nodemap[key] = Node(key,value, None,None)
            self.insert(self.tail.prev,self.tail,self.nodemap[key])


    def insert(self,left,right,node):
        left.next = node
        right.prev = node
        node.prev = left
        node.next = right

    def remove(self,left,right,node):
        left.next = right
        right.prev = left
        
