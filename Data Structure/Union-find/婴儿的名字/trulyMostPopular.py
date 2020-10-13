class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        size = defaultdict(int)
        parent = defaultdict(str)
        name_fre = defaultdict(int)
        ans = []
        res = defaultdict(int)
        for i in names:
            name,fre = (part.strip().strip(")") for part in i.split("("))
            name_fre[name] = int(fre)
            
            parent[name] = name #初始化
            size[name] = 1
        
        for st in synonyms:
            a,b = (name.strip().strip("(").strip(")") for name in st.split(","))
            union(a,b,parent,size)
          
        for i,j in name_fre.items():
            
            root = find(i,parent)
            res[root] += j   

        for i,j in res.items():
            s = i+"({})".format(j) 
            ans.append(s)
        
        return ans

def find(x,parent):
    if not parent[x]:return x
    while x!=parent[x]:
        x = parent[x]
    return x

def union(x,y,parent,size):
    x_root = find(x,parent)
    y_root = find(y,parent)

    if x_root<y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root
