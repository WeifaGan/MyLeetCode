**链接**:  
https://leetcode-cn.com/problems/find-the-duplicate-number/

**解题思路**:  
* 寻找重复数，用快慢指针，双指针的话，还要记得有快慢指针这回事啊。
* 参考题目142，
* 环路的创建，如[1,3,4,2,2]，数组其实就是建立了位置到值的映射，0->1，1->3，2->4，3->2，4->3，根据这个映射创建环路即可。
* 一开始我以为这样子创建环路，1->3->4->2->2。就是根据数组的值的顺序来创建，但是flow的index的顺序为0 1 2 3 ...，fast的index的顺序为0 2 4 6...这里的6是超数组长度的，所以不好搞！
