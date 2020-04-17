**题目链接**  
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/  

**题目描述**  
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

**示例**  
```
输入: 1->2->3->3->4->4->5
输出: 1->2->5
```

**题目思路**  
* 我之前的思路是当cur.val = cur.next.val时候，pre和cur都向前走，不过写了很久还没写出
* 为了解决一开始就pre,cur相等的情况，在前面多加一个节点，这个想法真妙啊
* 当cur.val = cur.next.val时候，cur不断地往后不断判断跟前面的相不相等就行。
