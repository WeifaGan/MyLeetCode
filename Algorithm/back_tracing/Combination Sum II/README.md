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
* 同一层次的重复是要避免的，不同层次的重复是不用避免的，所以j>i and candicates[j]==candicates[j-1]，这是做子集2时候想到的，做这个题目时候又想不起来了。在这里捋一捋思路。对于for j in range(i,n),正常来说第一个j是等于i的，如果要j=i时候判断 candicates[j]==candicates[j-1]，说明对于下一个层次的第一个元素跟上一个层次的元素做了对比，这种跨越层次的对比我们是不需要的，所以j>i，忽略掉这样的对比。同一层次的第二次循环开始同一层次的对比。
