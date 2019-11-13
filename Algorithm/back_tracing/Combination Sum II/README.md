**题目链接**  
https://leetcode.com/problems/combination-sum-ii/  

**题目描述**  
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.
**note**  
```
* All numbers (including target) will be positive integers.
* The solution set must not contain duplicate combinations.
```

**解题思路**  
* 因为每个数只能用一次，所以那个taceback里面的参数是i+1
* 因为解决方案不能重复，所以用p来判断是否为本次循环的下一个循环，如果是tb进去的循环，尽管当前的值与前一个值是相同的，但是当前值也是需要的。如果是tb结束后的下一个循环，如果当前值与前一个值是相同的，我们是跳过的。
* for里面的条件判断需要放前面。
