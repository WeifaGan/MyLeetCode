**题目链接**  
https://leetcode.com/problems/triangle/submissions/  

**题目描述**  
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
**example**  
```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).  

**解题思路**  
* 贪婪算法？我们选择近邻两个数字中的最小的一个，每一次达到局部最小值，但是，这样子就不一定能达到全局最小值了。  
* 暴力法？我们要得到全局最小值，那么对比所有路径的和，求出最小值，时间复杂度为n(2+4+6+...+2*(n-1))=n^2;  
* 动态规划？首先这个求最优值，其次，可以划分为若个子问题吗？能找出状态转移方程吗？对于上面的例子，若干个子问题是什么？不管有多少条路径，最后到达就是4，1，8，3，
，那么在到达4的所有路径中总有一个最小的路径把。所有我们可以先求出到达4的最小路径，到达1的最小路径，以此类推。最后对比所有的最小路径就可以了。所以子问题是到达某个点
点的最小路径。转移方程呢，对于i,j点，设dp[i][j]为到达第i行，第j列的最小路径，点i,j无非来自i-1,j 或者是i-1,j，所以有转移方程
dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]。那我们需要建一个跟triangle一样大小的vector吗?如果是不能的话是什么原因呢?我们无非是担心需要用到的值
被覆盖掉了，但我们可以从转移方程看到，dp只跟位置的triangle有关系，所以覆盖也是没有关系。
