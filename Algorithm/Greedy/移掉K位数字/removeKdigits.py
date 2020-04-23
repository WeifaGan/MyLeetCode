class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in num:
            while k and stack and stack[-1]>i:
                stack.pop()
                k -= 1
            stack.append(i)

        stack = stack[:-k] if k else stack
        return "".join(stack).lstrip("0") or "0"  
