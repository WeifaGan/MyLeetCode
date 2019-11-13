**题目链接**   
https://leetcode.com/problems/path-sum/  

**题目描述**  
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

**Note:** A leaf is a node with no children.
**example**  
Given the below binary tree and sum = 22,
```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
```

**解题思路**  
* 把一个前序遍历的所得结果之和其实就是根节点到叶节点的路径的和
* remain=0时候，注意当前结点是不是叶节点
