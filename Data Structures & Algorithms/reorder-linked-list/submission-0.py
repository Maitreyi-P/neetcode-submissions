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

        #reverse l2 starting at h2

        prev = sp.next = None
        while h2 is not None:
            nxt = h2.next
            h2.next = prev
            prev = h2
            h2 = nxt
        
        first, second = head, prev
        #merge the 2 lists

        # final = ListNode(None,None)
        # finhead = final
        
        # while head and h2:
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1,t2
        
        # return finhead.next


