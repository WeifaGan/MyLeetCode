**题目链接**  
https://leetcode.com/problems/permutations-ii/  

**题目描述**  
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
**example** 
```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

*解题思路**  
* 主要的难点是如何避免重复，使用一个列表记录被访问过的元素，当第一层循环时候，i=1时，temp=[1]，这个1是第二个1时候，第一个1应该是不需要push进去的，你也会发现此时visted=[0,1,0],所以continuet添加中的visted[i-1]==0就是用来检查对应位置的状态。如果不加入visted[i-1]的话，那第一个[1,1,2]也会被过滤。

