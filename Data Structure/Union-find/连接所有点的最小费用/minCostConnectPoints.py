class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points or len(points)==1:return 0
        parents = defaultdict(int)
        
        dt = {}
        for i in range(len(points)):
            parents[i] = i

        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dt[(i,j)] = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])

        res = sorted(dt.items(),key=lambda item:item[1])

        total = 0
        c = 0
  
        for t,value in res:          
            x,y = t
            if union(x,y,parents):
                c += 1
                total += value
           
            if c == len(points)-1:
                return total


def find(x,parents):
    r = x
    while x != parents[x]:
        x = parents[x]
    parents[r] = x
    return x

def union(x,y,parents):
    x_r = find(x,parents)
    y_r = find(y,parents)
    if x_r != y_r:
        parents[y_r] = x_r
        return True
    else:return False
