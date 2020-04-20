class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s:return 0

        g.sort()
        s.sort()
        g_len,s_len = len(g),len(s)
        g_n,s_n,result =0,0,0
        while g_n < g_len and s_n < s_len:
            if s[s_n]>=g[g_n]:
                g_n += 1
                s_n += 1
                result +=1
            else:s_n += 1
        return result
