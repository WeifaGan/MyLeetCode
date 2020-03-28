**题目链接**  
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/  

**题目描述**  
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

**example**  
```
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
```

**解题思路**  
因为行和列都是从小到大排序的，最小的是位于左上角p1(0,0)，第二小的数要不位于p2(0,1)，要不位于p3(1,0),可以把这些都放进最小堆里面，弹出最小值，
假如第二小的数是p2,那么下一次最小是有可能是p4(1,1),也有可能是p5(0,2)，把这两个数字进堆，然后弹出堆中最小值，以此类推...

**youtube链接**  
https://www.youtube.com/watch?v=LIaS7xmxlLg&t=171s
