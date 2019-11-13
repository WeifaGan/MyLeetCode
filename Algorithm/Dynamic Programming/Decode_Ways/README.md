**题目链接**  
https://leetcode.com/problems/decode-ways/

**题目描述**  
A message containing letters from A-Z is being encoded to numbers using the following mapping:  
```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```
Given a non-empty string containing only digits, determine the total number of ways to decode it.  

**Example 1:**  
```
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
```
**Example 2:**  
```
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

**解题思路**  
这是动态规划规划的题目。跟青蛙爬楼梯的题目神似。通常DP的解题思路如下：
* 1.寻找状态转移方程  
  * 1.1 对于该题，第[i]个字符的Decode ways要不自身要不跟前面一个字符结合。如果跟自身的话，decode ways的数量还是那么多，dp[i]=dp[i-1]。如果是跟前一个字符组合的话，把这两个字符当作一个整体(一个字符)，那么这个整体对dp[i-2]来说是没有帮助的，所以dp[i]=d[i-2]。
* 2.从低向上运算。
