# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l3 = ListNode(None,None)
        ans = l3

        carry = 0
        while l1 and l2:
            newval = l1.val + l2.val + carry
            digit = newval % 10
            carry = newval // 10
            l3.next = ListNode(digit,None)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        
        while l1:
            newval = l1.val + carry
            digit = newval % 10
            carry = newval // 10
            l3.next = ListNode(digit,None)
            l3 = l3.next
            l1 = l1.next

        while l2:
            newval = l2.val + carry
            digit = newval % 10
            carry = newval // 10
            l3.next = ListNode(digit,None)
            l3 = l3.next
            l2 = l2.next

        if carry != 0:
            l3.next = ListNode(carry,None)

        return ans.next

