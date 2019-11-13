**题目链接**  
https://leetcode.com/problems/minimum-path-sum/  

**题目描述**  
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
**example**  
```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

**解题思路**  
* 这题目跟Triangle十分类似。
* 动态规划。  
  * 可以分解成若个问题求解：先求出前面若干个点的最优路径  
  * 状态转移方程：dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j];
  * 空间优化： 从上面的状态转移方程可以看到，dp[i][j]决取与前面的dp和当前位置的grid,所以覆盖以前的grid是没有问题的。所以修改grid来存储计算的结果是ok的。
  
**my submission**  
Runtime: 4 ms, faster than 99.37% of C++ online submissions for Minimum Path Sum.  
Memory Usage: 10.4 MB, less than 99.55% of C++ online submissions for Minimum Path Sum.  
  
