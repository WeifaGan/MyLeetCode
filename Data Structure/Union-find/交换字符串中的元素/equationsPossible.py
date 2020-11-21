class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        if not equations:return False
        parent = {}
        import string 
        for i in string.lowercase:
            parent[i] = i

        equations = sorted(equations,key=lambda x:x[1:3])
       

        for i in equations[::-1]:
           
            if i[1:3] == '==':
                union(i[0],i[3],parent)
            else:
                if find(i[0],parent) == find(i[3],parent):
                    return False

        return True

def find(x,parent):
    r = x
    while x!=parent[x]:
        x=parent[x]
    parent[r] = x
    return x

def union(x,y,parent):
    x_r = find(x,parent)
    y_r = find(y,parent)
    if x_r != y_r:
        parent[x_r] = y_r
    
