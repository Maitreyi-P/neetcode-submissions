# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        sp,fp = head, head.next
        
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next

        h2 = sp.next
        sp.next = None
 
        #reverse l2 starting at h2
        prev = None
        curr = h2
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        h2 = prev
        #merge the 2 lists
        
        h1 = head
        while h2:
            t1, t2 = h1.next, h2.next
            h1.next = h2
            h2.next = t1
            h1, h2 = t1, t2
        
        # return finhead.next


