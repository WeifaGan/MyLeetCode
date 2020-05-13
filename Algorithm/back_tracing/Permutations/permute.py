class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        lst = []
        def backtrace(j,temp):
            if len(temp)==n: 
                lst.append(temp)
                return
            for i in range(n):
                if nums[i] in temp:continue 
                backtrace(i,temp+[nums[i]])
        
        backtrace(0,[])
        return lst
