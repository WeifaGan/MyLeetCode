**题目链接**  
https://leetcode.com/problems/longest-substring-without-repeating-characters/  

**题目描述**  
Given a string, find the length of the longest substring without repeating characters.  

**Example 1:**  
```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

**解题思路**  
**使用哈希表**  
* 用left来记录当前最长无重复子字符串的左边位置，res来记录最长子字符串的长度,left初始化为-1,为什么呢？当遍历第一个元素i=0时候，若left=0,res=i-left=0，显然是不对的。
* 遍历每个元素都更新最长无重复子字符串，找最大。如果当前位置i的字符串在前面已经出现过的并且所在位置大于当前left，就更新left=map[s[i]]。因为这时候最长无重复的子字符串只能是该位置的后面了。（为什么要大于left?举个例子，abba,当遍历到第二个b的时候，left会更新为1，当遍历到第二个a的时候，如果left更新为0，我们知道left是记录当前最长无重复子字符串左边位置，但是现在明显不是最长无重复的子字符串。就是说，left要往后走，往前走并没有意义。）。
  

**使用数值模拟哈希表**   
* map[char]=i,char这个时候会char会转换为ASCII码，ASCII可以表示256个字符，所以可以声明一个256长度的数组。或者，因为键盘只能输入128个字符，所以申请
128长度的数据也是可以的。
* 把数据全部初始化为-1这就不用if判断是否存在映射关系了，尽管不存在映射关系，也可以更新，那就初始化的值-1更新为数组里面的值-1。

**复杂度分析**  
时间：O(n)  
空间：O(n)
