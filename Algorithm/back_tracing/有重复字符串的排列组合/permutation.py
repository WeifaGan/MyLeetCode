class Solution(object):
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        lst = []
        lgth = len(S)
        s = ''
        s1 = list(S)
        s1.sort()
        S=''.join(s1)
        visited=[0]*lgth
        def backtrace(start,s):
            if len(s)==lgth:
                lst.append(s)
                return 
            for i in range(0,lgth):
                if visited[i]==1:continue  \\过滤位置重复
                if i>0 and S[i]==S[i-1] and visited[i-1]==0:continue \\过滤整体重复
                visited[i] = 1
                backtrace(0,s+S[i])
                visited[i] = 0
        backtrace(0,s)
        return lst
