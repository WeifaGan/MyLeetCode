**题目链接**  
https://leetcode.com/problems/valid-parentheses/description/  

**题目描述**  
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
**Example**  
```
Input: "()"
Output: true
Input: "()[]{}"
Output: true
Input: "([)]"
Output: false
```

**解题思路**  
一开始我一心想着根据规律解题,但是很难把所有情况都考虑进去，后面看了别人的解题思路，用栈来做，很简单。 看来做题要多想想可能用到哪些数据结构和算法。   
这里把‘（’，‘{’，‘[’记为左边符号，相应地有右边符号。 
我们从左到右依次访问字符串，把左边符号进栈，遇到右边符号为止，这时候检查栈顶元素与右边符号是否是对应的，不是则返回false，是继续往右走。  
**有两点需要注意**
* 当s[i]为右边符号时候，如果栈为空，返回false，因为这情况类似是“}}}}”
* 最后返回要判断是否为空，有可能一直进栈  

**My submission**  
Your runtime beats 100.00 % of cpp submissions.  
Your memory usage beats 88.22 % of cpp submissions.  
