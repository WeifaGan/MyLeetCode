"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        def dfs(emap,id):
            sm = emap[id].importance
            for i in emap[id].subordinates:
                sm += dfs(emap,i)
            return sm
        emap = {e.id:e for e in employees}
        sm = emap[id].importance
        return dfs(emap,id)
