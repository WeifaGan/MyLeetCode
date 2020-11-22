class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        if not stones:return 0
        total = 0
        parent = {}
        for i in range(len(stones)):
            parent[i] = i 

        for i in range(len(stones)):
           
            a,b = stones[i]
     
            for j in range(i+1,len(stones)):
             
                c,d  = stones[j]
         
                if a==c or b==d:
                    print([a,b],[c,d])
                    total = union(i,j,parent,total)
                    total += 1

        return total

            

def find(x,parent):
    r = x
    while x!=parent[x]:
        x = parent[x]
    parent[r] = x
    return x        

def union(x,y,parent,total):
    x_r = find(x,parent)
    y_r = find(y,parent)
    if x_r != y_r:
        parent[x_r] = y_r
    else:total -= 1
    return total
