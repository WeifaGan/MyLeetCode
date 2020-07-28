class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        def dfs(emap,id):
            sm = 0
            while q:
                id = q.popleft()
                sm += emap[id].importance
                for i in emap[id].subordinates:
                    q.append(i)
            return sm
            
        emap = {e.id:e for e in employees}
        q = collections.deque()
        q.append(id)
        return dfs(emap,id)
