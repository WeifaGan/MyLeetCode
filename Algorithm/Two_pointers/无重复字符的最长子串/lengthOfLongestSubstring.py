class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,-1
        lgth = len(s)
        st = set()
        opmax = 0
        while right<lgth:
            while right<lgth:
                right+=1
                if right<lgth and s[right] not in st:
                    st.add(s[right])
                    opmax = max(opmax,right-left+1)
                else:
                    break
            
            if right==lgth:break

            while left<right:
                if s[left]!=s[right]:
                    st.remove(s[left])#让set仅仅存放左右指针所指的范围
                    left+=1
                else:
                    left+=1 #这里就不用move了，跳过了重复那个数字，相当于从left-right重新开始了,left-right范围的数都需要
                    break

        print(st)
        return opmax
