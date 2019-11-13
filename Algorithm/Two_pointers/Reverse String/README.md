**题目链接**  
https://leetcode.com/problems/reverse-string/  

**题目描述**  
Write a function that reverses a string. The input string is given as an array of characters char[].Do not allocate extra space for another array, you must do this by **modifying the input array in-place with O(1) extra memory.**
You may assume all the characters consist of printable ascii characters.
```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**解题思路**  
两个指针，一头一尾，交换即可，头指针++，尾指针--即可，但是要注意的是头指针<size/2,尾指针>=size/2;范围要覆盖全啊。

**My submission**  
Runtime beats 73.77%  
Memorry beats 100%
