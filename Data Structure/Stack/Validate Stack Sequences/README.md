**题目链接**  
https://leetcode.com/problems/validate-stack-sequences/  

**题目描述**  
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

**example1**  
```
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```

**解题思路**   
这里需要栈和队列一起完成。创建一个模拟栈，让pushed的进栈，进栈后，对比栈中的top()元素与popped.front()元素是否相等。相等则栈和队列都pop();如果序列是valid的，队列肯定是空的
