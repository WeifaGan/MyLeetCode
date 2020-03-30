**题目链接**  
https://leetcode.com/problems/remove-outermost-parentheses/  

**题目描述**  
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

**example**  
```
Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
```

**解题思路**  
* 按顺序入栈，如果栈顶元素和准备入栈的元素是相同的，该元素入栈，否则出栈，当栈为空的时候，说明已经遍历了一个valid parentheses string。
* 创建空的字符串s1，在元素进出栈的过程中，移除外围括号。
