**题目链接**:
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/  

**解题思路**：
一开始想着滑动窗口，其实普通的双指针就行了。于是写下这样子的代码：
这个代码的问题是空间复杂度较高。
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        elif len(nums)==1:return 1
        left,right = 0,1
        dep = 0
        li = []
        while right<len(nums):
            if nums[left]==nums[right]:
                dep+=1
                if dep>=2:
                    li.append(left-1)
                    dep-=1
            else:
                dep=0
            left+=1
            right+=1
        for index,i in enumerate(li):del nums[i-index]
        return len(nums)
```

看了一下别人的，修改了代码,pop一个之后，将索引-1，这是个好主意，不过这个时间花费还是蛮高的。不知道为毛
```python
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
```
