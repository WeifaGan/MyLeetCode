**题目链接**: https://leetcode-cn.com/problems/clone-graph/    

**解题思路**：
* 因为要深度克隆，所以对于每个节点我们都需要用Node类来生成。
* 使用哈希来记录访问过的，并且可以根据原节点和克隆节点。
* bfs 的套路：
  * 用队列来遍历节点
  * 访问过的要记录下来。以免死循环。
* dfs 套路：
  * 其实就是迭代，所以要要主要设置条件return 
