**题目链接**  
https://leetcode-cn.com/problems/sort-list/  

**题目描述**  
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

**示例**  
```
输入: 4->2->1->3
输出: 1->2->3->4
```

**解题思路**  
* 因为时间复杂度为O(nlogn),所以用归并排序
* 分割链表  
  * 快慢指针找出mid
  * head.next=None,说明只有一个节点
* 合并链表
