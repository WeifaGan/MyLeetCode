class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        if len(heights)==1 and len(heights[0])==1 :return 0
        r = len(heights)
        c = len(heights[0])
        weights = []
        for i in range(r):
            for j in range(c-1):
                n1 = i*c+j
                n2 = n1+1
                weight = abs(heights[i][j]-heights[i][j+1])
                weights.append((weight,n1,n2))
          
        for i in range(r-1):
            for j in range(c):
                n1 = i*c+j
                n2 = (i+1)*c+j
                weight = abs(heights[i][j]-heights[i+1][j])
                weights.append((weight,n1,n2))

        parent = dict()
        for i in range(r*c):
            parent[i] = i
        weights = sorted(weights)


       
        print(weights)
        for w,p1,p2 in weights:
            union(p1,p2,parent)
            
            if find(0,parent)==find(r*c-1,parent):
                return w

def find(x,parent):
    r = x
    while x!=parent[x]:
        x = parent[x]
    parent[r] = x
    return x

def union(x,y,parent):
    x_r = find(x,parent)
    y_r = find(y,parent)
    if x_r!=y_r:
        parent[x_r] = y_r
