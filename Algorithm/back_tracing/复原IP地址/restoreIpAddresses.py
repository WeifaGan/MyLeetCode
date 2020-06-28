class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        s1 = ''
        lst = []
        if len(s)<4:return []
        def backtrace(start,s1):
            if s1.count('.')==4 and len(s)==len(s1)-4:
                lst.append(s1[:-1])
                return

            for end in range(start+1,n+1):
                if s1.count('.')>4:continue
                if int(s[start:end])>255:continue

                backtrace(end,s1+s[start:end]+'.')

        backtrace(0,s1)
        return lst
