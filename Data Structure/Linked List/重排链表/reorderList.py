# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:return None
        st =[]
        pre = head
        cur = head.next
        while head:
            st.append(head)
            head = head.next

        leng = (len(st)-1)//2 #找到中点前一个位置
        while leng :
            s = st.pop()
            pre.next,s.next = s,cur
            pre,cur = cur,cur.next
            leng -=1

        st.pop().next = None 
        
