class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left,right = 0,-1
        lgth = len(A)
        sm = 0
        opmax = 0
        while right<lgth:
            while right<lgth:
                right+=1
                if right<lgth:

                    if A[right]==0:
                        K -= 1
                    if K>=0:
                        opmax = max(opmax,right-left+1)
                    else:break
                    
            if right==lgth:break

            while left<right:
                if A[left]==0:
                    K+=1
                left += 1
                if K>=0:break
             
        return opmax
