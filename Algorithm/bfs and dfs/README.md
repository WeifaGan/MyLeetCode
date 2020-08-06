**题目链接**:
https://leetcode-cn.com/problems/rotting-oranges/submissions/  

**解题思路**：
* 广度优先
* 一开始写下这样子的代码
```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:return -1    
        move = ((1,0),(-1,0),(0,1),(0,-1))
        row,col = len(grid),len(grid[0])
        q = collections.deque()

        def bfs(i,j):
            q.append((i,j))
            cnt = 0
            grid[i][j]='B'
            while q:
                flag = False
                i,j = q.popleft()
                for x,y in move:
                    newx,newy = x+i,y+j
                    if newx<0 or newx>=row or newy<0 or newy>=col or grid[newx][newy]==2 or grid[newx][newy]==0 or grid[newx][newy]=='B':continue
                    grid[newx][newy]='B'
                    q.append((newx,newy))
                    flag = True
                if flag: cnt += 1
            return cnt

        max_value = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    max_value = max(max_value,bfs(i,j))
       
        for i in grid:
            if 1 in i:return -1
        return max_value
```
发现有些答案就是过不了，例如[[2,1,1],[1,1,1]],原因在于这做法并不是一圈完了才加1，我以为是，真实的情况是只是某个位置的一圈罢了.  
于是修改成这样子的代码  
```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:return -1    
        move = ((1,0),(-1,0),(0,1),(0,-1))
        row,col = len(grid),len(grid[0])
        q = collections.deque()

        def bfs(i,j):
            q.append((i,j))
            cnt = 0
            grid[i][j]='B'
            while q:
                flag = False
                for _ in range(len(q)):
                    i,j = q.popleft()
                    for x,y in move:
                        newx,newy = x+i,y+j
                        if newx<0 or newx>=row or newy<0 or newy>=col or grid[newx][newy]==2 or grid[newx][newy]==0 or grid[newx][newy]=='B':continue
                        grid[newx][newy]='B'
                        q.append((newx,newy))
                        flag = True
                if flag: cnt += 1
            return cnt

        max_value = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    max_value = max(max_value,bfs(i,j))
       
        for i in grid:
            if 1 in i:return -1
        return max_value
```
发现有些题目还是过不了[[2],[1],[1],[1],[2],[1],[1]],原因在max()有问题，如果两个腐烂的同时感染，就不是max了.还是想不出，看看别人的吧。  
别人用集合+bfs，嗯嗯，我还嫩.
