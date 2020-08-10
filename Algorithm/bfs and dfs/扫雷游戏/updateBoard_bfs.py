class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        move = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1))
        q = collections.deque()
        col = len(board[0])
        row = len(board)
        visited = []
        tep_visited = []
        def bfs(i,j):
            if board[i][j]=='M':
                board[i][j]='X'
                return
            q.append((i,j))
            while q:
                i,j = q.popleft()
                M_cnt = 0
                tep_deque = collections.deque()
                tep_visited = []
                for x,y in move:
                    newx,newy = i+x,j+y
                    if newx<0 or newx>=row or newy<0 or newy>=col or board[newx][newy]=='B' or board[newx][newy].isdigit() or (newx,newy) in visited:continue
                    if board[newx][newy]=='M':M_cnt+=1
                    if board[newx][newy]!='M':
                        tep_visited.append((newx,newy))
                        tep_deque.append((newx,newy))
                if M_cnt:board[i][j]=str(M_cnt)
                else:
                    board[i][j]='B'
                    visited.extend(tep_visited)
                    q.extend(tep_deque)

        bfs(click[0],click[1])
        return board
