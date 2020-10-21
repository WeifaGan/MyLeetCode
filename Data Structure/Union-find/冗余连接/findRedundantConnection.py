class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        size = {}
        for i in range(1,len(edges)+1):
            parent[i] = i
            size[i] = 1

        for lst in edges:
           if not union(lst[0],lst[1],parent,size):
               return lst 


def find(x,parent):
    while x!=parent[x]:
        x = parent[x]
    return x

def union(x,y,parent,size):
    x_root = find(x,parent)
    y_root = find(y,parent)
    if x_root != y_root:
        if size[x]>size[y]:
         
            parent[y_root] =x_root
        else:
            parent[x_root] = y_root
        if size[x] == size[y]:
            size[y_root] += 1
        
        return True
    else:
        
        return False
