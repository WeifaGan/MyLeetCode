class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        if not n: return [[]]
        if n == 1:return [[s]]
        lst = [] 
        tmp = []
        def backtrace(start,tmp):
            if start>=n:lst.append(tmp)
            for end in range(start+1,n+1):
                split_s = s[start:end]
                if split_s==split_s[::-1]:
                    backtrace(end,tmp+[split_s])
        
        backtrace(0,tmp)
        return lst
            
