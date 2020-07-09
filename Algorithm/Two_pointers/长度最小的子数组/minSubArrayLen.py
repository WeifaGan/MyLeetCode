class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        L, R = 0, -1
        sum1, n = 0, len(nums)
        opmin = n+1
        while R<n:
            while R<n:
                R+=1
                if R<n:
                    sum1 +=nums[R]
                if sum1>=s:
                    opmin = min(opmin,R-L+1)
                    break
            
            if R==n:break

            while L<R:
                sum1 -= nums[L]
                L+=1              
                if sum1>=s:
                    opmin = min(opmin, R-L+1)
                else:break
        return opmin if opmin != n+1 else 0
