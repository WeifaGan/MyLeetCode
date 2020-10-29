**题目链接**:  
https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected/  

**题目描述**:
用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。

网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。

**示例**:
```
输入：n = 4, connections = [[0,1],[0,2],[1,2]]
输出：1
解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

**解题思路**:
一开始的解题思路：先求出冗余连通数量max_c，在求出有多少台电脑没有被链接op，如果max_c大于等于op，那么结果就是op了，否则为-1，后面发现还没有考虑到多台电脑被连接成几个集合的情况。最后的代码如下，
但是时间超时了。
```python
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = defaultdict(int)
        visited = defaultdict(set)
        size = defaultdict(int)
        max_c = 0
        for i in range(n):
            parent[i] = i
            size[i] = 1

        for a,b in connections:
            if not union(a,b,parent,visited,size):
                max_c += 1
        
        op = 0
   
        for a,b in connections:
            a_r = find(a,parent)
            b_r = find(b,parent)
            visited[a_r].add(a)
            visited[b_r].add(b)
            
        op += len(visited)-1

        v = []
        for key,value in visited.items():
                v += list(value)

        for i in range(n):
            if i not in v:
                op +=1

        print(v)
        print(op,max_c)
        if op<=max_c:
            return op
        else:return -1


def find(x,parent):
    r = x
    while x!=parent[x]:
        x = parent[x]
    parent[r] = x
    return x

def union(x,y,parent,visited,size):
    x_root = find(x,parent)
    y_root = find(y,parent)
    if x_root!=y_root:
        if size[x_root]<size[y_root]:
            parent[x_root] = y_root
        else:
            parent[y_root]=x_root
        if size[x_root]==size[y_root]:
            size[x_root]+=1
        return True
    else:return False
```

后面看了一下答案，思路简单多了，n台电脑连接在一起需要连接n-1次，只要统计连接了多少次就Ok啦。
