**题目链接**  
https://leetcode.com/problems/kth-largest-element-in-an-array/  

**题目描述**  
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

**example1**  
```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```

**Note:**  
You may assume k is always valid, 1 ≤ k ≤ array's length.  

**解题思路**  
* 先排序的方法，复杂度较高
* 用堆去完成。维护一个长度为k的最小堆q。如果带push的值大于q.top(),则q.pop(),然后push对应的值。这样子q.top()就是第k大的值。

**复杂度分析**  
* N*log(k)，维护长度为k的堆，复杂度为log(k)
