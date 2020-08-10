**题目链接**：
https://leetcode-cn.com/problems/minesweeper/submissions/  

**解题过程**：
* 一开始写下这样子的代码
```python
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        move = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1))
        q = collections.deque()
        col = len(board[0])
        row = len(board)

        def bfs(i,j):
            if board[i][j]=='M':
                board[i][j]='X'
                return
            q.append((i,j))
            while q:
                i,j = q.popleft()
                M_cnt = 0
                tep_deque = collections.deque()
                for x,y in move:
                    newx,newy = i+x,j+y
                    if newx<0 or newx>=row or newy<0 or newy>=col or board[newx][newy]=='B' or board[newx][newy].isdigit():continue
                    if board[newx][newy]=='M':M_cnt+=1
                    tep_deque.append((newx,newy))
                if M_cnt:board[i][j]=str(M_cnt)
                else:
                    board[i][j]='B'
                    # while tep_deque:
                    #     i = tep_deque.popleft()
                    q.extend(tep_deque)

        bfs(click[0],click[1])
        return board
```
这代码超时了，原因在于进去队列的点没有做标记，有些点重复地进去了，所以就超时罗。  
然后又写了这样子地代码
```python
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        move = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1))
        q = collections.deque()
        col = len(board[0])
        row = len(board)
        visited = []
        def bfs(i,j):
            if board[i][j]=='M':
                board[i][j]='X'
                return
            q.append((i,j))
            while q:
                i,j = q.popleft()
                M_cnt = 0
                tep_deque = collections.deque()
                for x,y in move:
                    newx,newy = i+x,j+y
                    if newx<0 or newx>=row or newy<0 or newy>=col or board[newx][newy]=='B' or board[newx][newy].isdigit() or (newx,newy) in visited:continue
                    if board[newx][newy]=='M':M_cnt+=1
                    if board[newx][newy]!='M':
                        visited.append((newx,newy))
                        tep_deque.append((newx,newy))
                if M_cnt:board[i][j]=str(M_cnt)
                else:
                    board[i][j]='B'
                    q.extend(tep_deque)

        bfs(click[0],click[1])
        return board
```
这代码还是过不了，原因在于 tep_deque最后有没有extend，有没有最后进入队列，有些点都会进入visited
