class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        row = len(land)
        col = len(land[0])
        q = collections.deque()
        if not land or not land[0]:return []
        move = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
        def bfs(i,j):
            q.append((i,j))
            sm = 1
            land[i][j] = 'B'
            while q:
                i,j = q.popleft()               
                for x,y in move:
                    newx,newy = x+i,y+j
                    if newx<0 or newx>=row or newy<0 or newy>=col or land[newx][newy]!=0 or land[newx][newy]=='B':continue  
                    q.append((newx,newy))
                    sm += 1
                    land[newx][newy] = 'B'
            return sm

        count = []
        for i in range(row):
            for j in range(col):
                if land[i][j]==0:
                    count.append(bfs(i,j))

        count.sort()
        return count
