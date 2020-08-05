class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        goto, frm = collections.defaultdict(set),collections.defaultdict(set)
        for i,j in connections:
            goto[j].add(i)
            frm[i].add(j)

        cities = [0]
        seen = set(cities)
        cnt = 0
        while cities:
            c = cities.pop()
            for i in frm[c] | goto[c]:
                if i not in seen:
                    if i in frm[c]:cnt+=1
                    seen.add(i)
                    cities.append(i)
        return cnt
