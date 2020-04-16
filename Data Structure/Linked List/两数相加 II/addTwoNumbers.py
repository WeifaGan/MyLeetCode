# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_stack,l2_stack = [],[]
        while l1 :  
                l1_stack.append(l1.val) 
                l1 = l1.next         
        while l2:            
                l2_stack.append(l2.val)
                l2 = l2.next

        ln2 = None
        
        flag = 0
        while l1_stack or l2_stack or flag:
            a = 0 if not l1_stack else l1_stack.pop()
            b = 0 if not l2_stack else l2_stack.pop()
            s = a + b + flag
            flag1 = s % 10
            flag = s // 10
                       
            ln1 = ListNode(flag1)
            ln1.next,ln2  = ln2,ln1 

        return ln1
