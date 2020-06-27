**题目链接**  
https://leetcode.com/problems/palindrome-partitioning/  

**题目描述**  
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
```
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
```

**解题思路**  
* 好明显，暴力试错。
* 判断回文字符串，比较简单，s==s[::-1]即可。
* 判断什么时候将templist push 到list,如果起点超出了最后字符的位置，说明已经把所有字符都遍历了。
* 这里回溯其实就是按顺序的组合，这个还是不太熟悉啊，有一段时间没写了。

**回溯算法真的巨慢！**
