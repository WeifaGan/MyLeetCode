**题目链接**：
https://leetcode-cn.com/problems/surrounded-regions/  

**解题思路**：
* 一开始的想法是直接用深度或者广度把区域中的包围的O改写成X,但是这样子很难。看了别人的答案，先将从边界开始的O的区域用bfs或者dfs找出来并改成为B，这样子的话之后凡是找到的O都是被包围的。  
* 这段代码超出时间限制
```python
def bfs(i,j):
    q.append((i,j))
    while q:
        i,j = q.popleft()
        board[i][j]='B'
        for x,y in move:
            newx,newy = i+x,j+y
            if newx<0 or newx>=row or newy<0 or newy>=col:continue   
            if board[newx][newy]=="O":
                q.append((newx,newy))   
```
参考别人改写成就行了，区别在于for循环中的命令行数不同。
```python
def bfs(i,j):
    q.append((i,j))
    while q:
        i,j = q.popleft()
        if 0<=i<row and 0<=j<col and board[i][j]=='O':  
            board[i][j]='B'
            for x,y in move:
                q.append((i+x,j+y))    
                
```
