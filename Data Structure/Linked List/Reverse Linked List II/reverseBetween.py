# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        a = []
        for i in range(n):
            a.append(head)
            head=head.next
            
        a = a[:m-1] + a[m-1:][::-1]
        
        for i in range(len(a)-1,-1,-1):
            tep=a[i]
            tep.next=head
            head=tep
            
        return head
