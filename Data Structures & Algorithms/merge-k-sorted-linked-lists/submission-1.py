# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
        if not lists:
            return None
        def merge(list1,list2):

            if not list1:
                return list2
            if not list2:
                return list1
            
            # if list1.val <= list2.val:
            #     list1.next = merge(list1.next, list2)
            #     return list1
            # else:
            #     list2.next = merge(list1, list2.next)
            #     return list2

            newlist = ListNode(0, None)
            newhead = newlist
            while list1 and list2:
                if list1.val<=list2.val:
                    newlist.next = list1
                    list1 = list1.next
                else:
                    newlist.next = list2
                    list2 = list2.next
                newlist = newlist.next

            if list1:
                newlist.next = list1
            if list2:
                newlist.next = list2

            return newhead.next

        l1 = lists[0]
        for i in range(1,len(lists)):
            l2 = lists[i]
            l1 = merge(l1,l2)

        return l1
