# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        sp = head
        fp = head

        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next

        #reverse
        prev = None
        while sp:
            temp = sp.next
            sp.next = prev
            prev = sp
            sp = temp

        #check 
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True