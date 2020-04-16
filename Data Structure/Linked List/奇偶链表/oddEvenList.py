# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p1 = head
        p2 = head.next
        p1_2 = p2
        
        while p2 and p2.next:
                p1.next = p2.next 
                p1 = p1.next
                p2.next = p1.next
                p2 = p2.next

        p1.next = p1_2
        return head
