**题目链接**:  https://leetcode-cn.com/problems/path-with-minimum-effort/


**解题思路**：将边的权重从小到大排序，然后添加到并查集，如果左上角和右下角的连通，那么最后那条边的权重就是最小的体力值。
