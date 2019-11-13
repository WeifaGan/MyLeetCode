**题目链接**  
https://leetcode.com/problems/unique-paths-ii/  

**题目描述**  
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

**Note:** m and n will be at most 100.

**example1:**
```
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

**解题思路**  
* 明显的DP问题
  * 第i,j格子的要不在第i-1,j格子走过来，要不在第i,j-1格子走过来，所以状态转移方程dp[i][j]=dp[i-1][j]+dp[i][j]
  * 如果走的过程中有障碍物，对应dp[i][j]=0;
