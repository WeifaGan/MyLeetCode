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
* 判断回文字符串，比较简单，动态规划则可。
* 提取了子字符串之后，下一个起点在哪里？start+i,不是start+1
* 判断什么时候将templist push 到list,如果起点超出了最后字符的位置，说明已经把所有字符都遍历了。

**回溯算法真的巨慢！**
