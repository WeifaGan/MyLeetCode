**题目链接**  
https://leetcode.com/problems/is-subsequence/  

**题目描述**  
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative
positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).  
**example**   
```
s = "abc", t = "ahbgdc"

Return true.

s = "axc", t = "ahbgdc"

Return false.
```
**解题思路**  
* 只有s的每个字符都能在t上面相应找到(位置没有不是乱)就可以了。找到s的每个字符都能要找到，这是局部最优解，全部相应地找到就能达到全局最优解了。所以
用的是贪婪算法
