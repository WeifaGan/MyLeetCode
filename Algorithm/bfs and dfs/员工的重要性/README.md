**题目链接**:  
https://leetcode-cn.com/problems/employee-importance/

**解题思路**:
* 深度遍历，广度遍历

一开始写下这样子的代码：然后报错返回了null，还纠结了很久，为什么有null的返回，一直都检查不出来，参考别人的代码有了灵感，
下面的代码的返回只是在最后的一次回溯中有返回，但是其他的回溯是没有返回的，看条件就知道了！为什么我会写出这样子的代码？可能被以前的题目模板毒害得比较深吧。。。看来对回溯理解得还是不够深刻。另外一个
问题是sum作为参数传递，这样子的话，会有重复计算的！！！
```python
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        def dfs(emap,id,sm):
            if emap[id].subordinates==[]:return emap[id].importance
            for i in emap[id].subordinates:
                sm += dfs(emap,i,sm)
     
        emap = {e.id:e for e in employees}
        sm = emap[id].importance
        
        return dfs(emap,id,sm)
```
参考了别人的代码,你看，sm应该是局部的，这样子才不会重复计算，而不是全局。记得以前的题目都是定义一个全局的变量，但是具体问题具体分析吧。
```python

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
```
