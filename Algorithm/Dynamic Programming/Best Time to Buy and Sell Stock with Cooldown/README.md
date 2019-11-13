**题目链接**  
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/  

**题目描述**  
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:
* You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).  
* After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)  

**example**  
```
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

**解题思路**  
* 求第i天的最大利润，可以先求前面的i-1,i-2...的最大利润，就是可以分成若个干问题来求解。可以用动态规划。
* 由于对于不同的元素，它都可以有不同的状态，所以只用一条转移方程来完成是不可能的。
* 这道题题目让我想起了求三角矩阵的最短路径和，它求出到达最后一层的各个元素的最短路径，然后作对比取最小值。这题目也是类似的，可以求出最后的一个元素的不同
状态下的最大利润，然后作比对取最大值即可。对比如下:
![image](https://github.com/WeifaGan/MyLeetCode/blob/master/Image/3.PNG)
* 我的转移方程
  * sell[i]=max(buy[i-1]+prices[i-1],cooldown[i-1]);
  * cooldown[i]=max(sell[i-1],buy[i-1]);
  * buy[i]=cooldown[i-1]-prices[i];
* 正确的转移方程
  * cooldown任何时候都可以，所以cooldown[i]=max(sell[i-1],cooldown[i-1]); cooldown[i]=max(cooldown[i],buy[i-1]);
  * 要买了才能sell,或则不sell, sell[i]=max(buy[i-1]+prices[i],sell[i-1]);
  * 要cooldown后才能buy,或者不buy,buy[i]=max(cooldown[i-1]-prices[i],buy[i-1]);
  
**my submission**  
* runtime beats 74.53%
* memory beats 100%
