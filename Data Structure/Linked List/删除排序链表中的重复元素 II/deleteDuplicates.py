# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        N=ListNode(-1)
        N.next = head
        pre,cur= None,N
        while cur:
            pre = cur
            cur = cur.next
            while cur and cur.next and cur.val ==cur.next.val:
                t = cur.val
                while cur and cur.val == t:
                    cur = cur.next
            pre.next = cur
        return N.next 
