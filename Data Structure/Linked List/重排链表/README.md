**题目链接**  
https://leetcode-cn.com/problems/reorder-list/  

**题目描述**  

给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

**示例**  

```
给定链表 1->2->3->4, 重新排列为 1->4->2->3.
```

**解题思路**  
* 利用栈把链表的数据翻转，然后链接
* 链接时候注意中点的寻找，这个计算也没有想到
* 最后一个节点其实也是stack.pop()，这点当时没想到
* 写整洁一点的代码还真不容易
