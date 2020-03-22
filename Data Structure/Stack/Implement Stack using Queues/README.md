**题目链接**  
https://leetcode.com/problems/implement-stack-using-queues/  

**题目描述**  
mplement the following operations of a stack using queues.

* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* empty() -- Return whether the stack is empty.

**example**  
```
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
```

**解题思路** 
用两个队列实现stack的pop()或者push()
