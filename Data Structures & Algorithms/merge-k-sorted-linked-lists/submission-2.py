# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1,l2):
            dummy = ListNode(None,None)
            temp = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    dummy.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    dummy.next = ListNode(l2.val)
                    l2 = l2.next
                dummy = dummy.next
            
            if l1:
                dummy.next = l1
            elif l2:
                dummy.next = l2

            return temp.next

        if len(lists) == 0:
            return None
        else:
            l1 =lists[0]
            for i in range(1,len(lists)):
                l2 = lists[i]
                l1 = merge(l1,l2)

        return l1

        