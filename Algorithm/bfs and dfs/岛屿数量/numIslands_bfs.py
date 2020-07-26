class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j):
            q.append((i,j))
            while q:
                for _ in range(len(q)):
                    i,j = q.popleft()
                    for x,y in move:
                        newx, newy = x+i, y+j
                        if newx<0 or newx>=len(grid) or newy<0 or newy>=len(grid[0])  or grid[newx][newy]=='0' or grid[newx][newy]==2:continue
                        
                        q.append((newx,newy))
                        grid[newx][newy]=2


          

        move = ((0,1),(1,0),(0,-1),(-1,0))
        count = 0
        q = collections.deque()
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if grid[i][j]=='1':
                    bfs(i,j)
                    count+=1
        return count
