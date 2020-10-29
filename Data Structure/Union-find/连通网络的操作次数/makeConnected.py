class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        part = n-1
        parent = defaultdict(int)
        size = defaultdict(int)
        
        for i in range(n):
            parent[i] = i
            size[i] = 1
        
        def find(x,parent):
            r = x
            while x!=parent[x]:
                x = parent[x]
            parent[r] = x
            return x

       
        for x,y in connections:
            x_root = find(x,parent)
            y_root = find(y,parent)
            if x_root!=y_root:
                if size[x_root]<size[y_root]:
                    parent[x_root] = y_root
                else:
                    parent[y_root]=x_root
                if size[x_root]==size[y_root]:
                    size[x_root]+=1
                part -= 1
        
        return part
            
