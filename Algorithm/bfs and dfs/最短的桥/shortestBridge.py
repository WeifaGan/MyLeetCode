class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        #先用dfs寻找两座岛屿，再用bfs找最小的距离
        def dfs(i,j):
            if i<0 or i>=len(A) or j<0 or j>=len(A[0]) or A[i][j]==0 or A[i][j]==2:return
            if A[i][j]==1:
                A[i][j]=2
                q.append((i,j))
                for x,y in dirs:
                    newx,newy = x+i,y+j
                    dfs(newx,newy)
            
        def bfs(i,j):
            step=0
            while q:
                for _ in range(len(q)):
                    i,j = q.popleft()
                    for x,y in  dirs:
                        newx,newy = x+i,y+j
                        if newx<0 or newx>=len(A) or newy<0 or newy>=len(A[0]) or A[newx][newy]==2:continue
                        if A[newx][newy]==1:return step
                        A[newx][newy]=2
                        q.append((newx,newy)) 
                step+=1

        dirs = ((0,1),(1,0),(-1,0),(0,-1))
        q = collections.deque()
        for i, row in enumerate(A):
            for j,col in enumerate(row):
                if A[i][j]==1:
                    dfs(i,j)
                    return bfs(i,j)
