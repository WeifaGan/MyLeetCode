class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a={}
        while head:
            if head in a:
                return head
            a[head]=1
            head=head.next
        return None
