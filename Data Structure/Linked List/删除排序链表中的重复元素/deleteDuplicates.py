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
        pre,cur = None,head
        while cur:
            pre,cur = cur,cur.next
            while cur and cur.val==pre.val:
                while cur and cur.val == pre.val:
                    cur = cur.next
                pre.next = cur

        return head
