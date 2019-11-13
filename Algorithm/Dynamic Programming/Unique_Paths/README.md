**题目链接**  
https://leetcode.com/problems/unique-paths/ 

**题目描述**
```
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
```
example1
```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
```
**解题思路**  
因为每个格子只能从左边或者上面走下来，所以n(i,j)=n(i-1,j)+n(i,j-1),这是典型的动态规划问题.  
* 用递归,简介,但速度慢,超时,
* 用for循环计算到达每个格子的独立路径的数目,直到统计完毕为止

**My submission**  
Your runtime beats 86.06 % of cpp submissions
Your memory usage beats 16.96 % of cpp submissions.
