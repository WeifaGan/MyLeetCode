**题目链接**  
https://leetcode.com/problems/climbing-stairs/

**题目描述**
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
**Example**
```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```
**解题思路**   
* 1.状态转移方程
  * 第n阶楼梯要不就从第n-1阶楼梯上来，要不就从第n-2阶楼梯上来。而第n-1阶楼梯上来的方式的数量有dp[n-1]冲，为什么呢？从第n-2阶楼梯上来就有dp[n-2]种，为什么呢？
* 2.自底往上运算
  
 **My submission**  
  our run time beats 77.35 % of cpp submissions.  
  our memory usage beats 55.32 % of cpp submissions.  
