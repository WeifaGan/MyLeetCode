**题目链接**  
https://leetcode.com/problems/next-greater-element-ii/  

**题目描述**  
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

**example**  
```
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
```

**解题思路**  
* 环形数组，可以将原数组扩展，模拟环形数组，如[1,2,1]扩展成[1,2,1,1,2,1]
* 结果取原数组对应的结果即可
