**题目链接**  
https://leetcode.com/problems/reverse-linked-list/  

**题目描述**  
Reverse a singly linked list.  
```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

**解题思路**  
* 当后面的指针指向的节点指向前面节点时候，后面指针的数据就会连不上了，所有需要三个指针，第三个指针是用于连接后面的节点。
* 注意只有一个节点的情况。
