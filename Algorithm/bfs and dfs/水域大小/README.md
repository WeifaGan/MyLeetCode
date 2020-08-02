**题目链接**：  
https://leetcode-cn.com/problems/pond-sizes-lcci/

**解题思路**:
* dfs时，写下这样子的代码,
```python
def dfs(i,j):
    q.append((i,j))
    sm=0
    while q:
        i,j = q.popleft()
        for x,y in move:
            newx,newy = x+i,y+j
            if newx<0 or newx>=row or newy<0 or newy>=col or land[newx][newy]!=0 or land[newx][newy]=='B':continue
            sm += 1
            land[i][j]='B'
            sm += dfs(newx,newy)
    return sm
```
这样子的代码问题在于sm加一和改写B的时候，除了i,j，四周无符合条件的，无法对i,j进行相关的操作，所以，要把相应操作放在前面
```python
def dfs(i,j):
    q.append((i,j))
    sm = 1
    land[i][j]='B'
    while q:
        i,j = q.popleft()
        for x,y in move:
            newx,newy = x+i,y+j
            if newx<0 or newx>=row or newy<0 or newy>=col or land[newx][newy]!=0 or land[newx][newy]=='B':continue
            sm += dfs(newx,newy)
    return sm
```
