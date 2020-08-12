class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        move = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1))
        col = len(board[0])
        row = len(board)

        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board

        def cal(i,j):
            cnt = 0
            for x,y in move:
                if 0<=i+x<row and 0<=j+y<col and board[i+x][j+y]=='M':cnt+=1
            return cnt

        def dfs(i,j):
            m_cnt = cal(i,j)
            if m_cnt>0:
                board[i][j]=str(m_cnt)
                return
            board[i][j]='B'
            for x,y in move:
                newx,newy = i+x,j+y
                if 0<=newx<row and 0<=newy<col and board[newx][newy]=='E':
                    dfs(newx,newy)

        dfs(click[0],click[1])
        return board
