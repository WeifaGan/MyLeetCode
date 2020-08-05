**题目链接**:
https://leetcode-cn.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/  

**解题思路**：
* 广度优先
* 对于一个目的地，有从这个目的地出发的，有到这个目的地的，先用字典记录
* 从0开始，若从0这个目的地出发到A，cnt+=1,之后如果有从A出发的，再加1，因为希望A后后面的城市都是可以到达A的，这样子才能到达0。以此类推...
* 不是模板题，难啊
