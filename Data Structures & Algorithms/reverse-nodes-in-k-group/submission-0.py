# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(start, end):
            prev = end
            curr = start
            nxt = None

            while curr!= end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        
        dummy = ListNode(None, head)
        groupPrev = dummy
        
        while True:

            kth = groupPrev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            start = groupPrev.next
            end = groupNext

            new = reverse(start, end)
            groupPrev.next = new
            groupPrev = start

        return dummy.next
        


        