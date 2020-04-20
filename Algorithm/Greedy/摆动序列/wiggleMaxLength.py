class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng = len(nums)
        if not leng:return 0
        if leng<2:return 1
        up,down =[1]*leng,[1]*leng
        i = 1
        while i<leng:
            if nums[i]>nums[i-1]:
                up[i] = down[i-1]+1
                down[i] = down[i-1]
            elif nums[i]<nums[i-1]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]
            i += 1

        return up[leng-1] if up[leng-1]>down[leng-1] else down[leng-1]
