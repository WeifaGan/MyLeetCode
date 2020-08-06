class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        rotten = {(i,j) for i in range(row) for j in range(col) if grid[i][j]==2}
        fresh ={(i,j) for i in range(row) for j in range(col) if grid[i][j]==1}
        move = {(1,0),(-1,0),(0,1),(0,-1)}
        cnt = 0
        while fresh:
            if not rotten:return -1
            rotten = {(i+x,j+y) for i,j in rotten for x,y in move if (i+x,j+y) in fresh}
            fresh -= rotten
            cnt +=1
        return cnt
