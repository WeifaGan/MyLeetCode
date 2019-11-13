**题目链接**  
https://leetcode.com/problems/subsets-ii/  

**题目描述**
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

**example**
```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

**解题思路**  
最主要还是避开重复的子集,一开始我是想着，向前+1判断是否有重复的数字，但是这样子容易出现出界带来一些问题，
有一个重要的地方忘记了，就是先排序，这样子就可以避免重复向后判断是否有重复的数字了。  

**My Submission**  
Your runtime beats 93.08 % of cpp submissions.  
Your memory usage beats 39.89 % of cpp submissions.
