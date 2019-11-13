**题目链接**  
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/  

**题目描述**  
Say you have an array for which the ith element is the price of a given stock on day i.  

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).  
**Note** You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
**example**  
```
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
```

**解题思路**  
* 动态规划? 设p(i,j)为第i天买，j天卖的所得利润，但是p(i,j)跟p(i-1,j)或者p(i,j-1)或者p(i-1,j-1)有关系吗？反正我找不到状态转移方程
* 贪婪算法？只要后一天比前一天的价格高，就买和卖，实现局部最优解。最后可以达到全局最优解。可以的。
* 回溯算法？ 我觉得可以的，但是没有贪婪算法方便。
