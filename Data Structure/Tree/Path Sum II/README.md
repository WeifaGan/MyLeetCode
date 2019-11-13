**题目链接**  
https://leetcode.com/problems/path-sum-ii/  

**题目描述**  
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

**Note:** A leaf is a node with no children.
**example**  
Given the below binary tree and sum = 22,
```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
```
return
```
[
   [5,4,11,2],
   [5,8,4,5]
]
```

**解题思路**
* 在PathSum1的基础上，用递归很快就可以完成了。
