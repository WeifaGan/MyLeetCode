**题目链接**  
https://leetcode.com/problems/two-sum/  

**题目描述**  
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
**example** 
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

**解题思路**
* 返回的位置，自然想到哈希表  
* 先把(nums[i],i)放到哈希表，然后判断target-nums[i]是否再哈希表里面  
* 要注意一个数不能用两遍，所有有i!=nums[target-nums[i]]  

**复杂度分析**  
* 时间:O(n)
* 空间:O(n)
