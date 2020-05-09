**题目链接**  
https://leetcode.com/problems/combination-sum/  

**题目描述**  

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.  
**Note**  
* All numbers (including target) will be positive integers.  
* The solution set must not contain duplicate combinations.  

**example**  
```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

**解题思路**   
* 用回溯模板即可  
* 在backtrace(list,templist,candidatates,remain-candidatates[i],i)中，传入的是i,不是i+1，不然第i个数只能用1次了
* 因为已经排序了，所以if remain<0,直接break退出同一层次的循环
