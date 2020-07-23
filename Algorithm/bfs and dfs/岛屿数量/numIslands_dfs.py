class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='2' or grid[i][j]=='0':return 
            if grid[i][j]=='1':
                grid[i][j]='2'
            for x,y in move:
                newx,newy = i+x,j+y
                dfs(newx,newy)

        move = ((0,1),(1,0),(0,-1),(-1,0))
        count = 0
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if grid[i][j]=='1':
                    dfs(i,j)
                    count+=1
        return count
