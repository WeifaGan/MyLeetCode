**题目链接**：https://leetcode-cn.com/problems/min-cost-to-connect-all-points/  

**解题思路**：  
* 首先对所有可能的连线进行排序(这一步我是没有想到的)
* 如果连线的两个端点是在同一棵树，说明已连通，那么就不需要添加该费用，下一个。

可以推测如果用并查集又是求最值得，应该可以考虑排序了。
