class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:return 0
        row,col = len(grid),len(grid[0])
        move = ((1,0),(-1,0),(0,1),(0,-1))
        q = collections.deque()
        maxvalue = 0
        def dfs(i,j):
            sm = 1             
            for x,y in move:
                newx,newy = i+x,j+y
                if newx<0 or newx>=row or newy<0 or newy>=col or grid[newx][newy]==0 or grid[newx][newy]=='B':continue 
                grid[newx][newy]='B'
                sm += dfs(newx,newy)
            return sm

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    grid[i][j]='B'
                    maxvalue = max(dfs(i,j),maxvalue)

        return maxvalue
