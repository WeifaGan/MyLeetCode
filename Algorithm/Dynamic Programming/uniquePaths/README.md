**题目链接**  
https://leetcode.com/problems/unique-paths/submissions/  

**题目描述**  
```
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
```
**example**  
```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Input: m = 7, n = 3
Output: 28
```

**解题思路**  
这是动态规划的题目。
* 可以理解为求最值吗？
* 可以分解成若干个问题求解。对于第(i,j)个格子来说，要不来自上面的格子(i,j-1)，要不来自于左边的格子(i-1，j）。格子(i,j-1)和格子(i-1，j）也如此。有dp
(i,j)=dp(i-1,j)+dp(i,j-1)。

**复杂度分析**  
* 优化前:空间O(n*m),时间O(n*m)  
* 优化后:空间O(n),时间O(n*m)

**My submission**   
Your runtime beats 100% of cpp submissions.  
Your memory usage beats 65.47 % of cpp submissions.  
