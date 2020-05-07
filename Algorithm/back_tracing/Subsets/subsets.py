class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = []
        n = len(nums)

        def helper(i,tmplst):
            lst.append(tmplst)
            for j in range(i,n):
                helper(j+1,tmplst+[nums[j]])

        helper(0,[])
        return lst
