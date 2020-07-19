**题目链接**:  
https://leetcode-cn.com/problems/sorted-matrix-search-lcci/

**解题思路**:
这里很容易想到用双指针，开始写下这样子的代码：  
这代码可以使可以，但是没用充分利用题目的信息。
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:return False
        M,N = len(matrix),len(matrix[0])
        p1,p2 = 0,N-1
        for mat in matrix:
                if mat[p1]<target and  mat[p2]<target:
                    continue
                elif mat[p1]<=target and mat[p2]>=target:
                    if target in mat: return True
                    else:continue
                elif mat[p1]>target:return False
        return False
    
```
看了一下别人的答案：
可以从左下角出来，进行搜索，这才充分利用题目的信息。这个自己没想到。试了一下，如果从右上角出发的话，速度没那么快，大概是因为目标很大程度在后面吧。。。。
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:return False
        i,j =len(matrix)-1,0
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                j+=1
            else :i-=1
        return False
```
