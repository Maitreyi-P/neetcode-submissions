# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        sumd=0
        l3=ListNode(None,None)
        ans=l3
        while l1 is not None and l2 is not None:
            val1=l1.val
            val2=l2.val
            c=val1+val2+carry
            carry=c//10
            sumd=c%10
            l3.next=ListNode(sumd,None)
            l3=l3.next
            l1=l1.next
            l2=l2.next
        while l1 is not None:
            v=l1.val+carry
            carry=v//10
            sumd=v%10
            l3.next=ListNode(sumd,None)
            l3=l3.next
            l1=l1.next
        while l2 is not None:
            v=l2.val+carry
            carry=v//10
            sumd=v%10
            l3.next=ListNode(sumd,None)
            l3=l3.next
            l2=l2.next
        if carry!=0:
            l3.next=ListNode(carry,None)
        return ans.next
        
        
