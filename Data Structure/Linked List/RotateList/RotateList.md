**题目链接**  
https://leetcode.com/problems/rotate-list/

**题目描述**  
Given a linked list, rotate the list to the right by k places, where k is non-negative.

**exmaple1** 
```
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
```
**exmaple2**
```
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
```
**解题思路**

* 从例子1中，我们可以看到，如果节点个数为5，k=2的时候，其实是把后面的两个节点般到最前面。
* 从例子2中，我们可以看到，如果节点数少于k，那是把多少个节点般到前面呢？搬到前面节点的个数为k对链表取了模值的结果。
* 要注意一些情况： k=0，链表为空，链表节点为1，k刚好等于节点的个数(这个可能跟程序写法有关系)
