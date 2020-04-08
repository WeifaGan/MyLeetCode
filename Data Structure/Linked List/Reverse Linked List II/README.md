**题目链接**  
https://leetcode.com/problems/reverse-linked-list-ii/

**题目描述**  

Reverse a linked list from position m to n. Do it in one-pass.

**Note:** 1 ≤ m ≤ n ≤ length of list.

**example**  
```
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
```

**解题思路**  
* cpp:找到中间部分逆转链表，然后解决开头和结尾。主要m=1和m>1两种情况
* python：把前n节点append到列表，翻转需要翻转的，然后重新链接所有节点
