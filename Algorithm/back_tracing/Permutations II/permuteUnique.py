class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        lst = []
        nums.sort()
        visited = [0]*n
        def backtrace(temp):
            if len(temp)==n:
                lst.append(temp)
                return 
            for j in range(n):
                if visited[j] == 1: continue
                if j >0 and nums[j]==nums[j-1] and visited[j-1]==0:continue
                visited[j] = 1 
                backtrace(temp+[nums[j]])
                visited[j] = 0
        backtrace([])
        return lst
