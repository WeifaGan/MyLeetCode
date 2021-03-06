lass Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:return
        row = len(board)
        col = len(board[0])

        move=((0,1),(0,-1),(-1,0),(1,0))
        q = collections.deque()

        def bfs(i,j):
            q.append((i,j))
            while q:
                i,j = q.popleft()
                if 0<=i<row and 0<=j<col and board[i][j]=='O':  
                    board[i][j]='B'
                    for x,y in move:
                        q.append((i+x,j+y))    
                
                    
        #第一列和最后一列         
        for i in range(row):
            if board[i][0]=='O':
                bfs(i,0)
            if board[i][col-1]=='O':
                bfs(i,col-1)
        
        #第一行和最后一行
        for j in range(col):
            if board[0][j]=='O':
                bfs(0,j)
            if board[row-1][j]=='O':
                bfs(row-1,j)

        for i in range(row):
            for j in range(col):
                if board[i][j]=="O":
                    board[i][j]='X'
                if board[i][j]=='B':
                    board[i][j]='O'
