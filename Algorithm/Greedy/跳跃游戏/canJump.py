class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        outmost = 0
        for i in range(len(nums)):
            if i <= outmost:
                outmost = max(nums[i]+i,outmost)
                if outmost>=len(nums)-1:return True
        return False
