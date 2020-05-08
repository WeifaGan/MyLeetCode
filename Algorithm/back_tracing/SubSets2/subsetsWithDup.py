class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        lst = []
        nums = sorted(nums)
        flag = True
        def backtrace(i,teplist):
            lst.append(teplist)
            for j in range(i,n):
                if j>i and nums[j]==nums[j-1] :continue
                backtrace(j+1,teplist+[nums[j]])

        backtrace(0,[])
        return lst
