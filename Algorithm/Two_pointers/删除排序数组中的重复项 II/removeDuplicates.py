class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        elif len(nums)==1:return 1
        left = 0
        dep = 0
        
        while left+1<len(nums):
            if nums[left]==nums[left+1]:
                dep+=1
                if dep>=2:
                    nums.pop(left-1)
                    dep -= 1
                    left -= 1
            else:
                dep=0
            left+=1
            
        return len(nums)
