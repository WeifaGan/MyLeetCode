**题目链接**  
https://leetcode.com/problems/set-matrix-zeroes/description/

**题目描述:**    
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place. 

**exmaple**
```
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

**解题思路:**  
* 空间复杂度O(m*n),时间复杂度O(m*n)  
遍历所有元素，用O(m*n)的空间记录哪些元素需要置0,然后对需要置0的元素置0.  

* 空间复杂度O(1),时间复杂度O(m*n)  
利用第一行和第一列记录需要置0的位置,实现Do it in-place.  
1.记录第一列和第一行是否应该全为0.  
2.记对剩下的矩阵matrix,对matrix逐个元素查看是否为0，若为0,则更新第一行第一列对应的位置.  
3.根据新第一行和第一列更新matrix.  
4.根据第一行和第一类是否应该全为0更新第一行第一列.如果前面更新了第一行和第一类,更新matrix时候并不知道更新后为0还是原来就为0，所以最后更新第一行和第一列  
  
**My submission:**    
Your runtime beats 88.33 % of cpp submissions.
Your memory usage beats 19.85 % of cpp submissions



