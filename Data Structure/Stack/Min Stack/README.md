**题目链接**  
https://leetcode.com/problems/min-stack/  

**题目描述**  
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* getMin() -- Retrieve the minimum element in the stack

**Example:**  
···
MinStack minStack = new MinStack();  
minStack.push(-2);  
minStack.push(0);  
minStack.push(-3);  
minStack.getMin();   --> Returns -3.  
minStack.pop();
minStack.top();      --> Returns 0.  
minStack.getMin();   --> Returns -2.  
···

**解题思路**  
* 我当时只能想到遍历原栈，但不符合题意
* 如果用一个变量记录最小值，pop后无法解决下一个最小值
* 方法是用一个栈来记录每次原栈操作后的最小值
