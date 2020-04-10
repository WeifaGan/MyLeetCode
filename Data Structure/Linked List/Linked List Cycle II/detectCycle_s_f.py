class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head;
        fast=head;
        try:
            while 1:
                slow=slow.next
                fast=fast.next.next
                if slow==fast:
                    break
        except:return None
        
        slow=head
        while fast!=slow:
            slow=slow.next
            fast=fast.next
        
        return slow
            
