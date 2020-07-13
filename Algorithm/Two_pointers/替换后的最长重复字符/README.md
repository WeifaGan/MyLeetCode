**题目链接**:
https://leetcode-cn.com/problems/longest-repeating-character-replacement/

**解题思路**:
* 可以替换的字符数：right-left+1-字符频率最大的数量，之前也没想到这样子计算，但是想着通过求频率最小的，len(d)==2 and 频率最小 <k or len(d)==3
* 对于left+1之后，如何求频率呢？这个参考别人，原来还有这种操作，max(d,d.get)可以求出最大频率的字符。那直接求最大频率如何操作呢？
