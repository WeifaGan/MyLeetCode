**题目链接**  
https://leetcode.com/problems/intersection-of-two-linked-lists/  

**解题思路**  
* 先遍历一个链表，存储地址(用集合set)，再看在另外一个链表是否存在这个地址，但是存储空间是O(n)
* 先求出长链表比短链表长多少，长链表先行弥补差距，然后再一起走，如果指针相等，则为交叉点
