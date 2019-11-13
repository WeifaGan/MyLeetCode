**题目链接**  
https://leetcode.com/problems/average-of-levels-in-binary-tree/  

**题目描述**  
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
```
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
```
**Note**:The range of node's value is in the range of 32-bit signed integer.  

**解题思路**  
难点主要是不知道如何确定每一层的个数，其实是这样子的，首先根结点先进队列，根结点出队之前会先把其子结点都进队，所以根结点出队之后的队列的个数就是下一层
结点的个数，如果第二层的结点个数为2，第三层结点个数为4，因为结点出队前会把其子结点进队，当第二层的结点都出队列了，这时候队列剩下来的就是第三个层的结点了。



