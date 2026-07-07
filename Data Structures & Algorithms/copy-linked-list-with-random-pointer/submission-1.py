"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        dummy = Node(0, None, None)

        seen = {}

        newnode = Node(head.val,None,None)
        seen[head] = newnode
        dummy.next = newnode

        while head and head.next:
            if head.next in seen:
                newnode.next = seen[head.next]
            else:
                newnode.next = Node(head.next.val, None, None)
                seen[head.next] = newnode.next

            if not head.random:
                newnode.random = None
            else:
                if head.random in seen:
                    newnode.random = seen[head.random]
                else:
                    newnode.random = Node(head.random.val, None,None)
                    seen[head.random] = newnode.random

            head = head.next
            newnode = newnode.next

        if head and not head.next:
            newnode.next = None
            if not head.random:
                newnode.random = None
            else:
                newnode.random = seen[head.random]


        return dummy.next
