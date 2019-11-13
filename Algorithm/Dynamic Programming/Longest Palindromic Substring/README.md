**题目连接**  
https://leetcode.com/problems/longest-palindromic-substring/  

**题目描述**  
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.  
**example**  
```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"
```

**解题思路**  
动态规划  
* 求最值
* 可以分解若干个问题，一个回文串s[i]-s[j]，它的子字符串s[i+1]-s[j-1]也是回文串,所以分解成先求解小小回文串，小回文串等等。所以有dp[i][j]=dp[i+1][j-1]
&& s[i]==s[j]。一开始没有想到子字符串也是个回文串，在寻找状态转移方程的时候应该集中大问题与子问题的关系，不是纠结如何求解大问题。

**复杂度分析**  
时间 O(n*n)，空间O(n*n)
